from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name ='index'),
    path('about-us', views.about_us_view , name ='about'),
    path('hostels', views.hostels_view , name ='hostels'),
    path('property-services', views.property_services_view , name ='property_services'),
    path('contact-us', views.contact_us_view , name ='contact_us'),
    path('booking-now', views.booking_view , name ='book_now'),
]