from django.db import models

# Create your models here.
class Exame(models.Model):
    nome = models.CharField(max_length=60, null=False, blank=False)
    validade = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'exame'