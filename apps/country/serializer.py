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
