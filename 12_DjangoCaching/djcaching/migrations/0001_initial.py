# Generated by Django 2.2 on 2021-01-20 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0, verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Shop name')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_price', models.FloatField(default=0, verbose_name='sale_price')),
                ('good_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_shops.Good')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='app_shops.Shop')),
            ],
        ),
        migrations.AddField(
            model_name='good',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='app_shops.Shop'),
        ),
    ]