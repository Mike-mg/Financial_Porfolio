from django.urls import path
from . import views

urlpatterns = [
     path('',
          views.dashboard,
          name='dashboard'),

     path('asset_buy_detail/',
          views.asset_buy_detail,
          name='asset_buy_detail'),

     path('asset_new_buy.html/',
          views.form_asset_new_buy,
          name='form_asset_new_buy'),

     path('invest_detail/',
          views.invest_detail,
          name='invest_detail'),

     path('invest_detail/<int:invest_id>/invest_delete/',
          views.invest_delete,
          name='invest_delete'),

     path('new_investisment/',
          views.form_new_invest,
          name='form_new_invest'),

     path('asset_buy_detail/<int:asset_id>/sell/',
          views.asset_sell,
          name='asset_sell'),
]
