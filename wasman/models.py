from django.db import models

# Create your models here.
class WasmanBase(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        abstract = True
