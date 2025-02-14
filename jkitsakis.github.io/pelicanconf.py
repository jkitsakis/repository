# pelicanconf.py

AUTHOR = 'John Kitsakis'
SITENAME = 'John Kitsakis - Resume'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/Athens'
DEFAULT_LANG = 'en'
THEME = 'themes/resume'  # Or your chosen theme
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
CATEGORY_URL = ''  # Single category URL
CATEGORY_SAVE_AS = ''  # Save path for single category pages
ARTICLE_URL = ''
ARTICLE_SAVE_AS = ''
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican_resume']  # Add this plugin if using pelican-resume

# Optional: Add your resume content markdown file path
RESUME_SRC = 'pages\\resume.md'
RESUME_PDF = 'pdfs\\resume.pdf'
RESUME_TYPE = 'moderncv'  # or 'moderncv'
#Profile information
NAME = 'Kitsakis Yannis'
TAGLINE = 'Full Stack Developer'
PIC = 'me.png'
FAVICON = 'favicon.ico'
#sidebar links
EMAIL = 'j_kitsakisk@yahoo.com'
LINKEDIN = 'ikitsakis'
GITHUB = 'jkitsakis'

CAREER_SUMMARY = 'Exprerienced Software Engineer with a demonstrated history of working in the information technology and services industry. Solid professional experience and excellent technical skills mostly with JEE standards. I have worked for a number EU and Public sector projects, implementing and delivering high quality software. Working in Intrasoft Intl, I have participated in many projects delivering e-Customs solutions for many counties like Greece, UK, Malaysia, Singapore, Thailand, FYROM, and others. Ιn previous year and beyond, I worked in e-payments services. Specifically I worked in main/core Credit Card Issuing Process application of Wirecard AG, as long as in e-Wallet application for Wirecard NZ Ltd. I had the opportunity to lead a team of 4 developers QA and BA according to Scrum (Agile) methodologies.'

SKILLS = [
	{
		'title': 'JAVA',
   		'level': '90'
   	},
  	{
  		'title': 'Spring Framework',
   		'level': '95'
   	},
    {
  		'title': 'HTML5 &amp; CSS',
  		'level': '95'
  	},
  	{
  		'title': 'Hibernate',
  		'level': '90'
  	},
  	{
  		'title': 'JPA',
  		'level': '85'
  	}
]

LANGUAGES = [
	{
		'name': 'Greek',
		'description': 'Native'
	},
	{
		'name': 'English',
		'description': 'Professional'
	}
]

INTERESTS = [
	'Coding',
	'Music'
]

EXPERIENCES = [
	{
		'job_title': 'Software Development Engineer',
		'time': 'Sep 2020 - Present',
		'company': 'Netcompany-Intrasoft',
		'details': 'Part of the web team working European Union Intellectual Property Office (EUIPO) .'
	},
	{
		'job_title': 'Software Development Engineer',
		'time': 'Mar 2019 - Aug 2020',
		'company': 'Wirecard',
		'details': 'Worked on developing  E-Payment System at Issuing Department of Wirecard.'
	},
	{
		'job_title': 'Software Engineer',
		'time': 'May 2016 - Aug 2016',
		'company': 'Intrasoft International',
		'details': 'Worked on the  Greek Customs Transit module (NCTS), Transit System for Skopje Customs (CDEPS), e-Customs Services for ASIAN Customs '
	}
]

EDUCATIONS = [
	{
		'degree': 'MSc, Computer Science',
		'meta': 'University of Wales - Swansea',
		'time': '2001 - 2002'
	},
	{
		'degree': 'Bachelor of Science (BSc), Computer Science',
		'meta': 'Hellenic Open University',
		'time': '2000'
	}
]

CERTIFICATIONS = [
	{
		'degree': 'Data Science with R Language - Credential ID 92130',
		'meta': 'University of the Aegean',
		'time': '2022'
	},
	{
		'degree': 'Python Programming - Credential ID 92262',
		'meta': 'University of the Aegean',
		'time': '2022'
	},
	{
		'degree': 'Java Platform Enterprise Edition 7 (Java EE 7) - Credential ID 8765675',
		'meta': 'Java Certification',
		'time': '2014'
	}
]


# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
#
# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
#
# DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#PROJECT_INTRO = 'You can list your side projects or open source libraries in this section. '

# PROJECTS = [
# 	{
# 		'title': 'Open Source Contributions',
# 		'tagline': 'Active contributor in FOSSASIA, worked on the Open Event project (both server and android app).Active contributor in CLTK, worked on the CLTK Web app and API.Made valuable contributions in phpBB, implemented a live search feature.Also made a few contributions to Processing.org and phpMyAdmin.'
# 	},
# 	{
# 		'title': 'Music Hub',
# 		'tagline': 'Android app that connects multiple devices via wifi and plays music in all connected devices simultaneously to create a loud stereo-like sound effect.'
# 	},
# 	{
# 		'title': 'Music Timer',
# 		'tagline': 'Android app that monitors phone’s movement to detect whether the user’s asleep and pause music playback accordingly.'
# 	}
# ]


