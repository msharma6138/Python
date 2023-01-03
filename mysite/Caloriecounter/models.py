from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    
    def __str__(self):
        return self.first_name + " " + self.last_name

# Create your models here.
