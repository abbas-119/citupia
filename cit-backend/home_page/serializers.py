from . import models
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '[user, firstName_custom, lastName_custom, user_type, company, city, position]'

class GeoJSONDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GeoJSONData
        fields = '[name, geojson_file]'