#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pascal Rabier'
SITENAME = 'Pascal Rabier'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

#
THEME = 'pelican-themes/pelican-blue'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/pascalrabier'),
        ('github', 'https://github.com/rabierp'),
        ('twitter', 'https://twitter.com/SWDefinedInfra'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Pelican-Blue theme parameters
SIDEBAR_DIGEST = 'Cloud Infrastructure Architect'
#FAVICON = 'url-to-favicon'
DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = '@SWDefinedInfra'
MENUITEMS = (('Blog', SITEURL),)
