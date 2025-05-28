from django.urls import path
from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.index, name = 'listings'),
    path('<int:listing_id>', views.listing, name = 'listing'),     #url叫no (s) ->  goto database get id
    path('search', views.search, name='search'),             #左邊ur叫lsearch ; 右邊for 之後 {% url 'listings:search' %}
]

