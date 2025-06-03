from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . choices import price_choices,bedroom_choices,district_choices

# Create your views here.


def index(request):
    listings = Listing.objects.all()          #由model's class Listing 拎database ;  (每禁一次，都會行一次，for show most updated info)
    paginator = Paginator(listings, 3)        #對於backend 用pagc分件上面data (listings's model 全部key為一組) 
    page = request.GET.get('page')            #從frontend咩page, 知道邊份    #GET係method,  var=page, 
    paged_listings = paginator.get_page(page)  #back front 結合，選擇邊一份放入website     
    context = {'listings' : paged_listings}     #左=key(隨便比), 右=value(database) -> 之後listings.html會用database既listings
    return render (request, 'listings/listings.html', context)      #context係動態數據（已經入左listings.html)

def listing(request,listing_id):                #listing_id 係sql自動gen
    listing = get_object_or_404(Listing,pk=listing_id)   #object=manager; Listing=database + search by id; ***no need all database, only need 1 record
    context = {'listing' : listing}                     #因noneed for loop, naming:listing no need +s
    return render (request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')           #拎data; 不會exe, 直至有list/{}->先做野[from sql to vari]
                                                                        #地址顯示&keyword=value  會用request object function
    if 'keywords' in request.GET:                                   #'keywords' related to search.html ; if 佢有輸入＝個variable keywords有野      
        keywords = request.GET['keywords']                          #-> 拎value
        if keywords:                                                   #如有野先下一步
            queryset_list = queryset_list.filter(description__icontains=keywords)    #用description=fied; icontain=有依個字 
    
    if 'title' in request.GET:
        title = request.GET['title']
        if title:   
            queryset_list = queryset_list.filter(title__icontains=title)           # all會累積，keywords&title

    if 'district' in request.GET:
        district = request.GET['district']
        if district:   
            queryset_list = queryset_list.filter(district__iexact=district)     #district因為唔使打,選擇：要exact

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:   
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)     #因int:less than or eq to

    if 'price' in request.GET:
        price = request.GET['price']
        if price:   
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
               'price_choices' : price_choices,                     #加入context入面, FOR SEARCH FIELD
               'bedroom_choices' : bedroom_choices,
               'district_choices' : district_choices,
               'listings' : queryset_list, 'values' : request.GET}     #用s因為唔係得一間; value pass back to text field
    

    return render (request, 'listings/search.html', context)

