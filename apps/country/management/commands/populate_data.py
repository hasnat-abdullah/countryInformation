import requests
from countryInformation.settings import COUNTRY_MODEL_POPULATE_API_URL
from apps.country.models import CountryInfo
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'populate data to DB'

    def handle(self, *args, **kwargs):
        obj = CountryRecord()
        result = obj.get_country_information()
        populate_data_to_db(result)


def populate_data_to_db(data):
    failed_count = 0
    if data is not None:
        for item in data:
            print(item.get('name',None), end="--------->")
            try:
                obj = CountryInfo(
                    name=item.get('name'),
                    alphacode2=item.get('alpha2Code', None),
                    capital=item.get('capital',None),
                    population=item.get('population',None),
                    timezones=item.get('timezones',None),
                    flag_url=item.get('flag',None),
                    languages=item.get('languages',None),
                    neighbouring_countries=item.get('borders',None)
                )
                obj.save(raise_exception=True)
                print("Success")
            except Exception as ex:
                print("Faild")
                failed_count+=1
        print(f"Successfully inserted data. Success: {len(data)},Failed: {failed_count}")
    else:
        print("SORRY! No data found to insert.")


class CountryRecord:
    def __init__(self, request=None):
        self._country_model_populate_url = COUNTRY_MODEL_POPULATE_API_URL
        self.request = request

    def get_country_information(self):
        try:
            headers = {
                'Content-Type': 'application/json'
            }

            url = self._country_model_populate_url
            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as E:
            return None

