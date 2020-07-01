import json
import time

from IccBank.wallet.conf import ApiConfig, Account
from common.utils.logger import Logger
from IccBank.wallet.monitor import WalletService
from IccBank.wallet.request import Api

log = Logger(__name__).log()

encrypt_token = Account.encrypt_token
private_key_pem = Account.private_key_pem


class WalletApiRequest(WalletService):

    def request(self, api, params, check_point):
        '''

        :param url:
        :param headers:
        :param params:
        :param check_point:
        :return:
        '''
        encrypted_data = self.aes_encrypt(params, encrypt_token, private_key_pem)

        params = {"algorithm": "AES", "encryptedData": encrypted_data}
        data_all = {'url': ApiConfig.host + api, 'method': 'post', 'param_type': 'json', 'headers': ApiConfig.headers,
                    'params': params}
        resp = Api(**data_all).request()
        if "encryptedData" in resp['json'].keys():
            decrypt_text = self.aes_decrypt(resp['json']['encryptedData'], encrypt_token)
            resp['json']['encryptedData'] = json.loads(decrypt_text)
        # if isinstance(check_point, dict):
        #     pass
        return resp