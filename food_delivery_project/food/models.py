from django.db import models

# Create your models here.

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def _str_(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    food_item = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=50, default='Pending')

    def _str_(self): 
        return "Order for {self.customer_name} - {self.food_item.name}"









    

