import hashlib

print(hashlib.algorithms_available)
# prints out available algorithms

hash_obj = hashlib.sha384()
# calling one of hash algorithm
hash_obj.update(b'hello')
# hash a byte string
print(hash_obj.hexdigest())
# hash version of string 'hello' - minor change in string will change the hash


# ### decryption #######################################################################################################
from cryptography.fernet import Fernet
#
# key = Fernet.generate_key()
#
# print('key: {}'.format(key))
# ''' key: b'a-cBzq1hHTT9aDkbp0xHTSFCTlOpJ6pdX6V63dUkjN8='
# with each execution new key will be generated  '''
#
#
# cipher = Fernet(key)
#
#
# print(cipher.encrypt(b'This is text to encrypt'))
# # # b'gAAAAABdpruVLY_MY9P_crb584E1rI168oIwXjph1OHAyiCtUIzZIWQzv_m3kiv3MGXhE533vDHrziNwbQmO5iwB0QTwnNaqd6W4QwN5QP76z_A6sa82lRw='
# #
# # on different computer we will pass generated key to encryption purpose
# other_ciper = Fernet(b'a-cBzq1hHTT9aDkbp0xHTSFCTlOpJ6pdX6V63dUkjN8=')
# #
# other_ciper.decrypt(b'gAAAAABdpruVLY_MY9P_crb584E1rI168oIwXjph1OHAyiCtUIzZIWQzv_m3kiv3MGXhE533vDHrziNwbQmO5iwB0QTwnNaqd6W4QwN5QP76z_A6sa82lRw=')

# ### decryption #######################################################################################################

keyword = b'123'
key = hashlib.sha3_256(keyword)

import base64

key_bytes = key.digest()

fernet_key = base64.urlsafe_b64encode(key_bytes)

custom_cipher = Fernet(fernet_key)

custom_cipher.encrypt(b'hello')
