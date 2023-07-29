from django.shortcuts import render
from .models import Category,Customer,Product
from .serializers import CategorySerializer,CustomerSerializer,ProductSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny
from datetime import datetime,timedelta


# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def ListCustomer(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)
        
        


@csrf_exempt
@api_view(['GET','PUT','PATCH','DELETE'])
@permission_classes((AllowAny,))
def DetailCustomer(request,pk):
    customer=Customer.objects.get(pk=pk)
    if request.method =='GET':
        serializer =CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors, status=400)  
    
    elif request.method == 'PATCH':
        serializer = CustomerSerializer(customer,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)
        
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=204)
    
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def ProductList(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
          return Response(serializer.errors, status=400)
    

@csrf_exempt
@api_view(['GET','PUT','PATCH','DELETE'])
@permission_classes((AllowAny,))
def ProductDetail(request,pk):
     product = Product.objects.get(pk=pk)
     if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

     elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data,status=201)
        else:
          return Response(serializer.errors, status=400)

     elif request.method == 'PATCH':
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            
            registration_date = product.product_added_on
            two_months_ago = datetime.now() - timedelta(days=60)
            if registration_date <= two_months_ago:
                product.product_active = False
            serializer.save()
            return Response(serializer.data,status=201)
        else:
          return Response(serializer.errors, status=400)

     elif request.method == 'DELETE':
        product.delete()
        return Response(status=204)









  
    
    
    