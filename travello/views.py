from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    Dest1 = Destination()
    Dest1.name = 'Mumbai'
    Dest1.desc = 'The city that never sleeps'
    Dest1.img = 'destination_1.jpg'
    Dest1.price = 700
    Dest1.offer = False
  
    Dest2 = Destination()
    Dest2.name = 'Hyderabad'
    Dest2.desc = 'First Biryani, Then Sherwani'
    Dest2.img = 'destination_2.jpg'
    Dest2.price = 650
    Dest2.offer = True

    Dest3 = Destination()
    Dest3.name = 'Bengaluru'
    Dest3.desc = 'Beautiful City'
    Dest3.img = 'destination_3.jpg'
    Dest3.price = 750
    Dest3.offer = True

    dests = [Dest1, Dest2, Dest3]
    return render(request,"index.html",{'dests': dests})