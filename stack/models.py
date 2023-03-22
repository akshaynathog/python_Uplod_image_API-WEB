from django.db import models

# Create your models here.

class Questions(models.Model):
    question=models.CharField(null=True, max_length=200,blank=True)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    # created_date=models.DateField(auto_now_add=True)

    # def __str__(self) :
    #     return self.created_date