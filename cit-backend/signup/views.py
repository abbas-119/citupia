from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from home_page.models import UserProfile
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def addName(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Only POST method is allowed")

    try:
        post_data = json.loads(request.body)
        userName = post_data['username']
        first_name = post_data['first_name']
        last_name = post_data['last_name']
        user_type = post_data['user_type']
        company = post_data['company']
        city = post_data['city']
        position = post_data['position']
        try:
            user = User.objects(username=userName)
            profile = UserProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type,
            company=company,
            city=city,
            position=position
            )
            profile.save()
            return JsonResponse({"success": True})
        except ObjectDoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)



