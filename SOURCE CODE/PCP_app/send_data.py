import encryption, random, serial, time

def split_string_nth(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]

passkey = random.randbytes(32).replace(b'\n', b'\0')
nonce = random.randbytes(8).replace(b'\n', b'\0')

enc = encryption.File_Enc()
enc.enc("env_secure.json", passkey, nonce)

s = serial.Serial('COM5', 9600, timeout=10)
with open("env_secure.json", "rb+") as infile:
    for line in infile:
        sections = split_string_nth(line, 7)
        for section in sections:
            s.write(section+b'\n')
            time.sleep(0.1)

# Send data to the server. File used for simplicity.
with open("../server/server", "wb+") as outfile:
    outfile.write(passkey + b'\n\n' + nonce)
