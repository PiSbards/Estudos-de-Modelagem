from django.contrib import admin
from . models import Ata

class ataAdmin(admin.ModelAdmin):
    list_display = ('dataInicio', 'titulo')


admin.site.register(Ata,ataAdmin)
