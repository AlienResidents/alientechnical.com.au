from pelicanconf import *

from datetime import datetime

AUTHOR = 'Chrispy'
SITENAME = 'Alien Technical Consulting'
SITETITLE = 'Alien Technical'
SITEURL = ""
#SITEURL = "https://alientechnical.com.au"

#SITESUBTITLE = "Web Developer"
SITEDESCRIPTION = "Alien Technical News and Blog"
SITELOGO = SITEURL + "/images/site-logo.png"
FAVICON = SITEURL + "/images/favicon.ico"

PATH = "content"

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'en'
DATE_FORMATS = {
    "en": "%Y/%m/%d",
}

DISABLE_URL_HASH = True

COPYRIGHT_YEAR = datetime.now().year
ROBOTS = "index, follow"
MAIN_MENU = True
MENUITEMS = (
    ("Services", "/services.html"),
    ("Tags", "/tags.html"),
    ("Categories", "/categories.html"),
    ("Archives", "/archives.html"),
)

BROWSER_COLOR = "#333333"
THEME = 'Flex'
THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
PYGMENTS_STYLE_DARK = 'monokai'
PYGMENTS_STYLE= 'default'
PYGMENTS_RST_OPTIONS = {"linenos": "table"}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = "http://github.com/alienresidents/"

GITHUB_CORNER_URL = "http://github.com/alienresidents/"

LINKS_IN_NEW_TAB = True
LINKS = (
    ("Resume", "https://docs.google.com/document/d/1mylgxMiPIjgMZYflaXA6Eo-cUP3waT8u-9QwAhQNnTM"),
)

SOCIAL = (
    ("github", "http://github.com/alienresidents/"),
    ("linkedin", "https://www.linkedin.com/in/alienresidents/"),
    ("envelope", 'mailto:chrispy@alientechnical.com.au'),
)

DEFAULT_PAGINATION = 10

OG_LOCALE = "en_GB"
LOCALE = "en_GB"
I18N_TEMPLATES_LANG = "en"


#
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
#
#BROWSER_COLOR = "#333"
#
#
#STATIC_PATHS = ["extra/custom.css"]
#
#EXTRA_PATH_METADATA = {
#    "extra/custom.css": {"path": "static/custom.css"},
#}
#
#CUSTOM_CSS = "static/custom.css"
#
#
#ADD_THIS_ID = "ra-77hh6723hhjd"
#DISQUS_SITENAME = "yoursite"
#GOOGLE_ANALYTICS = "UA-1234-5678"
#GOOGLE_TAG_MANAGER = "GTM-ABCDEF"
#
## Enable i18n plugin.
#PLUGINS = ["i18n_subsites"]
## Enable Jinja2 i18n extension used to parse translations.
#JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
#
# Translate to German.
#DEFAULT_LANG = "de"
#OG_LOCALE = "de_DE"
#LOCALE = "de_DE"

# Default theme language.
#I18N_TEMPLATES_LANG = "en"
#
## Pelican-search Configuration
#STORK_INPUT_OPTIONS = {"stemming": "German", "url_prefix": SITEURL}
