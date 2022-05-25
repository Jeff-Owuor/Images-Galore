from django.shortcuts import render
from .models import Images,ImageLocation

def index(request):
    
    images = Images.all_images()
    locations = ImageLocation.locations()
    return render(request,'art_gallery/index.html',{"images":images,"locations":locations})

# Create your views here.
