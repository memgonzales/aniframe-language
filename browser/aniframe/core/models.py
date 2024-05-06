from django.db import models


# Create your models here.
class Codes(models.Model):
    # filename = models.CharField(max_length=60, default="None")
    code = models.TextField()

    def __str__(self):
        return self.title
