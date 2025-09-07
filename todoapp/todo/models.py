from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    deadline = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)  # ✅ mark if task is done
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']
    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.title} ({self.priority})"
