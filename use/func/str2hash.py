import hashlib

hash=hashlib.sha256()
hash.update('1413525')
'''
In [19]: hash
Out[19]: <sha256 HASH object @ 0x7fe951503530>
'''
a=hash.hexdigest()
'''
In [21]: a
Out[21]: 'fde7c693c03806fbb75c06d50e5afbd1dd58f7f0323ffab9d140dd059f08deb0'
'''
b = hash.digest()
'''
In [23]: b
Out[23]: '\xfd\xe7\xc6\x93\xc08\x06\xfb\xb7\\\x06\xd5\x0eZ\xfb\xd1\xddX\xf7\xf02?\xfa\xb9\xd1@\xdd\x05\x9f\x08\xde\xb0'
'''
print a


a = '1413525'
b = hashlib.sha256(a).hexdigest()
print b
'''
b=fde7c693c03806fbb75c06d50e5afbd1dd58f7f0323ffab9d140dd059f08deb0
'''