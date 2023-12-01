from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imageUser = models.ImageField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Profile of user {}".format(self.user.username)




