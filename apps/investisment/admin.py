from django.contrib import admin
from .models import Investisment


@admin.register(Investisment)
class ListDisplayInvestisment(admin.ModelAdmin):

    list_display = ('date', 'new_invest')
