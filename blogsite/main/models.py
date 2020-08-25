from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    date_published = models.DateField()

class PostCard(models.Model):
    post = models.OneToOneField(BlogPost, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='card_pics')