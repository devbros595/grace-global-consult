from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name ='index'),
    path('about-us', views.about_us_view , name ='about'),
    path('our-services', views.services_view , name ='services'),
    path('contact-us', views.contact_us_view , name ='contact_us'),
    path('faq', views.faq_view , name ='faq'),
]