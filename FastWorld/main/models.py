from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

'''class Profile(models.Model):
    prof_photo = models.ImageField(width_field='picture_width',height_field='picture_height', max_length=255, upload_to ='profile_images/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.prof_photo
'''

class Profile(models.Model):
    GENDER_CHOICE = (
    ("M", "М"),
    ("F", "F"),
    (None, "-")
    )

    LANG_CHOICE = (
        ("R", "Русский"),
        ("E", "English"),
        (None, "-")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField('Avatar', blank=True, upload_to = 'main')
    lang = models.CharField('Language', max_length=1, choices=LANG_CHOICE, blank=True)
    gender =  models.CharField('Gender', max_length=1, choices=GENDER_CHOICE, blank=True)
    city = models.CharField('Country', max_length=100, blank=True)
    birth_date = models.DateField('Birth date', null=True, blank=True)
    followers = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    follower_for = models.ForeignKey(User, related_name = 'follower_for', on_delete = models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Follower'
        verbose_name_plural = 'Followers'

class Report(models.Model):
    text = models.CharField('Report:', max_length=200)
    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
