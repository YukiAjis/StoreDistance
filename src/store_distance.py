from geopy.distance import geodesic
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="user", timeout=10)
location = geolocator.geocode(u'')
store = (location.latitude, location.longitude)
myhome = (36.3516337, 139.108283)
myroom = (35.7080334, 139.9598361)

dis = geodesic(myhome, store)

print(dis)
