from django.db import models
from django.db.models.fields import DateField, SlugField

class Data(models.Model):
    title=models.CharField(max_length=100)
    data=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

