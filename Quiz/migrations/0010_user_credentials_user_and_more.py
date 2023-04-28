# Generated by Django 4.1.8 on 2023-04-26 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Quiz', '0009_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_credentials',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_credentials',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
