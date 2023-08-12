from django.db import models

class Data(models.Model):
    text = models.CharField()
    label =  models.CharField()

    def __str__(self):
        return self.text
