from django.db import models

# Create your models here.


class Questions(models.Model):
    question = models.CharField(null=True, max_length=200)
    image = models.ImageField(upload_to="images", null=True)
