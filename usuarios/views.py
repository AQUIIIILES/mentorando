from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
# Create your views here.

class cadastro(View):
    template_name = 'cadastro.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmarSenha = request.POST.get('confirmarSenha')
        
        if senha != confirmarSenha:
            messages.add_message(request, constants.ERROR, 'Senha e confirmar senha devem ser iguais.')
            return redirect(reverse('cadastro'))
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve ter 6 ou mais caracteres.')
            return redirect(reverse('cadastro'))
        
        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com este username.')
            return redirect(reverse('cadastro'))
        
        User.objects.create_user(username=username, password=senha)
        messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
        return redirect(reverse('cadastro'))