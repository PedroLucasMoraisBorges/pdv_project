from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterCompanyForm
from auth_user.models import *
from .models import *

# Create your views here.
class CreateCompany(View):
    def post(self, request):
        user = request.user
        form = RegisterCompanyForm(request.POST)
        role = Role.objects.get(name='Proprietário')

        if form.is_valid():
            company = form.save(commit = False)
            company.fkUser = user
            company.save()

            UserRoles.objects.create(
                fkUser = user,
                fkCompany = company,
                fkRole = role
            ).save()

            CompanyUser.objects.create(
                company = company,
                user = user
            ).save()

            return redirect('dashBoardCompany', id=company.id)

class DashBoardCompany(View):
    def get(self, request, id):
        company = Company.objects.get(id=id)

        context = {
            'company' : company
        }

        return render(request, 'company/dashBoardCompany.html', context)