from django.contrib import admin
from . import models

# Register your models here.
class TipoExameAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(models.TipoExame, TipoExameAdmin)
