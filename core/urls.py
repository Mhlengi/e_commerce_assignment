from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^product-list/$', views.product_list, name='product_list'),
    # url(r'^product-detail/$',
    #     views.product_list,
    #     name='product_list_by_category'),
    url(r'^product-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
    url(r'^cart/$', views.cart_detail, name='cart_detail'),
    url(r'^cart-add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^cart-remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]
