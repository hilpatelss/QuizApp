# Generated by Django 4.1.8 on 2023-04-16 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Quiz', '0002_delete_usersubmittedanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubmittedAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_answer', models.CharField(max_length=200)),
                ('right_answer', models.CharField(max_length=200)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Submitted Answers',
            },
        ),
    ]
