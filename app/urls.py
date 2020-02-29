from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path("register", views.register, name="register"),
    path("registerr", views.registerr, name="registerr"),
    path("registerrr", views.registerrr, name="registerrr"),
    path("aboutt/", views.aboutt, name="aboutt"),
    path("login/", views.login, name="login"),
    path("loginn/", views.loginn, name="loginn"),
    path("done", views.done, name="done"),
    path("submitt", views.submitt, name="submitt"),
    path("loginnn/", views.loginnn, name="loginnn"),
]