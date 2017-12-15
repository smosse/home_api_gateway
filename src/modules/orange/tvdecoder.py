import web
import requests
import json

from config import *
from auth import *
from tvdecoder_mapping import *

orange_ip = config.get('orange', 'orange_ip')


@requires_auth
class get_orangetv_info:
    def GET(self):
      try:
          r = requests.get('http://%s:8080/remoteControl/cmd?operation=10' % orange_ip , timeout=10)
          r.raise_for_status()
          output = r.content
      except requests.exceptions.HTTPError as err:
          print err
          output = "{ Oups !!! Something Goes Wrong ... }"

      return output

@requires_auth
class post_orangetv_action:
    def POST(self):
      params = json.loads(web.data())

      channel = params.get('channel', '')
      volume = params.get('volume', '')
      state = params.get('state', '')

      if channel != '':
          try:
              int(channel)
              epg_id = mapping[channel]
              try:
                  r = requests.get('http://%s:8080/remoteControl/cmd?operation=09&epg_id=%s&uui=1' % ( orange_ip , epg_id))
                  r.raise_for_status()
                  output = r.content
              except requests.exceptions.HTTPError as err:
                  print err
                  output = "{ Oups !!! Something Goes Wrong ... }"
              return output
          except:
              key = mapping[channel]
              try:
                  r = requests.get('http://%s:8080/remoteControl/cmd?operation=01&key=%s&mode=0' % ( orange_ip , key))
                  r.raise_for_status()
                  output = r.content
              except requests.exceptions.HTTPError as err:
                  print err
                  output = "{ Oups !!! Something Goes Wrong ... }"
              return output
