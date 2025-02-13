from __future__ import unicode_literals

LOCAL_BUILD = False
SITEURL = '' if LOCAL_BUILD else '/pelican/euipo'
DEFAULT_DATE = 'fs' #Pelican will use the file system's last modified date
SITENAME = 'EUIPO FO Dev Hub'
PATH = "content"
TIMEZONE = 'Europe/Athens'
DEFAULT_LANG = 'en'
THEME = './theme/notmyidea'
CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True

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
CATEGORY_URL = '/{slug}.html'  # Single category URL
CATEGORY_SAVE_AS = '/{slug}.html'  # Save path for single category pages

# URL structure for individual articles
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['jinja2content']

#values like SITEURL will be globally accessible in all Jinja templates.
JINJA_GLOBALS = {
    'SITEURL': SITEURL
}

MENUITEMS = [
    ("APIs", SITEURL+'/apis.html'),
    ("Tutorials", SITEURL+'/tutorials.html')
]

DISPLAY_CATEGORIES_ON_MENU = False
