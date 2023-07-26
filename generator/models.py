from django.db import models

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name
