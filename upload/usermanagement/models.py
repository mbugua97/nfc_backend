from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)
    phone=models.CharField(max_length=100,unique=True,blank=False,null=False)

    def __str__(self):
        return self.phone