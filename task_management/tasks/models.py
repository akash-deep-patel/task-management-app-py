from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255,blank=True)
    category = models.CharField(max_length=50, blank=True)
    tags = models.CharField(max_length=255, blank=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
