from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    pages_url = reverse('pages:index')
    return render(request,'pages/index.html')          #render - 一定會去templates file's pages' index

def about(request):
    return render(request,'pages/about.html')

