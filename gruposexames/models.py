from django.db import models
from grupos.models import Grupo
from exames.models import Exame 
from tiposexames.models import TipoExame

# Create your models here.
class GrupoExame(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)
    exame = models.ForeignKey(Exame, on_delete=models.PROTECT)
    tipoexame = models.ForeignKey(TipoExame, on_delete=models.PROTECT)
    grupo_exame = Grupo.nome + ' - ' + Exame.nome + ' - ' + TipoExame.nome

    def __str__(self):
        return self.grupo_exame

    class Meta:
        db_table = 'grupoexame'