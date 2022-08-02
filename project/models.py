from django.db import models

# Create your models here.




class Product(models.Model):
   name = models.CharField(max_length=200,blank=True,null=True)
   category = models.CharField(max_length=50, blank=True,null=True)
   price = models.DecimalField(max_digits=10,decimal_places=2)
   desc = models.CharField(max_length=200, blank=True,null=True)
   

   starts = models.IntegerField()


   def __str__(self):
      return self.name

   
   class Meta:
      verbose_name_plural='Product'  