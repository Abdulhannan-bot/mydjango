# Generated by Django 3.2.16 on 2022-12-15 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20221215_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
