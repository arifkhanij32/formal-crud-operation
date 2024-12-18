from django.db import models

# Create your models here.
class Emp(models.Model):
    S_NO=models.IntegerField(primary_key=True)
    NAME=models.CharField(max_length=40)
    AGE=models.IntegerField()
    
