from django.db import models
from signup.models import UserAccount

# Create your models here.
class student(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=12)
    author=models.TextField()
    year=models.IntegerField()
    starting_date = models.DateField(null=True, blank=True)
    ending_date = models.DateField(null=True, blank=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.title


