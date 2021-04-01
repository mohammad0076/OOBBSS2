from django import forms

from .models import Profile
from  django import  forms
from .models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'image', 'price', 'publisher', 'edition', 'category', 'city','language','pages']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('contact_no', 'full_name', 'email','district','city','postal_code','street_address','house_no' )
