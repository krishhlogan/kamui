
from django.urls import path,include
from .views import *

API_VERSION = 'api/v0/'

urlpatterns = [
    path('store/',store_file,name='store')
]
