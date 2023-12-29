from environs import Env
import hashlib, time, rsa
import encryption, os

public=Env()
public.read_env("env_hash.env")

#decrypt file holding information
def remove_secure():
    PASS_HASH = public("HASH")
    enc=encryption.Aes_enc()
    enc.dec_file("secure.env", PASS_HASH.encode())
    os.remove("secure.env.aes")

#encrypt file holding information
def resecure():
    PASS_HASH = public("HASH")
    enc=encryption.Aes_enc()
    enc.enc_file("secure.env", PASS_HASH.encode())
    os.remove("secure.env")


#remove_secure()


#resecure()