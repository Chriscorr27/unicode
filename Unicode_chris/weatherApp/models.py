from django.db import models

# Create your models here.
class City_weather(models.Model):
    name= models.CharField(max_length=250)
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.name