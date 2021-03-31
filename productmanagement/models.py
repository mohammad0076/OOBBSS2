from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Books (models.Model):
    title =models.CharField(max_length=200,default='BOOK TITLE')
    author =models.CharField(max_length=200,default='AUTHOR')
    image =models.ImageField(upload_to='product/images' ,null=True,default='')
    price=models.IntegerField(blank=False)
    publisher = models.CharField(max_length=200,blank=False)
    edition = models.CharField(blank=False,max_length=200)
    category= models.CharField(blank= False,max_length=200)
    city = models.CharField(blank= False,max_length=200,default ="")
    language = models.CharField( blank =False,max_length= 200,default= "")
    pages = models.CharField(blank=False,max_length= 2000,default="")


    def __str__(self):
        return self.title + self.city

