# Generated by Django 3.2.16 on 2022-12-13 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='nada'),
            preserve_default=False,
        ),
    ]
