# Generated by Django 4.2.6 on 2023-12-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='text',
            field=models.CharField(max_length=200, verbose_name='Report:'),
        ),
    ]