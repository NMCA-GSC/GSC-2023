import hashlib, time, zlib, rsa

file = open("Hashes.txt", "w+") #uncomment to write all results to a file (1/2)

def genVanity(name: bytes):
    now=time.time().hex().encode()
    result=hex(zlib.crc32(name+now)).removeprefix('0x')
    return result[:4]

def genKey(vanity: str):
    while True:
        pubKey, privKey=rsa.newkeys(64)
        result=hashlib.new('SHA512', str(privKey).encode()).hexdigest()
        file.write(result+"\n") #uncomment to write all results to a file (2/2)
        #print(result) #uncomment to see all hash attempts (1/1)
        if vanity in result:
            return result
        

if __name__=='__main__':
    key=genKey(genVanity(b'Malachi Syfrett'))
    print(key)