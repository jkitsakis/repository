#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# --------------------------------------
# Now compatible with Pelican 4.0.x!
# --------------------------------------

# Added by me
import time

AUTHOR = 'Κωνσταντινιδου Κυριακη'
SITENAME = 'Κωνσταντινιδου Κυριακη'
SERVICES='Υπηρεσίες'
GP_SERVICES='Γενικη Ιατρικη - Συνταγογραφηση'
BOTOX_SERVICES='Αισθητική Ιατρική'

SITEURL = ""
PATH = "content"
TIMEZONE = 'Europe/Athens'
DEFAULT_DATE_FORMAT = '%d %B %Y'
CURRENT_DATE = time.strftime(DEFAULT_DATE_FORMAT)
DEFAULT_LANG = 'en-us'
THEME = './theme/doctor-blue'
FAVICON = 'favicon.ico'
# Whether to display pages on the menu of the template. Templates may or may not honor this setting.
DISPLAY_PAGES_ON_MENU = False
# Whether to display categories on the menu of the template.
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_SUMMARY = True
ARTICLE_ORDER_BY = 'order'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

NAME = 'Κωνσταντινιδου Κυριακη'
PROFESSION_DESCRIPTION ='Γενικη Οικογενειακή Ιατρός'
PROFESSION_TITLE= 'Διευθυντρια Ε.Σ.Υ'


# Blogroll
# LINKS = (
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
# )

# Social widget
# SOCIAL = (
    # ("You can add links in your config file", "#"),
    # ("Another social link", "#"),
# )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MENUITEMS = (
  ('Βιογραφικό','/pages/CV.html'),
  ('Υπηρεσίες','/pages/Services.html'),
  ('Επικοινωνια','/pages/Contact.html'),
)