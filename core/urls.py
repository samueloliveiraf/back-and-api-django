from django.urls import path
from core import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('posts/',
         views.PostList.as_view(),
         name='post-list'),
    path('posts/<int:pk>/',
         views.PostDetail.as_view(),
         name='post-detail'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail'),
    path('register/', 
         views.RegisterAPI.as_view()),
    path('login/', views.LoginAPIView.as_view())
])
