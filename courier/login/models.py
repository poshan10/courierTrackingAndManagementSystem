from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete= models.CASCADE)

    post = models.CharField(max_length=60)
    branch = models.CharField(max_length=100)
    age = models.IntegerField()


    def __str__(self):
        return self.user.username