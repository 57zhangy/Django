
from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login1/', views.LoginView1.as_view(), name='login1'),
    path('login2/', views.LoginView2.as_view(), name='login2'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('home1/', views.home1, name='home1'),
    path('home1/home3.html', views.home2),
]