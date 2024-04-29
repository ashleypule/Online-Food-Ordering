import random
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from product.models import Product 

from .forms import SignUpForm

from .models import Locations, driver
from django.views import View

def frontpage(response):
    return render(response, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})


def myaccount(request):
    return render(request, 'core/myaccount.html')


def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')

def menu(request):
    products = Product.objects.all()[0:20]
    
    return render(request, 'core/menu.html', {'products': products})


class MapView(View): 
    template_name = "core/map.html"

    def get(self, request):
        key = 'AIzaSyC3Zcg-Rod-bnXvODcqRry4g7Soz5AdjDU'
        eligible_locations = Locations.objects.filter(place_id__isnull=False)
        locations = []

        for location in eligible_locations:
            data = {
                'lat': float(location.lat),
                'lng': float(location.lng),
                'name': location.name
            }
            locations.append(data)

        # Select one random driver
        drivers = list(driver.objects.all())
        selected_driver = None
        if drivers:
            selected_driver = random.choice(drivers)

        context = {
            "key": key,
            "locations": locations,
            "selected_driver": selected_driver,
        }
        return render(request, 'core/map.html', context)