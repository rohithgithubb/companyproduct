from django.db import models

# Create your models here.
class Company_User(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    class Meta:
        db_table='Company_User'

class Company_Product(models.Model):
    Product_id=models.IntegerField(primary_key=True)
    Product_name=models.CharField(max_length=30)
    Product_quantity=models.IntegerField()
    class Meta:
        db_table='Company_Product'