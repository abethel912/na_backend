from django.db import models

class Nabars(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=700)
    state = models.CharField(max_length=2, null=True)
    description = models.CharField(max_length=3000)
    address = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    
    
