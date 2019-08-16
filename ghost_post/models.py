from django.db import models


class Message(models.Model):
    is_boast = models.BooleanField()
    like = models.IntegerField()
    text = models.CharField(max_length=280)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
