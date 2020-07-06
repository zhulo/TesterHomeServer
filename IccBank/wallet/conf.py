# linux
# private_key_pem = b"""
# -----BEGIN RSA PRIVATE KEY-----
# MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAI5BR2omOyPsT9PQSdbzoNRnwGfNjqCsF3Dt9ueI69mDiUFjaT/TwIYJ2VBjkrlSB5j1KdD92nx7Za+F0TmocaxT/rEWNqHsozxPEZMzekk/SjM3tV+Dw6V8pnp0HGcP32bLzTHJiavGHdWVlLewSVI+IhLPnIemRfK9AehNbC6JAgMBAAECgYAbgy6PrhM0EGkj+x28z+OkEOjaapwSIRZrheqBvy52JAVwuwxJBuguREteS9O9ucq0X34V6HLQLoFtIAFmGFjbhJXvhgUovXyiH4pifQhpZdoilJoyFlc8uic4ZK1fZG+0O41VzvkOwGeaaqi0dFJkBzyGJd0ZnEgcf3cyQKa6PQJBAL/1SObxx/IvC9eEe0Jl1anQbM6bg8Cm/hzaUjszyZFc8aDh3nuatr0/RMvfvrHf3gM3TRo/q3xuLEoNblnZDF8CQQC9tvWqzTpjDD30iqYpiH8CnF06h9vfXH7zn0SPo+xJl0R8tOL2DtV/Vtf/gomvr6w5c6QnK05+B9QxE+iyLS4XAkAoK9nE0uZoDWZqBMSSwaL0NbT/i9YHtCrLuPiqgQz2yb+bTolzzo3djucDz2Al81aPz7vn+VkW4iuMl8D3No/7AkEAmb9EqP9Zahvpud0DfHVaOUtvYpfn4MSdPeK9NYurWph0sHwH01GCRIik1DV+UBsWgBjv166JFipSFNQFqSBkUQJAYG760IuctcnGe7lz+qRHpU20pv2gD/+dy2HX8imydgjZWMNAN+DClNTALjUdIH7FJ3uHpcoc3Mu5NRaFH34gUw==
# -----END RSA PRIVATE KEY-----
# """
#
#
# class Account:
#     '''
#     账户信息可以从以下地址注册
#     http://10.10.23.116:41008/v1/script/create_user_api?phone=12366667777
#     账号密码  dssj dssj123456
#     {"code":200,"data":{"appId":"d4f998ab4baa410786286a15a25c25d6","appSecret":"MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAKAMJbl4Wu4/eUmnHA6eW2HKkjj5R9Ik/dTOKJ83UeXJ0ZMbkK4/O/BBP183U9sZukIAEpBT6h2Sey0mt9DbzNQaYy45Q7COENJShn7BKv5DmRm8q1kMDF8lXmw9L0QSZPGIyT//Xizi7e/NE4kCQqU27MhhlpaphdJvKuWtMk3TAgMBAAECgYBwwj4t3tLJumScdKT606z0SAEfLNnh/3fqX1kVW6dSqw8BgtE7QofbLE0Wq2dkHUsxxtVNZCG0tggcdoPZHZK/1bqyL7dIms7IHaPWvLokKAuNNoiQlLgiL+P93YV5n+3k4ZUWlfW6eEpG2X8p9D6DLUCy5gZ4uLF1PHKEqeO06QJBAPgDiG8gSgcxh9qpgTZKjADQvMMgj1+PIisgNqISrgL3VJE0qV9sJVALKVZbNzCu57BZ5jdHMTJSQwrvJDs2nZ0CQQClM3njFGxjAOr7FmlLSgGTfl3chMQWyvzDNWluieMRu1RfQTM/T5l2arvA17FS2j1617MEfANlXqa9SGhDCXYvAkACjubFXqvkzxn7o2v1x2cSSxTnXlqcPbm4gCiQG2k4Fp0Esmpc1Zy86qCOh3pWQjeZlhPN1ionvrl6T2UsRy/xAkB0ZbCbrugvWZY3E7NcuOgjZAX+Og1vgdZWNGv01nKHK9Zmxym0kgEuzkU7ur3WAq8OvqwDnN1Hr0kMVNghY6lBAkAzhMdU+H1xd+YPIl1nUEXDaXcCKK3q8vF/mIDgGUnn/Kqh7u4soRT80LhDa0YtM7hsKHAL3Wf84ieX2XFXhNxz","expireDate":"2020-08-02 20:11:02","encryptToken":"bd42b0d753b745b0b66465a8de2b93cd"},"msg":"HTTP_OK","subCode":"0","subMsg":"success"}
#     '''
#
#     app_id = "2de1498a7cbd4380a669464dbeb6abc9"
#     encrypt_token = "b2f7e45faf0347eea2efd26ba26c086c"
#     private_key_pem = private_key_pem

# # 20200703
# private_key_pem = b"""
# -----BEGIN RSA PRIVATE KEY-----
# MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAMiad16ELlpV2CruPjaTebS1DqaXayXJzMBX7ZhVgx3jCwzqcq6n9gJneCEXUEwLvf1ExEdrTuYZZlAPywd+SVCEaTNZasVbfDqdTM9hVbSe1obbnABJhev4eeSiUiUE5bd6VG9jAiXn8g6RXFLMDhIO0f95P9qZKHUX+ykJM1NfAgMBAAECgYEAu2VA+bR1MMJcy83/pDAkU6GH7CwrVgOsGEqLk/DeKX89hXVGaM5SzHAoEpGa209kzkH9MdKWw/EaWNRID9nzVXE3IsTvuTB0U5nsrU7L5z/+pcWV8EPFtesR3VPHxN7jIdw1x81HMFiE0brjc+LEEsHyrEtleaF37pBEKqhQmZECQQD3W050HBue7sizkcOXuWCOZzXW7sfCL78swACVwERpp12NROTUaTHtMMgHrZLTiQPf14Z0BfHRjfbpmdXQZUXdAkEAz5zvX9CdglKrZjZ8u24n8P+r2zSpC7b6Y4HbZRZx7XocNbQKoc2brP2p7M3shyjL9O7jkrzT72WBN1NWmTmgawJAMuCs+mTtqXsj/Qt2V7bhjWjdQiBLJj377JBxjlvFtpWeQHhzON2KT2dBPZMOKER+b4Q9O5AddSTmLJZfzEWIYQJARHYArXzSY8Y1BPiUuw3BGASHPDqqP9WvzZ5lpXj4SpIIuWDMXLy7SBlBrnfdNliqoPMhkiK4VGoJaSAPH2nUTwJBAPVCxEzflYBXLJLptzVCkls/MIcyvDSfqnWdMRZrRPHtFnSV3vfd/El2+J35cZ/uiOVlXLPqIRSB4RXwCiKHzyU=
# -----END RSA PRIVATE KEY-----
# """
#
#
# class Account:
#     '''
#     账户信息可以从以下地址注册
#     http://10.10.23.116:41008/v1/script/create_user_api?phone=12366666666
#     账号密码  dssj dssj123456
#     {"code":200,"data":{"appId":"d4f998ab4baa410786286a15a25c25d6","appSecret":"MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAKAMJbl4Wu4/eUmnHA6eW2HKkjj5R9Ik/dTOKJ83UeXJ0ZMbkK4/O/BBP183U9sZukIAEpBT6h2Sey0mt9DbzNQaYy45Q7COENJShn7BKv5DmRm8q1kMDF8lXmw9L0QSZPGIyT//Xizi7e/NE4kCQqU27MhhlpaphdJvKuWtMk3TAgMBAAECgYBwwj4t3tLJumScdKT606z0SAEfLNnh/3fqX1kVW6dSqw8BgtE7QofbLE0Wq2dkHUsxxtVNZCG0tggcdoPZHZK/1bqyL7dIms7IHaPWvLokKAuNNoiQlLgiL+P93YV5n+3k4ZUWlfW6eEpG2X8p9D6DLUCy5gZ4uLF1PHKEqeO06QJBAPgDiG8gSgcxh9qpgTZKjADQvMMgj1+PIisgNqISrgL3VJE0qV9sJVALKVZbNzCu57BZ5jdHMTJSQwrvJDs2nZ0CQQClM3njFGxjAOr7FmlLSgGTfl3chMQWyvzDNWluieMRu1RfQTM/T5l2arvA17FS2j1617MEfANlXqa9SGhDCXYvAkACjubFXqvkzxn7o2v1x2cSSxTnXlqcPbm4gCiQG2k4Fp0Esmpc1Zy86qCOh3pWQjeZlhPN1ionvrl6T2UsRy/xAkB0ZbCbrugvWZY3E7NcuOgjZAX+Og1vgdZWNGv01nKHK9Zmxym0kgEuzkU7ur3WAq8OvqwDnN1Hr0kMVNghY6lBAkAzhMdU+H1xd+YPIl1nUEXDaXcCKK3q8vF/mIDgGUnn/Kqh7u4soRT80LhDa0YtM7hsKHAL3Wf84ieX2XFXhNxz","expireDate":"2020-08-02 20:11:02","encryptToken":"bd42b0d753b745b0b66465a8de2b93cd"},"msg":"HTTP_OK","subCode":"0","subMsg":"success"}
#     '''
#
#     app_id = "f43db5f64ae443b093c19a6723ab96b7"
#     encrypt_token = "5188b129cfd94bcbbf2cc7c6ba059291"
#     private_key_pem = private_key_pem


# 朱玲玲
# private_key_pem = b"""
# -----BEGIN RSA PRIVATE KEY-----
# MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAIaXe6J+c1EbvVQkbx5kWY5+e9Nd8hgrndlb5OF/iA3zgIQnpXE5U1DvMaudISWJir86LqPriFl2+0sdpzDazGd/EFabelIl5bbdhlbaTw5f98jVpNTTvYpFfLzPs66FfmGTxStWM7Q7f2xDvGwujyggN1+MTkoLtlgyEwgLz7cfAgMBAAECgYAAuynsxAsUUbZBksEXxSvHXmCF0WjTQMlmuN0RbIPsr3nvPdfkOY9+TQ5UBFJ9xbV/PG2sbkcbVU4gJlUWKtoZY8QU8yz/1XCTrGy/+5CV8aW4STeAc1+FA48CcRKlyqTb1HGGiITjGfNyY/6M+FzqPIsjomkuvn584YoNJCqqAQJBAOQGmA7vlTSC4HMpKEEzrshReOLSqr93xt5IxwILOsz1EBZrTdrTaFL+iegfrC3xvfM2gDS44Vmm9KZQ0E2cPMECQQCXGnzs8B/c9LvOu89zThBS25Le1rfVA1Pi3xsjKrTzCPpC2SmssRvYSfyluNIKw9Ctc8z4EyPk8xL8tMjYOovfAkBYPHT60praBwrzhSmekXFA8sXkf8Cy9pZtzZu0nsPSK8Jd6ofl9YiZFQYoXJkz7ieixaQ2wpPxLTneYcc5QQwBAkBQ9j1XivXXoz358EGgS4SNkN7qDWxkcysAVYCp4BkiW34UUV12DVOZGVOIzDWm1PK77V820LKb2u4ifw9aZExLAkBNAvK+o4hHuPzKy2nqVprBH15FoARv07sZFBraR2eqr/2J4b+CNV/uf8Hw5U5Q392SUyWCUzwlyMPNOQE2f7yN
# -----END RSA PRIVATE KEY-----
# """
#
#
# class Account:
#     '''
#     账户信息可以从以下地址注册
#     http://10.10.23.116:41008/v1/script/create_user_api?phone=12366666667
#     账号密码  dssj dssj123456
#     {"code":200,"data":{"appId":"d4f998ab4baa410786286a15a25c25d6","appSecret":"MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAKAMJbl4Wu4/eUmnHA6eW2HKkjj5R9Ik/dTOKJ83UeXJ0ZMbkK4/O/BBP183U9sZukIAEpBT6h2Sey0mt9DbzNQaYy45Q7COENJShn7BKv5DmRm8q1kMDF8lXmw9L0QSZPGIyT//Xizi7e/NE4kCQqU27MhhlpaphdJvKuWtMk3TAgMBAAECgYBwwj4t3tLJumScdKT606z0SAEfLNnh/3fqX1kVW6dSqw8BgtE7QofbLE0Wq2dkHUsxxtVNZCG0tggcdoPZHZK/1bqyL7dIms7IHaPWvLokKAuNNoiQlLgiL+P93YV5n+3k4ZUWlfW6eEpG2X8p9D6DLUCy5gZ4uLF1PHKEqeO06QJBAPgDiG8gSgcxh9qpgTZKjADQvMMgj1+PIisgNqISrgL3VJE0qV9sJVALKVZbNzCu57BZ5jdHMTJSQwrvJDs2nZ0CQQClM3njFGxjAOr7FmlLSgGTfl3chMQWyvzDNWluieMRu1RfQTM/T5l2arvA17FS2j1617MEfANlXqa9SGhDCXYvAkACjubFXqvkzxn7o2v1x2cSSxTnXlqcPbm4gCiQG2k4Fp0Esmpc1Zy86qCOh3pWQjeZlhPN1ionvrl6T2UsRy/xAkB0ZbCbrugvWZY3E7NcuOgjZAX+Og1vgdZWNGv01nKHK9Zmxym0kgEuzkU7ur3WAq8OvqwDnN1Hr0kMVNghY6lBAkAzhMdU+H1xd+YPIl1nUEXDaXcCKK3q8vF/mIDgGUnn/Kqh7u4soRT80LhDa0YtM7hsKHAL3Wf84ieX2XFXhNxz","expireDate":"2020-08-02 20:11:02","encryptToken":"bd42b0d753b745b0b66465a8de2b93cd"},"msg":"HTTP_OK","subCode":"0","subMsg":"success"}
#     '''
#
#     app_id = "d9bb351282f14cc0a72ba9e3604c8e2e"
#     encrypt_token = "dc8db706ed8343b5be75c9dc41721920"
#     private_key_pem = private_key_pem


# USDT_OMNI
#
# private_key_pem = b"""
# -----BEGIN RSA PRIVATE KEY-----
# MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAI9GLWOUPmz+bZJ6PfFnS+3RsqddV+haPai0Z3cgeGGTMFYkbVgRHDB/U9b0lwAx9uSWSkBKCGVU5n9uRwdS+P5mxquLgqaPPEspvrNjR3LykCjUIzw2qcCSz+3IAtPhU6WiuBnmv6jI0JWde690T3Z9uy4ROR6Pm71SeNEET/pvAgMBAAECgYBnZX3cH1/tyK/Kxe1uCd4CAxOrNPH7/SQCXC9PCV/XCyIXCLLgm3h8h2c5+cn/mg9TaCKtwr/MYTj3Pd6EqpyF55/IrsU5TyOlxrUqSIgxyzlnxqRlVed7XlmWOgFjEdW4noLqwjAPyx6837nT5rABkqOmw9gzJbDb/tqvOweuAQJBAMSyeyip4gQUSo8MdBI9X4dSkrgkwdSI77lzGt0Fss45rPxxGFxawiY7SvWvxQtZ6zP/jGIcekuMt+VZFxhjbfMCQQC6eGM67xFWWDbDFLXNeabi3bM1N2X5ycW7dSJ8s4gztBGnr+tXrCo2QAfOTICT5LLD0Mxs89BFmInYN2EfPhSVAkBgM37i23usTRRONGQMi7HOKIeTwn5+aV79z5si4GecTz8Y1GN6v/TW6Ab4dLglnhvX+bN6RL1XeAJ1DIasKe0bAkA8Qol20ylcKPfRhVDXTTgEWrb+PJ/k4DLZSJpTiEU8yDVoZm58j7O4gmrDXW+z25V1uHVHxGcLBqeNSyBE03AdAkBLwWeb1LJYd4oWC9CXNOGh0h3/8JTl0e4oNzYsDLoMetQyWWSoh6XxIXWi+lA7MpMJYcJMv9xVJtkkRdw7X5X5
# -----END RSA PRIVATE KEY-----
# """
#
#
# class Account:
#     '''
#     账户信息可以从以下地址注册
#     http://10.10.23.116:41008/v1/script/create_user_api?phone=12366669999
#     账号密码  dssj dssj123456
#     {"code":200,"data":{"appId":"d4f998ab4baa410786286a15a25c25d6","appSecret":"MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAKAMJbl4Wu4/eUmnHA6eW2HKkjj5R9Ik/dTOKJ83UeXJ0ZMbkK4/O/BBP183U9sZukIAEpBT6h2Sey0mt9DbzNQaYy45Q7COENJShn7BKv5DmRm8q1kMDF8lXmw9L0QSZPGIyT//Xizi7e/NE4kCQqU27MhhlpaphdJvKuWtMk3TAgMBAAECgYBwwj4t3tLJumScdKT606z0SAEfLNnh/3fqX1kVW6dSqw8BgtE7QofbLE0Wq2dkHUsxxtVNZCG0tggcdoPZHZK/1bqyL7dIms7IHaPWvLokKAuNNoiQlLgiL+P93YV5n+3k4ZUWlfW6eEpG2X8p9D6DLUCy5gZ4uLF1PHKEqeO06QJBAPgDiG8gSgcxh9qpgTZKjADQvMMgj1+PIisgNqISrgL3VJE0qV9sJVALKVZbNzCu57BZ5jdHMTJSQwrvJDs2nZ0CQQClM3njFGxjAOr7FmlLSgGTfl3chMQWyvzDNWluieMRu1RfQTM/T5l2arvA17FS2j1617MEfANlXqa9SGhDCXYvAkACjubFXqvkzxn7o2v1x2cSSxTnXlqcPbm4gCiQG2k4Fp0Esmpc1Zy86qCOh3pWQjeZlhPN1ionvrl6T2UsRy/xAkB0ZbCbrugvWZY3E7NcuOgjZAX+Og1vgdZWNGv01nKHK9Zmxym0kgEuzkU7ur3WAq8OvqwDnN1Hr0kMVNghY6lBAkAzhMdU+H1xd+YPIl1nUEXDaXcCKK3q8vF/mIDgGUnn/Kqh7u4soRT80LhDa0YtM7hsKHAL3Wf84ieX2XFXhNxz","expireDate":"2020-08-02 20:11:02","encryptToken":"bd42b0d753b745b0b66465a8de2b93cd"},"msg":"HTTP_OK","subCode":"0","subMsg":"success"}
#     '''
#
#     app_id = "c2bf899a2fb8480cb6a0236001b9bd33"
#     encrypt_token = "580539afaef14bfcb1a17866c3e522d7"
#     private_key_pem = private_key_pem


'''
钱包线上商户信息
'''
private_key_pem = b"""
-----BEGIN RSA PRIVATE KEY-----
MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAJqEI+YkurLWieUJGBWWgWrFmyqKVsjE1ZO9WQKX1+kp79uWXoCDi/NI8ryVYmzrMdy/ffSXJb1EnDPlRFMMRjLsQCT0G1cE6lwQOpk0QdyJXGIxgZ3lNRqp41JsZCkjXU4cZ6QtNwS47cfuJL5tqIQoU7gbvkeImo0PtQJIMRltAgMBAAECgYB9SRWenztulLwcpMINhwqKm41T8fWqNseCUm5gxuP/n8xnfUZE5+TLL+P5+xpifFXiyrYDY6brDz2kaop62CH2FhuVmu3IfIfwfbTb2Bbu2KTog4DaEy1LxTg+2x1A+GHFPkoJXVvPexkNLJQsAJ+IPuZjG2PatiCXIaBjv4+ktQJBANwywe1I0VwwN4myRbGWxV5xjIUv0JfuQEPCr5COC4bBCJI48XWuJAohHhUs+xxwrPkyM+qGlv5oQgaPXFYORssCQQCzo4SEDEhW+drPG3dTCcoacAoNamNSArk5B8DNjAfqTeu2HMJbjWICr1onC1Q9alf3AhikNTozlv99mWrEamGnAkA93NS2wTpwV+uCd980oVMZ0XTVBjXoOTs8zjlct0tttFWgHvdXRHFDl0JIWLbDqrQt3njPbriFCO1jwmsCkkg5AkBEoT4pbL/easqLwYSO9vh9rTxJ79FOLbgx76JbZRpJC8f35XjjnVpKiE+7BvsCE7TTq7taUPORbijiBVDjBXmVAkBPVLgxr6cG6aM7dNo/MiIWQ2VAKY30k3a5Wuq6fkckgkbeeAJOXUdXBBTD6L7OMolN52anbsH+jHVLeSseryVX
-----END RSA PRIVATE KEY-----
"""


class Account:
    '''
    账户信息可以从以下地址注册
    http://10.10.23.116:41008/v1/script/create_user_api?phone=12366669999
    账号密码  dssj dssj123456
    {"code":200,"data":{"appId":"d4f998ab4baa410786286a15a25c25d6","appSecret":"MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAKAMJbl4Wu4/eUmnHA6eW2HKkjj5R9Ik/dTOKJ83UeXJ0ZMbkK4/O/BBP183U9sZukIAEpBT6h2Sey0mt9DbzNQaYy45Q7COENJShn7BKv5DmRm8q1kMDF8lXmw9L0QSZPGIyT//Xizi7e/NE4kCQqU27MhhlpaphdJvKuWtMk3TAgMBAAECgYBwwj4t3tLJumScdKT606z0SAEfLNnh/3fqX1kVW6dSqw8BgtE7QofbLE0Wq2dkHUsxxtVNZCG0tggcdoPZHZK/1bqyL7dIms7IHaPWvLokKAuNNoiQlLgiL+P93YV5n+3k4ZUWlfW6eEpG2X8p9D6DLUCy5gZ4uLF1PHKEqeO06QJBAPgDiG8gSgcxh9qpgTZKjADQvMMgj1+PIisgNqISrgL3VJE0qV9sJVALKVZbNzCu57BZ5jdHMTJSQwrvJDs2nZ0CQQClM3njFGxjAOr7FmlLSgGTfl3chMQWyvzDNWluieMRu1RfQTM/T5l2arvA17FS2j1617MEfANlXqa9SGhDCXYvAkACjubFXqvkzxn7o2v1x2cSSxTnXlqcPbm4gCiQG2k4Fp0Esmpc1Zy86qCOh3pWQjeZlhPN1ionvrl6T2UsRy/xAkB0ZbCbrugvWZY3E7NcuOgjZAX+Og1vgdZWNGv01nKHK9Zmxym0kgEuzkU7ur3WAq8OvqwDnN1Hr0kMVNghY6lBAkAzhMdU+H1xd+YPIl1nUEXDaXcCKK3q8vF/mIDgGUnn/Kqh7u4soRT80LhDa0YtM7hsKHAL3Wf84ieX2XFXhNxz","expireDate":"2020-08-02 20:11:02","encryptToken":"bd42b0d753b745b0b66465a8de2b93cd"},"msg":"HTTP_OK","subCode":"0","subMsg":"success"}
    '''

    app_id = "c22cc2585c8e4235994cc045ef9edeba"
    encrypt_token = "0736760a6cb34e67bba8ccb16fdac1e8"
    private_key_pem = private_key_pem


class ApiConfig:
    # host = "http://10.10.23.116:41008" # 内部测试环境
    # host = "http://58.33.9.130:41008" # 对外测试环境
    host = "http://api.iccbank.net"  # 线上域名
    headers = {"application": "json", "charset": "utf-8", "OPENAPI_APP_ID": Account.app_id}


class Address:
    valid_btc = "1Hm6q7BWkdn2tbEA84gY4rNBF2tDekcccP"
    valid_eth = "0x5D281db74F856237556e428ad27922caDbfB3A02"
    invalid_btc = "1AbaXRtPE5tzQMNWhC8Va2RLj4Xg42g1L62"
    none = None
    type_int = 123456789
    type_float = 123.456789


class Code:
    btc_code = "BTC"
    eth_code = "ETH"
    error_code = "AAACCCC"
    none_code = None
    int_code = 123321


class OrderNo:
    valid_order_no = "123321"  # 缺少有效的订单号
    error_order_no = "123321123"
    int_order_no = 999999999999999
    str_order_no = "ChinaOrderNo"
    none_order_no = None


class BusinessNo:
    valid_business_no = "123321"  # 缺少有效的订单号
    error_business_no = "123321123NNNN"
    int_business_no = 999999999999999
    str_business_no = "ChinaOrderNo"
    none_business_no = None


class RespMsg:
    success_0 = {"code": 200, "msg": "ok", "subCode": "0", "subMsg": "success"}
    success_1 = {"code": 200, "msg": "HTTP_OK", "subCode": "0", "subMsg": "success"}

    error_35002 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35002", "subMsg": "平台尚未开通该币种支持"}
    error_35006 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35006", "subMsg": "地址格式不合法"}

    error_400 = {"code": 400, "msg": "该币种不支持", "subCode": "4003", "subMsg": "请求参数不合法"}

    error_400_4003 = {"code": 400, "msg": "数量范围 [1-100]", "subCode": "4003", "subMsg": "请求参数不合法"}
    error_35009 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35009", "subMsg": "数量范围 [1-100]"}

    error_35000 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35000", "subMsg": "商户订单号，平台订单号不能同时为空"}
    error_35001 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35001", "subMsg": "代付订单不存在"}
    error_35008 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35008", "subMsg": "请输入正确的订单号"}
