# Generated by Django 3.2.6 on 2021-09-09 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_pv_titre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annonce',
            options={'ordering': ['date_fin']},
        ),
    ]
