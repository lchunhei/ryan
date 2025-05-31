from django.shortcuts import render
from listings.models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def index(request):
    listings = Listing.objects.all()          # from sql拎all   每禁一次，都會行一次，for show most updated info
    paginator = Paginator(listings, 3)        #from sql , 分件   #先上面拎data, 經過PAG分類;  (）係class, 3間為一組
    page = request.GET.get('page')            #from font come back, 知道邊份    #GET係method,  var=page, 
    paged_listings = paginator.get_page(page)   #選擇邊一份，放入website     #from sq拎咩,       右邊page= no.;  其實係用上面 (9)paginator.get_page(page 10)
    context = {'listings' : paged_listings}                         #dictionary
    return render (request, 'listings/listings.html', context)


def listing(request,listing_id):                #listing_id 係sql自動gen
    return render (request, 'listings/listing.html')


def search(request):
    return render (request, 'listings/search.html')

