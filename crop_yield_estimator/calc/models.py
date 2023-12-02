from django.db import models

# Create your models here.
class Calculator(models.Model):
    number1=models.IntegerField()
    number2=models.IntegerField()
    name_of_user=models.CharField(max_length=100)
    offer=models.BooleanField(default=False)
    img=models.ImageField(upload_to='pics')