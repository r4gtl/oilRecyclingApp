# Generated by Django 5.1.5 on 2025-02-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0003_remove_cliente_address_remove_cliente_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='pickup_date',
        ),
        migrations.AddField(
            model_name='cliente',
            name='pickup_interval',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Numero di giorni tra i ritiri (ad es.: 30 per un ritiro mensile)', null=True),
        ),
    ]
