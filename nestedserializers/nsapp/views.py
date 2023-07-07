from django.shortcuts import render
from .models import Customer, Order
from nsapp.serializers import CustomerSerializer, OrderSerializer
from rest_framework import viewsets
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
