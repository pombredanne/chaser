from django.db import models

# Create your models here.

class Chaser(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

