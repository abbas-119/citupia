from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from home_page.models import UserProfile
import json

@csrf_exempt
def addName(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Only POST method is allowed")

    try:
        post_data = json.loads(request.body)
        userName = post_data['username']
        first_name_custom = post_data['firstname_custom']
        last_name_custom = post_data['lastname_custom']
        user_type = post_data['user_type']
        company = post_data['company']
        city = post_data['city']
        position = post_data['position']

        # Check if the user already exists
        if User.objects.filter(username=userName).exists():
            return JsonResponse({"error": "User already exists"}, status=400)

        # Create the user and user profile
        user = User.objects.create(username=userName)
        # user.set_password("your_password_here")  # Set the user's password (replace with actual password)
        # user.save()

        profile = UserProfile.objects.create(
            user=user,
            first_name=first_name_custom,  # Use the custom field names
            last_name=last_name_custom,    # Use the custom field names
            user_type=user_type,
            company=company,
            city=city,
            position=position
        )
        profile.save()

        return JsonResponse({"success": True})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
