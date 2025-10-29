from django.db import models

# Create your models here.
class student(models.Model):
    title=models.CharField(max_length=12)
    author=models.TextField()
    year=models.IntegerField()
    starting_date = models.DateField(null=True, blank=True)
    ending_date = models.DateField(null=True, blank=True)
    is_booked = models.BooleanField(default=False)


