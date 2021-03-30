from .models import Books
from django import forms
class BooksForm(forms.Modelform):
    class Meta:
        model = Books
        fields = ('title','author','image','price','publisher', 'category','location')