from jinja2 import Environment

AUTHOR = 'IK'
SITENAME = 'DAMA51'
SITEURL = ""
DEFAULT_DATE = 'fs' #Pelican will use the file system's last modified date
PATH = "content"
TIMEZONE = 'Europe/Athens'
DEFAULT_LANG = 'en'
THEME= 'theme/notmyidea'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
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

INDEX_SAVE_AS = 'index.html'  # Ensure the homepage is saved as index.md

ARTICLE_ORDER_BY = 'order'
PAGE_ORDER_BY = 'order'
CATEGORY__ORDER_BY = 'category_order'

# URL structure for categories
CATEGORY_URL = '{slug}.html'  # Single category URL
CATEGORY_SAVE_AS = '{slug}.html'  # Save path for single category pages

# URL structure for individual articles
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

DEFAULT_PAGINATION = 10

# In pelicanconf.py
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n', 'jinja2.ext.do'],
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
