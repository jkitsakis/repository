#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time

LOCAL_BUILD = False
SITEURL = '' if LOCAL_BUILD else '/pelican/sandy'

PATH = "content"
TIMEZONE = 'Europe/Athens'
DEFAULT_DATE_FORMAT = '%d %B %Y'
CURRENT_DATE = time.strftime(DEFAULT_DATE_FORMAT)
DEFAULT_LANG = 'el'

THEME = './theme/doctor-blue'
AVATAR = 'avatar.ico'
FAVICON = 'favicon.ico'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_SUMMARY = False
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
PROFESSION_DESCRIPTION ='Γενικη Οικογενειακη Ιατρος'
PROFESSION_TITLE= 'Διευθυντρια Ε.Σ.Υ'

SCROLL_MSG='Η ιστοσελίδα ειναι υπο κατασκευή'
MOBILE = '690XXXXXX'
EMAIL = 'prosopiki.iatros@gmail.com'
ADDRESS = 'prosopiki.iatros address'
SERVICES='Υπηρεσίες'
SERVICE_EOPYY='Υπηρεσίες ΕΟΠΥΥ'
SERVICE_ASSISTANCE='Κατ’ οίκον Φροντίδα'
SERVICE_BOTOX= 'Αισθητικές Επεμβάσεις'
SERVICE_CERTIFICATES='Έκδοση Ιατρικών Πιστοποιητικών & Βεβαιώσεων'
SERVICE_EMERGENCY='Επείγoντα Περιστατικά'
SERVICE_PREVENTIVE_MEDICINE='Προληπτική Ιατρική'
SERVICE_CHRONIC_DISEASE='Χρόνιες Παθήσεις'

GP_SERVICES='Γενικη Ιατρικη - Συνταγογραφηση'
BOTOX_SERVICES='Αισθητική Ιατρική'
OPERATION_HOURS='Ωρες Λειτουργιας'
OPERATION_DAYS_GROUP_1='Δευ-Παρ'
OPERATION_HOURS_GROUP_1='08:00 - 14.30'
OPERATION_DAYS_GROUP_2='Σαβ'
OPERATION_HOURS_GROUP_2='09:00 - 14.30'
EMERGENCY_CASES='Έκτακτες Περιπτώσεις'
RANDEVOUZ='ΚΛΕΙΣTΕ ΡΑΝΤΕΒΟΥ'

MENUITEMS = (
  ('Υπηρεσιες',SITEURL+'/pages/Services.html'),
  ('Επικοινωνια',SITEURL+'/pages/Contact.html'),
  ('Βιογραφικο',SITEURL+'/pages/CV.html')
)