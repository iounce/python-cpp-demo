def sayHello():
    return "Hello World-你好世界"

def addValue(a, b):
    return a + b

def int2str(data):
    return [str(i) for i in data]

def packOrder(order):
    req = {}
    req['price'] = order['input_price']
    req['volume'] = order['input_volume']
    req['remark'] = 'fruit'
    return req