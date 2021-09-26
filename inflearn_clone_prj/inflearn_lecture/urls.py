from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name="home_list"),
    path('lecture_list/', views.lecture_list, name="lecture_list"),

    path('login/', views.login, name="login"),
    path('join/', views.join, name="join"),


]
