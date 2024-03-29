###########################################################
'''
                    NMCA GSC LISCENSE
            Copyright (c) <year> Authors.txt
        See full license in attached license.md

    The code contained below is a covered in full as 
    part of the entity as defined in the license and
    it's stated admendments. No warranty or liability 
    is claimed for the use of this code, which is 
    provided on an AS-IS BASIS. 
'''
###########################################################
import serial, encryption, os

def read_data():
    def get_keys():
        with open("../server/server", "rb+") as infile:
            data=infile.read().splitlines()
            infile.close()
        password=data[0]
        nonce=data[-1]
        return password, nonce

    ser = serial.Serial('COM5', 9600)
    print("connected")
    ser.write(b"S")
    data = ser.read_until().removesuffix(b'\n')
    print("writing...")
    if data:
        print(data)

    with open("env_secure.enc", "wb+") as outfile:
        outfile.write(data)
        outfile.close()

    password, nonce = get_keys()

    enc=encryption.File_Enc()
    enc.dec("env_secure.enc", password, nonce)
    os.rename("env_secure.enc", "env_secure.json")

if __name__ == "__main__":
    read_data()