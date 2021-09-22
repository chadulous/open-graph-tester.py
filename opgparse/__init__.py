import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
def get_page(url):
    """Scrapes a URL and returns the HTML source.
    
    Args:
        url (string): Fully qualified URL of a page.
    
    Returns:
        soup (string): HTML source of scraped page.
    """
    
    response =urllib.request.urlopen(url)
    soup = BeautifulSoup(response, 
                         'html.parser', 
                         from_encoding=response.info().get_param('charset'))
    
    return soup
def get_og_title(soup):
    """Return the Open Graph title

    Args:
        soup: HTML from Beautiful Soup.
    
    Returns:
        value: Parsed content. 
    """

    if soup.findAll("meta", property="og:title"):
        return soup.find("meta", property="og:title")["content"]
    else:
        return
    
    return
def get_og_locale(soup):
    """Return the Open Graph locale

    Args:
        soup: HTML from Beautiful Soup.
    
    Returns:
        value: Parsed content. 
    """

    if soup.findAll("meta", property="og:locale"):
        return soup.find("meta", property="og:locale")["content"]
    else:
        return
    
    return
def get_og_description(soup):
    """Return the Open Graph description

    Args:
        soup: HTML from Beautiful Soup.
    
    Returns:
        value: Parsed content. 
    """

    if soup.findAll("meta", property="og:description"):
        return soup.find("meta", property="og:description")["content"]
    else:
        return
    
    return
def get_og_site_name(soup):
    """Return the Open Graph site name

    Args:
        soup: HTML from Beautiful Soup.
    
    Returns:
        value: Parsed content. 
    """

    if soup.findAll("meta", property="og:site_name"):
        return soup.find("meta", property="og:site_name")["content"]
    else:
        return
    
    return
def get_og_image(soup):
    """Return the Open Graph site name

    Args:
        soup: HTML from Beautiful Soup.
    
    Returns:
        value: Parsed content. 
    """

    if soup.findAll("meta", property="og:image"):
        return soup.find("meta", property="og:image")["content"]
    else:
        return
    
    return
def get_og_url(soup):
    """Return the Open Graph site name

    Args:
        soup: HTML from Beautiful Soup.
    
    Returns:
        value: Parsed content. 
    """

    if soup.findAll("meta", property="og:url"):
        return soup.find("meta", property="og:url")["content"]
    else:
        return
    
    return
class OpenGraph:
    def __init__(self, url):
        self.url = url
        self.soup = get_page(url)
        self.url = get_og_url(self.soup)
        self.title = get_og_title(self.soup)
        self.description = get_og_description(self.soup)
        self.image = get_og_image(self.soup)
        self.sitename = get_og_site_name(self.soup)
        self.locale = get_og_locale(self.soup)
        self.parsed = urlparse(self.url)
    def __call__(self):
        return {
            'url': self.url,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'sitename': self.sitename,
            'locale': self.locale,
            'baseurl': f'{self.parsed.scheme}://{self.parsed.netloc}/'
            }
from markupsafe import escape
import flask
import os
def htmlify(og: OpenGraph):
    og = og()
    template = open(f'{os.path.dirname(__file__)}/templates/index.html', 'r').read()
    return flask.render_template_string(template, url=og['url'], image=og['image'], description=og['description'], simage=og['image'], sitename=og['sitename'], title=og['title'], base=og['baseurl'])