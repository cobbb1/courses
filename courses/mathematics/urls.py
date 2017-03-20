__author__ = 'Administrator'


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^questions$' , views.index, name="zc"),
    url(r'^neurons$' , views.indexz, name="zcq"),
    url(r'^$' , views.index, name="zc"),
    url(r'^preview$',views.preview, name='preview'),
    url(r'^questions/all$', views.allquestion, name='allquestion'),
    url(r'^questions/(?P<code>.+)$', views.get, name='index'),
    url(r'^previewneurons$', views.getneuron, name='index')

]