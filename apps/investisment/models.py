from django.db import models
from django.utils import timezone
from ..buy_asset.models import BuyAsset


class Investisment(models.Model):

    new_invest = models.fields.FloatField(default=0)
    date = models.fields.DateField(
        default='DD/MM/YY',
        error_messages={
            "unique": "The Geeks Field you entered is not unique."})

    def __str__(self):

        date_format = "%d/%m/%Y"
        timestamp = timezone.datetime.strftime(self.date, date_format)
        return timestamp

    def _amount_buy(self):
        return f"{'$'} {self.new_invest:.3f}"

    def total_invest(self):
        all_amount_investisment = sum(amount.new_invest for amount in Investisment.objects.all()) # noqa

        return all_amount_investisment

    def current_invest(self):

        current_all_invest = sum(amount.amount for amount in BuyAsset.objects.all()) # noqa

        return current_all_invest

    def profit(self):

        return self.current_invest() - self.total_invest()
