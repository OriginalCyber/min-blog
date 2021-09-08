from django.urls import path
from web.views import about, contact, detaill, index

urlpatterns = [
    path("", index, name="index"),
    path("detaill/<int:id>", detaill, name="detaill"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]
