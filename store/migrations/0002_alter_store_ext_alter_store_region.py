# Generated by Django 5.0 on 2023-12-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='ext',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='store',
            name='region',
            field=models.CharField(max_length=50),
        ),
    ]
