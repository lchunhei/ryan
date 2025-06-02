from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def index(request):
    listings = Listing.objects.all()          #由model's class Listing 拎database ;  (每禁一次，都會行一次，for show most updated info)
    paginator = Paginator(listings, 3)        #對於backend 用pagc分件上面data (listings's model 全部key為一組) 
    page = request.GET.get('page')            #從frontend咩page, 知道邊份    #GET係method,  var=page, 
    paged_listings = paginator.get_page(page)  #back front 結合，選擇邊一份放入website     
    context = {'listings' : paged_listings}                         #左=key(隨便比), 右=value(database) -> 之後listings.html會用database既listings
    return render (request, 'listings/listings.html', context)      #context係動態數據（已經入左listings.html)

def listing(request,listing_id):                #listing_id 係sql自動gen
    listing = get_object_or_404(Listing,pk=listing_id)   #object=manager; Listing=database + search by id; ***no need all database, only need 1 record
    context = {'listing' : listing}                     #no for loop, naming:listing no need +s
    return render (request, 'listings/listing.html', context)


def search(request):
    return render (request, 'listings/search.html')

