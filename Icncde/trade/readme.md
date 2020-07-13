- 脚本币币数据初始化
```
多个用户多个币种随机创建N个盘口信息（卖盘1 > 买盘1）， N自定义，等到盘口到达一定高度、深度后在生成新的委托订单进行撮合
多个用户多个币种进行撮合

```
- 相关服务
```
icc-match-app-service 撮合
icc-market-coin-app-service 画线 
icc-market-coin-web-socket 行情 
icc-openapi-websocket
icc-openapi-web
icc-trade-coin-app-service 委托 
icc-trade-coin-clearing-app-service 清算 
```
##### 修改币对配置(建议从后台配置 后台禁用 修改参数 在启用)
```sql
-- 币对节点设置
-- ENCRY_DRAW_KLINE_NODE_IP 画线节点ip（格式 127.0.0.1:22837）
-- ENCRY_MATCH_ENGINE_NODE_IP 撮合引擎节点ip（格式 127.0.0.1:22837）
-- ENCRY_MATCH_RESULT_HANDLER_NODE_IP 撮合结果处理节点IP
SELECT * FROM icc_instrument.ins_parameter WHERE obj_code='BTC_USDT_ICNCDE_ENCRY' AND TYPE=41 AND CODE IN ('ENCRY_MATCH_RESULT_HANDLER_NODE_IP',
'ENCRY_MATCH_ENGINE_NODE_IP','ENCRY_DRAW_KLINE_NODE_IP')

-- 币种清算节点设置
-- 清算节点IP SPOT_DEAL_ONWAY_CAPITAL_NODE_IP
SELECT * FROM icc_instrument.ins_parameter WHERE obj_code='BTC' AND TYPE=20 AND CODE ='SPOT_DEAL_ONWAY_CAPITAL_NODE_IP';

-- 币对配置修改（若之前已经启动过，先修改成0，重启所有服务后在启动服务改成1）：
-- 包括修改节点信息等
-- enabled = 1 启动服务
SELECT * FROM icc_instrument.instrument WHERE code like 'TEST%_USDT_ICNCDE_ENCRY' AND ex_type = 'ENCRY' and enabled = 0
SELECT * FROM icc_instrument.instrument WHERE code like '%TEST_BTC_ICNCDE_ENCRY' AND ex_type = 'ENCRY' and enabled = 1
```


##### 服务重启相关操作
- 第一步：关闭服务
```shell script
- test-a test-b
supervisorctl stop icc-trade-coin-web
supervisorctl stop icc-trade-coin-app-service
supervisorctl stop icc-market-coin-web-socket
supervisorctl stop icc-match-app-service
```
- 第二步：清除数据
```sql
TRUNCATE coin_capital_freeze_water ;
TRUNCATE coin_capital_water;
TRUNCATE coin_deal_onway_capital;
TRUNCATE coin_entrust_record;
TRUNCATE coin_idempotent;
TRUNCATE coin_idempotent_7;
TRUNCATE coin_idempotent_8;
TRUNCATE coin_idempotent_10;
TRUNCATE coin_match_record;
TRUNCATE coin_orders;
TRUNCATE coin_orders_detail;
TRUNCATE coin_orders_done;
TRUNCATE coin_platform_onway_capital;
TRUNCATE coin_entrust_push_match_fail;

UPDATE coin_capital_detail SET balance=1000000000.00000000000000000000 ,freeze=0 and user_id<>9999999999999 ;
UPDATE coin_capital_detail SET balance=0 ,freeze=0 WHERE user_id=9999999999999;

SELECT CONCAT('truncate icc_match.', table_name , ';') FROM information_schema.TABLES WHERE table_name LIKE 'match_history_%'; -- 查询结果，复制语句执行

```


- 第四步：启动服务
```shell script
-- test-a test-b
supervisorctl start icc-market-coin-web-socket
supervisorctl start icc-trade-coin-app-service
supervisorctl start icc-trade-coin-web
supervisorctl start icc-match-app-service

-- 重启
supervisorctl restart icc-trade-coin-app-service
supervisorctl restart icc-match-app-service

-- 查看状态
supervisorctl status
```
