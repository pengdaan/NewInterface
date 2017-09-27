# -*- coding: utf-8 -*-
__author__ = 'leo'
import yaml
from Public.All_secrets import *
from Test_Data.Interface.Dp_url import *
from Public.TestRequest import *
from Public.DBConns import *
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Times=int(time.time())
CommonData=parentdir+'\Test_Data\Common\Common.yaml'
times=Times

def test_Create_Order():
    '''
    点评下单
    '''
    TestData=parentdir+'\Test_Data\DP\OrderDPSuces.yaml'
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
        api_sign=TestCase.api_signs(Data,dp_secrets)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(orderDP_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1


def test_UserOrderListDP():
    '''
    获取用户订单列表
    '''
    TestData=parentdir+'\Test_Data\DP\OrderListDP.yaml'
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
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成验签
        api_sign=TestCase.api_signs(Data,dp_secrets)
        Data.setdefault('api_sign',api_sign)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        TestPostRequest(UserOrderListDP_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1



def test_cancelOrder():
    '''
    取消订单
    '''
    ComData=open(CommonData,'rb')
    TestData=parentdir+'\Test_Data\DP\CancelOrder.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    Data=[]
    for data in yaml.load_all(ComData):
        Data.append(data)
    OrderDp=Data[1]
    OrderDp.setdefault('timestamp',times)
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
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        # 创建订单
        DP_Orders=TestCase.send_data(OrderDp,orderDP_url,dp_secrets)
        # 提取订单
        DP_Order=TestCase.parse_data(DP_Orders,regular_data='.+order_sn:(.+?\d+),?.*')
        #print(DP_Order)
        # 重组取消订单json
        Data.setdefault('order_sn',DP_Order)
        # 生成验签
        api_sign=TestCase.api_signs(Data,dp_secrets)
        Data.setdefault('api_sign',api_sign)
        TestPostRequest(UserOrderListDP_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1


def test_applyRefund():
    '''
    前台取消订单，申请退款
    '''
    ComData=open(CommonData,'rb')
    TestData=parentdir+'\Test_Data\DP\ApplyRefund.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    Data=[]
    for data in yaml.load_all(ComData):
        Data.append(data)
    OrderDp=Data[1]
    PayOrder=Data[2]
    OrderDp.setdefault('timestamp',times)
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
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        # 创建订单
        DP_Orders=TestCase.send_data(OrderDp,orderDP_url,dp_secrets)
        # 提取订单号
        DP_Order=TestCase.parse_data(DP_Orders,regular_data='.+order_sn:(.+?\d+),?.*')
        # 提取订单金额
        Order_amount=TestCase.parse_data(DP_Orders,regular_data='.+order_amount:(.+?\d+),?.*')
        # 生成支付订单json
        PayOrder.setdefault('timestamp',times)
        PayOrder.setdefault('order_sn',DP_Order)
        PayOrder.setdefault('order_amount',Order_amount)
        # 支付订单
        TestCase.send_data(PayOrder,updatePayStatus_url,update_dpStatus)
        # 取消订单，申请退款接口json生成
        Data.setdefault('order_sn',DP_Order)
        Data.setdefault('timestamp',times)
        if Data.get('amount')=='1':
            Data.setdefault('order_amount','500')
        else:
            Data.setdefault('order_amount',Order_amount)
        # 生成验签
        api_sign=TestCase.api_signs(Data,dp_secrets)
        Data.setdefault('api_sign',api_sign)
        TestPostRequest(UserOrderListDP_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1



def test_OrderBySnDp():
    '''
    前台取消订单，申请退款
    '''
    ComData=open(CommonData,'rb')
    TestData=parentdir+'\Test_Data\DP\OrderBySnDp.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    headers=None
    Data=[]
    for data in yaml.load_all(ComData):
        Data.append(data)
    OrderDp=Data[1]
    OrderDp.setdefault('timestamp',times)
    # 创建订单
    DP_Orders=TestCase.send_data(OrderDp,orderDP_url,dp_secrets)
    # 提取订单号
    DP_Order=TestCase.parse_data(DP_Orders,regular_data='.+order_sn:(.+?\d+),?.*')
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
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        if Data.get('order_sn')=='0':
            Data.setdefault('order_sn','0')
        else:
            Data.setdefault('order_sn',DP_Order)
        # 生成验签
        api_sign=TestCase.api_signs(Data,dp_secrets)
        Data.setdefault('api_sign',api_sign)
        TestPostRequest(OrderBySnSnDp_url,Data,headers, testcaseId, testcaseName,Code)
        i=i+1

def test_UpdateComment():
    '''
    点评或旅游--更新评价状态
    '''
    ComData=open(CommonData,'rb')
    TestData=parentdir+'\Test_Data\DP\CommentStatus.yaml'
    f = open(TestData,'rb')
    TestCase=XsxDriver()
    Sqldata=Mysql()
    headers=None
    Data=[]
    for data in yaml.load_all(ComData):
        Data.append(data)
    OrderDp=Data[1]
    PayOrder=Data[2]
    PayOrder.setdefault('timestamp',times)
    OrderDp.setdefault('timestamp',times)
    # 创建订单
    DP_Orders=TestCase.send_data(OrderDp,orderDP_url,dp_secrets)
    # 提取订单号
    DP_Order=TestCase.parse_data(DP_Orders,regular_data='.+order_sn:(.+?\d+),?.*')
    # 提取订单金额
    Order_amount=TestCase.parse_data(DP_Orders,regular_data='.+order_amount:(.+?\d+),?.*')
    # 生成支付订单json
    PayOrder.setdefault('timestamp',times)
    PayOrder.setdefault('order_sn',DP_Order)
    PayOrder.setdefault('order_amount',Order_amount)
    # 通过数据库查询order_id
    Dp_id=Sqldata.select(data='order_id',table='mall_order_info',where="order_sn='%s'"%DP_Order)
    order_id=Dp_id[0].get('order_id')
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
        del Data['CaseName']
        # 插入时间戳
        Data.setdefault('timestamp',times)
        # 生成测试ID
        testcaseId = "1-1-"+str(i)
        testcaseName = CaseName
        if Data.get('order_sn')=='1':
            Data.setdefault('order_id',order_id)
        else:
            # 支付订单
            TestCase.send_data(PayOrder,updatePayStatus_url,update_dpStatus)
            Data.setdefault('order_id',order_id)
        # 生成验签
        api_sign=TestCase.api_signs(Data,update_dpStatus)
        Data.setdefault('api_sign',api_sign)
        TestPostRequest(UpdateCommentStatusUrl,Data,headers,testcaseId,testcaseName,Code)
        i=i+1


def test_GoodsByIdsDp():
    '''
    获取商品基本信息-列表页
    '''
    TestData=parentdir+'\Test_Data\DP\GoodsByIdsDp.yaml'
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
        TestPostRequest(GoodsByIdsDpUrl,Data,headers, testcaseId, testcaseName,Code)
        i=i+1

def test_GoodsByIdsDetailDp():
    '''
    批量获取商品基本信息详情
    '''
    TestData=parentdir+'\Test_Data\DP\DetailGoods.yaml'
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
        TestPostRequest(GoodsByIdsDetailDpUrl,Data,headers, testcaseId, testcaseName,Code)
        i=i+1


def test_UpdateConsumeStatus():
    '''
    更新到店状态
    '''
    TestData=parentdir+'\Test_Data\DP\SumeStatus.yaml'
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
        TestPostRequest(UpdateConsumeStatusUrl,Data,headers, testcaseId, testcaseName,Code)
        i=i+1


def test_GoodsBySupplierIdDp():
    '''
    根据供应商ID获取商品-商户页
    '''
    TestData=parentdir+'\Test_Data\DP\GoodsBySupplierIdDp.yaml'
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
        TestPostRequest(GoodsBySupplierIdDpUrl,Data,headers, testcaseId, testcaseName,Code)
        i=i+1







# 测试数据
#test_UpdateComment()
#test_OrderBySnDp()
#test_GoodsByIdsDp()
#test_GoodsByIdsDetailDp()
#test_UpdateConsumeStatus()
test_GoodsBySupplierIdDp()

