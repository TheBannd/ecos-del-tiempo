from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Eco(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="ecos", null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
    
class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to="pages")
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to="pages")
    created = models.DateField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)