from django.conf import settings as django_settings
from magi.default_settings import DEFAULT_ENABLED_PAGES
from circles import models

SITE_NAME = 'Circles'
SITE_URL = 'http://circles.com/'
SITE_IMAGE = 'circles.png'
SITE_STATIC_URL = '//localhost:{}/'.format(django_settings.DEBUG_PORT) if django_settings.DEBUG else '//i.circles.com/'
GAME_NAME = 'various games'
DISQUS_SHORTNAME = None
ACCOUNT_MODEL = models.Account
COLOR = '#32D5CC'

ENABLED_PAGES = DEFAULT_ENABLED_PAGES

ENABLED_PAGES['index']['enabled'] = True
for _p in ENABLED_PAGES['about']:
    _p['enabled'] = False
ENABLED_PAGES['map']['enabled'] = False

SHOW_TOTAL_ACCOUNTS = False
