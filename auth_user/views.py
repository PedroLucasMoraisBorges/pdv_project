from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from .forms import *
from .utilits import *

# Create your views here.

# Classe para redirecionamento de tipo de usuário
class Redirect(View):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return redirect('login')
        else:
            return redirect('home')

# Logind de usuário geral
class Login(View):
    def get(self, request):
        form = AuthenticationForm()

        context = {
            'form' : form
        }

        return render(request, 'auth/login.html', context)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        errors = getErrors([form])
        
        if form.is_valid():
            user = form.get_user()  
            login(request, user)
            return redirect('/')
        
        context = {
            'errors' : errors,
            'form'   : form
        }

        return render(request, 'auth/login.html', context)

# Cadastro de manager
class Register(View):
    def get(self, request):
        form = CustomUserCreationForm()

        context = {
            'form' : form
        }

        return render(request, 'auth/register.html', context)
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        errors = getErrors([form])

        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()

            login(request, user)
            return redirect('/')
        
        context = {
            'form'   : form,
            'errors' : errors
        }

        return render(request, 'auth/register.html', context)

class Home(View):
    def get(self, request):
        return render(request, 'geral/home.html')