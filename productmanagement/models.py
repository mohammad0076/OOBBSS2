from django.db import models

# Create your models here.
class Books (models.Model):
    title =models.CharField(max_length=200,default='BOOK TITLE')
    author =models.CharField(max_length=200,default='AUTHOR')
    price=models.IntegerField(blank=False)
    publlisher = models.CharField(max_length=200,blank=False)
    edition = models.DateField(blank=False,max_length=200)
    category= models.CharField(blank= False,max_length=200)

    def __str__(self):


        return self.title

