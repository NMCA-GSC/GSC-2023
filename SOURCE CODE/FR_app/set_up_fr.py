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

import rsa

def get_key():
    pub_key, priv_key=rsa.newkeys(512)
    with open("pubkey.pem", 'wb') as file:
        file.write(pub_key.save_pkcs1('PEM'))
    with open("privkey.pem", 'wb') as file:
        file.write(priv_key.save_pkcs1('PEM'))