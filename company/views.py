from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import RegisterCompanyForm

# Create your views here.
class CreateCompany(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        form = RegisterCompanyForm(request.data)

        print(request.data)
        print(form.errors)

        if form.is_valid():
            company = form.save(commit = False)
            company.fkUser = user

            company.save()

        return Response('tets')
