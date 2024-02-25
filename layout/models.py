from django.db import models
from datetime import datetime
from django.utils import timezone


class Messages(models.Model):
    """This is a model to get messages from users"""
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "messages"

    def __str__(self):
        return f"{self.full_name}, {self.email}, {self.company}"
    

class Newsletter(models.Model):
    """This is a model for newsletter"""
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=200)
    join_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "newsletter"
