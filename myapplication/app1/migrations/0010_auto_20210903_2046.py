# Generated by Django 3.2.6 on 2021-09-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20210903_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='demande',
            name='date_paiement',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
