from django.shortcuts import render
from django.db.models import Count

from api.models import Product,Order
from api.serializers import UserSerializer,ProductSerializer,OrderSerializer

from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions

# Create your views here.

class SignUpView(APIView):
    def post(self,request,*args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.error)
    
class ProductCrud(viewsets.ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class ProductReadOnly(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def update(self, request, *args, **kwargs):
        return Response({"message": "Updates are not allowed for this user."})

    def destroy(self, request, *args, **kwargs):
        return Response({"message": "deletes are not allowed for this user."})

    def create(self, request, *args, **kwargs):
        return Response({"message": "creates are not allowed for this user."})
    
class OrderView(viewsets.ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=OrderSerializer
    def get_queryset(self):
        product_id=self.kwargs.get('product_id')
        return Order.objects.filter(product_id=product_id)
    
    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        serializer.save(user=self.request.user, product_id=product_id)
    
    def update(self, request, *args, **kwargs):
        return Response({"message": "Updates are not allowed for this user."})

class AllOrderedProductsView(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
    
class ProductListView(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.annotate(purchase_count=Count('order'))
        return queryset.order_by('-purchase_count')