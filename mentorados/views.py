from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Mentorados, Navigators
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
class mentorados(View):
    template_name = 'mentorados.html'
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        
        estagios = Mentorados.estagio_choices
        navigators = Navigators.objects.filter(user=request.user)
        mentorados = Mentorados.objects.filter(user=request.user)
        context = {'estagios': estagios, 'navigators': navigators, 'mentorados': mentorados}
        return render(request, self.template_name, context)
   
    def post(self, request):
        
        if not request.user.is_authenticated:
            return redirect('login')
        
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        estagio = request.POST.get('estagio')
        navigator = request.POST.get('navigator')
        user = request.user
        
        mentorado = Mentorados(nome=nome, foto=foto, estagio=estagio, navigator_id=navigator, user=user)
        mentorado.save()
      
        messages.add_message(request, constants.SUCCESS, 'Mentorado cadastrado com sucesso!')
        return redirect('mentorados')