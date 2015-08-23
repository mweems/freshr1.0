from django.db import models

class Item(models.Model):
	name = models.TextField(default='')
	phone = models.TextField(default='')
	text = models.TextField(default='')
	image = models.FileField(upload_to='fish/', null=True, blank=True)
