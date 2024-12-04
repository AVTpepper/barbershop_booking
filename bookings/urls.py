from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('booking-list/', views.booking_list, name='booking_list'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('update/<int:booking_id>/', views.update_appointment, name='update_appointment'),
    path('delete/<int:booking_id>/', views.delete_appointment, name='delete_appointment'),
    path('success/', views.booking_success, name='booking_success'),
    path('calendar/', views.booking_calendar, name='booking_calendar'),
]