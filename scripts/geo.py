from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="weventDataViz")

def listCountries(events: list) -> dict:
    countries = {}
    for event in events:
        if event['latitude'] == 0 and event['longitude'] == 0 and event['category'] == 'Online': continue
        country = get_geodata(event['latitude'], event['longitude']).get('country', 'Unknown')
        if country in countries:
            countries[country] += 1
        else:
            countries[country] = 1
    return countries

def get_geodata(latitude: float, longitude: float) -> dict:
    try:
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        if location:
            return location.raw['address']
        else:
            return 'Unknown'
    except Exception as e:
        return 'Error: ' + str(e)