from django.db import models

class Activity(models.Model):
    start_time = models.DateTimeField(default=None)
    end_time = models.DateTimeField(default=None)
    

class User(models.Model):
    real_name = models.CharField(max_length=255, default=None, unique=True)
    tz = models.CharField(max_length=255, default=None)
    activity_periods = models.ManyToManyField(Activity, related_name='activity', blank=True)
    def __str__(self):
        return self.real_name
