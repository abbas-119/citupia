import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from home_page.models import UserProfile


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def delete_account(request):
    if request.method == 'DELETE':
        # load the json data

        user = request.user

        user.delete()
        return JsonResponse({'message': 'Account deleted successfully'}, status=200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def change_username(request):
        if request.method == 'POST':
            user = UserProfile.objects.get(user=request.user)
            post_data = json.loads(request.body)
            first_name = post_data['first_name']
            last_name = post_data['last_name']
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return JsonResponse({'first_name': first_name, 'last_name': last_name})

