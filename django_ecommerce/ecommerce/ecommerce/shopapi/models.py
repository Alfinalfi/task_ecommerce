from django.db import models
import uuid


# Create your models here.


class Customer(models.Model):
    first_name=models.CharField(max_length=250,help_text='Enter first name')
    last_name=models.CharField(max_length=250,help_text='Enter last name')
    mobile_number=models.CharField(max_length=50,help_text='Enter mobile number')
    email_id=models.EmailField(unique=True)
    address=models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name    
    
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name=models.CharField(max_length=250,help_text='Enter product name')
    categories=models.ManyToManyField(Category)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    description = models.TextField()
    price=models.IntegerField()
    product_active=models.BooleanField(default=True)
    product_added_on=models.DateField()


    class Meta:
        ordering=['-product_added_on']

    def __str__(self):
        return self.name






   


