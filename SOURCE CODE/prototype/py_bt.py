import serial, time

with open("SOURCE CODE/prototype/test.txt", "rb+") as infile:
    data=infile.read()
    infile.close()

print(data)

s = serial.Serial('COM5', 9600,timeout=10)
print("connected!")
time.sleep(10)
s.write(data+b'\n')
print("Sent Message!")