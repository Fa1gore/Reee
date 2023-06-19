AUTHOR = 'fa1gore'
SITENAME = 'Reee'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'


#Template engine configuration, If its not explicitly set,
#Pelican will use the Jina2 default index.html and generate one in your root subdirectory

#TEMPLATE_PAGES = {'templates/index.html': 'index.html'}

#THEME = 'themes/basicbitch'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Output articles in the "articles" subdirectory
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
