# Generated by Django 4.2.2 on 2023-07-17 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_alter_investisment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyasset',
            old_name='amount',
            new_name='asset_amount',
        ),
        migrations.RenameField(
            model_name='buyasset',
            old_name='asset_price',
            new_name='asset_asset_price',
        ),
        migrations.RenameField(
            model_name='buyasset',
            old_name='name',
            new_name='asset_name',
        ),
    ]
