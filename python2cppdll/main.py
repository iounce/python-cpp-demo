from python_trader_api import *
import time

#测试地址账号根据实际情况填写
FRONT_ADDR = "tcp://222.66.235.70:61205"
BROKER_ID = "1026"
USER_ID = "00000021"
USER_PWD = "888888"

def run_api():
    api = CThostFtdcTraderApi.CreateFtdcTraderApi()
    spi = NewTraderSpi()
    
    api.RegisterSpi(spi)
    api.SubscribePublicTopic(THOST_TERT_RESTART)
    api.SubscribePrivateTopic(THOST_TERT_RESTART)
    api.RegisterFront(FRONT_ADDR)
    api.Init()
    
    time.sleep(3)
    
    field = CThostFtdcReqUserLoginField()
    field.UserID = USER_ID
    field.Password = USER_PWD
    field.BrokerID = BROKER_ID
    
    ret = api.ReqUserLogin(field, 0)
    print('login: ', ret)

if __name__ == '__main__':
    run_api()