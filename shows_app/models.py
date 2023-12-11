from django.db import models


# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Show(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Meta:
    ordering = ['-date']
