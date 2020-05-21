from django.db import models
import pandas as pd
# Create your models here.

class Companies(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return str(self.id) + "--" + self.name

