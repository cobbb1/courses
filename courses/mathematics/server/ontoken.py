__author__ = 'Administrator'





from mathematics.models import Users
import re

def gettokens(request):
    if request.COOKIES.has_key("token")==0:
        w = re.findall("/users/(?P<token>.+?)",request.path)
        if len(w)==0:
            return ""
        else:
            token = w[0]
    else:
        token = request.COOKIES["token"]
    print(1)
    z = Users.objects.filter(token=token)
    if z.count()==0:
        print("3")
        return ""
    else:
        return z[0].id