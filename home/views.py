from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Hotel,Booking
from django.contrib import messages

# Create your views here.
def index(request):
    hotel = get_object_or_404(Hotel,id=1)
    return render(request,'home/index.html',{'hotel':hotel})

def order(request):
    hotel = get_object_or_404(Hotel,id=1)
    if request.method == 'POST':
        checkin_dtime = request.POST.get('checkin_dtime')
        checkout_dtime= request.POST.get('checkout_dtime')
        rooms_already_booked =Booking.objects.all().count()
        number_of_rooms_left = hotel.total_rooms - rooms_already_booked
        if number_of_rooms_left  >= 1:
            entry=Booking(checkin_dtime=checkin_dtime,checkout_dtime=checkout_dtime)
            entry.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            finished_bookings_count = Booking.objects.filter(checkout_dtime__lte=checkin_dtime, booked=True).count()
            if finished_bookings_count > 0:
                entry=Booking(checkin_dtime=checkin_dtime,checkout_dtime=checkout_dtime)
                entry.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.success(request,'Rooms full,Better luck next time!')
                return render(request,'home/index.html',{'hotel':hotel})
    return render(request,'home/booking.html',{'hotel':hotel})
