from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=16)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    have = models.BooleanField(default=True)
    image = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.product_name

class Comment(models.Model):
    name = models.CharField(max_length=16)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.name} - {self.product}'

