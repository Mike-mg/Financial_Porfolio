from django.urls import path
from . import views

urlpatterns = [
     path('invest_detail/',
          views.invest_detail,
          name='invest_detail'),

     path('invest_detail/<int:invest_id>/invest_delete/',
          views.invest_delete,
          name='invest_delete'),

     path('new_investisment/',
          views.form_new_invest,
          name='form_new_invest'),
          ]
