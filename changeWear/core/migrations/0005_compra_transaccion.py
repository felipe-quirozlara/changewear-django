# Generated by Django 3.2.4 on 2021-06-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_compra_transaccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='transaccion',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
