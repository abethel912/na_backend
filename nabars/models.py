from django.db import models

class Nabars(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=700)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    website = models.CharField(max_length=100)
    
    
