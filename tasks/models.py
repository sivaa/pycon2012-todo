from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 15, choices = { ('P', 'PERSONAL'), ('O', 'OFFICIAL'),})
    priority = models.CharField(max_length = 15, choices = { ('H', 'HIGH'), ('M', 'MEDIUM'), ('L', 'LOW'),})
    last_date = models.DateField()
    done = models.BooleanField(default = False)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name