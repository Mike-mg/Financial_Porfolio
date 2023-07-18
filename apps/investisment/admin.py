from django.contrib import admin
from .models import Investisment


@admin.register(Investisment)
class ListDisplayInvestisment(admin.ModelAdmin):

    list_display = ('date', '_amount_buy')

    list_filter = ('date',)
