from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from src.models.Contact import Contact


@csrf_exempt
def submit_form(request):
    if request.method == "POST":
        data = json.loads(request.body)
        contact = Contact.objects.create(
            name=data["name"], email=data["email"], message=data["message"]
        )
        return JsonResponse({"status": "Form submitted successfully"})
    return JsonResponse({"status": "Failed to submit form"})
