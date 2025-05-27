from django.urls import path
from . import views     #. = current directory = pages


app_name = 'pages'          #所以下面唔使page.index

urlpatterns = [
   path('', views.index, name='index'),         #index作用：要黎做_navbar既endpoint
   path('about', views.about, name='about'),        #左邊about: www./about


]

