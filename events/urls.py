from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from KYusers.views import *

app_name='events'

urlpatterns = [

	# url(r'^$', IndexView, name= 'index'),

]
