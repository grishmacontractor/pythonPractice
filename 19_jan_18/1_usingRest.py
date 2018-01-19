import requests
import pprint
url = "http://services.groupkt.com/country/get/all"
get_countries = requests.get(url);

get_countries_json = get_countries.json()

print(type(get_countries_json))
# pprint.pprint(get_countries_json)
data = get_countries_json['RestResponse']['result']
# pprint.pprint(data)

for x in data:
    print("\nCountry Name:{0} and code = {1} ".format(x['name'], x['alpha2_code']))