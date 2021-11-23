from django.urls import path
from .import views


urlpatterns = [
    path("", views.contact, name="ContactUs"),
    path("thanks", views.thanks, name="Thanks"),
]