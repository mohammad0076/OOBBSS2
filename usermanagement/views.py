from .models import Books
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .forms import BooksForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile

from .models import User


def registers(request):

    form = UserCreationForm()
    if request.method == "POST":


        form = UserCreationForm(request.POST)
        if form.is_valid():

            user = form.save()
            if request.user.is_authenticated:
                return  redirect('book_list')

    context={
        'form' : form
    }

    return render(request, 'usermanagement/registration.html', context)



@login_required
def create_profile(request):


    profile_list = Profile.objects.filter(user=request.user)

    if len(profile_list) != 0:
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm({'contact_no':profile.contact_no,
                                     'full_name':profile.full_name,
                                    'email': profile.email, 'district':profile.district,'city':profile.city,'postal_code':profile.postal_code,'street_address':profile.street_address,'house_no':profile.house_no
                          })

    else:


        profile = None
        form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user



            if profile == None:
                instance.save()
            else:
                profile.contact_no = instance.contact_no

                profile.save()

                return redirect('book_list')


    context = {
        'form': form
    }


    return render(request, 'usermanagement/creation_of_profile.html', context)


@login_required
def show_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = "Please complete your profile "

    context = {
        'profile': profile
    }
    return render(request, 'usermanagement/showing_user_profile.html', context)


def showbooks(request):


    book = Books.objects.all()

    if request.method == 'POST':


        P = Books.objects.filter(category__icontains=request.POST['search'])
        Q = Books.objects.filter(title__contains=request.POST['search'])
        R = Books.objects.filter(author__icontains=request.POST['search'])

        book = P | Q | R



    context = {
        'all_books': book
    }
    return render(request, 'productmanagement/showbooks.html', context)



@login_required
def upload_product_by_user(request):
    form = BooksForm()
    if request.method == "POST":
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid:

            form.save()


            return redirect('book_list')



    return render(request, 'productmanagement/upload_product.html', {'form': form})



def ij(request):
    d = Books.city
    e = Profile.city
    P = d | e

    return render(request,'usermanagement/location_wise book.html',{'P': p })
