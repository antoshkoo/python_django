# Generated by Django 2.2 on 2021-01-22 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0010_auto_20210122_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price_order',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shops.Good'),
        ),
    ]
