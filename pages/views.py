from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from listings.models import Listing


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]     #= e d is sql
    context = {'listings' : listings }                              #same as morning    
    #pages_url = reverse('pages:index')
    return render(request,'pages/index.html', context)          #render - 一定會去templates file's pages' index

def about(request):
    return render(request,'pages/about.html')

