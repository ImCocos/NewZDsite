import json
import requests

while True:
    cmd = input('CMD: ')
    st_num = int(input('ST_NUM: '))
    data = {
        'key': 'zsrgdragae5hrbzdhnsrtWQA354',
        'data': cmd,
    }

    data = json.dumps(data)

    response = requests.post(url=f'http://127.0.0.1:8000/data-getter/{st_num}', data=data)
