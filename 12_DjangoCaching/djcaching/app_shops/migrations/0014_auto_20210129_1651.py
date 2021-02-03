# Generated by Django 2.2 on 2021-01-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0013_auto_20210128_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantity'),
        ),
        migrations.AlterUniqueTogether(
            name='good',
            unique_together={('shop', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='sale',
            unique_together={('shop', 'good')},
        ),
    ]