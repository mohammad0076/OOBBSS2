from django.shortcuts import render
from .models import Books

def showbooks(request):

    book = Books.objects.all()

    context ={
        'all_books': book
    }
    return render(request,'productmanagement/showbooks.html', context)

