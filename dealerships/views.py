from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import DealershipSerializer
from .models import Dealership
from cars.serializers import CarSerializer

from dealerships import serializers

@api_view(['GET', 'POST'])
def dealership_detail(request):
    if request.method == 'GET':
        dealerships = Dealership.objects.all()
        serializer = DealershipSerializer(dealerships, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DealershipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def dealership_detail_by_id(request, pk):
    dealership = get_object_or_404(Dealership, pk = pk)
    if request.method == 'GET':
        serializer = DealershipSerializer(dealership)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DealershipSerializer(dealership, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        dealership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def dealership_get_associated_cars(request, pk):
    dealership = get_object_or_404(Dealership, pk = pk)
    associated_cars = dealership.car_set.all()
    serializer = CarSerializer(associated_cars, many=True)
    return Response(serializer.data)