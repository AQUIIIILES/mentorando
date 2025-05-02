from django.db import models
from django.contrib.auth.models import User

class Navigators(models.Model):
    nome = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Mentor
    
    def __str__(self):
        return self.nome

# Create your models here.
class Mentorados(models.Model):
    estagio_choices = (('E1', '10-100k'), ('E2', '100-1kk'))
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    estagio = models.CharField(max_length=2, choices=estagio_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    navigator = models.ForeignKey(Navigators, on_delete=models.CASCADE, null=True, blank=True) #Mentor designado pelo mentor pai
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome 
    