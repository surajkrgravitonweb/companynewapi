from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.IntegerField(max_length=12)
    title=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    address=models.CharField(max_length=200)


    def __str__(self):
        return self.name