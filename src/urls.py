from django.urls import path

from src.views.create_puzzle_view import create_puzzle

urlpatterns = [
    path("create_puzzle", create_puzzle, name="create_puzzle"),
]
