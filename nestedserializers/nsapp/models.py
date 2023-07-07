from django.db import models
# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)

class Order(models.Model):
    product = models.CharField(max_length=25)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer,related_name="customers",on_delete=models.CASCADE)
