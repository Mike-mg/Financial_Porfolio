from django.contrib import admin
from .models import BuyAsset, Investisment


@admin.register(BuyAsset)
class DisplayAssetBuy(admin.ModelAdmin):

    list_display = ['asset_name',
                    'asset_price',
                    'asset_amount',
                    'asset_tokens'
                    ]


@admin.register(Investisment)
class ListDisplayInvestisment(admin.ModelAdmin):

    list_display = ('date', '_amount_buy')

    list_filter = ('date',)
