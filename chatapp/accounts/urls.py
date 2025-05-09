from django.urls import path
from .views import register,login_view,home,logout_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('accounts/login/',login_view,name='login_view'),
    path('logout/',logout_view,name='logout_view')
]
