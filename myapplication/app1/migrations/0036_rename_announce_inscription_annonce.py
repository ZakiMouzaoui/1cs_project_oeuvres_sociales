# Generated by Django 3.2.6 on 2021-09-11 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0035_auto_20210911_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscription',
            old_name='announce',
            new_name='annonce',
        ),
    ]
