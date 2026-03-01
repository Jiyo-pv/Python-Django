# Program 32: Student Management System
# @JIYO P V ROLL NO:33 Date: 01-03-2026

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name