"""OOBBSS2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from productmanagement import  views as pviews
from django.conf import settings
from django.conf.urls.static import static
from usermanagement import views as uviews

urlpatterns =[
    path('admin/', admin.site.urls),

    path('books/', uviews.showbooks, name='book_list'),
    path('registration/', uviews.registers,name='reg'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_profile/', uviews.create_profile,name = 'create_profile'),
    path('show_profile/', uviews.show_profile,name='show_profile'),
    path('upload_product/',uviews.upload_product_by_user, name='upload_product'),
    path('lcp/',uviews.ij,name='location')
]



if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
