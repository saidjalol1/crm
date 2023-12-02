# Generated by Django 4.2.7 on 2023-11-30 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_expenses_orders_received_admin_usertrack'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=250)),
                ('car_type', models.CharField(max_length=250)),
                ('car_color', models.CharField(max_length=250)),
                ('car_number', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='deliver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deliver_products', to='main.deliver'),
        ),
    ]
