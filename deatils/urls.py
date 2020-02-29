from django.urls import path

from . import views

urlpatterns = [
    path("about", views.about, name="about"),
    path("shop", views.shop, name="shop"),
    path("index", views.index, name="index"),
    path("complain", views.complain, name="complain"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("data", views.data, name="data"),
    path("suggest", views.suggest, name="suggest"),
    path("expert", views.expert, name="expert"),
    path("cart", views.cart, name="cart"),
    path("online", views.online, name="online"),
    path("register1", views.register1, name="register1"),
    path("logout", views.logout, name="logout"),
    path("product_single", views.product_single, name="product_single"),

]