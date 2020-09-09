from django.contrib import admin
from empresa.models import Empresa

class Empresas(admin.ModelAdmin):
    list_display = ('id', 'razao_social', 'nome_fantasia','cnpj', 'endereco', 'telefone', 'celular', 'email', 'site',)
    list_display_links = ('id', 'razao_social', 'nome_fantasia', 'cnpj')
    search_fields = ('nome_fantasia', 'razao_social', 'cnpj')

admin.site.register(Empresa, Empresas)
