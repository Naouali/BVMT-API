from django.db import models

# Create your models here.
class Companies(models.Model):
    number = models.IntegerField(null=False)
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name
class Data(models.Model):
    id = models.ForeignKey(Companies)
    date = models.DateField()
    price = models.IntegerField(null=False)
    opening_price = models.IntegerField(null=False)
    low = models.IntegerField(null=False)
    high = models.IntegerField(null=False)
    volume = models.IntegerField(null=False)
    variation = models.IntegerField()


    def __str__(self):
        return 

