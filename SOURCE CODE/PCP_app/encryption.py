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

import rsa.randnum as r, binascii
from Crypto.Cipher import AES, Blowfish, Salsa20
from Crypto import Random

#Generate the random passkey and nonce, and set the blocksize to 32 bytes (256 bits)
class Enc:
    def __init__(self):
        self.passkey=r.read_random_bits(256)
        self.nonce=r.read_random_bits(64)
        self.block_size=32

#Define Aes encryption initilization vectors
class Aes_enc:
    def pad(self,s,block_size):
        return s + b"\0" * (block_size - len(s) % block_size)

    def encrypt(self,message, key, block_size=32):
        message = self.pad(message, block_size)
        iv = Random.new().read(block_size)
        cipher = AES.new(key, AES.MODE_ECB)
        return iv + cipher.encrypt(message)

    def decrypt(self,ciphertext, key, block_size=32):
        iv = ciphertext[:block_size]
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = cipher.decrypt(ciphertext[block_size:])
        return plaintext.rstrip(b"\0")

    def enc_file(self, filename, passkey):
        with open(filename, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, passkey)
        enc_hex=binascii.hexlify(enc)
        with open(filename, 'wb') as fo:
            fo.write(enc_hex)

    def dec_file(self, filename, passkey):
        with open(filename, 'rb') as fo:
            ciphertext_hex = fo.read()
        ciphertext=binascii.unhexlify(ciphertext_hex)
        dec = self.decrypt(ciphertext, passkey)
        with open(filename, 'wb') as fo:
            fo.write(dec)

#Define Blowfish encryption using initilization vectors
class Bfs_enc():
    def pad(self,s, block_size):
        return s + b"\0" * (block_size - len(s) % block_size)

    def encrypt(self,message, key, block_size=32):
        message = self.pad(message, block_size)
        iv = Random.new().read(block_size)
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)
        return iv + cipher.encrypt(message)

    def decrypt(self,ciphertext, key, block_size=32):
        iv = ciphertext[:block_size]
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)
        plaintext = cipher.decrypt(ciphertext[block_size:])
        return plaintext.rstrip(b"\0")

    def enc_file(self, filename, passkey):
        with open(filename, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, passkey)
        with open(filename, 'wb') as fo:
            fo.write(enc)

    def dec_file(self, filename, passkey):
        with open(filename, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, passkey)
        with open(filename, 'wb') as fo:
            fo.write(dec)

#Define Salsa20 encryption using nonce
class Sla_enc():
    def encrypt(self, key, nonce, message):
        Salsa20.block_size=32
        cipher = Salsa20.new(key=key, nonce=nonce)
        ciphertext = cipher.encrypt(message)
        return ciphertext

    def decrypt(self, key, nonce, ciphertext):
        Salsa20.block_size=32
        cipher = Salsa20.new(key=key, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext

    def enc_file(self, filename, passkey, nonce):
        with open(filename, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(passkey, nonce, plaintext)
        with open(filename, 'wb') as fo:
            fo.write(enc)

    def dec_file(self, filename, passkey, nonce):
        with open(filename, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(passkey,nonce, ciphertext)
        with open(filename, 'wb') as fo:
            fo.write(dec)

#Encrypt file in one go
class File_Enc(Enc):
    def __init__(self):
        super().__init__()

        self.sla=Sla_enc()
        self.bfs=Bfs_enc()
        self.aes=Aes_enc()

    def enc(self, filename, passkey, nonce):
        self.sla.enc_file(filename,passkey, nonce)
        self.bfs.enc_file(filename, passkey)
        self.aes.enc_file(filename, passkey)

    def dec(self, filename, passkey, nonce):
        self.aes.dec_file(filename, passkey)
        self.bfs.dec_file(filename, passkey)
        self.sla.dec_file(filename, passkey, nonce)

    def return_keys(self):
        return self.passkey, self.nonce