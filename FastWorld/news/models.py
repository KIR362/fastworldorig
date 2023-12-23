from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField('Name', max_length=55)
    intro = models.CharField("Intro", max_length=200)
    full_text = models.TextField('Text')
    date_added = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/feed/{self.id}'

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'

class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, default=0, related_name="comment")
    text = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.text