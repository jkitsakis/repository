from __future__ import unicode_literals
import os

LOCAL_BUILD = False
SITEURL = '' if LOCAL_BUILD else '/pelican/euipo'

SITENAME = 'EUIPO dev'
PATH = "content"
TIMEZONE = 'Europe/Athens'
DEFAULT_LANG = 'en'
THEME = './theme/notmyidea'
CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True
ARTICLE_ORDER_BY = 'order'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 5
PLUGIN_PATHS = [os.getenv('PYTHON_PLUGINS_PATH')]
PLUGINS = [
    "jinja2content",
]
