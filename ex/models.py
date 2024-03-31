from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos")


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    text = models.TextField()
