import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Wishlist(models.Model):
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Item(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(default='noimage.jpg')
    url = models.CharField(null = True, blank = True, max_length=120)
    date = models.DateTimeField(default=timezone.now)
    wishlist = models.ForeignKey(Wishlist, default=None, on_delete=models.CASCADE)
    checkbox = models.BooleanField(default=False)
    boughtby = models.CharField(null = True, blank = True, max_length=120)
