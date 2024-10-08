from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('calendar/', views.booking_calendar, name='booking_calendar'),
]