from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import NewsletterSubscriber
from django.contrib import messages
import json
from .models import Booking, ContactMessage
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage

# from .models import Consult
from django.contrib import messages

# Create your views here.


def home_view(request):
    return render(request, "index.html")


def about_us_view(request):
    return render(request, "about_us.html")


# def contact_us_view(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         company = request.POST.get("company")
#         email = request.POST.get("work-email")
#         phone_number = request.POST.get("phone-number")
#         message = request.POST.get("message")

#         try:
#             Consult.objects.create(
#                 name=name,
#                 company=company,
#                 email=email,
#                 phone_number=phone_number,
#                 message=message,
#             )

#             messages.success(
#                 request,
#                 "Your message was successfully sent, sit back our response is on it's way to you!",
#             )
#             next_url = request.POST.get("next", "/")

#             return redirect(next_url)

#         except Exception as e:
#             messages.error(request, f"An error occurred: {e}")
#             return redirect("index")

#     return render(request, "contact_us.html")


def property_services_view(request):
    return render(request, "property_services.html")


def cleaning_services_view(request):
    return render(request, "cleaning_service.html")


def admin_services_view(request):
    return render(request, "admin_services.html")


def hostels_view(request):
    return render(request, "hostels.html")


def booking_view(request):
    return render(request, "booking.html")


from django.shortcuts import render
from django.http import JsonResponse
from .models import ContactMessage


def contact_us_view(request):
    if request.method == "GET":
        return render(request, "contact_us.html")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not name or not email or not subject or not message:
            return JsonResponse(
                {"status": "error", "message": "All fields are required."}, status=400
            )

        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )

        return JsonResponse(
            {"status": "success", "message": "Message sent successfully."}
        )


@require_POST
def subscribe_newsletter(request):
    try:
        data = json.loads(request.body)

        email = data.get("email", "").strip().lower()

        if not email:
            return JsonResponse({"success": False, "message": "Email is required."})

        # Validate email here
        try:
            validate_email(email)

        except ValidationError:
            return JsonResponse(
                {"success": False, "message": "Please enter a valid email address."}
            )

        subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)

        if not created:
            return JsonResponse(
                {"success": False, "message": "You are already subscribed."}
            )

        return JsonResponse(
            {"success": True, "message": "Successfully subscribed to our newsletter."}
        )

    except Exception:
        return JsonResponse({"success": False, "message": "Something went wrong."})


@require_POST
def create_booking(request):
    try:
        data = json.loads(request.body)

        check_in = data.get("check_in")
        check_out = data.get("check_out")
        guests = data.get("guests")

        # basic validation
        if not check_in or not check_out or not guests:
            return JsonResponse(
                {"success": False, "message": "All fields are required."}
            )

        # create booking
        booking = Booking.objects.create(
            check_in=check_in, check_out=check_out, guests=int(guests)
        )

        return JsonResponse(
            {
                "success": True,
                "message": "Booking successful! We will contact you shortly.",
                "booking_id": booking.id,
            }
        )

    except Exception:
        return JsonResponse(
            {"success": False, "message": "Something went wrong. Please try again."}
        )

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not name or not email or not subject or not message:
            return JsonResponse(
                {"status": "error", "message": "All fields are required."}, status=400
            )

        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )

        return JsonResponse(
            {"status": "success", "message": "Message sent successfully."}
        )

    return JsonResponse(
        {"status": "error", "message": "Invalid request method."}, status=405
    )
