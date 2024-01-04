import serial

import time, json

with open("env_secure.json", 'r+') as infile:
    data=json.dumps(json.load(infile))


serialcomm = serial.Serial('COM3', 9600)

serialcomm.timeout = 1

serialcomm.write(data.encode())

time.sleep(5)

serialcomm.readline().decode()

serialcomm.write(data.encode())

time.sleep(5)

print(serialcomm.readline().decode())

serialcomm.close()

