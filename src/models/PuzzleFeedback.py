from django.db import models

from src.models.Puzzle import Puzzle


class PuzzleFeedback(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    feedback_type = models.CharField(max_length=50)
    feedback_text = models.TextField()
    feedback_value = models.IntegerField()

    def __str__(self):
        return self.feedback_text
