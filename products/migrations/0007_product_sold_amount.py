# Generated by Django 4.2.7 on 2023-12-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]