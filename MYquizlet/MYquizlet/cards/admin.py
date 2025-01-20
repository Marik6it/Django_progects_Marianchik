from django.contrib import admin
from django.utils.html import format_html
from .models import CardSet, Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('term', 'card_set', 'view_link')

    def view_link(self, obj):
        return format_html('<a href="/card/{}/">Переглянути</a>', obj.id)
    view_link.short_description = 'Деталі'

admin.site.register(CardSet)
admin.site.register(Card, CardAdmin)
