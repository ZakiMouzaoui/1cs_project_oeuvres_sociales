# Generated by Django 3.2.6 on 2021-09-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_auto_20210907_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='numero_article',
            field=models.IntegerField(null=True),
        ),
    ]