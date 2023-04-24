from django.db import models
from datetime import datetime
# Create your models here.

class Ecosystem(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    website = models.CharField(max_length=150, blank=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    