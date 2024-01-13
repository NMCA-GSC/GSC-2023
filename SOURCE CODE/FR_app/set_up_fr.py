import rsa

def get_key():
    pub_key, priv_key=rsa.newkeys(512)
    with open("pubkey.pem", 'wb') as file:
        file.write(pub_key.save_pkcs1('PEM'))
    with open("privkey.pem", 'wb') as file:
        file.write(priv_key.save_pkcs1('PEM'))