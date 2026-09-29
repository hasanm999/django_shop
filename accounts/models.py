from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    def __str__(self):
        return self.user.username




class Ticket(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tickets')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username