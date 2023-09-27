from django.db import models
from account.models import *
from project.models import *
import uuid
from datetime import datetime
from tinymce.models import HTMLField
# Create your models here.

class TaskStatus(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

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
    comments = HTMLField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

