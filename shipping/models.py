from django.db import models

# Create your models here.
from django.db import models
class data2(models.Model):
  product = models.CharField(max_length=255)
  price = models.CharField(max_length=255)
