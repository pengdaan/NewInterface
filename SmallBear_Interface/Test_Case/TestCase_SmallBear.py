# -*- coding: utf-8 -*-
__author__ = 'leo'
import yaml
from Public.All_secrets import *
from Test_Data.Interface.SmallBear_url import *
from Test_Data.Interface.Dp_url import *
from Public.TestRequest import *
from Public.DBConns import *
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Times=int(time.time())
CommonData=parentdir+'\Test_Data\Common\Common.yaml'
times=Times

def test_PromotionNums():
    '''
    获取秒杀订单实际秒杀购买数
    '''
    TestData=parentdir+'\Test_Data\SmallBear\PromotionNums.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成验签
        api_sign=TestCase.api_signs(Data,update_dpStatus)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(PromotionNums_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1


def test_RemindMsg():
    '''
    获取订单客服留言接口
    '''
    ComData=open(CommonData,'rb')
    TestData=parentdir+'\Test_Data\SmallBear\RemindMsgNew.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    Data=[]
    for data in yaml.load_all(ComData):
        Data.append(data)
    OrderXsx=Data[3]
    result=requests.post(createOrderXsx_url,params=OrderXsx)
    results=TestCase.result_json(result.text)
    Order_sn=TestCase.parse_data(results,regular_data='.+order_sn:(.+?\d+),?.*')
    TestCase.store('Order_sn',Order_sn,'MsgOrdersn',status=1)
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 获取持久化数据
        Order_sn=TestCase.load(value=None,model='MsgOrdersn',status=1)
        if Data.get('order_sn')==1:
            del Data['order_sn']
            Data.setdefault('order_sn','XS11111111111111')
        elif Data.get('order_sn')==2:
            del Data['order_sn']
            Data.setdefault('order_sn','')
        else:
            Data.setdefault('order_sn',Order_sn)
        # 生成验签
        api_sign=TestCase.api_signs(Data,update_dpStatus)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(RemindMsg_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1


def test_updateRemindMsg():
    '''
    更新订单客服留言接口
    '''
    TestData=parentdir+'\Test_Data\SmallBear\RemindMsg.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 获取持久化数据
        Order_sn=TestCase.load(value=None,model='MsgOrdersn',status=1)
        if Data.get('order_sn')==1:
            del Data['order_sn']
            Data.setdefault('order_sn','XS11111111111111')
        elif Data.get('order_sn')==2:
            del Data['order_sn']
            Data.setdefault('order_sn','')
        else:
            Data.setdefault('order_sn',Order_sn)
        # 生成验签
        api_sign=TestCase.api_signs(Data,update_dpStatus)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(updateRemindMsg_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1


def test_PayStatus():
    '''
    支付订单接口
    '''
    ComData=open(CommonData,'rb')
    TestData=parentdir+'\Test_Data\SmallBear\PayStatus.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    Data=[]
    for data in yaml.load_all(ComData):
        Data.append(data)
    OrderXsx=Data[3]
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        result=requests.post(createOrderXsx_url,params=OrderXsx)
        results=TestCase.result_json(result.text)
        # 提取支付金额
        Order_sn=TestCase.parse_data(results,regular_data='.+order_sn:(.+?\d+),?.*')
        #  提取订单金额
        Order_amount=TestCase.parse_data(results,regular_data='.+order_amount:(.+?\d+),?.*')
        if Data.get('order_sn')==1:
            del Data['order_sn']
            Data.setdefault('order_sn','XS11111111111111')
            Data.setdefault('order_amount',Order_amount)
        elif Data.get('order_sn')==2:
            del Data['order_sn']
            Data.setdefault('order_sn','')
            Data.setdefault('order_amount',Order_amount)
        elif Data.get('order_sn')==3:
            del Data['order_sn']
            Data.setdefault('order_sn',Order_sn)
            Data.setdefault('order_amount','0.01')
        elif Data.get('order_amount')==1:
            del Data['order_amount']
            Data.setdefault('order_sn',Order_sn)
            Data.setdefault('order_amount','')
        elif Data.get('order_sn')==2:
            del Data['order_amount']
            Data.setdefault('order_sn',Order_sn)
            Data.setdefault('order_amount','##@%@#$#')
        else:
            Data.setdefault('order_sn',Order_sn)
            Data.setdefault('order_amount',Order_amount)
        # 生成验签
        api_sign=TestCase.api_signs(Data,update_dpStatus)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(updatePayStatus_url,Data,headers,testcaseId,testcaseName,Code)
        i=i+1


def test_OrderByProductId():
    '''
    过商品id获取订单列表
    '''
    TestData=parentdir+'\Test_Data\SmallBear\OrderByProductId.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成验签
        api_sign=TestCase.api_signs(Data,YG_secrets)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(OrderByProductId_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1


def test_UserOrderNums():
    '''
    根据订单分类获取分类订单总数
    '''
    TestData=parentdir+'\Test_Data\SmallBear\OrderNums.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成验签
        api_sign=TestCase.api_signs(Data,www_secrets)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(UserOrderNums_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1


def test_OrderPromotionList():
    '''
    获取用户购买的促销订单信息
    '''
    TestData=parentdir+'\Test_Data\SmallBear\OrderPromotionList.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成验签
        api_sign=TestCase.api_signs(Data,www_secrets)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(OrderPromotionList_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1


def test_OrderSource():
    '''
    获取订单参数来源
    '''
    TestData=parentdir+'\Test_Data\SmallBear\OrderSource.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成验签
        api_sign=TestCase.api_signs(Data,www_secrets)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(G_dingdan_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1

def test_GetStock():
    '''
    获取单个商品的库存
    '''
    TestData=parentdir+'\Test_Data\SmallBear\GetStock.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成验签
        api_sign=TestCase.api_signs(Data,www_secrets)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(GetStocks_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1


def test_CreateSupplier():
    '''
    获取单个商品的库存
    '''
    TestData=parentdir+'\Test_Data\SmallBear\CreateSupplier.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成验签
        api_sign=TestCase.api_signs(Data,www_secrets)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(CreateSupplier_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1



def test_Ship():
    '''
    输入消费券发货
    '''
    Tsql=Mysql()
    ComData=open(CommonData,'rb')
    TestData=parentdir+'\Test_Data\SmallBear\ShipData.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    Data=[]
    for data in yaml.load_all(ComData):
        Data.append(data)
    OrderLy=Data[4]
    PayOrder=Data[2]
    PayOrder.setdefault('timestamp',Times)
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 创建订单
        result=requests.post(createOrderTour_url,params=OrderLy)
        results=TestCase.result_json(result.text)
        print(results)
        # 提取订单号
        DP_Order=TestCase.parse_data(results,regular_data='.+order_sn:(.+?\d+),?.*')
        print(DP_Order)
        # 提取订单金额
        #Order_amount=TestCase.parse_data(results,regular_data='.+order_amount:(.+?\d+)')
        Order_amount=0.1
        print(Order_amount)
        # 获取订单id
        Order_ids= Tsql.select(data='order_id',table='mall_order_info',where="order_sn='%s'"%DP_Order)
        Order_id=Order_ids[0].get('order_id')
        # 生成支付订单json
        PayOrder.setdefault('timestamp',times)
        PayOrder.setdefault('order_sn',DP_Order)
        PayOrder.setdefault('order_amount',Order_amount)
        # 支付订单
        TestCase.send_data(PayOrder,updatePayStatus_url,update_dpStatus)

        SendData=str(Data.get('data'))
        print(SendData)
        couponId=TestCase.couponId()
        print(couponId)
        SendData=SendData%(str(Order_id),str(couponId))
        print(SendData)
        del Data['data']
        Data.setdefault('data',SendData)
        print(Data)
        # if Data.get('order_sn')==1:
        #     del Data['order_sn']
        #     Data.setdefault('order_sn','XS11111111111111')
        #     Data.setdefault('order_amount',Order_amount)
        # elif Data.get('order_sn')==2:
        #     del Data['order_sn']
        #     Data.setdefault('order_sn','')
        #     Data.setdefault('order_amount',Order_amount)
        # elif Data.get('order_sn')==3:
        #     del Data['order_sn']
        #     Data.setdefault('order_sn',Order_sn)
        #     Data.setdefault('order_amount','0.01')
        # elif Data.get('order_amount')==1:
        #     del Data['order_amount']
        #     Data.setdefault('order_sn',Order_sn)
        #     Data.setdefault('order_amount','')
        # elif Data.get('order_sn')==2:
        #     del Data['order_amount']
        #     Data.setdefault('order_sn',Order_sn)
        #     Data.setdefault('order_amount','##@%@#$#')
        # else:
        #     Data.setdefault('order_sn',Order_sn)
        #     Data.setdefault('order_amount',Order_amount)
        # # 生成验签
        api_sign=TestCase.api_signs(Data,update_dpStatus)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(ship_url,Data,headers,testcaseId,testcaseName,Code)
        i=i+1









def test_BatchCreateSku():
    '''
    ERP自动创建sku
    '''
    TestData=parentdir+'\Test_Data\SmallBear\BatchCreateSku.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        # 获取code值
        Code=(Data.get('code'))
        # 删除code键值对，生成验签出错
        del Data['code']
        CaseName=(Data.get('CaseName'))
        times=Times
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('t',times)
        # 生成验签
        api_sign=TestCase.api_signs(Data,www_secrets)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        print(Data)
        TestPostRequest(batchCreateSku_url,Data,headers,testcaseId,testcaseName,Code)
        i=i+1






def test_GetStock1():
    '''
    获取单个商品的库存
    '''
    TestData=parentdir+'\Test_Data\SmallBear\Test.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    i=1
    for data in yaml.load_all(f):
        Data=data
        # 转换成字典
        yaml.safe_dump(Data)
        print(Data)
        # 获取code值
        # Code=(Data.get('code'))
        # # 删除code键值对，生成验签出错
        # del Data['code']
        # CaseName=(Data.get('CaseName'))
        # times=Times
        # del Data['CaseName']
        # # 插入时间戳
        # Data.setdefault('t',times)
        # print(Data)
        # data1='100'
        # data2='200'
        # content = Data['data']
        # modified_content = content%{:data1 =>data1}
        Code=str(Data.get('data'))
        print(Code)
        Code=Code%(2500, "qiwsir")
        print(Code)
        # a="'"+Code+"'"
        # print(a)
        # orderId=1
        # coupons_ship=2
        # del Data['data']
        # Data.setdefault('data',a)
        # print(Data)









        # 生成验签
        # api_sign=TestCase.api_signs(Data,www_secrets)
        # Data.setdefault('api_sign',api_sign)
        # # 生成测试ID
        # testcaseId = "1-1-"+str(i)
        # testcaseName = CaseName
        # TestPostRequest(GetStocks_url,Data,headers, testcaseId, testcaseName,Code)
        # i=i+1



#test_PromotionNums()
#test_RemindMsg()
#test_updateRemindMsg()
#test_PayStatus()
#test_OrderByProductId()
#test_UserOrderNums()
#test_OrderPromotionList()
#test_OrderSource()
#test_GetStock()
#test_GetStock1()
#test_CreateSupplier()
#test_BatchCreateSku()
test_Ship()