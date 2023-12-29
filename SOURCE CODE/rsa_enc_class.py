import rsa, rsa.randnum

#rsa class for data stream encryption
class Rsa_Enc:
    #make the public and private keys
    def makeKeys(self):
        pubkey, privkey=rsa.newkeys(2048)
        return pubkey, privkey

    #save keys (unused currently)
    def saveKeys(self, pubkey, privkey):
        with open("pubkey.pem", 'wb') as file:
            file.write(pubkey.save_pkcs1('PEM'))
        with open("privkey.pem", 'wb') as file:
            file.write(privkey.save_pkcs1('PEM'))

    #load keys (unused currently)
    def loadKeys(self, pubkey, privkey):
        with open("pubkey.pem", 'rb') as file:
            pubkey = rsa.PublicKey.load_pkcs1(file.read())
        with open("privkey.pem", 'rb') as file:
            privkey = rsa.PrivateKey.load_pkcs1(file.read())
        return pubkey, privkey

    #encrypt any data
    def enc(self, data, pubkey):
        enc=rsa.encrypt(data, pubkey)
        return enc
    
    #decrypt any data
    def dec(self, data, privkey):
        dec=rsa.decrypt(data,privkey)
        return dec