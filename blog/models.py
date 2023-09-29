from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(default='', null=True, blank=True, max_length=100)
    thumbnail = models.ImageField(upload_to='blog', default='')
    content = RichTextField(default='', config_name='default')
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            base_slug = self.slug
            counter = 1
            while Post.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title