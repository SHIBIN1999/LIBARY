from django.db import models

# Create your models here.
class student(models.Model):
    title=models.CharField(max_length=12)
    author=models.TextField()
    year=models.IntegerField()

