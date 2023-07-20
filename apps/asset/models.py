from django.contrib import admin
from django.db import models


class BuyAsset(models.Model):
    """
    Model buy asset
    """

    class Blockchain(models.TextChoices):
        """
        Choice type of blockchain
        """

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

    @admin.display()
    def asset_name(self) -> str:
        # Format show name in capitalize

        return self.name.capitalize()

    @admin.display()
    def asset_tokens(self) -> float:
        # calc and show the nomber of token

        return f"{self.amount / self.price:.8f}"

    @admin.display()
    def asset_amount(self) -> float:
        # Format show amount

        return f"{'$'} {self.amount:.3f}"

    @admin.display()
    def asset_price(self) -> float:
        # Format show price asset

        return f"{'$'} {self.price:.8f}"

    def current_invest(self):
        # Calc sum all buys assets

        sum_current_invest = sum(
            amount.amount for amount in BuyAsset.objects.all())

        return sum_current_invest
