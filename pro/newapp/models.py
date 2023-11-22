from django.db import models


# Create your models here.
class user_details(models.Model):
    Fname=models.CharField(max_length=128)
    Lname = models.CharField(max_length=128)
    User_Name= models.CharField(max_length=128)
    Password=models.IntegerField()

class Book_details(models.Model):
    Book_Name=models.CharField(max_length=128)
    Code=models.IntegerField(max_length=5)
    Author_Name=models.CharField(max_length=128)
    Status=models.CharField(max_length=128)
    Amount=models.IntegerField()
    Created_date=models.DateField()
    Updated_date=models.DateField()