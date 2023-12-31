# Generated by Django 4.2.6 on 2023-11-18 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='profile_images', verbose_name='Avatar')),
                ('gender', models.CharField(blank=True, choices=[('M', 'М'), ('F', 'Ж'), (None, '-')], max_length=1, verbose_name='Gender')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Country')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
