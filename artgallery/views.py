from django.shortcuts import render

def index(request):
    return render(request,'artgallery/index.html',{"Title":"money men"})

# Create your views here.
