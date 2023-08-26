from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models  import Ferramentas
# Register your models here.
@admin.register(Ferramentas)
class FerramentasAdmin(ImportExportModelAdmin):
    search_fields = ['nome_ferramenta', 'descricao_curta','categoria']
    list_display = ('nome_ferramenta',
    'descricao_curta',
    'descricao_longa',
    'categoria' ,
    )