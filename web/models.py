from django.db import models


class Review(models.Model):
    author = models.CharField(max_length=30)
    stars = models.SmallIntegerField()
    content = models.TextField(max_length=300)