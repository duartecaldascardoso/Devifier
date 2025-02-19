from django.db import models
from src.models.PuzzleType import PuzzleType


class Puzzle(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", null=True)
    eloRating = models.IntegerField(default=1000)
    answer = models.CharField(max_length=50)
    hint = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    puzzleType = models.TextField()

    def __str__(self):
        return self.name
