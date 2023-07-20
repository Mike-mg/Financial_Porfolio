from django.shortcuts import render, redirect
from .forms import FormNewInvestisment
from .models import Investisment


def invest_detail(request):

    all_investisment = Investisment()

    return render(request,
                  'investisment/invest_detail.html',
                  {'invest_sort_by_date': Investisment.objects.order_by('date'), # noqa
                   'total_invest': all_investisment.total_invest()})


def invest_delete(request, invest_id):

    invest = Investisment.objects.get(id=invest_id)

    if request.method == 'POST':

        invest.delete()

        return redirect('invest_detail')

    return render(request,
                  'investisment/invest_delete.html',
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
                  'investisment/invest_new_invest.html',
                  {'new_invest': new_invest}
                  )
