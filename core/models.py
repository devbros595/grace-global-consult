from django.db import models

# Create your models here.

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class Booking(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guests} guest(s) from {self.check_in} to {self.check_out}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

from django.db import models

class CleaningJobGallery(models.Model):
    title = models.CharField(max_length=150, help_text="e.g., Commercial Office, Kitchen Deep Clean")
    image = models.ImageField(upload_to='static/cleaning_gallery/', help_text="Upload the job photo here")
    alt_text = models.CharField(max_length=200, blank=True, help_text="Description for search engines and screen readers")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cleaning Gallery Image"
        verbose_name_plural = "Cleaning Gallery Images"
        ordering = ['-created_at'] # Shows newest jobs first

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Fallback to title if alt text is left blank
        if not self.alt_text:
            self.alt_text = f"Grace Global Consult - {self.title}"
        super().save(*args, **kwargs)