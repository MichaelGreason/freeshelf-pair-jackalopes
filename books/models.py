from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse


class User(AbstractUser):
    location = models.CharField(blank=True, null=True, max_length=250)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Resources(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    url = models.URLField(max_length=300)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to="Category", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Resources"

    def __str__(self):
        return f'{self.title}, by {self.author}'


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})
