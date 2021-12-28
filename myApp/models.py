from django.db import models

# Create your models here.
class Event(models.Model):
    Name = models.CharField(max_length=100,null=False,blank=False)
    Date = models.CharField(max_length=100,null=False,blank=False)
    Time = models.CharField(max_length=100,null=False,blank=False)
    Location=models.CharField(max_length=100,null=False,blank=False)
    Image=models.ImageField(upload_to="",blank=True)
    Is_Liked=models.BooleanField(default=False)