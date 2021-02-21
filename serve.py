#!python3
import logging
import os
import shutil
import tempfile
import sys
import subprocess

from os.path import isfile, join
from mkdocs.commands.build import build
from mkdocs.config import load_config

log = logging.getLogger('mkdocs')


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


def _get_handler(site_dir, StaticFileHandler):
    from tornado.template import Loader

    class WebHandler(StaticFileHandler):

        def write_error(self, status_code, **kwargs):

            if status_code in (404, 500):
                error_page = '{}.html'.format(status_code)
                if isfile(join(site_dir, error_page)):
                    self.write(Loader(site_dir).load(error_page).generate())
                else:
                    super().write_error(status_code, **kwargs)

    return WebHandler


def _livereload(host, port, languages, builder, site_dir):
    # We are importing here for anyone that has issues with livereload. Even if
    # this fails, the --no-livereload alternative should still work.
    _init_asyncio_patch()
    from livereload import Server
    import livereload.handlers

    class LiveReloadServer(Server):

        def get_web_handlers(self, script):
            handlers = super().get_web_handlers(script)
            # replace livereload handler
            return [(handlers[0][0], _get_handler(site_dir, livereload.handlers.StaticFileHandler), handlers[0][2],)]

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
    log.info(f'Merged sources: {docs_dir}')
    log.info(f'Built site: {site_dir}')

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

        config['site_url'] = f'http://{host}:{port}/' + lang + '/'

        build(config, live_server=True, dirty=False)

    try:
        for lang in languages:
            builder(lang)
        _livereload(host, port, languages, builder, site_dir)
    finally:
        shutil.rmtree(docs_dir)
        shutil.rmtree(site_dir)


if __name__ == '__main__':
    log.propagate = False
    stream = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)-7s -  %(message)s ")
    stream.setFormatter(formatter)
    log.addHandler(stream)
    log.setLevel(logging.INFO)

    logging.getLogger('tornado').setLevel(logging.WARNING)

    serve('localhost', 8000, ['en', 'ru'])
