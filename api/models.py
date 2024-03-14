from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    size=models.PositiveIntegerField()
    color=models.CharField(max_length=200)
    options=(
        ("Available","Available"),
        ("Sold out","Sold out"),
    )
    status=models.CharField(max_length=200,choices=options,default="Available")

    def __str__(self):
        return self.name

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    purchased_date=models.DateTimeField(auto_now_add=True)
    qty=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product