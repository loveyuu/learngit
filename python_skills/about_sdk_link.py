# encoding=utf-8
import base64
from urllib import urlencode, unquote

import rsa

data = {'name': 'iPhone6s', 'version': 1.4, 'area': '上海'}
url_data = urlencode(data)
print url_data

ud = unquote(url_data)
print ud

be = base64.b64encode(ud)
print be

bd = base64.b64decode(be)
print bd

"""
RSA加密明文最大长度117字节，解密要求密文最大长度为128字节，所以在加密和解密的过程中需要分块进行。
RSA加密对明文的长度是有限制的，如果加密数据过大会抛出异常
"""
# 先生成一对密钥, 然后保存.pem格式文件, 当然也可以直接使用
# pub_key, pri_key = rsa.newkeys(1024)
#
# pub, pri = pub_key.save_pkcs1(), pri_key.save_pkcs1()
#
# pub_file, pri_file = open('public.pem', 'w+'), open('private.pem', 'w+')
#
# pub_file.write(pub)
# pri_file.write(pri)
# pub_file.close()
# pri_file.close()

# load公钥和密钥
with open('PUBLIC.pem') as public:
    p = public.read()
    pub_key = rsa.PublicKey.load_pkcs1(p)

with open('PRIVATE.pem') as private:
    p = private.read()
    pri_key = rsa.PrivateKey.load_pkcs1(p)

message = 'you are apple in my eye'
print message
# 用公钥加密、再用私钥解密
crypto = rsa.encrypt(message, pub_key)
print crypto
print rsa.decrypt(crypto, pri_key)


def sub_decryption(_data):
    start, step, length = 0, 128, len(_data)
    while length > start:
        yield rsa.decrypt(_data[start:start+step], pri_key)
        start += step

for i in sub_decryption(2*crypto):
    print "decryption", i

# sign 用私钥签名认证、再用公钥验证签名
signature = rsa.sign(message, pri_key, 'SHA-1')
print signature
print rsa.verify('you are apple in my eye', signature, pub_key)
#待续...
