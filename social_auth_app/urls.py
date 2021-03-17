from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('profile/<str:username>/', views.ProfileView.as_view(),
         name='profile'),
    path('profile/<str:username>/edit/', views.EditProfileView.as_view(),
         name='edit_profile'),
    path('profile-redirect/', views.profile_redirect, name='profile-redirect')
]
