from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField(blank=True, null=True, max_length=250)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
