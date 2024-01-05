from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    website = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    company = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Todo(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField()

class Post(models.Model):
    userId= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=200)

class Comment(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    body = models.CharField(max_length=200)
