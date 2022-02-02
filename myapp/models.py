from django.db import models


# Create your models here.
class Person(models.Model):
    # id=models.IntegerField()
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name, self.country
