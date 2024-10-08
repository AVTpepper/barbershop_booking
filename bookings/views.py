from django.shortcuts import render
from .models import Booking
import calendar
from datetime import date, timedelta

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