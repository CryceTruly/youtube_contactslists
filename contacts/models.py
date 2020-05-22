from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    phone_number = models.CharField(max_length=100,)
    picture_url = models.URLField(null=True)
    country_code = models.CharField(max_length=100,)
    is_favorite = models.BooleanField(default=False,)

    class Meta:
        ordering = ['created_at']
