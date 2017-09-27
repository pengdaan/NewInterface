# -*- coding: utf-8 -*-
import yaml,json
__author__ = 'leo'
#成功创建订单,发卷
orderId='+str(orderId)+'
coupons_ship='+str(coupons_ship)+'
data={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'data':'{"supplierId":110,"orderId":'+str(orderId)+',"coupons":["'+str(coupons_ship)+'"]}'
    }
print (type(data))
datas=json.dumps(data)
data1=json.loads(datas)
print(data1)

data2={'api_key': '9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o', 'data': '{"supplierId":110,"orderId":+str(orderId)+,"coupons":["+str(coupons_ship)+"]}'}