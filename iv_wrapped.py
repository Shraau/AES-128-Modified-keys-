"""
    Here the AES will be wrapped with a seprate key in which the set's of plain text
    and cipher texts are modified
"""

from main import main_encrypt, main_decrypt
# Perform ctr and file formation with cython functions
#from AES_cpp.aes_cpp import cython_encrypt as main_encrypt, cython_decrypt as main_decrypt

import time

def modified_encrypt(plain_text, key, iv):
    """
        Here IV is 64 bit key
        The modifications are as follows:
            mod_plain_text = plain_text^(IV||IV)
            mod_key        = key^(IV||IV)
    """
    int_iv          = int((iv*2), 16)

    list_plain_text = list(map(''.join, zip(*[iter(plain_text)]*32)))
    mod_int_plain   = map(lambda x: int(x, 16)^int_iv, list_plain_text)
    mod_int_key     = int(key, 16) ^ int_iv

    mod_plain_text  = ''.join(map(lambda x: '{:x}'.format(x).zfill(32), mod_int_plain))
    mod_key_text    = '{:x}'.format(mod_int_key)

    cipher          = main_encrypt(mod_plain_text, mod_key_text)

    return cipher

def modified_decrypt(cipher_text, key, iv):
    """
        Here we invert the above effect
    """
    int_iv          = int((iv*2), 16)
    mod_key         = int(key, 16) ^ int_iv
    mod_key_text    = '{:x}'.format(mod_key)

    mod_plain_text  = main_decrypt(cipher_text, mod_key_text)
    
    list_mod_plain  = list(map(''.join, zip(*[iter(mod_plain_text)]*32))) 
    list_int_plain  = map(lambda x: int(x,16)^int_iv, list_mod_plain)
    plain_text      = ''.join(map(lambda x: '{:x}'.format(x).zfill(32), list_int_plain))

    return plain_text

if __name__ == '__main__':
    key         = '4afcdd29d71e9f911f63e273858ff8ec'
    iv          = '0e905298a4114e45'
    plain_text  = '046888375b45b2e59c98c1baaa7a830f'
    cipher_text = 'c448a13bdefb87e0f8349bbc2648ac0f'

    print 'Testing'
    print modified_encrypt(plain_text, key, iv)
    print modified_decrypt(cipher_text, key, iv)
