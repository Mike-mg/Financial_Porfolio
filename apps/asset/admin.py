from django.contrib import admin
from .models import BuyAsset


@admin.register(BuyAsset)
class DisplayBuyAsset(admin.ModelAdmin):
    """
    Format show all buys assets in table
    """

    list_display = ['asset_name',
                    'asset_price',
                    'asset_amount',
                    'asset_tokens',
                    'blockchain'
                    ]
