from django.urls import path

from .views import register, login,otp

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('otp', otp, name='otp')

]
