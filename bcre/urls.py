"""
URL configuration for bcre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [                                                     #list入面有function
    path('', include('pages.urls', namespace='pages')),             #namespace=將所有相關入pages + 配合pages url -> 定義app_name叫pages (如果定義左namespace可以唔加)
    path('listings/', include('listings.urls', namespace='listings')),
    path('accounts/', include('accounts.urls', namespace='accounts')),      #一次分流
    path('contacts/', include('contacts.urls', namespace='contacts')),
    path('admin/', admin.site.urls),                                    #網址打admin
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)     # ]外面 = internal ; =go to setting file to find media url and media root

