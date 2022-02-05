from django.contrib import admin
from django.urls import path, include

from . import views
from .views import logout_user

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('contact/', views.MessageAdmin.as_view(), name='message-admin'),
    path('comment/', views.CommentView.as_view(), name='message-admin'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('profiles/', views.ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', views.ProfileInfo.as_view(), name='user-detail'),
    path('logout/', logout_user, name='logout'),
    path('create/', views.NewPost.as_view(), name='create'),
    path('post/', views.PostList.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostInfo.as_view(), name='post-detail'),
    path('authors/<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
    path('authors/<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
]
