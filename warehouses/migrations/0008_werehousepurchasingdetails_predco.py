# Generated by Django 5.0 on 2024-01-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0007_werehousepurchasing_werehousepurchasingdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='werehousepurchasingdetails',
            name='predco',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
