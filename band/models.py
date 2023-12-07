from django.db import models


# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Meta:
    ordering = ['-name']
