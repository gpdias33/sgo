from django.contrib import admin
from . import models

# Register your models here.
class ExameAdmin(admin.ModelAdmin):
    list_display = ('nome', 'validade',)
    search_fields = ('nome',)


admin.site.register(models.Exame, ExameAdmin)
