from django.db import models
from django.utils import timezone

# Create your models here.
class House(models.Model):
  category = models.CharField(max_length=255)
  use = models.CharField(max_length=255)
  size =models.CharField(max_length=255)
  rooms = models.IntegerField(null=True)
  baths = models.IntegerField(null=True)
  price =models.CharField(max_length=20)
  address = models.CharField(max_length=255)
  phone = models.CharField(max_length=20)
  image = models.ImageField(upload_to='shop/images',default='')
  image2 = models.ImageField(upload_to='shop/images',default='')
  image3 = models.ImageField(upload_to='shop/images',default='')
  image4 = models.ImageField(upload_to='shop/images',default='')
  image5 = models.ImageField(upload_to='shop/images',default='')
  MoreDescription = models.TextField(max_length=255, default='')
  date = models.DateTimeField(default=timezone.now)


  def __str__(self):
    return f"{self.category} {self.address}"
  
class LandPlot(models.Model):
  category = models.CharField(max_length=255)
  use = models.CharField(max_length=255)
  size =models.CharField(max_length=255)
  price =models.CharField(max_length=20)
  address = models.CharField(max_length=255)
  phone = models.CharField(max_length=20)
  plotImage1 = models.ImageField(upload_to='shop/images',default='')
  plotImage2 = models.ImageField(upload_to='shop/images',default='')
  plotImage3 = models.ImageField(upload_to='shop/images',default='')
  plotImage4 = models.ImageField(upload_to='shop/images',default='')
  plotImage5 = models.ImageField(upload_to='shop/images',default='')
  MoreDescription = models.TextField(max_length=255, default='')
  date = models.DateTimeField(default=timezone.now)

class Car(models.Model):
  category = models.CharField(max_length=255)
  carModel = models.CharField(max_length=255, default='' )
  use = models.CharField(max_length=255)
  price =models.CharField(max_length=20)
  phone = models.CharField(max_length=20)
  carImage1 = models.ImageField(upload_to='shop/images',default='')
  carImage2 = models.ImageField(upload_to='shop/images',default='')
  carImage3 = models.ImageField(upload_to='shop/images',default='')
  MoreDescription = models.TextField(max_length=255, default='')
  date = models.DateTimeField(default=timezone.now)


  

