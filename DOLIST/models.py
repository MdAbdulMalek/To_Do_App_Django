from django.db import models

# Create your models here.
class DOLIST(models.Model):
    title = models.CharField(max_length=1000)
    time = models.TimeField(blank=True)

    def __str__(self):
        return self.title