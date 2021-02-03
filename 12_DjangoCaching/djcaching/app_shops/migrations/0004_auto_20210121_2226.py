# Generated by Django 2.2 on 2021-01-21 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0003_auto_20210121_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='app_shops.Shop'),
        ),
    ]