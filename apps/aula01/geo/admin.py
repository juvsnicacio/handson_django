from django.contrib.admin import ModelAdmin, register

from apps.aula01.geo.models import Edital
from .models import UF, Municipio, Edital


@register(UF)
class UFAdmin(ModelAdmin):
    list_display = ('sigla', 'nome', 'codigo')


@register(Municipio)
class MunicipioAdmin(ModelAdmin):
    list_display = ('codigo', 'uf', 'nome')
    list_editable = ('uf', 'nome')
    list_filter = ('uf__nome', )
    search_fields = ('nome', 'codigo')

@register(Edital)
class EditalAdmin(ModelAdmin):
    list_display = ('numero','sigla','tipo','programa','link','descricao','ano','periodo')