#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jelmer Vernooij'
SITENAME = 'Xandikos'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Etc/UTC'

DEFAULT_LANG = 'en'

THEME = 'pjport'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
PLUGIN_PATHS = ['plugins', 'sitemap', 'assets']

# Blogroll
LINKS = (('Code', 'https://jelmer.uk/code/xandikos'),
         ('GitHub', 'https://www.github.com/jelmer/xandikos'))

# Social widget
SOCIAL = (
)

DEFAULT_PAGINATION = 10

# Menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('', ''), # this item is to show link on top and bottom of page
)

#
# SITEMAP PLUGIN
#
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_DATE_FORMAT = ('- %d -<br/>%B<br/>%Y')

STATIC_PATHS = []
EXTRA_PATH_METADATA = {}

# about me
ABOUT_ME = None # showed on left side of footer

# contacts
CONTACT_EMAIL = 'jelmer@jelmer.uk'
CONTACT_PHONE = None
CONTACT_CITY = None

# GOOGLE ANALYTICS (set to  None if don't want it)
GOOGLE_ANALYTICS = None
