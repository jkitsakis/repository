from __future__ import unicode_literals
from plugins.configuration_params import Parameters


AUTHOR = Parameters.AUTHOR
SITENAME = Parameters.SITENAME
SITEURL = Parameters.SITEURL
SITEURL_OG = Parameters.SITEURL_OG
SITE_LOGO_IMG = Parameters.SITE_LOGO
SITESUBTITLE = Parameters.SITESUBTITLE
SITESUBTITLE_ESY = Parameters.SITESUBTITLE_ESY
HOME_COVER = Parameters.HOME_COVER + '?w=1380'
HOME_COVER_URL_OG= Parameters.HOME_COVER_URL_OG
HOME = Parameters.HOME
SERVICES = Parameters.SERVICES
KEYWORDS = Parameters.KEYWORDS
SITE_DESCRIPTION = Parameters.SITE_DESCRIPTION

GOOGLE_ANALYTICS = "G-GX37CVK7L3"
PATH = "content"
TIMEZONE = 'Europe/Athens'
DEFAULT_LANG = 'Greek'
DEFAULT_DATE = 'fs' #Pelican will use the file system's last modified date

THEME = 'theme/attila'
INDEX_SAVE_AS = 'index.html'  # Ensure the homepage is saved as index.html
ARTICLE_ORDER_BY = 'order'
PAGE_ORDER_BY = 'order'
DEFAULT_PAGINATION = 10
USE_TAGS = False
TAGS_URL = ''
TAGS_SAVE_AS = ''
ARCHIVES_URL = ''
ARCHIVES_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_URL = ''
CATEGORIES_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL structure for categories
CATEGORY_URL = 'services/{slug}.html'  # Single category URL
CATEGORY_SAVE_AS = 'services/{slug}.html'  # Save path for single category pages

# URL structure for individual articles
ARTICLE_URL = 'services/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'services/{category}/{slug}.html'

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['sitemap', 'plugins.inject_constants', 'plugins.article_order_navigation', 'plugins.minify' ]

STATIC_PATHS = ['robots.txt', 'images', 'favicon.ico', 'cookies']
# Map extra files to specific locations
EXTRA_PATH_METADATA = {
    'cookies/policy.html': {'path': 'policy.html'},
}

MENUITEMS = [
    (HOME, '/'),
    (SERVICES, '/services/services.html')
]


# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)
# Social widget
# SOCIAL = (
#     ("Facebook", Parameters.FACEBOOK_URL),
#     # ("Twitter", "https://twitter.com/your-profile"),
#     ("LinkedIn", Parameters.LINKEDIN_URL),
#     ("Instagram", Parameters.INSTAGRAM_URL)
# )



