from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import datetime


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    descript = models.TextField(max_length=3000)
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    is_posted = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_date(self):
        return f'{self.pub_date.strftime("%b")} {self.pub_date.day}, {self.pub_date.year}'

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50, default='Anonymous')
    text = models.TextField()

    def __str__(self):
        return f'{self.user_name}'


class UserUrl(User):

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})

