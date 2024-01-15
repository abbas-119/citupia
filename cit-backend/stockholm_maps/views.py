from django.shortcuts import render
from django.http import JsonResponse
import requests


def get_wms_maps(request):
    wms_url = 'https://geodata.stockholm.se/gi/gwc/service/wms'
    params = {
        'SERVICE': 'WMS',
        'VERSION': '1.1.1',
        'REQUEST': 'GetMap',
    }
    response = requests.get(wms_url, params=params)
    return JsonResponse(response.json())
# Create your views here.
