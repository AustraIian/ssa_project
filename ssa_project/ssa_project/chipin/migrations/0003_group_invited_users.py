# Generated by Django 5.0.2 on 2024-11-06 23:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipin', '0002_alter_group_members'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='invited_users',
            field=models.ManyToManyField(blank=True, related_name='pending_invitations', to=settings.AUTH_USER_MODEL),
        ),
    ]