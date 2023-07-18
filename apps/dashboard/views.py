from django.shortcuts import render
from ..investisment.models import Investisment


def dashboard(request):

    objects_investisments = Investisment()

    return render(request,
                  'dashboard/dashboard.html',
                  {
                      'total_invest_actual':
                      objects_investisments.current_invest(),

                      'total_invest':
                      objects_investisments.total_invest(),

                      'profit_actual':
                      objects_investisments.profit(),

                      'text':
                      'No data'
                      })
