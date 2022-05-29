from django.urls import re_path,path
from artgallery.views import index,search_results,single_image,CategoryOneView,CategoryTwoView,CategoryThreeView,all_categories
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$',index,name='newsToday'),
    re_path(r'^search/',search_results, name='search_results'),
    re_path(r'^image/(\d+)',single_image, name = 'single_image'),
    path('category/1/', CategoryOneView ,  name='category_one'),
    path('category/2/', CategoryTwoView ,  name='category_two'),
    path('category/3/', CategoryThreeView ,  name='category_three'),
    path('all', all_categories ,  name='all_categories'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)