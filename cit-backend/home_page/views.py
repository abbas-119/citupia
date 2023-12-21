import json
from datetime import datetime

from django.http import JsonResponse
from home_page.models import UserProfile
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profiles(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    context = {
        'username': user.username,
        'full_name': user_profile.get_full_name(),
    }
    return JsonResponse(context, safe=False)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def userInfo(request):
    if request.method == 'GET':
        post_data = json.loads(request.body)
        userName = post_data['username']
        first_name = post_data['first_name']
        last_name = post_data['last_name']
        user = User.objects.get(username=userName)
        profile = UserProfile.objects.create(user=user, first_name=first_name, last_name=last_name)
        profile.save()
        return JsonResponse({"success": True})
