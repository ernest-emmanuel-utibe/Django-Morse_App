from django.db import models
from django.urls import reverse


# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=255)
#     age = models.IntegerField()


class Post(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
