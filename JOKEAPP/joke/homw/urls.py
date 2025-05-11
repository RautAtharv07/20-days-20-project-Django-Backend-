from django.urls import path
from .views import home,get_joke_json

urlpatterns = [
    path('',home,name='home'),
    path('get-joke/', get_joke_json, name='get_joke_json')
]
