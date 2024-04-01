from email import message
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Post(models.Model):

    def __str__(self) -> str:
        return self.title

    title = models.CharField(max_length=255)
    # content = models.TextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    view = models.IntegerField(default=0)
    create_by = models.ForeignKey(
        User, related_name='author', on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, related_name='category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)


class Comment(models.Model):
    def __str__(self) -> str:
        return self.message
    
    post = models.ForeignKey(
        Post, related_name='comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comment_author', on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()