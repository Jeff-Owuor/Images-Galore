from django.urls import re_path
from artgallery.views import index

urlpatterns = [
    re_path(r'^$',index,name='newsToday'),
    
]