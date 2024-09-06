from django.urls import path
from .views import index, main

urlpatterns = [
    path('', index, name="index"),
    path('', main, name="main"),
    path('', main, name="login"),
    path('', main, name="logout"),
    path('', main, name="signup"),
    path('', main, name="chat"),
    path('', main, name="profile"),
]
