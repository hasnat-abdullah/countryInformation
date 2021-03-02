from rest_framework import serializers
from .models import CountryInfo


class CountryModelSerializer(serializers.ModelSerializer):
    flag = serializers.SerializerMethodField()
    class Meta:
        model = CountryInfo
        fields = (
            'name',
            'alphacode2',
            'capital',
            'population',
            'timezones',
            'flag',
            'languages',
            'neighbouring_countries',
        )

    def get_flag(self, obj):
        if obj.flag and hasattr(obj.flag, 'url'):
            return self.context['request'].build_absolute_uri( obj.flag.url)
        else:
            return None


class NeighbouringCountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryInfo
        fields = (
            'neighbouring_countries',
        )
