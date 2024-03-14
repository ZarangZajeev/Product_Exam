from django.contrib.auth.models import User

from rest_framework import serializers

from api.models import Product,Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        read_only_fields=["id","user"]

class OrderSerializer(serializers.ModelSerializer):
    product=serializers.StringRelatedField()
    user=serializers.StringRelatedField()
    class Meta:
        model=Order
        fields="__all__"
        read_only_fields=["id","user","product","purchased_date"]