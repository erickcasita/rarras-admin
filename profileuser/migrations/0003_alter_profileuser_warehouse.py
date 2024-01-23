# Generated by Django 5.0 on 2024-01-15 21:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileuser', '0002_alter_profileuser_user'),
        ('warehouses', '0003_werehousestock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='warehouse',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='warehouses.warehouses'),
        ),
    ]
