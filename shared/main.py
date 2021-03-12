from urllib.parse import urlparse, urljoin


def is_absolute(url):
    return bool(urlparse(url).netloc)


def define_env(env):
    "Hook function"

    @env.macro
    def gif(url):
        if not is_absolute(url):
            url = urljoin(env.conf['site_url'], url)
        return f'<p><video autoplay muted loop playsinline style="width: 100%"> <source src="{url}" type="video/mp4"></video></p>'

    @env.macro
    def video(url):
        if not is_absolute(url):
            url = urljoin(env.conf['site_url'], url)
        return f'<p><video controls style="width: 100%"> <source src="{url}" type="video/mp4"></video></p>'

    @env.macro
    def screenshot(url, width='400px'):
        if not is_absolute(url):
            url = urljoin(env.conf['site_url'], url)
        return f'<p><svg style="width: {width};" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 282 158"> <g id="flipper__screen"> <rect width="282" height="158" x="0" y="0" fill="#c6c5c3" rx="18"></rect> <rect width="278" height="154" x="2" y="2" fill="#d9d8d6" rx="15"></rect> <rect width="276" height="152" x="3" y="3" fill="#e5e5e5" rx="15"></rect> <rect width="266" height="142" x="8" y="8" fill="#ff8b29" rx="10"></rect> <foreignObject width="256" height="128" x="13" y="15"> <img src="{url}" style="image-rendering: pixelated; width: 256px;"/> </foreignObject></g></svg></p>'

    @env.macro
    def altium(id):
        return f'<script src="https://viewer.altium.com/client/static/js/embed.js"></script><div class="altium-ecad-viewer" data-project-src="{id}" style="height: 500px; overflow: hidden; max-width: 1280px;"></div>'