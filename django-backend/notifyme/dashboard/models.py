from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(default='', max_length=100)
    code = models.CharField(default='', max_length=10)

    def __str__(self):
        return self.name


class Deadline(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    message = models.CharField(default='', max_length=500)

    def __str__(self):
        return self.message
