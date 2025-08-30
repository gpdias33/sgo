from django.contrib import admin
from . import models

# Register your models here.
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(models.Funcao, FuncaoAdmin)
