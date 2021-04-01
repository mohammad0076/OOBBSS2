from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import Books
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .forms import BooksForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
def showbooks(request):


    book = Books.objects.all()
    if request.method == 'POST':
        P = Books.objects.filter (category__icontains = request.POST['search'])
        Q = Books.objects.filter(category__icontains  = request.POST['search'])
        R = Books.objects.filter(author__icontains = request.POST['search'])

        book = P | Q | R

       

    context ={
        'all_books': book
             }
    return render(request,'productmanagement/showbooks.html', context)


@login_required
def upload_product_by_user(request):
    form = BooksForm()
    if request.method  == "POST":
        form = BooksForm( request.POST,request.FILES)
        if form.is_valid:
            form.save()




            return redirect('book_list')

    return  render (request,'productmanagement/upload_product.html',{'form':form })

