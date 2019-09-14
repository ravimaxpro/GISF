"""tryjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myapp.views import (homepage, homehtml,BootStrap,rawHtml,Product_object_list_view,
        product_detail_view,product_Rawcreate_view,Product_update_view,caluate_view,product_ModelForm_create_view,prod_ModelForm_CRUD_view)
from FormsCustomize.views import CarsModelFormDisplay_view,FormWidgets_view,ChoiceForm_view,ProductFormvalidate_view,product2_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('hhome/', homehtml, name='homepage'),
    path('Bstrap/', BootStrap, name='homepage'),
    path('rawhtml/', rawHtml, name='homepage'),
    path('Products/', product_detail_view, name='Products'),
    path('ProdList/', Product_object_list_view, name='prodlist'),
    path('productrawcreate/',product_Rawcreate_view,name='prodlist'),
    #path('Produpdate/',Product_update_view, name='ProdUpdate'),
    path('ProdList/Produpdate/<int:my_id>/', Product_update_view, name='ProdUpdate'),
    path('ProdMFCreate/', product_ModelForm_create_view, name='ProdMFCreate'),
    path('ProdMFCRUD/',prod_ModelForm_CRUD_view, name='ProdMFCRUD'),
    path('Ptrcalc/', caluate_view, name='Ptrcalc'),
    path('StaticMediaRead/', CarsModelFormDisplay_view, name='StaticMediaRead'),
    path('Formwidget/',FormWidgets_view,name='Formwidget'),
    path('ChoiceField/',ChoiceForm_view,name='ChoiceField'),
    path('Formvalidate/',ProductFormvalidate_view,name='Formvalidate'),
    path('hai/',product2_views)

]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
