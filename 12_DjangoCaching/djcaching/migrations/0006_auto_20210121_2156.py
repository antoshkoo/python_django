# Generated by Django 2.2 on 2021-01-21 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0005_auto_20210121_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='shop_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shop_sales', to='app_shops.Shop'),
        ),
    ]