from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    title = models.CharField(max_length=212)

    def __str__(self):
        return self.title


class Tag(TimeStampedModel):
    title = models.CharField(max_length=212)

    def __str__(self):
        return self.title


class Post(TimeStampedModel):
    title = models.CharField(max_length=212)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    tags = models.ManyToManyField(Tag, verbose_name="tags")
    description = models.TextField()
    image = models.ImageField(upload_to='posts')

    def __str__(self):
        return self.title

