from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from src.models.Puzzle import Puzzle


@csrf_exempt
def create_puzzle(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Puzzle.objects.create(
            name=data["name"],
            description=data["description"],
            image=data["image"],
            eloRating=data["eloRating"],
            answer=data["answer"],
            hint=data["hint"],
            puzzleType=data["puzzleType"],
        )
        return JsonResponse({"status": "Puzzle created with success!"})
    return JsonResponse({"status": "Failed to create the Puzzle."})
