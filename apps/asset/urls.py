from django.urls import path
from . import views

urlpatterns = [

     path('asset_buy_detail/',
          views.asset_buy_detail,
          name='asset_buy_detail'),

     path('asset_new_buy.html/',
          views.buy_new_asset,
          name='buy_new_asset'),

     path('asset_buy_detail/<int:asset_id>/sell/',
          views.asset_sell,
          name='asset_sell'),
]
