from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length = 50)

class Attendee(models.Model):
    firstname = models.CharField(max_length = 50)
    secondname = models.CharField(max_length = 50)
    email = models.EmailField()
    gender = models.CharField(max_length = 50)
    country = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 20)
    event = models.ForeignKey(Events, models.CASCADE)

class Subscriber(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    email = models.EmailField()