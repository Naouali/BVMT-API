from django.db import models
import pandas as pd
# Create your models here.



class Data(models.Model):
    class Meta:
        verbose_name_plural = 'Data'
    date = models.CharField(max_length=20)
    price = models.IntegerField()
    opening = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    volume = models.IntegerField()

    def __str__(self):
        return str(str(self.date) + " " + str(self.price) +' '+ str(self.opening) +' ' + str(self.high)+' ' +str(self.low) + " " + str(self.volume))
class Companies(models.Model):
    name = models.CharField(max_length=20, null=False)
    data = models.ForeignKey(Data, default=1, on_delete=models.SET_DEFAULT)
    def __str__(self):
        return str(self.id) + "--" + self.name