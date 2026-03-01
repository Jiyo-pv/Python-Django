# Program 22: Student Model and Admin Registration
# @JIYO P V ROLL NO:33 Date: 01-03-2026

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.name