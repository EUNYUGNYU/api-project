from django.shortcuts import render
from .models import Photo

# Create your views here.

def home(request):
    blogs=Photo.objects
    return render(request, 'home.html',{'blogs':blogs})