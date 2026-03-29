from django.db import models

from django.db import models

class staff(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name
