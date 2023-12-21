from environs import Env
import hashlib, time, zlib, rsa
import encryption, os

global NAME, EMERGENCY_CONTACT, SOCIAL_SECURITY, DOB

public=Env()
public.read_env("public.env")

NAME = public("NAME")
EMERGENCY_CONTACT=public("EMERGENCY_CONTACT")

def remove_secure():
    PASS_HASH = public("HASH")
    enc=encryption.Aes_enc()
    enc.dec_file("secure.env", PASS_HASH.encode())
    os.remove("secure.env.aes")

def resecure():
    PASS_HASH = public("HASH")
    enc=encryption.Aes_enc()
    enc.enc_file("secure.env", PASS_HASH.encode())
    os.remove("secure.env")


#remove_secure()

secure=Env()
secure.read_env("secure.env")

SOCIAL_SECURITY = secure("SS")
DOB = secure("DOB")

resecure()


print(SOCIAL_SECURITY)
print(DOB)