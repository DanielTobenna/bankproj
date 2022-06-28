# Generated by Django 3.2 on 2022-06-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankprojapp', '0002_auto_20220628_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreign_transaction',
            name='account_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='foreign_transaction',
            name='bank_code',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='foreign_transaction',
            name='routing_number',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]