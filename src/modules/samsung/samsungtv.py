import socket
import fcntl
import struct
import base64
import time, datetime
import web
import requests
import json
import uuid

from auth import *
from config import *

def get_mac_address():
    return ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])

tvip = "192.168.64.7"
appstring = "iphone..iapp.samsung" #NE PAS CHANGER#
tvappstring = "iphone.%s.iapp.samsung" % config.get('samsung', 'tv_model') #REFERENCE A CHANGER SUIVANT VOTRE TV#
remotename = "Python Samsung Remote"

@requires_auth
class post_samsung_action:
    def POST(self):
        params = json.loads(web.data())

        key = params.get('key', '')

        if key != '':

            #declaration du socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((tvip, 55000))
            source_ip = sock.getsockname()[0]

            #Initiation de la connexion
            ipencoded = base64.b64encode(source_ip)
            macencoded = base64.b64encode(get_mac_address())
            messagepart1 = chr(0x64) + chr(0x00) + chr(len(ipencoded)) + chr(0x00) + ipencoded + chr(len(macencoded)) + chr(0x00) + macencoded + chr(len(base64.b64encode(remotename))) + chr(0x00) + base64.b64encode(remotename)

            part1 = chr(0x00) + chr(len(appstring)) + chr(0x00) + appstring + chr(len(messagepart1)) + chr(0x00) + messagepart1
            sock.send(part1)

            messagepart2 = chr(0xc8) + chr(0x00)
            part2 = chr(0x00) + chr(len(appstring)) + chr(0x00) + appstring + chr(len(messagepart2)) + chr(0x00) + messagepart2
            sock.send(part2)
            try:
                sendKey(key,sock,tvappstring) #Pause #
                output = "{ OK  }"
            except:
                output = "{ Oups !!! Something Goes Wrong ... }"
            time.sleep(1) #Attente d une seconde avant la prochaine touche#

            # Fermeture du socket
            sock.close()
            return output

# Fonction d'envoi
def sendKey(skey, dataSock, appstring):
    messagepart3 = chr(0x00) + chr(0x00) + chr(0x00) + chr(len(base64.b64encode(skey))) + chr(0x00) + base64.b64encode(skey);
    part3 = chr(0x00) + chr(len(appstring)) + chr(0x00) + appstring + chr(len(messagepart3)) + chr(0x00) + messagepart3
    dataSock.send(part3);

#KEY_0', # --TOUCHE 0
#'KEY_1', # --TOUCHE 1
#'KEY_2', # --TOUCHE 2
#'KEY_3', # --TOUCHE 3
#'KEY_4', # --TOUCHE 4
#'KEY_5', # --TOUCHE 5
#'KEY_6', # --TOUCHE 6
#'KEY_7', # --TOUCHE 7
#'KEY_8', # --TOUCHE 8
#'KEY_9', # --TOUCHE 9
#'KEY_UP', # --CROIX HAUT
#'KEY_DOWN', # --CROIX BAS
#'KEY_LEFT', # --CROIX GAUCHE
#'KEY_RIGHT', # --CROIX DROITE
#'KEY_MENU', # --TOUCHE MENU
#'KEY_PRECH', # --TOUCHE PRE-CH
#'KEY_GUIDE', # --TOUCHE GUIDE
#'KEY_INFO', # --TOUCHE INFO
#'KEY_RETURN', # --TOUCHE RETURN
#'KEY_CH_LIST', # --TOUCHE CH LIST
#'KEY_EXIT', # --TOUCHE EXIT
#'KEY_ENTER', # --CROIX ENTER
#'KEY_SOURCE', # --TOUCHE SOURCE
#'KEY_AD'
#'KEY_PLAY', # --TOUCHE PLAY
#'KEY_PAUSE', # --TOUCHE PAUSE
#'KEY_MUTE', # --TOUCHE MUTE
#'KEY_PICTURE_SIZE', # --
#'KEY_VOLUP', # --TOUCHE VOL +
#'KEY_VOLDOWN', # --TOUCHE VOL -
#'KEY_TOOLS', # --TOUCHE TOOLS
#'KEY_POWEROFF', # --TOUCHE POWEROFF
#'KEY_CHUP', # --TOUCHE PROG +
#'KEY_CHDOWN', # --TOUCHE PROG -
#'KEY_CONTENTS', # --TOUCHE SMART HUB
#'KEY_W_LINK', # --TOUCHE Media P
#'KEY_RSS', # --TOUCHE Internet
#'KEY_MTS', # --TOUCHE Dual
#'KEY_CAPTION', # --TOUCHE Subt
#'KEY_REWIND', # --TOUCHE <>
#'KEY_REC',
#'KEY_STOP' ]) # --TOUCHE STOP
