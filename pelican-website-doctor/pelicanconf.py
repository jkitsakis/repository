from __future__ import unicode_literals
from plugins.configuration_params import Parameters

AUTHOR = Parameters.AUTHOR
SITENAME = Parameters.SITENAME
SITEURL = Parameters.SITEURL
SITESUBTITLE = Parameters.SITESUBTITLE
SITESUBTITLE_ESY = Parameters.SITESUBTITLE_ESY
HOME = Parameters.HOME
SERVICES = Parameters.SERVICES


PATH = "content"
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'Greek'
DEFAULT_DATE = 'fs' #Pelican will use the file system's last modified date

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
#---------------------------------------------------#


THEME = 'theme/attila'
HOME_COVER = 'https://img.freepik.com/premium-photo/doctor-front-bright-background-with-stethoscope-hand_397897-55.jpg?w=1380'
INDEX_SAVE_AS = 'index.html'  # Ensure the homepage is saved as index.html



MENUITEMS = [
    (HOME, '/'),
    (SERVICES, '/services/services.html')
]
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
ARTICLE_ORDER_BY = 'order'
PAGE_ORDER_BY = 'order'


USE_TAGS = False
TAGS_URL = ''
TAG_SAVE_AS = ''

# URL structure for categories
CATEGORY_URL = 'services/{slug}.html'  # Single category URL
CATEGORY_SAVE_AS = 'services/{slug}.html'  # Save path for single category pages
CATEGORIES_URL = ''
# CATEGORIES_SAVE_AS = 'services.html'  # Save path for the categories index page

# URL structure for individual articles
ARTICLE_URL = 'services/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'services/{category}/{slug}.html'

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['plugins.inject_constants', 'plugins.update_category']


# Translations
DEFAULT_LANG = 'el'
I18N_SUBSITES = {
    'en': {
        'SITENAME': 'KONSTANTINIDOY KYRIAKI',
        'SITESUBTITLE': 'General Practitian',
        'LOCALE': 'en_US'
    }
}