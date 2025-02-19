from django.contrib import admin

from src.models.Puzzle import Puzzle
from src.models.User import User

admin.site.register(User)
admin.site.register(Puzzle)
