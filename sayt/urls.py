from django.urls import path

from sayt.views import *

urlpatterns = [
    path("", index, name="home"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("service/", service, name="service"),
    path("booking/", booking, name="booking"),
    path("team/", team, name="team"),
    path("testimonial/", testimonial, name="testimonial"),
]