from django import forms
from .models import Investisment


class FormNewInvestisment(forms.ModelForm):

    date = forms.DateField(label_suffix='',
                           error_messages={
                               'invalid': 'Entrer une date type : JJ/MM/AA'})

    new_invest = forms.FloatField(label_suffix='', min_value=10)

    class Meta:

        model = Investisment
        fields = ('date', 'new_invest')
