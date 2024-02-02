#AUTHOR = 'jk'
SITENAME = 'EUIPO dev'

LOCAL_BUILD = True
SITEURL = '' if LOCAL_BUILD else '/pelican/euipo'

PATH = "content"

TIMEZONE = 'Europe/Athens'
DEFAULT_LANG = 'en'
THEME = './theme/notmyidea'

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True
ARTICLE_ORDER_BY = 'order'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True