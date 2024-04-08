import json
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    user_type = models.CharField(max_length=100, blank=True, null=True)
    # company = models.CharField(max_length=150, blank=True, null=True)
    # city = models.CharField(max_length=100, blank=True, null=True)
    # position = models.CharField(max_length=100, blank=True, null=True)

    def get_full_name(self):
        return f'{self.firstName} {self.lastName}'

    def get_short_name(self):
        return self.firstName

# class GeoJSONData(models.Model):
#     name = models.CharField(max_length=255)
#     geojson_file = models.FileField(upload_to='geojson_files/', null=True)  # Set null=True to allow existing rows to have a null value
#
#     def get_geojson_as_json(self):
#         if self.geojson_file:
#             # Read and parse the GeoJSON file into a JSON object
#             with open(self.geojson_file.path, 'r') as file:
#                 geojson_data = json.load(file)
#             return geojson_data
#         return None  # Return None if geojson_file is not set
