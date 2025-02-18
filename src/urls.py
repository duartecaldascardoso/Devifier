from django.urls import path

from src.views.ContactView import submit_form

urlpatterns = [
    path("submit_form", submit_form, name="submit_form"),
]
