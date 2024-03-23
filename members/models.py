from django.db import models

# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return self.first_name + " " + self.last_name



