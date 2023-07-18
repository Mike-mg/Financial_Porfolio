from django.contrib import admin
from django.db import models


class BuyAsset(models.Model):

    class Blockchain(models.TextChoices):
        Ethereum = 'Ethereum'
        Bsc = 'Bsc'
        Bitcoin = 'Bitcoin'
        Avalanche = 'Avalanche'
        Polkadot = 'Polkadot'
        Oasis = 'Oasis'
        Galeon = 'Galeon'
        Harmony = 'Harmony'
        Autres = 'Autres'

    name = models.fields.CharField(max_length=15)
    price = models.fields.FloatField()
    amount = models.fields.FloatField()
    blockchain = models.fields.CharField(choices=Blockchain.choices,
                                         max_length=25)

    @admin.display(description='name')
    def asset_name(self) -> str:
        return self.name.capitalize()

    @admin.display()
    def asset_tokens(self) -> float:
        return f"{self.amount / self.price:.8f}"

    @admin.display()
    def asset_amount(self) -> float:
        return f"{'$'} {self.amount:.3f}"

    @admin.display()
    def asset_price(self) -> float:
        return f"{'$'} {self.price:.8f}"
