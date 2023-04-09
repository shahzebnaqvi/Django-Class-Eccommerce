from django.db import models
from django.contrib.auth.models import User

class CartItem(models.Model):
    quantity = models.IntegerField(max_length = 150)
    price = models.IntegerField(max_length = 1000)
    cartid = models.IntegerField(max_length = 100)
    productid = models.CharField(max_length = 200)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    def __str__(self):
        return self.productid