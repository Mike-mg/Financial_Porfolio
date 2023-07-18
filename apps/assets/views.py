from django.shortcuts import render, redirect
from .models import BuyAsset, Investisment
from .forms import FormNewInvestisment, FormAsset, FormAssetSell


def dashboard(request):

    objects_investisments = Investisment()

    return render(request,
                  'assets/dashboard.html',
                  context={"total_invest_actual": objects_investisments.current_invest(), # noqa
                           'total_invest': objects_investisments.total_invest(), # noqa
                           'profit_actual': objects_investisments.profit(), # noqa
                           'text': 'Aucune données'})


def invest_detail(request):

    objects_Investisments = Investisment()

    return render(request,
                  'assets/invest_detail.html',
                  {'invest_sort_by_date': objects_Investisments.invest_sort_by_date(), # noqa
                   'total_invest': objects_Investisments.total_invest()})


def invest_delete(request, invest_id):

    invest = Investisment.objects.get(id=invest_id)

    if request.method == 'POST':

        invest.delete()

        return redirect('invest_detail')

    return render(request,
                  'assets/invest_delete.html',
                  {'invest': invest}
                  )


def form_new_invest(request):

    if request.method == 'POST':

        new_invest = FormNewInvestisment(request.POST)

        if new_invest.is_valid():

            new_invest.save()

            return redirect('invest_detail')

    else:

        new_invest = FormNewInvestisment()

    return render(request,
                  'assets/invest_new_invest.html',
                  {'new_invest': new_invest}
                  )


def asset_buy_detail(request):

    buy_asset_by_order = reversed(BuyAsset.objects.order_by('amount'))

    return render(request,
                  'assets/asset_buy_detail.html',
                  {'all_assets_buy': buy_asset_by_order})


def form_asset_new_buy(request):

    usdt = BuyAsset.objects.get(name='usdt')

    if request.method == 'POST':

        new_buy_asset = FormAsset(request.POST)

        if new_buy_asset.is_valid():

            new_buy_asset.save()

            all_asset_buy = list(BuyAsset.objects.all())

            last_buy_asset = all_asset_buy[-1]

            usdt.amount -= last_buy_asset.amount
            usdt.save()

            return redirect('asset_buy_detail')

    else:

        new_buy_asset = FormAsset()

    return render(request,
                  'assets/asset_new_buy.html',
                  {'new_buy_asset': new_buy_asset}
                  )


def asset_sell(request, asset_id):

    asset = BuyAsset.objects.get(id=asset_id)

    if request.method == 'POST':

        form = FormAssetSell(request.POST, instance=asset)

        if form.is_valid():

            asset.save()

            usdt = BuyAsset.objects.get(name='usdt')
            usdt.amount += asset.amount

            asset.delete()
            usdt.save()

            return redirect('asset_buy_detail')

    else:

        form = FormAssetSell(instance=asset)

    return render(request, 'assets/form_asset_sell.html', {'form': form})
