from django.db import models

class RegistrationForm(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    home = models.IntegerField()

    def __str__(self):
        return self.name

