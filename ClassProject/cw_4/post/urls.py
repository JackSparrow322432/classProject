from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_threads, name='home'),
    path('threads/', views.thread_list, name='thread-list'),
    path('threads/<int:id>/', views.thread_detail, name='thread-detail'),
    path('threads/<int:id>/delete/', views.thread_delete, name='thread-delete'),
    path('threads/<int:id>/edit/', views.thread_edit, name='thread-edit'),
    path('posts/<int:id>/delete/', views.post_delete, name='post-delete'),
    path('posts/<int:id>/edit/', views.post_edit, name='post-edit'),
]
