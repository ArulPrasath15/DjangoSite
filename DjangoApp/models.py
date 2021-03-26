from django.db import models

# Create your models here.
class formreg(models.Model):
    fname=models.CharField(max_length=20);
    lname=models.CharField(max_length=20);
    roll=models.CharField(max_length=20);
    email = models.CharField(max_length=30);
    phone = models.CharField(max_length=20);
    dept = models.CharField(max_length=20);
    batch = models.CharField(max_length=20);
    sec = models.CharField(max_length=20);
