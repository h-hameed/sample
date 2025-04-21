from django.db import models

# Create your models here.
from django.db import models

class Header(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Line(models.Model):
    header = models.ForeignKey(Header, on_delete=models.CASCADE, related_name='lines')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description