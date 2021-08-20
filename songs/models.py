from django.db import models
from django.db.models.base import Model

class Artist(models.Model):
    GENDER_TYPE =[
    ('M', 'Maleee'),
    ('F', 'Female')
]

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1,choices=GENDER_TYPE)


    def __str__(self):
        return self.name

class Song(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    listened_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title