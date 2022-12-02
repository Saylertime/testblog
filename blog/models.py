from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    post_image = models.ImageField(upload_to="event_images")
    post_date = models.DateField()


# Create your models here.
