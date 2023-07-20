from django.db import models
from django.contrib import admin
from apps.asset.models import BuyAsset


class Investisment(models.Model):

    invest = models.fields.FloatField(default=0)
    date = models.fields.DateField(default='DD/MM/YY')

    @admin.display()
    def new_invest(self) -> str:
        """
        return new invest with 3 decimals
        """

        return f"{'$'} {self.invest:.3f}"

    def total_invest(self):
        """
        return sum amount all objects investisment
        """

        all_amount_investisment = sum(
            amount.invest for amount in Investisment.objects.all())

        return all_amount_investisment

    def profit(self):
        """
        calculate the profit actual
        """

        objects_buy_asset = BuyAsset()

        return objects_buy_asset.current_invest() - self.total_invest()
