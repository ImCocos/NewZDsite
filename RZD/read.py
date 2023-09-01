import serial
import json
import requests
import time

while True:
  try:
    ser = serial.Serial('COM4', 9600, timeout=0)
    break
  except Exception as ex:
    print(ex)
    pass
print('connected')
def read():
  
  while 1:
    st = ser.readline()
    if st != b'':
      st = st.decode('utf-8').replace('\n', '').replace('\r', '')
      print(st)

      data_dict = {
        'key': 'zsrgdragae5hrbzdhnsrtWQA354',
        'data': st,
      }

      data_json = json.dumps(data_dict)


      requests.post(url='http://127.0.0.1:8000/data-getter/1', data=data_json)
  ser.close()
read()

def read_fast():
  while 1:
    st = ser.readline()
    print(st)
read_fast
# CD RZD; python manage.py runserver