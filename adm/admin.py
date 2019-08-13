from django.contrib import admin
from open_event.adm.models import Inscrito


class InscritoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'date')
    search_fields = ('name', 'email', 'cpf')
    list_filter = ('date',)


admin.site.register(Inscrito, InscritoModelAdmin)
