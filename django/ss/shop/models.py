from django.db import models

# Create your models here.

class Product(models.Model):
	Product_id = models.AutoField
	Product_name = models.CharField(max_length = 50)
	Product_about = models.CharField(max_length = 400)
	Product_price = models.IntegerField()
	Product_date = models.DateField()
	image = models.ImageField(upload_to = 'shop/image' ,default="")

	def __str__(self):
		return self.Product_name