from django import forms
from .models import BuyAsset


class FormAsset(forms.ModelForm):
    """
    Forms for detail asset
    """

    name = forms.CharField(max_length=10, label_suffix='')
    price = forms.FloatField(label_suffix='')
    amount = forms.FloatField(label_suffix='')
    blockchain = forms.CharField(max_length=25, label_suffix='')

    class Meta:
        model = BuyAsset
        fields = '__all__'
