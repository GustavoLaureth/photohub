from django.contrib import admin
from .models import Tag, Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'descricao', 'data_criacao']
    list_display_links = ['id', 'titulo', 'descricao', 'data_criacao']

admin.site.register(Tag)
admin.site.register(Cliente, ClienteAdmin)