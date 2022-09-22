from rest_framework import serializers
from .models import Dealership

class DealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealership
        fields = ['name', 'street_address', 'city', 'state', 'zip']