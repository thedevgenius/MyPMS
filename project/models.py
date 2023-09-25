from django.db import models
from account.models import Member
from datetime import datetime
from tinymce.models import HTMLField
from django.utils.text import slugify
import os

# Create your models here.
class ProjectStatus(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='', null=True, blank=True, max_length=100)
    associate = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE)
    description = HTMLField(null=True, blank=True)
    url = models.URLField(default='', null=True, blank=True)
    adminurl = models.URLField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=255, default='', null=True, blank=True)
    password = models.CharField(max_length=255, default='', null=True, blank=True)
    extra_credential = HTMLField(null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.now)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class File(models.Model):
    file = models.FileField(upload_to='file/', max_length=254)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return os.path.basename(self.file.name)