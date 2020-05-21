from django.db import models

# Create your models here.
class Companies(models.Model):
    number = models.IntegerField(null=False)
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name
