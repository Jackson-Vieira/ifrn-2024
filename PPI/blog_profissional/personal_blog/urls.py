from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("projetos/", views.projetos, name="projetos"),
  path("sobre/", views.sobre, name="sobre"),
]
