from django.db import models

class Jozve(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, max_length=100)
    description = models.TextField()
    file = models.FileField()
