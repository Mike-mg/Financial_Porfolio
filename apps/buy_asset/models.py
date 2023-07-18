from django.contrib import admin
from django.db import models


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
