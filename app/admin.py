from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models  import Ferramentas, CustomUser
# Register your models here.
@admin.register(Ferramentas)
class FerramentasAdmin(ImportExportModelAdmin):
    search_fields = ['nome_ferramenta', 'descricao_curta','categoria']
    list_display = ('nome_ferramenta',
    'descricao_curta',
    'descricao_longa',
    'categoria' ,
    )
    
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')  # Especifique os campos que deseja exibir na lista

admin.site.register(CustomUser, CustomUserAdmin)