from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('python/', views.python, name='python'),
    path('django/', views.django, name='django'),
    path('scrapy/', views.scrapy, name='scrapy'),
    # path('er/', views.er, name='er'),
    # path('all1/', views.all1, name='all')
]
