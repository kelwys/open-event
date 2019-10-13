from django.contrib import admin
from django.utils.html import format_html
from open_event.evento.models import Inscrito, Palestrante, Patrocinio, Agenda


class InscritoModelAdmin(admin.ModelAdmin):
    change_list_template = 'evento/_layouts/inscricao_lote_changelist.html'

    list_display = ('name', 'email', 'phone', 'cpf', 'date')
    search_fields = ('name', 'email', 'cpf')
    list_filter = ('date',)


class PalestranteModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}"/>', obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'


class PatrocinioModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo_img', 'nivel']

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}"/>', obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'


class AgendaModelAdmin(admin.ModelAdmin):
    list_display = ['palestrante', 'nome_palestra', 'date', 'time']


admin.site.register(Inscrito, InscritoModelAdmin)
admin.site.register(Palestrante, PalestranteModelAdmin)
admin.site.register(Patrocinio, PatrocinioModelAdmin)
admin.site.register(Agenda, AgendaModelAdmin)