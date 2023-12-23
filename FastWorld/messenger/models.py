from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    text = models.CharField('Message:', max_length=500)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name='to_reciever', on_delete=models.CASCADE)
    is_readed = models.BooleanField('Readed', default=False)
    date_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sender) + ' to ' + str(self.reciever)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
