# Generated by Django 3.2.6 on 2021-09-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_alter_article_contenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partie',
            name='titre',
            field=models.CharField(max_length=500),
        ),
    ]
