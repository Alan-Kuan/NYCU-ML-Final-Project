#! /usr/bin/env python3

import requests
import json
from time import sleep

api_url = 'https://api.nasa.gov/neo/rest/v1/neo/browse'
api_key = '<API KEY>'

for page in range(0, 600):
    query = {
        'page': page,
        'size': 20,
        'api_key': api_key
    }
    try:
        res = requests.get(api_url, params=query)
        res.raise_for_status()
        data = res.json()['near_earth_objects']
        with open(f'data/page{ page }.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            print(f'Saved page{ page }.json')

    except requests.exceptions.HTTPError as err:
        print(err)
        break

    sleep(1)
