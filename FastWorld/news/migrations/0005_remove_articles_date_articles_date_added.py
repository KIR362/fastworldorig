# Generated by Django 4.2.5 on 2023-11-05 07:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_articles_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='date',
        ),
        migrations.AddField(
            model_name='articles',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
