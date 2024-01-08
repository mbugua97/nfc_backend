from django.db import models
from usermanagement.models import Person

class Photo(models.Model):
    owner=models.ForeignKey(Person,on_delete=models.CASCADE)
    Photo=models.ImageField(upload_to='media')
    