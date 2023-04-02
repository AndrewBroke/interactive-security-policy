from django.db import models

class Policy(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=False)