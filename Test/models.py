from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length= 300)
    content = models.TextField()
    #total_like = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author


class Like(models.Model):
    #like = models.CharField(max_length=20)
    user = models.ManyToManyField(User,related_name="user_like",blank=True)
    post_like = models.ManyToManyField(Post, related_name="post_like",blank=True)

    def __str__(self):
        return str(self.user)
