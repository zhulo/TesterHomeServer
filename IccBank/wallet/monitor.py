import base64
import hashlib
import json

from Crypto.Cipher import AES
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

from common.utils.logger import Logger

log = Logger(__name__).log()


def str_to_md5(value: str):
    m = hashlib.md5()
    b = value.encode(encoding='utf-8')
    m.update(b)
    return m.hexdigest()


'''钱包测试相关加解密'''


class WalletService(object):

    def signature(self, sign_data, private_key):
        '''
        返回签名
        :param sign_data: 需要签名的数据
        :param private_key: 私钥
        :return:
        '''
        if isinstance(sign_data, dict):
            if "sign" in sign_data.keys(): del sign_data['sign']
            log.debug("准备签名数据: {}".format(sign_data))
            data = json.dumps(sign_data, sort_keys=True)
            data = data.replace(' ', '')
            log.debug("签名前数据:\n{}".format(data))
            private_key = serialization.load_pem_private_key(
                private_key,
                password=None,
                backend=default_backend()
            )
            signature = private_key.sign(data.encode('utf8'), padding.PKCS1v15(), hashes.SHA1())
            signature_base64 = base64.b64encode(signature)
            log.debug("完成签名数据: {}".format(signature_base64))
            return signature_base64
        else:
            log.error('签名数据格式不支持')
            return False

    def aes_encrypt(self, sign_data, encrypt_token, private_key):
        '''
        对sign进行加密
        :param sign_data:
        :param encrypt_token:
        :param private_key:
        :return:
        '''
        signature_value = self.signature(sign_data, private_key)
        sign_data['sign'] = str(signature_value, encoding="utf-8")
        log.debug('合并签名数据生成请求body: {}, 开始加密.......'.format(sign_data))
        data = json.dumps(sign_data, sort_keys=True)
        data = data.replace(' ', '')
        log.debug("合并sign后的数据:\n{}".format(data))
        padding = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        if isinstance(encrypt_token, str):
            encrypt_token = str.encode(encrypt_token)
        cryptos = AES.new(encrypt_token, AES.MODE_ECB)
        data = padding(data).encode("utf-8")
        cipher_text = cryptos.encrypt(data)
        encrypt_text = base64.b64encode(cipher_text).decode("utf-8")
        log.debug('加密后生成加密请求body: {}'.format(encrypt_text))
        return encrypt_text

    def aes_decrypt(self, data, encrypt_token):
        '''
        请求接口后返回的数据 data 进行解密
        :param data: 加密后请求接口返回的加密str，提取出来解密
        :param encrypt_token:
        :return:
        '''
        log.debug('待解密数据: {}'.format(data))
        if isinstance(data, str):
            data = data.encode('utf8')
        if isinstance(encrypt_token, str):
            encrypt_token = encrypt_token.encode('utf8')
        cryptos = AES.new(encrypt_token, AES.MODE_ECB)
        decrypt_bytes = base64.b64decode(data)
        meg = cryptos.decrypt(decrypt_bytes).decode('utf-8')
        decrypt_msg = meg[:-ord(meg[-1])]
        log.debug('完成解密: {}'.format(decrypt_msg))
        return decrypt_msg
