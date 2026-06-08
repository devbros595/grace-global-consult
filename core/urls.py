from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="index"),
    path("about-us/", views.about_us_view, name="about"),
    path("our-services/hostels/", views.hostels_view, name="hostels"),
    path("our-services/property-management/", views.property_services_view, name="property_services"),
    path("our-services/cleaning-services/", views.cleaning_services_view, name="cleaning_services"),
    path("our-services/admin-services/", views.admin_services_view, name="admin_services"),
    path("contact-us/", views.contact_us_view, name="contact_us"),
    path("booking-now/", views.booking_view, name="book_now"),
    path(
        "newsletter/subscribe/", views.subscribe_newsletter, name="subscribe_newsletter"
    ),
    path("booking/create/", views.create_booking, name="create_booking"),
]
