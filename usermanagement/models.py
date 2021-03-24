from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Address(models.Model):
    house_no = models.IntegerField(blank=True, null=True, default="")
    street_address = models.CharField(max_length=200)
    postal_address = models.CharField(max_length=200)
    post_code = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return str(self.house_no) + " " + self.street_address + " " + self.city

class Profile(models.Model):
    contact_no = models.CharField(max_length=20)
    full_name= models.CharField(max_length=200,null=False,default=None)
    email = models.EmailField(max_length=200,default=None,null=False)
    pro_pic = models.ImageField(upload_to='s/ss', blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, default=None, null=True)

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)



    def __str__(self):
        return self.user.username