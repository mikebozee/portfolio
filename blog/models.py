import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField('date published')
    featured_image = models.ImageField()
    content_text = models.TextField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now


class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=False)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

