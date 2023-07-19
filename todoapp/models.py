from django.db import models
from django.utils.timezone import now


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start = models.DateTimeField(default=now)
    link = models.URLField(max_length=400, blank=True)
    end = models.DateTimeField()

    def __str__(self):
        return f"{self.title}"
