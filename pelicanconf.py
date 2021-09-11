#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Julio Martinez'
SITENAME = 'Juliomdev'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Caracas'

DEFAULT_LANG = 'es'

THEME = 'basic'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True

PLUGIN_PATHS = [
    'plugins'
]

PLUGINS = [
    'pelican-cover-image'
]

COVER_IMAGES_PATH = "images"
STATIC_PATHS = ["images"]

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('instagram', 'https://www.instagram.com/juliomdev'),
    ('github', 'https://github.com/oilujc'),
    ('linkedin', 'https://www.linkedin.com/in/julio-martinez-valero-763567153/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
