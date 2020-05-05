from django.conf.urls import url,include

from django.contrib import admin
from  DemoApp import views #.views import hello
from django.urls import path,include


urlpatterns = [
url(r'^hello/',views.hello,name='hello'),
url(r'^index/',views.index,name='index'),
url (r'^showNumber/(\S+)/',views.showNumber),
]

"""urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello/',hello,name='hello'),
    #path('DemoApp/',include('DemoApp.url'))


]
"""
