from django.urls import re_path,path
from artgallery.views import index,search_results,CategoryView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$',index,name='newsToday'),
    re_path(r'^search/',search_results, name='search_results'),
    path('category/<int:cats>/', CategoryView ,  name='category')
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)