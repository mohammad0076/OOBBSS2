from django.contrib import admin

# Register your models here.
from .models import Profile,Books

admin.site.register([Profile,Books])
