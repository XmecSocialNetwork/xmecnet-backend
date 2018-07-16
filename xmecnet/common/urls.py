from django.urls import path

from .views import register, login,otp,trying,trying2,isloggedin,logout,search

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('otp', otp, name='otp'),
    path('isloggedin', isloggedin, name='isloggedin'),
    path('logout', logout, name='logout'),
    path('search', search, name='search'),
    path('trying', trying, name='trying'),
    path('trying2', trying2, name='trying2')
]
