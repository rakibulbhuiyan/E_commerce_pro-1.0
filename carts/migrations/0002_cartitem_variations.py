# Generated by Django 4.2.5 on 2023-09-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_variation'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='shop.variation'),
        ),
    ]
