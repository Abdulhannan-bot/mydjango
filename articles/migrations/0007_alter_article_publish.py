# Generated by Django 3.2.16 on 2022-12-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]