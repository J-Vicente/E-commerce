"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from commerce.views import index,product_criar,product_listar,product_editar,product_remover,product
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('product/<int:id>/',product,name='product'),
    path('admin/listar',product_listar,name='product_listar'),
    path('admin/product/',product_criar,name='product_criar'),
    path('admin/product/editar/<int:id>/',product_editar, name='product_editar'),
    path('admin/product/remover/<int:id>/',product_remover,name='product_remover'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)