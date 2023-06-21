from django.db import models
from django.contrib.auth.models import User

class Universe(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    universe = models.ForeignKey(Universe, related_name='stocks', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
