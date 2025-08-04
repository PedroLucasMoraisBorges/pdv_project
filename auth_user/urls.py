from django.urls import path
from .views import *

urlpatterns = [
    path('', Redirect.as_view(), name='redirect'),
    path('login/', Login.as_view(), name='login'),
    path('registerUser/', Register.as_view(), name='register'),
    path('home/', Home.as_view(), name='home')
]