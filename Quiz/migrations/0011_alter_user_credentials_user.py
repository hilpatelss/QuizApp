# Generated by Django 4.1.8 on 2023-04-26 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Quiz', '0010_user_credentials_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_credentials',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
