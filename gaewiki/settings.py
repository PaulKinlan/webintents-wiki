# encoding=utf-8

import model
import util


SETTINGS_PAGE_NAME = 'gaewiki:settings'

DEFAULT_SETTINGS = """title: My Wiki
start_page: Welcome
admin_email: nobody@example.com
sidebar: gaewiki:sidebar
footer: gaewiki:footer
open-reading: yes
open-editing: no
editors: user1@example.com, user2@example.com
interwiki-google: http://www.google.ru/search?sourceid=chrome&ie=UTF-8&q=%s
interwiki-wp: http://en.wikipedia.org/wiki/Special:Search?search=%s
---
# gaewiki:settings

Edit me."""

settings = None

def get_all():
    global settings
    if settings is None:
        page = model.WikiContent.gql('WHERE title = :1', SETTINGS_PAGE_NAME).get()
        if page is None:
            page = model.WikiContent(title=SETTINGS_PAGE_NAME, body=DEFAULT_SETTINGS)
            page.put()
        settings = util.parse_page(page.body)
    return settings

def get(key, default_value=None):
    return get_all().get(key, default_value)


def flush():
    global settings
    settings = None
