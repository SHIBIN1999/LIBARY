from django.db import models

# Create your models here.
class UserAccount(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_Admin=models.BooleanField(default=False)



    def __str__(self):
        return self.name
    
