from django.shortcuts import render, redirect
from .models import BuyAsset
from .forms import FormAsset, FormAssetSell


def asset_buy_detail(request):

    buy_asset_by_order = reversed(BuyAsset.objects.order_by('amount'))

    return render(request,
                  'buy_asset/asset_buy_detail.html',
                  {'all_assets_buy': buy_asset_by_order})


def buy_new_asset(request):

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
                  'buy_asset/asset_new_buy.html',
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

    return render(request, 'buy_asset/form_asset_sell.html', {'form': form})
