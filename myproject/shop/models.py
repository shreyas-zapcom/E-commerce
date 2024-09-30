from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #look at this>>
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.CharField(max_length=255)
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    