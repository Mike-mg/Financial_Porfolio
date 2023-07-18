from django import forms
from .models import BuyAsset


class FormAsset(forms.ModelForm):

    name = forms.CharField(max_length=10, label_suffix='')
    price = forms.FloatField(label_suffix='')
    amount = forms.FloatField(label_suffix='')

    class Meta:
        model = BuyAsset
        fields = ('name', 'price', 'amount')


class FormAssetSell(forms.ModelForm):

    name = forms.CharField(max_length=10, label_suffix='')
    amount = forms.FloatField(label_suffix='')

    class Meta:
        model = BuyAsset
        exclude = ['asset_price']
