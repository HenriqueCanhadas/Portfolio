from django.contrib import admin

from portfolio.models import Modulo, Programacao

class ListandoProgramacoes(admin.ModelAdmin):
    list_display = ("id", "linguagem", "legenda", "publicada")
    list_display_links = ("id","linguagem")
    search_fields = ("linguagem",)
    list_editable = ("publicada",)
    list_per_page = 10
    ordering = ['id']

admin.site.register(Programacao, ListandoProgramacoes)

admin.site.register(Modulo)
