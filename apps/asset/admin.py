from django.contrib import admin
from .models import BuyAsset


@admin.register(BuyAsset)
class DisplayAssetBuy(admin.ModelAdmin):

    list_display = ['asset_name',
                    'asset_price',
                    'asset_amount',
                    'asset_tokens',
                    'blockchain'
                    ]
