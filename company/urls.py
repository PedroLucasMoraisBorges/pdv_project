from django.urls import path
from .views import *

urlpatterns = [
    path('createCompany/', CreateCompany.as_view(), name='createCompany')
]