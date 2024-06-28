from django.db import models

# Create your models here.

class contacts(models.Model):
    Name = models.CharField(max_length=20)
    PhoneNumber = models.CharField(max_length=10)
    Location = models.CharField(max_length=20)
    