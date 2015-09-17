from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    text = models.TextField(default='')
    image = models.ImageField(upload_to='fish/', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
