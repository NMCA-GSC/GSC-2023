import serial, time
import encryption, random

def bt_write(port, data):
    s = serial.Serial(port, 9600,timeout=10)
    print("connected!")
    time.sleep(10)
    s.write(data+b'\4')
    print("Sent Message!")

enc=encryption.File_Enc()
passkey=random.randbytes(32)
nonce=random.randbytes(8)
'''
with open("../server/server", "rb+") as infile:
    data=infile.read().splitlines()

enc.dec("env_secure.json", data[0], data[-1])

'''
enc.enc("env_secure.json", passkey, nonce)
with open("env_secure.json", "rb+") as infile:
    try:
        bt_write('COM5', infile.read())
    except: pass

#send data to server. File used for simplicity.
with open("../server/server", "wb+") as outfile:
    outfile.write(passkey+b'\n\n'+nonce)