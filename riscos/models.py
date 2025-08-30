from django.db import models

# Create your models here.
class Risco(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    tiporisco = models.ForeignKey('tiporisco', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'risco'