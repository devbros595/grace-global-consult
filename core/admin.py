from django.contrib import admin
from .models import NewsletterSubscriber, Booking, ContactMessage, CleaningJobGallery
from django.utils.html import format_html


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



@admin.register(CleaningJobGallery)
class CleaningJobGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'alt_text')
    readonly_fields = ('preview_image_detail',)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height: 45px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "No Image"
    preview_image.short_description = "Image Preview"

    def preview_image_detail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 300px; border-radius: 8px;" />', obj.image.url)
        return "No Image"
    preview_image_detail.short_description = "Current Image Preview"