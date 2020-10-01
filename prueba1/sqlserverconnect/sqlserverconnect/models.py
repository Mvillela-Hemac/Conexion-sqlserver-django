from django.db import models

class sqlserverconn(models.Model):
    Empname=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Salary=models.IntegerField()