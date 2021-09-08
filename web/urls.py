from django.urls import path
from web.views import about, contact, detailll, index

urlpatterns = [
    path("", index, name="index"),
    path("detailll/<int:id>", detailll, name="detailll"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]
