from unicodedata import category
from django.shortcuts import render
from .models import ImageCategory, Images,ImageLocation
from django.core.exceptions import ObjectDoesNotExist
from django.http  import Http404

def index(request):
    return render(request,'art_gallery/index.html',{"locations":ImageLocation.objects.all()})

def all_categories(request):
    return render(request,'art_gallery/all_categories.html',{"locations":ImageLocation.objects.all()})

def single_image(request,image_id):
    try:
        image = Images.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"art_gallery/single_image.html", {"image":image})

def CategoryOneView(request):
    category_posts = Images.objects.filter(image_category=1)
    return render(request,'art_gallery/categories.html',{"category_posts":category_posts})

def CategoryTwoView(request):
    category_posts = Images.objects.filter(image_category=2)
    return render(request,'art_gallery/categories.html',{"category_posts":category_posts})

def CategoryThreeView(request):
    category_posts = Images.objects.filter(image_category=3)
    return render(request,'art_gallery/categories.html',{"category_posts":category_posts})



def search_results(request):
    
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = ImageCategory.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'art_gallery/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'art_gallery/search.html',{"message":message})
# Create your views here.
