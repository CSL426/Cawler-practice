import json

import requests

url = "https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6577139"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

json_string = res.text
json_data = json.loads(json_string)  # returns a list or dict
# print(type(json_data))
