from django.shortcuts import render

def index(request):
    return render(request,'art_gallery/index.html',{"Title":"money men"})

# Create your views here.
