from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('addtocart', views.addtocart, name='addtocart'),
    path('clearcart', views.clearcart, name='clearcart'),
    path('basket', views.basket, name='basket'),
    path(r'product/(?P<productid>[^]{256})$', views.product, name='product'),
]
