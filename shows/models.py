from django.db import models
from city.models import City
from band.models import Band


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
