from django.db import models

class Person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birthday=models.DateField()
    photo=models.ImageField(upload_to='people')