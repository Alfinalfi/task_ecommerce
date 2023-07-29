from .models import Customer,Category,Product
from rest_framework import serializers



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (

            'first_name',
            'last_name',
            'mobile_number',
            'email_id',
            'address'
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (

            'name'

        )       

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id ',
            'name',
            'categories',
            'Customer',
            'description',
            'price',
            'product_active',
            'product_added_on'



        )      