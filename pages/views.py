from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]     #= 有[:3]先正式開動
    context = {'listings' : listings }                              #same as morning    
    #pages_url = reverse('pages:index')
    return render(request,'pages/index.html', context)          #render - 一定會去templates file's pages' index

def about(request):
    realtors_base = Realtor.objects.all()
    realtors = realtors_base.order_by('-hire_date')                #why do twice? 因為2個地要2個logic 
    mvp_realtors = realtors_base.filter(is_mvp=True)        # =show 右上角
    context = {'realtors' : realtors, 'mvp_realtors' : mvp_realtors}
    return render(request,'pages/about.html', context)          #靠key帶sql入去，入去先gen，用[:3]先動

