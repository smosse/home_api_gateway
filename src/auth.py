import web
import re
import base64

from functools import wraps
from config import *

###############################################################################
#                      BASIC AUTH                                             #
###############################################################################

def check_auth(username, password):
    return username == config.get('global', 'username') and password == config.get('global', 'password')


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = web.ctx.env['HTTP_AUTHORIZATION'] if 'HTTP_AUTHORIZATION' in  web.ctx.env else None
        if auth:
            auth = re.sub('^Basic ', '', auth)
            username, password = base64.decodestring(auth).split(':')
        if not auth or not check_auth(username, password):
            web.header('WWW-Authenticate', 'Basic realm="admin"')
            web.ctx.status = '401 Unauthorized'
            return Unauthorized()

        return f(*args, **kwargs)

    return decorated

class Unauthorized():
    def GET(self):
        return "401 Unauthorized"

    def POST(self):
        return "401 Unauthorized"
