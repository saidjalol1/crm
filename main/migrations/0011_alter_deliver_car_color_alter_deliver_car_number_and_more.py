# Generated by Django 4.2.7 on 2023-12-07 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_product_old_price'),
        ('main', '0010_orders_payment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliver',
            name='car_color',
            field=models.CharField(max_length=250, verbose_name='Moshina rangi'),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='car_number',
            field=models.CharField(max_length=250, verbose_name='Moshina raqami'),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='car_type',
            field=models.CharField(max_length=250, verbose_name='Moshina nomi'),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Ismi'),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='phone_number',
            field=models.CharField(max_length=250, verbose_name='Telefon raqami'),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='surname',
            field=models.CharField(max_length=250, verbose_name='Familiyasi'),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Manzili'),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan"),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Ismi'),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='phone_number',
            field=models.CharField(max_length=250, verbose_name='Telefon raqami'),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='position',
            field=models.CharField(max_length=250, verbose_name='Lavozimi'),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='salary',
            field=models.BigIntegerField(default=0, verbose_name='Oyligi'),
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nabor nomi')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.orders')),
            ],
        ),
        migrations.CreateModel(
            name='PackageItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=0)),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='package_items', to='main.orders')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
