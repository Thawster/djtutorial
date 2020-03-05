from django.db import models

class Rider(models.Model):
    name = models.CharField(max_length=128)
    trips = models.ManyToManyField(self, through='Trip')

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=128)
    trips = models.ManyToManyField(self, through='Trip')

    def __str__(self):
        return self.name

class Trip(models.Model):
    driver = models.ForeignKey(Person, on_delete=models.CASCADE)
    rider = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_ride = models.DateField()
    location = models.CharField(max_length=64)
