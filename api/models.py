from django.db import models

# Create your models here.
class Router(models.Model):
    specifications = models.FileField(upload_to='router_specifications')
