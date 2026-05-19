from django.shortcuts import render, redirect

# from .models import Consult
from django.contrib import messages

# Create your views here.


def home_view(request):
    return render(request, "index.html")


def about_us_view(request):
    return render(request, "about_us.html")


def contact_us_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        company = request.POST.get("company")
        email = request.POST.get("work-email")
        phone_number = request.POST.get("phone-number")
        message = request.POST.get("message")

        try:
            Consult.objects.create(
                name=name,
                company=company,
                email=email,
                phone_number=phone_number,
                message=message,
            )

            messages.success(
                request,
                "Your message was successfully sent, sit back our response is on it's way to you!",
            )
            next_url = request.POST.get("next", "/")

            return redirect(next_url)

        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect("index")

    return render(request, "contact_us.html")


def property_services_view(request):
    return render(request, "property_services.html")


def hostels_view(request):
    return render(request, "hostels.html")


def booking_view(request):
    return render(request, "booking.html")
