from django.contrib.auth.models import User
from rest_framework import status, views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from home_page.serializers import UserProfileSerializer
from home_page.models import UserProfile

class SignUpView(views.APIView):
    def post(self, request, *args, **kwargs):
        # Create a user
        user_data = {
            'username': request.data.get('username'),
            'password': request.data.get('password'),
            'email': request.data.get('username'),  # Optional: remove if you don't want to collect email
        }
        user = User.objects.create_user(**user_data)
        user.save()

        # Create user profile
        profile_data = {
            'user': user.id,
            'firstName': request.data.get('firstName'),
            'lastName': request.data.get('lastName'),
            'user_type': request.data.get('user_type'),
            # Add other fields as necessary
        }
        serializer = UserProfileSerializer(data=profile_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Delete the created user if profile creation fails
            user.delete()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data)
