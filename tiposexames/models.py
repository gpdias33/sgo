from django.db import models

# Create your models here.
class TipoExame(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tipoexame'