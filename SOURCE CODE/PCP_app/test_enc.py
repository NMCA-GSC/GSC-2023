import serial
import time
import base64
import encryption
import random

def split_string_nth(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]

passkey = random.randbytes(32)
nonce = random.randbytes(8)

enc = encryption.File_Enc()
enc.enc("env_secure.json", passkey, nonce)

s = serial.Serial('COM5', 9600, timeout=10)
with open("env_secure.json", "rb+") as infile:
    for line in infile:
        sections = split_string_nth(line, 7)
        for section in sections:
            print(section)
            s.write(section+b'\n')  # Ensure the data is encoded before sending
            time.sleep(0.1)  # Reduce the delay

# Send data to the server. File used for simplicity.
with open("../server/server", "wb+") as outfile:
    outfile.write(passkey + b'\n\n' + nonce)
