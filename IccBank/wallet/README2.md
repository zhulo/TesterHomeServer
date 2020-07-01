#### 钱包相关信息（测试环境）
- 流程图
```
https://www.processon.com/view/link/5eb8e334f346fb6907e8ba65
```
- api文档
```
https://www.showdoc.cc/846626167169774?page_id=4609219402706935
```
- API 限流
```
http://10.10.23.116:8180/#/dashboard/identity/didipay-openapi-web
```

- 注册账号
```text
http://10.10.23.116:41008/v1/script/create_user_api?phone=13088888888
dssj
dssj123456
生成账号  appId、appSecret（私钥）、encryptToken 一对一
{"code":200,"data":{"appId":"212cbf63ee2640c1895aa59d9e1e2ffd","appSecret":"MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAMingNdfHeVn3NMhXUJTNXyRro/z23nF7i0qCWA+8fglqRY6SGbQJ0qIxxD51JpOg/JmhcvNgCSazyBfdweQg/uwIhbRunBbxLW3GChsLhgqzJTAgo4BDDy0ejkZZtwanh8XetZx9qDQTZj9fyanke/P14JvsdYmPIwqT4EYdzQJAgMBAAECgYBxEYKW2nB8TxSunIRy1XS0Z1tYnu+0JQbbyG5UH+Q2EvK/JcSauv0JER4rwLw+37OWqpMGjxyAhAPnmCP4zUSxVFysV00ijmX+iZF9pTj1dJPVQkBdB0IO4kMoBlO6OE/KLgGLEuhCMoow2uwxTAbVtU7LtYddp66OJRas+lLQAQJBAPxeJbMh6YeNsREd/kwZVNXtbg4lxQMfYAEy1BY4rkzjxUB5PLa0dSKf07bJXf+Cwy0SWZ75GUNykhDKfwtTDwkCQQDLitEpu3cRmedwliQIt0lqBPIcF6nz74JYkOZeJO2EAzseVrt1ql2Do+dRkn+Mu3cHh9v+BZ6nq89YakcS1z0BAkBYjWCFHp0m51z+OJwGb80I06sOY8phchzpzsAEnBbs++821FOteFyxrYtIVBgbk/KQWiQAWD+5HvaJ1cQGYTqhAkBxu6Oceg/SWfkkxABmjmQLRbAzWlWw5IglDPJscJ33QgbqsPQWj5epUxCSWBXFgYrFPnkCvAknD63QbbJBKNwBAkAttut3eysOPXhqx2ulPCftbuV/GNx5y9jQPYx87WjQC7k+nplIW5eKI1LMWQ6zLQgLDELOvgsRzcGga3pW/0aw","expireDate":"2020-07-08 18:41:35","encryptToken":"e77df9b63915486598f3047f3f4a53e7"},"msg":"HTTP_OK","subCode":"0","subMsg":"success"}
```

- 数据库相关
```
10.10.23.99
didipay_user
```
- linux
```
ssh test-pay
/data/didipay-openapi-web
```

#### ETH
```
'''
查询地址:
https://cn.etherscan.com/
以太坊热钱包: 0x419f041aC7490f7AE1db6243F050d4FFFc1Ff9c1    0.1 ETH
```


##### FIL(测试币)
```
领币地址： https://faucet.testnet.filecoin.io/
查币地址： https://filfox.io/
```


OpenApi 限流控制台

http://10.10.23.116:8180/
sentinel
sentinel

##### 矿工费计算
```
是这两个数相乘，注意那个单位是AttoFIL， 1AttoFIL = 1FIL* 10^-18
```

