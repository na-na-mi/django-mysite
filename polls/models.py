from django.db import models


# Create your models here.
class SalesData(models.Model):
    line_ID = models.IntegerField()
    order_ID = models.CharField(max_length=100)
    order_Date = models.CharField(max_length=100)
    sent_Date = models.CharField(max_length=100)
    post_Way = models.IntegerField()
    customer_ID = models.CharField(max_length=100)
    customer_Name = models.CharField(max_length=100)
    split = models.IntegerField()
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    product_ID = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    son_Series = models.CharField(max_length=100)
    product_Name = models.CharField(max_length=100)
    sales_Total = models.DecimalField(max_digits=11, decimal_places=2)
    product_Num = models.IntegerField()
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    profit = models.DecimalField(max_digits=12, decimal_places=2)

