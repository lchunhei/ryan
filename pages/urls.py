from django.urls import path
from . import views     #. = current directory = pages


app_name = 'pages'          #所以下面唔使page.index

urlpatterns = [
   path('', views.index, name='index'),         #右邊index：要黎係_navbar既endpoint -> pages:index
   path('about', views.about, name='about'),        #左邊about: www./about


]

