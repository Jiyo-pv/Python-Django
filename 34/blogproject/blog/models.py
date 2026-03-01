# Program 34: Blog Application
# @JIYO P V ROLL NO:33 Date: 01-03-2026

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title