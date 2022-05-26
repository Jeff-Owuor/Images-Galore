from django.urls import re_path
from artgallery.views import index,search_results
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$',index,name='newsToday'),
    re_path(r'^search/',search_results, name='search_results')
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)