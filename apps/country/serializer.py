from rest_framework import serializers
from .models import CountryInfo


class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryInfo
        fields = (
            'name',
            'alphacode2',
            'capital',
            'population',
            'timezone',
            'flag',
            'languages',
            'neighbouring_countries',
        )