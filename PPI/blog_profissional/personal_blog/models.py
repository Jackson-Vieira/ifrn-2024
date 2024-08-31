from django.db import models

class Interesses(models.Model):
  nome = models.CharField(max_length=255)

class Projetos(models.Model):
  nome = models.CharField(max_length=255)
  descricao = models.CharField(max_length=255)
  tecnologias = models.CharField(max_length=255)
  link = models.URLField(blank=True)
  ano_inicio = models.DateField()
  ano_fim = models.DateField()

  def tecnologias_list(self):
    return self.tecnologias.split(', ')
