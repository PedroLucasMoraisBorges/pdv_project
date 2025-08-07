from django.urls import path
from .views import *

urlpatterns = [
    path('', Redirect.as_view(), name=''),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registerUser/', Register.as_view(), name='register'),
    path('home/', Home.as_view(), name='home')
]