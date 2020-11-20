# -*- coding: utf-8 -*-
import pandas as pd
from geopy.geocoders import Nominatim
import requests
from bs4 import BeautifulSoup
import time

def coordinate(address):
    payload = {'q': address}
    html = requests.get(URL, params=payload)
    soup = BeautifulSoup(html.content, "html.parser")
    if soup.find('error'):
        # raise ValueError(f"Invalid address submitted. {address}")
        latitude = None
        longitude = None        
    else:
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
cvs_mst = pd.read_csv('00001_m_store.csv', header=0, encoding='cp932')

for i, r in cvs_mst.iterrows():
    if r.GEO_LOCATION_LAT != r.GEO_LOCATION_LAT or r.GEO_LOCATION_LNG != r.GEO_LOCATION_LNG:
        latlng = coordinate('セブンイレブン' + r.STORE_NAME_KANJI)
        cvs_mst.at[cvs_mst.index[i], 'GEO_LOCATION_LAT'] = latlng[0]
        cvs_mst.at[cvs_mst.index[i], 'GEO_LOCATION_LNG'] = latlng[1]
        time.sleep(10)
pd.to_csv('00001_m_stores.csv')


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

