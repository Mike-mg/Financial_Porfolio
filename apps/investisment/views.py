from django.shortcuts import render, redirect
from .forms import FormInvestisment
from .models import Investisment


def invest_detail(request):
    """
    return invest detail sort by date and total invest
    """

    all_investisment = Investisment()

    return render(request,
                  'investisment/invest_detail.html',
                  {'invest_sort_by_date': Investisment.objects.order_by('date'), # noqa
                   'total_invest': all_investisment.total_invest()})


def invest_delete(request, invest_id):
    """
    forms delete invest
    """

    invest = Investisment.objects.get(id=invest_id)

    if request.method == 'POST':

        invest.delete()

        return redirect('invest_detail')

    return render(request,
                  'investisment/invest_delete.html',
                  {'invest': invest}
                  )


def form_new_invest(request):
    """
    form new invest
    """

    if request.method == 'POST':

        new_invest = FormInvestisment(request.POST)

        if new_invest.is_valid():

            new_invest.save()

            return redirect('invest_detail')

    else:

        new_invest = FormInvestisment()

    return render(request,
                  'investisment/invest_new_invest.html',
                  {'new_invest': new_invest}
                  )
