from django.shortcuts import render
from .models import ImageCategory, Images,ImageLocation

def index(request):
    images = Images.all_images()
    
    return render(request,'art_gallery/index.html',{"images":images})


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
