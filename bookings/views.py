import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BookingForm
from .models import Booking

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def book_appointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_appointment.html', {'form': form})

def booking_calendar(request):
    bookings = Booking.objects.all()
    events = [
        {
            'title': f"{booking.customer_name} - {booking.service.name}",
            'start': f"{booking.date}T{booking.time}",
        } for booking in bookings
    ]
    return render(request, 'bookings/booking_calendar.html', {'events': json.dumps(events)})