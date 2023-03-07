from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField(blank=True, null=True, max_length=250)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Resources(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    url = models.URLField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.category}, {self.title}, {self.author}, {self.description}, {self.url}'
