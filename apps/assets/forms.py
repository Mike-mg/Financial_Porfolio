from django import forms
from .models import Investisment, BuyAsset


class FormNewInvestisment(forms.ModelForm):

    date = forms.DateField(label_suffix='',
                           error_messages={
                               'invalid': 'Entrer une date type : JJ/MM/AA'})

    new_invest = forms.FloatField(label_suffix='', min_value=10)

    class Meta:

        model = Investisment
        fields = ('date', 'new_invest')


class FormAsset(forms.ModelForm):

    name = forms.CharField(max_length=10, label_suffix='')
    asset_price = forms.FloatField(label_suffix='')
    amount = forms.FloatField(label_suffix='')

    class Meta:
        model = BuyAsset
        fields = ('name', 'asset_price', 'amount')


class FormAssetSell(forms.ModelForm):

    name = forms.CharField(max_length=10, label_suffix='')
    amount = forms.FloatField(label_suffix='')

    class Meta:
        model = BuyAsset
        exclude = ['asset_price']
