from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.urls import reverse

class Snack (models.Model):
    title= models.CharField(max_length=64)
    purchaser =models.CharField(max_length=64)
    description=models.TextField()
    def __Str__(self):
        return self.title
    def get_absolute_url (self):
            # Go to home page AFTER ADDED
        return reverse("detail", args=[str(self.id)])
        # return reverse('home')