AUTHOR = 'Regents of the University of California, Broad Institute, MIT'
SITENAME = 'GenePattern'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_PATHS = ['pages', 'modules']
STATIC_PATHS = ['uploaded']

DEFAULT_DATE_FORMAT = ("%A, %B %d, %Y at %I:%M%p")

#INDEX_URL = '/'
#INDEX_SAVE_AS = 'pages/landing.html'
INDEX_URL = 'blog/'
INDEX_SAVE_AS = 'blog/index.html'
DIRECT_TEMPLATES = ['index', 'archives', 'tags', 'categories']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

THEME = "theme"

# Unused template variables
LINKS = ()
SOCIAL = ()

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Sitemap plugin configuration
PLUGINS = ['pelican.plugins.sitemap']

# Primary XML sitemap with metadata (priorities and change frequencies)
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.4,
        'indexes': 0.5,
        'pages': 0.8,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
