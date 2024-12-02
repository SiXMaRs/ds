from django.db import models


# Create your models here.
class course(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=20)
    te = models.CharField(max_length=20)