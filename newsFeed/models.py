from django.db import models

class Item(models.Model):
	name = models.TextField(default='')
	phone = models.TextField(default='')
	text = models.TextField(default='')
	image = models.ImageField(upload_to='fish/', null=True, blank=True)
	date = models.DateTimeField(auto_now=True)
