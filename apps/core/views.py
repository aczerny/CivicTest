from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings

from rest_framework import viewsets, status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.authtoken.models import Token
from rest_framework import parsers, renderers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.exceptions import APIException

from .models import Address
from .serializers import AddressSerializer

import requests


class AddressViewSet(viewsets.ModelViewSet):
    """
        API para listar todas las address:
            URL: /core/api/address/

        API para listar address por id:
            URL: /core/api/address/<id>/
    """
    api_key = settings.API_KEY
    url = settings.API_URL
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def getLocation(self, address):
        url = self.url.format('geocode')
        param = 'address={0}&{1}'.format(address, self.api_key)
        api_response = requests.get(url + param)
        api_response_dict = api_response.json()

        return api_response_dict

    def getElevation(self, locations):
        url = self.url.format('elevation')
        param = '{0}&{1}'.format(locations, self.api_key)
        api_response = requests.get(url + param)
        api_response_dict = api_response.json()

        return api_response_dict

    def create(self, request):
        address = request.data['address'] if request.data['address'] else ''
        response_address = self.getLocation(address)

        response = ''
        status_code = status.HTTP_400_BAD_REQUEST
        if response_address['status'] == 'OK':
            result = response_address['results'][0]
            place_id = result['place_id']
            lat = result['geometry']['location']['lat']
            lng = result['geometry']['location']['lng']
            add = result['formatted_address']
            locations = 'locations={0},{1}'.format(lat,lng)
            response_elevation = self.getElevation(locations)

            if response_elevation['status'] == 'OK':
                result = response_elevation['results'][0]
                lat = result['location']['lat']
                lng = result['location']['lng']
                ele = result['elevation']

                data = {
                    'place_id': place_id,
                    'address': add,
                    'latitude': lat,
                    'longitude': lng,
                    'elevation': ele
                }

                serializer = AddressSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    response = serializer.data
                    status_code = status.HTTP_201_CREATED
                else:
                    response = serializer.errors
            else:
                response = response_elevation
        else:
            response = response_address

        return Response(response, status=status_code)


















