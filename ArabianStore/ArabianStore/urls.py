"""ArabianStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from store.views import index, detail_about, registrasi, belanja, contact, logoutView, form, about_arabian, all_produk, all_produkA, all_kategoriA, add_product_submit, add_categori_submit, hapus_produk, hapus_kategori, sunting_produk, sunting_kategori, on_sale, detail_parfum1, detail_parfum2, detail_parfum3, detail_parfum4, detail_parfum5, detail_parfum6, detail_parfum7, detail_parfum8, detail_parfum9, detail_parfum10, detail_parfum11, detail_parfum12, detail_parfum1_admin, detail_parfum2_admin, detail_parfum3_admin, detail_parfum4_admin, detail_parfum5_admin, detail_parfum6_admin, detail_parfum7_admin, detail_parfum8_admin, detail_parfum9_admin, detail_parfum10_admin, detail_parfum11_admin, detail_parfum12_admin
from django.urls import path, include
#from . import views
#from django.utils.translation import ugettext_lazy as _
#from material.admin.sites import site

#site.HEADER = ('Your site header')
#site.TITLE = ('Your site title')
#site.FAVICON = ('path/to/favicon')
#site.MAIN_BG_COLOR = ('color')
#site.LOGIN_LOGO = ('path/to/image')


urlpatterns = [
    path('store/', include('store.urls')),
    #path('admin/', include('material.admin.urls')),
    path('login/', form, name='login'),
    path('logout/', logoutView, name='logout'),
    path('belanja/', belanja, name='belanja'),
    path('contact/', contact, name='contact'),
    path('registrasi/', registrasi, name='registrasi'),
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('about/',about_arabian,name='about_arabian'),
    path('produk/',all_produk,name='produk'),
    path('administrasi/kategori/',all_kategoriA,name='adminKategoris'),
    path('administrasi/produk/',all_produkA,name='adminpProduks'),
    path('administrasi/produk/add/submit',add_product_submit,name='add_product_submit'),
    path('administrasi/kategori/add/submit',add_categori_submit,name='add_categori_submit'),
    path('hapus/produk/<id_produk>',hapus_produk,name='hapus_produk'),
    path('hapus/kategori/<id_kategori>',hapus_kategori,name='hapus_kategori'),
    path('sunting/produk/<id_produk>',sunting_produk,name='sunting_produk'),
    path('sunting/kategori/<id_kategori>',sunting_kategori,name='sunting_kategori'),
    path('on_sale/',on_sale,name='on_sale'),
    #user
    path('detail_about/',detail_about,name='detail_about'),
    path('detail_parfum1/',detail_parfum1,name='detail_parfum1'),
    path('detail_parfum2/',detail_parfum2,name='detail_parfum2'),
    path('detail_parfum3/',detail_parfum3,name='detail_parfum3'),
    path('detail_parfum4/',detail_parfum4,name='detail_parfum4'),
    path('detail_parfum5/',detail_parfum5,name='detail_parfum5'),
    path('detail_parfum6/',detail_parfum6,name='detail_parfum6'),
    path('detail_parfum7/',detail_parfum7,name='detail_parfum7'),
    path('detail_parfum8/',detail_parfum8,name='detail_parfum8'),
    path('detail_parfum9/',detail_parfum9,name='detail_parfum9'),
    path('detail_parfum10/',detail_parfum10,name='detail_parfum10'),
    path('detail_parfum11/',detail_parfum11,name='detail_parfum11'),
    path('detail_parfum12/',detail_parfum12,name='detail_parfum12'),
    #admin
    path('belanja/detail_parfum1_admin/',detail_parfum1_admin,name='detail_parfum1_admin'),
    path('belanja/detail_parfum2_admin/',detail_parfum2_admin,name='detail_parfum2_admin'),
    path('belanja/detail_parfum3_admin/',detail_parfum3_admin,name='detail_parfum3_admin'),
    path('belanja/detail_parfum4_admin/',detail_parfum4_admin,name='detail_parfum4_admin'),
    path('belanja/detail_parfum5_admin/',detail_parfum5_admin,name='detail_parfum5_admin'),
    path('belanja/detail_parfum6_admin/',detail_parfum6_admin,name='detail_parfum6_admin'),
    path('belanja/detail_parfum7_admin/',detail_parfum7_admin,name='detail_parfum7_admin'),
    path('belanja/detail_parfum8_admin/',detail_parfum8_admin,name='detail_parfum8_admin'),
    path('belanja/detail_parfum9_admin/',detail_parfum9_admin,name='detail_parfum9_admin'),
    path('belanja/detail_parfum10_admin/',detail_parfum10_admin,name='detail_parfum10_admin'),
    path('belanja/detail_parfum11_admin/',detail_parfum11_admin,name='detail_parfum11_admin'),
    path('belanja/detail_parfum12_admin/',detail_parfum12_admin,name='detail_parfum12_admin'),
]
