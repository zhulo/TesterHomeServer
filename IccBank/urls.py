from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list_url'),
    path('add/', views.post_request),
]
