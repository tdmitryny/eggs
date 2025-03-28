from email.policy import default
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']



    
