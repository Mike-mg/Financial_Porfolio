from django.shortcuts import render
from apps.investisment.models import Investisment
from apps.asset.models import BuyAsset


def dashboard(request):

    objects_investisments = Investisment()
    objects_buy_asset = BuyAsset()

    return render(request,
                  'dashboard/dashboard.html',
                  {'total_invest': objects_investisments.total_invest(),
                   'total_invest_actual': objects_buy_asset.current_invest(),
                   'profit_actual': objects_investisments.profit(),
                   'text': 'No data'})
