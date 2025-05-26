from django.urls import path
from . import views     #. = current directory = pages


app_name = 'pages'

urlpatterns = [
   path('', views.index, name='index'),     #app level   # abc.com/''/'' = abc.com/
   path('about', views.about, name='about'),


]

