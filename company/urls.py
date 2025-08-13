from django.urls import path
from .views import *

urlpatterns = [
    path('createCompany/', CreateCompany.as_view(), name='createCompany'),
    path('dashboard/<str:id>', DashBoardCompany.as_view(), name='dashBoardCompany')
]