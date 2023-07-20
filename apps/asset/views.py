from django.shortcuts import render, redirect
from .models import BuyAsset
from .forms import FormAsset


def asset_buy_detail(request):
    """
    Return object BuyAsset in order by 'amount'
    """

    buy_asset_by_order = reversed(BuyAsset.objects.order_by('amount'))

    return render(request,
                  'asset/asset_buy_detail.html',
                  {'all_assets_buy': buy_asset_by_order})


def buy_new_asset(request):
    """
    Form for new buy asset
    """

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
                  'asset/asset_new_buy.html',
                  {'new_buy_asset': new_buy_asset}
                  )


def asset_sell(request, asset_id):
    """
    Form for sell buy asset
    """

    asset = BuyAsset.objects.get(id=asset_id)

    if request.method == 'POST':

        form = FormAsset(request.POST, instance=asset)

        if form.is_valid():

            asset.save()

            usdt = BuyAsset.objects.get(name='usdt')
            usdt.amount += asset.amount

            asset.delete()
            usdt.save()

            return redirect('asset_buy_detail')

    else:

        form = FormAsset(instance=asset)

    return render(request, 'asset/asset_sell.html', {'form': form})
