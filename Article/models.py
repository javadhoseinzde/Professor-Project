from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    pic = models.ImageField(upload_to = "media/", blank=True)
    description = models.TextField()
    published = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
