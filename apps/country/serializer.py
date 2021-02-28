from rest_framework import serializers
from .models import CountryInfo


class CountryModelSerializer(serializers.ModelSerializer):
    alphacode2 = serializers.SerializerMethodField(source='alpha2Code')
    alphacode3 = serializers.SerializerMethodField(source='alpha3Code')
    neighbouring_countries = serializers.SerializerMethodField(source='borders')
    flag_url = serializers.SerializerMethodField(source='flag')

    class Meta:
        model = CountryInfo
        fields = (
            'name',
            'alphacode2',
            'alphacode3',
            'capital',
            'population',
            'timezones',
            'flag_url',
            'languages',
            'neighbouring_countries',
        )

    def create(self, validated_data):
        return CountryInfo.objects.create(**validated_data)


class CountrySavelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, allow_blank=False, allow_null=False)
    alphacode2 = serializers.CharField(max_length=3, allow_blank=True, allow_null=True,source='alpha2Code')
    alphacode3 = serializers.CharField(max_length=2, allow_blank=True, allow_null=True,source='alpha3Code')
    capital = serializers.CharField(max_length=25, allow_null=True, allow_blank=True)
    population = serializers.IntegerField(allow_null=True)
    timezones = serializers.JSONField(allow_null=True)
    flag_url = serializers.URLField(allow_null=True,source='flag')
    languages = serializers.JSONField(allow_null=True)
    neighbouring_countries = serializers.JSONField(allow_null=True,source='borders')

    def create(self, validated_data):
        return CountryInfo.objects.create(**validated_data)
