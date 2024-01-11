'''
with open("../server/server", "rb+") as infile:
    data=infile.read().splitlines()

enc.dec("env_secure.json", data[0], data[-1])

'''