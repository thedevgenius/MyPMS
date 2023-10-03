import uuid
from django.db import models
from account.models import *
from project.models import *
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class TaskStatus(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Task Status'
        verbose_name_plural = 'Task Status'

LOW = 3
NORMAL = 2
HIGH = 1
STATUS_CHOICES = (
    (LOW, 'Low'),
    (NORMAL, 'Normal'),
    (HIGH, 'High'),
)

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Member, on_delete=models.CASCADE)
    priority = models.IntegerField(default=1, choices=STATUS_CHOICES)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    comments = RichTextField(config_name='default')
    files = models.ImageField(upload_to='file/', null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'

class Commemts(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    description = RichTextField(config_name='default')
    commented_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Comment'

class CommentFile(models.Model):
    file = models.FileField(upload_to='file/', max_length=255)
    commemt = models.ForeignKey(Commemts, on_delete=models.CASCADE)
    attached_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return os.path.basename(self.file.name)