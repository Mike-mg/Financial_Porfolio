# Generated by Django 4.2.2 on 2023-07-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investisment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_invest', models.FloatField(default=0)),
                ('date', models.DateField(default='DD/MM/YY', error_messages={'unique': 'The Geeks Field you entered is not unique.'})),
            ],
        ),
    ]
