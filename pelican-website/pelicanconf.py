#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time

LOCAL_BUILD = True
SITEURL = '' if LOCAL_BUILD else '/pelican/sandy'

PATH = "content"
TIMEZONE = 'Europe/Athens'
DEFAULT_DATE_FORMAT = '%d %B %Y'
CURRENT_DATE = time.strftime(DEFAULT_DATE_FORMAT)
DEFAULT_LANG = 'en-us'

THEME = './theme/doctor-blue'
AVATAR = 'avatar.ico'
FAVICON = 'favicon.ico'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_SUMMARY = True
DISPLAY_FOOTER = False
DISPLAY_ASIDE_FOOTER = True
ARTICLE_ORDER_BY = 'order'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False

SITENAME = 'Προσωπικος Ιατρος'
NAME = 'Κωνσταντινιδου Κυριακη'
PROFESSION_DESCRIPTION ='Γενικη Οικογενειακή Ιατρός'
PROFESSION_TITLE= 'Διευθυντρια Ε.Σ.Υ'
MOBILE = '690XXXXXX'
EMAIL = 'prosopiki.iatros@gmail.com'
ADDRESS = 'prosopiki.iatros address'
SERVICE_EOPPY='Συνταγογραφηση ΕΟΠΠΥ'
SERVICE_EXAMS='Εξετασεις - Παραπεμπτικά'
SERVICE_BOTOX= 'Αισθητικές Επεμβάσεις'
SERVICES='Υπηρεσίες'
GP_SERVICES='Γενικη Ιατρικη - Συνταγογραφηση'
BOTOX_SERVICES='Αισθητική Ιατρική'
SCROLL_MSG='Ανακοινωσεις - ...'

MENUITEMS = (
  ('Υπηρεσίες',SITEURL+'/pages/Services.html'),
  ('Επικοινωνια',SITEURL+'/pages/Contact.html'),
  ('Βιογραφικό',SITEURL+'/pages/CV.html')
)