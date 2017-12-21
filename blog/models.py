from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField('date published')
    featured_image = models.ImageField()
    content_text = models.TextField()

    def __str__(self):
        return self.title
