__author__ = 'Administrator'

from django.http import HttpResponse

def get_response(status,set,cookie):
    httpresponse = HttpResponse(set)
    httpresponse.status=status
    for key in cookie:
        httpresponse.set_cookie(key,cookie[key])
    return httpresponse