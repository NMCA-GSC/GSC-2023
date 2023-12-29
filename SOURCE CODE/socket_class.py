#############################################################################
"""
 Copyright 2023 McFarland, Neil; Syfrett, Malachi

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
#############################################################################

import socket, platform, hashlib
import rsa_enc_class

class Send:
    def __init__(self):
        self.port=8597
        self.rsa=rsa_enc_class.Rsa_Enc()
    
    def TryEncode(self, data):
        try:
            return data.encode("utf-8")
        except:
            return data

    def BaseReceive(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((platform.uname()[1], self.port))
            s.listen(10)

            conn, (addr, port) = s.accept()
            while True:
                data=conn.recv(2048)
                if data:
                    pass

                return addr, port, data

    def BaseSend(self, hostname, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((hostname, self.port))
            s.sendall(data)

    def CheckRecv(self, host, data1, data2):
        if self.QHash(data1)==data2:
            self.BaseSend(host, "1")
        else: self.BaseSend(host, "0")

    def ISSend(self, hostname, data):
        self.BaseSend(hostname, data)
        self.BaseSend(hostname, self.QHash(data))
        addr, port, verify=self.BaseReceive()
        if verify=="1":
            pass
        else: self.ISSend(hostname, data)

    def SSend(self, hostname, data, pubkey):
        self.BaseSend(hostname, self.rsa.enc(data, pubkey))
        self.BaseSend(hostname, self.QHash(self.rsa.enc(data, pubkey)))
        addr, port, verify=self.BaseReceive()
        if verify=="1":
            pass
        else: self.SSend(hostname, data, pubkey)

class Receive:
    def __init__(self):
        self.port=8597
        self.rsa=rsa_enc_class.Rsa_Enc()
        self.send=Send()
        self.hostname=platform.uname()[1]

    #build socket and return the port (unused), addr, and data
    def BaseReceive(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.hostname, self.port))
            s.listen(10)

            conn, (addr, port) = s.accept()
            while True:
                data=conn.recv(2048)
                if data:
                    pass

                return addr, port, data

    def ISReceive(self):
        addr, port, data1= self.BaseReceive()
        addr, port, data2= self.BaseReceive()
        self.send.CheckRecv(addr, data1, data2)
        return addr, data1

    def SReceive(self, privkey):
        addr, port, data1= self.BaseReceive()
        addr, port, data2= self.BaseReceive()

        data1=self.rsa.dec(data1, privkey)
        data2=self.rsa.dec(data2, privkey)

        self.send.CheckRecv(addr, data1, data2)
        return data1