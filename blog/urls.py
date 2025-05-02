from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.post_create, name='post_create'),
    path('edit/<int:post_id>/', views.post_edit, name='post_edit'),
]
