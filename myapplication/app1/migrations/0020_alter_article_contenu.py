# Generated by Django 3.2.6 on 2021-09-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_article_numero_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=models.TextField(max_length=200),
        ),
    ]