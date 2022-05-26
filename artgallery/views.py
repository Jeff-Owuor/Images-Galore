from django.shortcuts import render
from .models import Images,ImageLocation

def index(request):
    images = Images.all_images()
    
    
    return render(request,'art_gallery/index.html',{"images":images})

# Create your views here.
