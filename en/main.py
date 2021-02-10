from urllib.parse import urlparse, urljoin

def is_absolute(url):
    return bool(urlparse(url).netloc)

def define_env(env):
  "Hook function"

  @env.macro
  def gif(url):
      if not is_absolute(url):
          url = urljoin(env.conf['site_url'], url)
      return '<video autoplay muted loop playsinline style="width: 100%"> <source src="' + url + '" type="video/mp4"></video>'

  @env.macro
  def video(url):
      if not is_absolute(url):
          url = urljoin(env.conf['site_url'], url)
      return '<video controls style="width: 100%"> <source src="' + url + '" type="video/mp4"></video>'