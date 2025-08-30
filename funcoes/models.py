from django.db import models

# Create your models here.
class Funcao (models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'funcao'
