from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    full_name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    post_data = models.DateField(default=timezone.datetime.now())
    message = models.CharField(max_length=240)

    def __str__(self):
        return f"Posted by :{self.full_name}"

