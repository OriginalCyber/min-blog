from django.urls import path
from web.views import about, contact, detall, index

urlpatterns = [
    path('', index, name='index'),
    path('detall/<int:id>', detall, name='detall'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]