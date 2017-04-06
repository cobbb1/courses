__author__ = 'Administrator'

from mathematics.server.action.create import create
from mathematics.server.ontoken import gettokens

class actionm(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if "/admin" in request.path:
            return response
        z = gettokens(request)
        if z=="":
            return response
        else:
            create(request,response,z)
            return response

        # Code to be executed for each request/response after
        # the view is called.

