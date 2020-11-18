# -*- coding: utf-8 -*-
import pandas as pd
from geopy.geocoders import Nominatim
import requests
from bs4 import BeautifulSoup


def coordinate(address):
    payload = {'q': address}
    html = requests.get(URL, params=payload)
    soup = BeautifulSoup(html.content, "html.parser")
    if soup.find('error'):
        raise ValueError(f"Invalid address submitted. {address}")
    latitude = soup.find('lat').string
    longitude = soup.find('lng').string
    return (latitude, longitude)


def coordinates(addresses, interval=10, progress=True):
    coordinates = []
    for address in progress and tqdm(addresses) or addresses:
        coordinates.append(coordinate(address))
        time.sleep(interval)
    return coordinates


URL = 'http://www.geocoding.jp/api/'    
cvs_addresses = pd.read_csv('tokyo.csv', header=None, encoding='SJIS', names=['name', 'address'])
cvs_addresses['LATLNG']=None
for i, r in cvs_addresses.iterrows():
  cvs_addresses.at[cvs_addresses.index[i], 'LATLNG'] = coordinate(r.address)

'''
geolocator = Nominatim(user_agent='geopy_test')

locator = geolocator.geocode("群馬県前橋市西善町182-2")
print(locator)

from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
df['location'] = df['name'].apply(geocode)

df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)

print(df['location'])
print("")
print(df['point'])
'''

