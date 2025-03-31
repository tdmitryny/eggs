from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='media/images/')
    slug = models.SlugField(max_length=200, blank=True, null=True)
    
    
    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # Only create a slug if it doesn't exist
            self.slug = slugify(self.title)
        super().save(*args, **kwargs) 

    

    class Meta:
        verbose_name = 'About'
        