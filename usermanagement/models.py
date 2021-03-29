from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    contact_no = models.CharField(max_length=20)
    full_name= models.CharField(max_length=200,null=False,default=None)
    email = models.EmailField(max_length=200,default=None,null=False)

    district = models.CharField(max_length=200, default=None, null=True)
    city = models.CharField(max_length=200)

    postal_code = models.CharField(max_length=20,null=True)
    street_address = models.CharField(max_length=200, default=None)
    house_no = models.CharField(max_length=200, default=None)


    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username