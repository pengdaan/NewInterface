# -*- coding: utf-8 -*-
__author__ = 'leo'
import sys
import pickle
sys.path.append('..')
import re
import hashlib
from Public.DBConns import Mysql
import requests
import json
import time
import random
times= int(time.time())
class XsxDriver(object):
    def __init__(self):
        pass

    def checkapi_key(self,test_data):
        """
        判断test_data里面api_Key是否存在
        """

        test_data=json.loads(test_data)
        if isinstance(test_data,dict):
            api_key=test_data.get('api_key')
            return api_key
        else:
            print(u"api_key 不存在，请检查接口数据！")
            return None


    def checkapi_secret(self,test_data):

        """
        通过api_key查询，判断secret是否存在
        """
        api_key=self.checkapi_key(test_data)
        mysql = Mysql()
        api_secret = mysql.select(data='api_secret',table='mall_app',where="api_key='%s'"%api_key)
        try:
            if api_secret[0].get('api_secret')!=[]:
                return api_secret[0].get('api_secret')
            else:
                print('api_key不存在')
        except:
            print('程序错误，请检查传入的sql语句以及return值的类型')


    def api_signs(self,test_data,api_secret):

        """
        生成验签算法
        """
        api_sign=[]
        for (key,value) in test_data.items():
            api_sign.append( key +str(value))
        #获取所有键值对，并升序排列
        api_sign.sort()
        api_signs = "".join(api_sign)
        pj=api_secret+api_signs+api_secret
        #对字符串内部的特殊字符进行转义
        pj = pj.replace("\\n", "\n")
        pj = pj.replace("\\r", "\n")
        pj = pj.replace("\\", "")
        #MD5加密

        #md5jm= hashlib.new("md5", pj).hexdigest()#python2写法
        #return md5jm.upper()

        m=hashlib.md5(pj.encode(encoding='utf-8'))#python3 写法
        md5jm=m.hexdigest()
        return (md5jm.upper())#然后把加密内容转换为大写


    def test_datas(self,test_data,api_secret):

        """
        重新组装测试数据，把生成的验签插入TestData
        """
        api_sign=self.api_signs(test_data,api_secret)
        test_data.setdefault('api_sign',api_sign)
        return test_data



    def result_json(self,result):
        """
        将json解析成python的数据类型,以特定的格式输出，且处理中文显示问题
        """
        try:
            js = json.loads(result)#将json解析成python的数据类型
            #print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10)) #转化为json，以特定的格式输出，且处理中文显示问题
            return js
        except:
            print (result)


    def send_data(self,test_data,url,api_secret):
        test_data=self.test_datas(test_data,api_secret)
        #print test_data
        r=requests.post(url, params=test_data)
        result=r.text
        js=self.result_json(result)
        return js


    def Post_data(self,test_data,url,headers=None):
        """
        Post请求的方法
        """
        if headers==None:
            r=requests.post(url, params=test_data)
            result=r.text
            js=self.result_json(result)
        else:
            r=requests.post(url, params=test_data,headers=headers)
            result=r.text
            js=self.result_json(result)
        return js


    def parse_data(self,test_data,regular_data):
        """
        从输出结果的json中提取需要的内容，其中regular_data为正则表达式
        如regular_data='.+order_status:(.+?\d+),?.*'
        处理json的特殊字符test_data.replac可以写多一点
        """
        test_data=json.dumps(test_data)
        test_data = test_data.replace("\\", "")
        test_data = test_data.replace("\"", "")
        test_data = test_data.replace("\'", "")
        data=re.compile(regular_data).findall(test_data)
        if data==[]:
            BadData={'msg':'Error'}
            return BadData
        else:
            datas=data[0]
            datas=datas.replace("\\n", "")
            datas=datas.replace(" ", "")
            return datas


    def Updatexux_Order(self,XUXorder):
        """
        通过修改数据库更改订单状态为已审核状态，只能改普通的直邮订单
        """
        XUXorders = "UPDATE mall_order_info SET order_status='1',order_amount='0',confirm_time='%(time)s' WHERE order_sn='%(XUX_OrderApi)s'"%{'time':times,"XUX_OrderApi":XUXorder}
        mysql = Mysql()
        mysql.query(XUXorders)


    def Return_data(self,sql_data,send_data):
        data=sql_data
        mysql = Mysql()
        datas=mysql.query(data)
        if send_data in datas:
            return datas[send_data]
        else:
            return 'The data does not exist'



    def store(self,data_name,data,model,status=None):
        '''
        持久化保存
        model作为pkl文件名
        status =1，传入参数组成键值对{data_name:data}
        status =None，传入参数为data
        '''
        if status==None:
            test={data_name:data}
            path='/SmallBear_Interface/Test_Data/RunData/'
            filename=path +'data_%s.pkl'% model
            output=open(filename,'wb')
            pickle.dump(test,output)
        elif status==1:
            test=data
            path='/SmallBear_Interface/Test_Data/RunData/'
            filename=path +'data_%s.pkl'% model
            output=open(filename,'wb')
            pickle.dump(test,output)


    def load(self,value,model,status=None):
        '''获取持久化数据，转换成json'''
        path='/SmallBear_Interface/Test_Data/RunData/'
        filename=path +'data_%s.pkl'% model
        pkl_file=open(filename,'rb')
        if status==None:
            data=pickle.load(pkl_file)[value]
            pkl_file.close()
            return data
        elif status==1and value==None:
            data=pickle.load(pkl_file)
            pkl_file.close()
            return data

    def couponId(self):
        '''
        生成7位数随机数
        '''
        coupon=random.randint(1000000, 10000000)
        return coupon

    def addWord(self,theIndex,word,pagenumber):

        theIndex.setdefault(word, []).append(pagenumber)

    def AssemblyData(self,JsonData,Data01,Data02):
        '''
        :param JsonData:存在需要封装的参数json
        :param Data01: 参数传入json
        :param Data02: 参数传入json
        :return:返回完整的json
        '''
        JsonData(str(Data01),str(Data02))
        return JsonData










































