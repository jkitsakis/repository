from __future__ import unicode_literals

LOCAL_BUILD = True
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

MARKDOWN = {
    'extensions': [
        'markdown.extensions.extra',
        'markdown.extensions.meta',
    ],
    'output_format': 'html5',
}

JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True}
PLUGINS = ['jinja2content']



MENUITEMS = [
    ("APIs", '/apis.html'),
    ("Tutorials", '/tutorials.html')
]

DISPLAY_CATEGORIES_ON_MENU = False
