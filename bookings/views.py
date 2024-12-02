from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking
from datetime import date, timedelta
import calendar


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


def book_appointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_appointment.html', {'form': form})


def update_appointment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/update_appointment.html', {'form': form})


def delete_appointment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'bookings/delete_appointment.html', {'booking': booking})


def booking_success(request):
    return render(request, 'bookings/booking_success.html')


def booking_calendar(request):
    today = date.today()
    month_calendar = calendar.Calendar().monthdatescalendar(today.year, today.month)
    calendar_data = []

    for week in month_calendar:
        week_data = []
        for day in week:
            day_bookings = Booking.objects.filter(date=day)
            week_data.append({'day': day, 'bookings': day_bookings})
        calendar_data.append(week_data)

    return render(request, 'bookings/booking_calendar.html', {'calendar': calendar_data})