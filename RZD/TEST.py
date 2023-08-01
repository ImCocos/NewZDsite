import json
import requests

data = {
    'key': 'zsrgdragae5hrbzdhnsrtWQA354',
    'input': '0',
    'output': '92',
}

data = json.dumps(data)

response = requests.post(url='http://127.0.0.1:8000/data-getter/4', data=data)
