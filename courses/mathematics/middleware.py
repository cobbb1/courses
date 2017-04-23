__author__ = 'Administrator'

from .models import Users
from django.http import HttpResponseRedirect
from django.contrib.auth import SESSION_KEY
from urllib import quote

import re
class TokenAuthenticationMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request)
        path = request.path
        # if admin site, return position, others return None
        match = re.match("/admin/*", path, flags=0)
        # if not the admin site
        if match != None:
            response = self.get_response(request)
            return response
        if request.COOKIES.has_key("token") and request.COOKIES.has_key("userid"):
            cookietoken = request.COOKIES["token"]
            userid = request.COOKIES["userid"]
            result = Users.objects.filter(names=userid,token=cookietoken)
            if result.count() != 1:
                return HttpResponseRedirect("http://lala.ust.hk")
            else:
                pass
                response = self.get_response(request)
                return response
        else:
            return HttpResponseRedirect("http://lala.ust.hk")
