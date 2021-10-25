from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Joke(models.Model):

   joke_title = models.CharField(max_length = 50, blank=True)
   joke_description = models.CharField(max_length = 500, blank=True)
   joke_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="joke_user")
   joke_likes = models.ManyToManyField(User)
   joke_image_base64 = models.TextField(blank=True)
   joke_json = models.TextField(blank=True)

   class Meta:
      db_table = "joke"