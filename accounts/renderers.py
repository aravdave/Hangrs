import json
import sys
sys.path.append("..")

from rest_framework.renderers import JSONRenderer
from core.renderers import HangrsJSONRenderer

class UserJSONRenderer(HangrsJSONRenderer):

    def render(self, data, media_type=None, renderer_context=None):
        
        token = data.get('token', None)
        
        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        return super(UserJSONRenderer, self).render(data)
        
class ProfileJSONRenderer(HangrsJSONRenderer):
    object_label = 'profile'

