from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sub Categories"


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    post = RichTextField(blank=True, null=True)
    category = models.ForeignKey(SubCategory, default=1,on_delete=models.SET_DEFAULT)
    date_published = models.DateField()

    def get_absolute_url(self):
        return f'{self.id}/'

    def __str__(self):
        return self.title


class PostCard(models.Model):
    category = models.ForeignKey(SubCategory, default=1, on_delete=models.SET_DEFAULT)
    post = models.OneToOneField(BlogPost, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='card_pics')

    def __str__(self):
        return self.post.title


class MetaInfo(models.Model):
    post = models.OneToOneField(BlogPost, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name_plural = "Meta Info"