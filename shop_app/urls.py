from django.urls import path
from . import views

app_name = 'shop_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('new_goods/', views.new_goods, name='new_goods'),
    path('catalog/<int:goods_id>/', views.goods, name='goods'),
    path('cart/', views.cart, name='cart'),
]