#!/usr/bin/env python
import web
import requests
import re
import json
import os

from config import *

from modules.samsung.samsungtv import *
from modules.orange.tvdecoder import *

urls = (
    '/','index',
    '/orange/tv', 'get_orangetv_info',
    '/orange/tv/', 'post_orangetv_action',
#    '/samsung/tv', 'get_samsung_info',
    '/samsung/tv/', 'post_samsung_action',
)


if config.get('global', 'ssl') == "yes":
  from web.wsgiserver import CherryPyWSGIServer
  CherryPyWSGIServer.ssl_certificate = config.get('global', 'ssl_certificate')
  CherryPyWSGIServer.ssl_private_key = config.get('global', 'ssl_private_key')

class HomeApiGateway(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))



@requires_auth
class index:
    def GET(self):
        return urls


if __name__ == "__main__":
    web.config.debug = True

    app = HomeApiGateway(urls, globals())
    app.run(port=int(config.get('global', 'port')))




#resp = requests.get('https://todolist.example.com/tasks/')
#if resp.status_code != 200:
    # This means something went wrong.
#    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
#for todo_item in resp.json():
#    print('{} {}'.format(todo_item['id'], todo_item['summary']))
#    http://home.pucheu.fr:8888/remoteControl/cmd?operation=01&key=116&mode
