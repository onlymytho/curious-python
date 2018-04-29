# problem statement.
#
# create a stock api which displays prices of each stock
# the api should have the following functionality
#
# 1. Should be able to sort stock from different _markets_
# 2. Should be able to search stock depending on stock _name_ ::DONE
# 3. sort stock in terms of _gain values_
# 4. Only registered _user_ should be able to access stock data


from django.db import models

# Create your models here.

class Stock(models.Model):
    stock_name = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    gain_value = models.CharField(max_length=200, null=True)
    sell_value = models.CharField(max_length=200, null=True)
