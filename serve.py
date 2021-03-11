#!/usr/bin/env python3
import logging
import os
import shutil
import tempfile
import sys
import subprocess

import tornado.web

from os.path import isfile, join

from mkdocs.commands.build import build
from mkdocs.config import load_config

log = logging.getLogger('mkdocs')
log.propagate = False
stream = logging.StreamHandler()
formatter = logging.Formatter("%(levelname)-7s -  %(message)s ")
stream.setFormatter(formatter)
log.addHandler(stream)
log.setLevel(logging.INFO)


def _init_asyncio_patch():
    if sys.platform.startswith("win") and sys.version_info >= (3, 8):
        import asyncio
        try:
            from asyncio import WindowsSelectorEventLoopPolicy
        except ImportError:
            pass  # Can't assign a policy which doesn't exist.
        else:
            if not isinstance(asyncio.get_event_loop_policy(), WindowsSelectorEventLoopPolicy):
                asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())


def _get_handler(site_dir, handler):
    from tornado.template import Loader

    class WebHandler(handler):

        def write_error(self, status_code, **kwargs):
            if status_code in (404, 500):
                error_page = '{}.html'.format(status_code)
                if isfile(join(site_dir, error_page)):
                    self.write(Loader(site_dir).load(error_page).generate())
                else:
                    super().write_error(status_code, **kwargs)

    return WebHandler


def _get_redirect_handler(language):
    class RedirectHandler(tornado.web.RequestHandler):
        def get(self, path):
            self.redirect(os.path.join('/' + language, path))

    return RedirectHandler


def _livereload(host, port, languages, builder, site_dir):
    # We are importing here for anyone that has issues with livereload. Even if
    # this fails, the --no-livereload alternative should still work.
    _init_asyncio_patch()
    from livereload import Server
    import livereload.handlers

    class LiveReloadServer(Server):
        def _setup_logging(self):
            logger = logging.getLogger('livereload')
            logger.setLevel(logging.INFO)
            return

        def get_web_handlers(self, script):
            handlers = []
            for lang in languages:
                handlers.append((fr'/{lang}/(.*)',
                                 _get_handler(os.path.join(site_dir, lang), livereload.handlers.StaticFileHandler), {
                                     'path': os.path.join(site_dir, lang),
                                     'default_filename': self.default_filename,
                                 }))
            handlers.append((r'/(.*)', _get_redirect_handler(languages[0])))
            return handlers

    server = LiveReloadServer()

    def full_builder_func():
        for lang in languages:
            builder(lang)

    server.watch('shared', full_builder_func, delay=0)
    for lang in languages:
        server.watch(lang, create_builder(builder, lang), delay=0)

    server.serve(root=site_dir, host=host, port=port, restart_delay=0)


def create_builder(builder, lang):
    def func():
        builder(lang)

    return func


def pre_build(language, out):
    subprocess.call(['rsync', '-a', '--delete', '.git', out])

    subprocess.call(['rsync', '-a', '--delete', '--exclude', 'mkdocs.yml',
                     'shared/', language + '/', out + '/' + language])
    config = subprocess.check_output(['yq', 'eval-all', 'select(fileIndex == 0) *d select(fileIndex == 1)',
                                      os.path.join('shared', 'mkdocs.yml'), os.path.join(language, 'mkdocs.yml')])
    with open(os.path.join(out, language, 'mkdocs.yml'), 'wb') as out:
        out.write(config)


def serve(host, port, languages):
    docs_dir = tempfile.mkdtemp(prefix='mkdocs_')
    site_dir = tempfile.mkdtemp(prefix='mkdocs_out_')

    def builder(lang):
        log.info(f'Building {lang}...')
        pre_build(lang, docs_dir)

        lang_path = os.path.join(docs_dir, lang)

        config = load_config(
            config_file=os.path.join(lang_path, 'mkdocs.yml'),
            dev_addr=f'{host}:{port}',
            strict=True,
            site_dir=os.path.join(site_dir, lang)
        )

        config['site_url'] = f'http://{host}:{port}/{lang}/'

        # mkdocs is usually launched from the docs root directory, so it doesn't resolve relative paths smart enough,
        # leading to some bugs when launched from another place.
        # For example, custom_icons don't work without this dirty hack, and our neat Flipper buttons fail to load :(
        # I could've filled an issue to mkdocs-material-extensions regarding this, but I believe it's more reliable
        # to just switch the working directory, cause there might be other features that rely on it.
        #
        # It was kinda hard to figure this out, and it's actually 9 AM right now and I haven't slept yet, so please
        # satisfy my praise kink by saying 'good girl' telepathically
        cwd = os.getcwd()
        os.chdir(lang_path)

        build(config, live_server=True, dirty=False)

        os.chdir(cwd)

    try:
        for lang in languages:
            builder(lang)
        _livereload(host, port, languages, builder, site_dir)
    finally:
        shutil.rmtree(docs_dir)
        shutil.rmtree(site_dir)


if __name__ == '__main__':
    serve('172.25.26.244', 8000, ['en', 'ru'])
