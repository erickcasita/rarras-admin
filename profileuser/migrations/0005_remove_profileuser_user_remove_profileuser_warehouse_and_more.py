# Generated by Django 5.0 on 2024-02-02 16:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileuser', '0004_remove_profileuser_user_profileuser_user'),
        ('warehouses', '0008_werehousepurchasingdetails_predco'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='warehouse',
        ),
        migrations.AddField(
            model_name='profileuser',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profileuser',
            name='warehouse',
            field=models.ManyToManyField(to='warehouses.warehouses'),
        ),
    ]
