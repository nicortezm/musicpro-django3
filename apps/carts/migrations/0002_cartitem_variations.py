# Generated by Django 3.2.3 on 2021-05-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_delete_variationmanager'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='tienda.Variation'),
        ),
    ]
