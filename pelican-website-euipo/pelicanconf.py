from __future__ import unicode_literals

LOCAL_BUILD = False
SITEURL = '' if LOCAL_BUILD else '/euipo'
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

STATIC_PATHS = ['images', 'favicon.ico']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['inject_constants', 'minify']

#values like SITEURL will be globally accessible in all Jinja templates.
JINJA_GLOBALS = {
    'SITEURL': SITEURL
}

MENUITEMS = [
    ("APIs", SITEURL+'/apis.html'),
    ("Tutorials", SITEURL+'/tutorials.html')
]

DISPLAY_CATEGORIES_ON_MENU = False
#
# # APIs - ENVs
# aws_dev = 'https://dev-www.euipo.europa.eu'
# aws_pp = 'https://pp-www.euipo.europa.eu'
# aws_test = 'https://test-www.euipo.europa.eu'
# aws_dev1 = 'https://dev-eutm.euipo.europa.eu'
# aws_pp1 = 'https://pp-eutm.euipo.europa.eu'
# aws_test1 = 'https://test-eutm.euipo.europa.eu'
#
# # APIs - EOPWA
# EOPWA_PREFIX_DEV='dev'
# EOPWA_PREFIX_TEST='test'
# EOPWA_PREFIX_PROD='production'
# EOPWA_NETWORK_AWS='nonprod.aws.oami.eu'
# EOPWA_NETWORK_AWS_PROD='prod.aws.oami.eu'
# APPEALS_SEARCH_EOPW_URI = 'eop/appeals-search'
# APPEALS_SEARCH_APPLICATION_NAME='appeals-search-api'
# COMMUNICATIONS_SEARCH_EOPW_URI = 'eop/communications/'
# COMMUNICATIONS_SEARCH_APPLICATION_NAME = 'communications-api'
# DESIGNS_SEARCH_EOPW_URI = 'eop/design-search/'
# DESIGNS_SEARCH_APPLICATION_NAME = 'design-search-api'
# DRAFTS_SEARCH_EOPW_URI = 'eop/drafts'
# DRAFTS_SEARCH_APPLICATION_NAME = 'drafts-api'
# FEEDBACK_SEARCH_EOPW_URI = 'eop/feedback/surveys/:indentifier'
# FEEDBACK_SEARCH_APPLICATION_NAME = 'feedback-api'
# INTERPARTES_SEARCH_EOPW_URI = 'eop/interpartes-search'
# INTERPARTES_SEARCH_APPLICATION_NAME = 'interpartes-search-api'
# NOTES_SEARCH_EOPW_URI = 'eop/notes/'
# NOTES_SEARCH_APPLICATION_NAME = 'notes-api'
# PRE_ASSESEMENT_SEARCH_EOPW_URI = 'eop/pre-assessment/'
# PRE_ASSESEMENT_SEARCH_APPLICATION_NAME = 'pre-assessment-api'
# USER_PROFILE_EOPW_URI = 'eop/user-profile/'
# USER_PROFILE_APPLICATION_NAME = 'user-profile-api'
#
# # APIs - EOPW
# EOPW_PREFIX_DEV='dev'
# EOPW_PREFIX_TEST='test'
# EOPW_PREFIX_PROD='production'
# EOPW_NETWORK_AWS='nonprod.aws.oami.eu'
# EOPW_NETWORK_AWS_PROD='prod.aws.oami.eu'
# WEBSITE_BE_APPLICATION_NAME='website-backend'
# WEBSITE_BE_EOPW_URI = 'portal/app/api'
# ADMIN_TOOL_EOPW_URI = 'eop/admintool/app/api/'
# ADMIN_TOOL_APPLICATION_NAME = 'eop-admintool-backend'
# STORY_BLOK_EOPW_URI = 'eop/storyblok/'
# STORY_BLOK_APPLICATION_NAME = 'storyblok-api'
#
# # APIs - EEA
# EEA_PREFIX_DEV='dev'
# EEA_PREFIX_TEST='test'
# EEA_PREFIX_PROD='production'
# EEA_NETWORK_AWS='nonprod.aws.oami.eu'
# EEA_NETWORK_AWS_PROD='prod.aws.oami.eu'
# EUTM_SEARCH_API_EOPW_URI = 'eop/eutm-search/trademarks?'
# EUTM_SEARCH_API_APPLICATION_NAME='eutm-search-api'
# EUTM_FILING_API_EOPW_URI = 'filing/api/'
# EUTM_FILING_API_APPLICATION_NAME = 'eutm-filing-api'
#
# # APIs -EEE
# EEE_PREFIX_DEV='dev'
# EEE_PREFIX_TEST='test'
# EEE_PREFIX_PROD='production'
# EEE_NETWORK_AWS='nonprod.aws.oami.eu'
# EEE_NETWORK_AWS_PROD='prod.aws.oami.eu'
# EUTM_EFORMS_EOPW_URI = 'eutm-efiling/app/api/'
# EUTM_EFORMS_APPLICATION_NAME='eutm-eform-backend'
#
# # APIs - EMEA
# EMEA_PREFIX_DEV='dev'
# EMEA_PREFIX_TEST='test'
# PREFIX_PROD='production'
# NETWORK_AWS='nonprod.aws.oami.eu'
# NETWORK_AWS_PROD='prod.aws.oami.eu'
# ME_API_EOPW_URI = 'eop/me/'
# ME_API_APPLICATION_NAME='me-api'
#
# # APIs - EPA
# EPA_PREFIX_DEV='dev'
# EPA_PREFIX_TEST='test'
# EPA_PREFIX_PROD='production'
# EPA_NETWORK_AWS='nonprod.aws.oami.eu'
# EPA_NETWORK_AWS_PROD='prod.aws.oami.eu'
# EUTM_SEARCH_API_APPLICATION_NAME='persons-api'
# EUTM_SEARCH_API_EOPW_URI = 'eop/persons/applicants?name=S%26P'
#
# # APIs - IPT
# PROCEEDING_SEARCH_API_EOPW_URI = 'search?query=type==RCD'
# PROCEEDING_SEARCH_API_PREFIX_DEV='dev'
# PROCEEDING_SEARCH_API_PREFIX_TEST='test'
# PROCEEDING_SEARCH_API_PREFIX_PREPROD='pp'
# PROCEEDING_SEARCH_API_PREFIX_PROD='production'
# PROCEEDING_SEARCH_API_APPLICATION_NAME='api.dev.oami.eu/proceeding-search-api'
# PROCEEDING_SEARCH_API_NETWORK_AWS='nonprod.aws.oami.eu'
# PROCEEDING_SEARCH_API_NETWORK_AWS_PROD='prod.aws.oami.eu'
#
#
# INFRASTRUCTURE_MICROSERVICES_GENERATOR_URI = 'eop/document-generator'
# INFRASTRUCTURE_MICROSERVICES_REPOSITORY_URI = 'eop/document-repository'
# INFRASTRUCTURE_MICROSERVICES_PREFIX_DEV='dev'
# INFRASTRUCTURE_MICROSERVICES_PREFIX_TEST='test'
# INFRASTRUCTURE_MICROSERVICES_PREFIX_PREPROD='pp'
# INFRASTRUCTURE_MICROSERVICES_PREFIX_PROD='production'
# INFRASTRUCTURE_MICROSERVICES_GENERATOR_APP_NAME='document-generator'
# INFRASTRUCTURE_MICROSERVICES_REPOSITORY_APP_NAME='document-repository'
# INFRASTRUCTURE_MICROSERVICES_NETWORK_AWS='nonprod.aws.oami.eu'
# INFRASTRUCTURE_MICROSERVICES_NETWORK_AWS_PROD='prod.aws.oami.eu'
#
# # APIs - EDA
# DESIGN_FILING_API_EOPW_URI = 'eop/design-filing/'
# DESIGN_FILING_API_PREFIX_DEV='dev'
# DESIGN_FILING_API_PREFIX_TEST='test'
# DESIGN_FILING_API_PREFIX_PROD='production'
# DESIGN_FILING_API_APPLICATION_NAME='design-filing-api'
# DESIGN_FILING_API_NETWORK_AWS='nonprod.aws.oami.eu'
# DESIGN_FILING_API_NETWORK_AWS_PROD='prod.aws.oami.eu'
#
# EGA_PREFIX_DEV='dev'
# EGA_PREFIX_TEST='test'
# EGA_PREFIX_PROD='production'
# EGA_NETWORK_AWS='nonprod.aws.oami.eu'
# EGA_NETWORK_AWS_PROD='prod.aws.oami.eu'
# GS_API_URI = 'ega/gs-api'
# GS_API_APPLICATION_NAME='gs-api'
# GS_LISTS_URI = 'ega/gs-lists/'
# GS_LISTS_APPLICATION_NAME = 'gs-lists'
# GS_LOADER_URI = 'ega/gs-loader/'
# GS_LOADER_APPLICATION_NAME = 'gs-loader'