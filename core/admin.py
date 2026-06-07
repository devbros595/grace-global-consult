from django.contrib import admin
from .models import NewsletterSubscriber, Booking, ContactMessage


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "subscribed_at",
    )

    search_fields = (
        "email",
    )

    ordering = (
        "-subscribed_at",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # Columns displayed in the admin list view
    list_display = ('name', 'email', 'subject', 'created_at')
    
    # Clickable links to view details
    list_display_links = ('name', 'subject')
    
    # Filter options on the right sidebar
    list_filter = ('created_at',)
    
    # Search bar parameters
    search_fields = ('name', 'email', 'subject', 'message')
    
    # Makes fields read-only so messages can't be accidentally edited
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')




@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('guests', 'check_in', 'check_out', 'created_at')
    list_filter = ('check_in', 'check_out', 'created_at')
    search_fields = ('guests',)
    ordering = ('-created_at',)