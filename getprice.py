#!/bin/env python3

import json
import time
import urllib.request

url = 'https://www.hetzner.com/a_hz_serverboerse/live_data.json?m={}'.format(int(time.time()))
response = urllib.request.urlopen(url)
data=json.loads(response.read())
servers=data["server"]
filtered=[v for v in servers if v['hdd_size'] > 3000 and v['hdd_count'] == 4]
srted=sorted(filtered, key=lambda item: float(item['price']))
price=srted[0]['price']
print(price)
