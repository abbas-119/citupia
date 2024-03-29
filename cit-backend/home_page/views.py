import json
import os
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserProfileSerializer
from .models import UserProfile
# from datetime import datetime

from django.conf import settings
from django.http import JsonResponse, FileResponse
from home_page.models import UserProfile
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id})

class UserProfileView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

# class GeoJSONDataView(APIView):
#     def get(self, request):
#         geojson_data = GeoJSONData.objects.all()
#         serializer = GeoJSONDataSerializer(geojson_data, many=True)
#         return Response(serializer.data)



# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def user_profiles(request):
#     user = request.user
#     user_profile = UserProfile.objects.get(user=user)
#     context = {
#         'username': user.username,
#         'full_name': user_profile.get_full_name(),
#     }
#     return JsonResponse(context, safe=False)
#
# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def userInfo(request):
#     if request.method == 'GET':
#         post_data = json.loads(request.body)
#         userName = post_data['username']
#         first_name = post_data['first_name']
#         last_name = post_data['last_name']
#         user = User.objects.get(username=userName)
#         profile = UserProfile.objects.create(user=user, first_name=first_name, last_name=last_name)
#         profile.save()
#         return JsonResponse({"success": True})
#
# def serve_gpkg(request):
#     gpkg_file_path = os.path.join(settings.BASE_DIR, 'static', 'gpkg', 'CityBikes_Punkt.gpkg')
#     return FileResponse(open(gpkg_file_path, 'rb'))