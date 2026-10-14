from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    cover= models.ImageField(upload_to='book/covers/', blank=True)  # تصویر جلد




