from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Course(models.Model):
    cName = models.CharField(max_length=100)

    DAY = (
        (1, 'SAT'),
        (2, 'SUN'),
        (3, 'MON'),
        (4, 'TUE'),
        (5, 'WED'),
        (6, 'SAT-MON'),
        (7, 'SUN-TUE')
    )
    day = models.IntegerField(choices=DAY)

    TIME = (
        (1, '07:45-09:15'),
        (2, '09:15-10:45'),
        (3, '10:45-12:15'),
        (4, '13:00-15:00'),
        (5, '15:00-17:00'),
        )
    time = models.IntegerField(choices=TIME)

    Id = models.IntegerField(primary_key=True)

class AllCourses(models.Model):
    Name = models.CharField(max_length=100,default="")

    acDAY = (
        (1, 'SAT'),
        (2, 'SUN'),
        (3, 'MON'),
        (4, 'TUE'),
        (5, 'WED'),
        (6, 'SAT-MON'),
        (7, 'SUN-TUE'),
    )
    Day = models.IntegerField(choices=acDAY,default=0)

    acTIME = (
        (1, '07:45-09:15'),
        (2, '09:15-10:45'),
        (3, '10:45-12:15'),
        (4, '13:00-15:00'),
        (5, '15:00-17:00'),
        )
    Time = models.IntegerField(choices=acTIME,default=0)

    Id = models.IntegerField(primary_key=True,default=0)
