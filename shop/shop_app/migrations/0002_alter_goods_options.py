# Generated by Django 4.0.5 on 2022-06-07 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': 'Good', 'verbose_name_plural': 'Goods'},
        ),
    ]