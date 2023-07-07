from rest_framework import serializers
from .models import Order,Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    orders = CustomerSerializer(read_only=True,many=True)
    class Meta:
        model = Order
        fields = '__all__'