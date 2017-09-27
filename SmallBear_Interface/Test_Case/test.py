# -*- coding: utf-8 -*-
__author__ = 'leo'
#加载yaml
import yaml
from Public.Driver import XsxDriver
from Public.All_secrets import *
import time
import requests
#读取文件
f = open('F:/SmallBear_Interface/Test_Data/DP/OrderDPSuces.yaml','rb')
orderDP_url="http://www.xiaoshuxiong.com/api/order/createOrderDp"
#导入
#yaml.safe_dump(data)
cc=XsxDriver()
for data in yaml.load_all(f):
    print (data)
    a=data
    yaml.safe_dump(a) #转换成字典
    #print (type(a))
    print(a.get('code'))
    del a['code']
    print(a)


    times=int(time.time())
    a.setdefault('timestamp',times)
    api_secrets=dp_secrets
    api_sign=cc.api_signs(a,api_secrets)
    print(api_sign)
    a.setdefault('api_sign',api_sign)
    bb=requests.post(orderDP_url,a)
    print(bb.text)




def test_Create_Order1():
    f = open(TestData,'rb')
    Driver=XsxDriver()
    for data in yaml.load_all(f):
        print (data)
        Data=data
        yaml.safe_dump(Data) #转换成字典
        Code=(Data.get('code'))
        del Data['code']
        times=Times
        Data.setdefault('timestamp',times)
        r=requests.post(orderDP_url,Data)
        print(r.text)
        Create_Orders= Driver.send_data(Data,orderDP_url,api_secret=dp_secrets)

