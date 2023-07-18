from django.contrib import admin
from django.db import models
from django.utils import timezone


class BuyAsset(models.Model):

    name = models.fields.CharField(max_length=15)
    price = models.fields.FloatField()
    amount = models.fields.FloatField()

    @admin.display(description='name')
    def asset_name(self) -> str:

        return self.name.capitalize()

    @admin.display()
    def asset_tokens(self) -> float:
        return f"{self.amount / self.price:.8f}"

    @admin.display(description='amount')
    def asset_amount(self) -> float:
        return f"{'$'} {self.amount:.3f}"

    @admin.display(description='price')
    def asset_price(self) -> float:
        return f"{'$'} {self.price:.8f}"


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

    # def invest_sort_by_date(self):

    #     return reversed(Investisment.objects.order_by('date'))


class Blockchain(models.Model):

    class BlockchainName(models.TextChoices):
        Ethereum = 'Ethereum'
        Bsc = 'Bsc'
        Bitcoin = 'Bitcoin'
        Avalanche = 'Avalanche'
        Polkadot = 'Polkadot'
        Oasis = 'Oasis'
        Galeon = 'Galeon'
        Harmony = 'Harmony'
        Autres = 'Autres'

    blockchain = models.fields.CharField(choices=BlockchainName.choices,
                                         max_length=25)
