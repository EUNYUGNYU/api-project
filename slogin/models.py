from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

class Photo(models.Model):
    text=models.TextField()
    image=models.ImageField(upload_to="blogimage")
    image_thumbnail = ImageSpecField(source = 'image',processors=[ResizeToFill(100,100)], format="PNG", options={'quality':60})