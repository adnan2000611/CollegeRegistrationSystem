from django.db import models

# Create your models here.
class Student(models.Model):
    StudentID=models.IntegerField(primary_key=True, unique=True )
    Name=models.CharField(max_length=60)
    Gender=models.CharField(max_length=1)
    Nationality=models.CharField(max_length=30)
    PhoneNumber=models.IntegerField()
    Major=models.CharField(max_length=60)
    BirthofDate=models.DateField()
    GPA=models.FloatField()
    Password=models.CharField(max_length=60, default="")
     