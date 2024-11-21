# Generated by Django 5.0.2 on 2024-11-20 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='max_spend',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
        ),
    ]