from django.shortcuts import render

from .models import Projetos, Interesses

def home(request):
  return render(request, 'personal_blog/index.html', context={})

def sobre(request):
  return render(request, 'personal_blog/sobre.html', context={})

def projetos(request):
  return render(request, 'personal_blog/projetos.html', context={
    "projetos": Projetos.objects.all(),
  })
