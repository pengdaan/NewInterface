# -*- coding: utf-8 -*-
__author__ = 'leo'
import json
import requests
from Public.Driver import XsxDriver
from Public.SmallBear_Log import *
title='测试日志'
log_Title=SmallBear_Log(title)

TDriver=XsxDriver()
ResultList = []#添加一个数组，用来装测试结果
def TestPostRequest(Turl,Data,Headers,TC_id,TC_name,Tcode):
    resultJson=requests.post(Turl,data=Data,headers=Headers)
    try:
        js = json.loads(resultJson.text)#获取并处理返回的json数据
        FailTest=(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10)) #转化为json，以特定的格式输出，且处理中文显示问题
        Result=TDriver.parse_data(resultJson.text,regular_data='SUCCESS') #提取接口返回的结果，通过正则匹配返回结果是否为SUCESS
        TCerror="Error" #默认接口返回的数据为Error,当执行反向的用例时，如不输入账号访问登录账号这种情况
        if TCerror in Result:
            ResultCode = str(js["code"]) #提取接口返回的code
            if str(ResultCode) == str(Tcode): #判断接口返回的code是否和预期值一致
                TResult={
                    "T_id":TC_id,
                    "T_name":TC_name,
                    "method":"POST",
                    "T_url": Turl,
                    "T_param": "测试数据:"+str(Data),
                    "T_hope": "code:"+str(Tcode),
                    "T_actual": "Code:" + ResultCode + ";msg:" + str(js['msg']),
                    "T_result": "通过"}
                # 把测试结果添加到数组里面
                ResultList.append(TResult)
                # print(TC_name)
                # print('')
                # print("测试通过")
                # print('')
                # print("返回的消息是："+str(js['msg']))
                # 记录日志
                log_Title.info_log('inputdata>用例名称:%s, 参数:%s, url:%s ,返回:%s,预期:%s, 测试结果:测试通过'%(TC_name,Data,Turl,(js['msg']),Tcode))

            else:
                TResult={
                    "T_id":TC_id,
                    "T_name":TC_name,
                    "method":"POST",
                    "T_url": Turl,
                    "T_param": "测试数据:"+str(Data),
                    "T_hope": "code:"+str(Tcode),
                    "T_actual": str(FailTest),
                    "T_result": "失败"}
                ResultList.append(TResult)#把测试结果添加到数组里面
                # print(TC_name)
                # print('')
                # print("测试不通过")
                # print('')
                # print("返回的消息是："+str(FailTest))
                # 记录日志
                log_Title.info_log('inputdata>用例名称:%s, 参数:%s, url:%s ,返回:%s,预期:%s, 测试结果:测试不通过'%(TC_name,Data,Turl,(js['msg']),Tcode))


        else: #正向用例判断入口，当接口返回的内容为sucess的时候
            ResultCode = str(js["code"]) #提取接口返回的code
            if str(ResultCode) == str(Tcode):
                TResult={
                    "T_id":TC_id,
                    "T_name":TC_name,
                    "method":"POST",
                    "T_url": Turl,
                    "T_param": "测试数据:"+str(Data),
                    "T_hope": "code:"+str(Tcode),
                    "T_actual": "Code:"+ResultCode+";msg:"+str(js['msg']),
                    "T_result": "通过"}
                ResultList.append(TResult)#把测试结果添加到数组里面
                # print(TC_name)
                # print('')
                # print("测试通过")
                # print('')
                # print("返回的消息是："+str(js['msg']))
                # 记录日志
                log_Title.info_log('inputdata>用例名称:%s, 参数:%s, url:%s ,返回:%s,预期:%s, 测试结果:测试通过'%(TC_name,Data,Turl,(js['msg']),Tcode))


            else:#处理接口返回sucess，但code与预期值不一致的情况
                TResult={
                    "T_id":TC_id,
                    "T_name":TC_name,
                    "method":"POST",
                    "T_url": Turl,
                    "T_param": "测试数据:"+str(Data),
                    "T_hope": "code:"+str(Tcode),
                    "T_actual": str(FailTest),
                    "T_result": "失败"}
                ResultList.append(TResult)#把测试结果添加到数组里面
                # print(TC_name)
                # print('')
                # print("测试不通过")
                # print('')
                # print("返回的消息是："+str(FailTest))
                # 记录日志
                log_Title.info_log('inputdata>用例名称:%s, 参数:%s, url:%s ,返回:%s,预期:%s, 测试结果:测试不通过'%(TC_name,Data,Turl,(js['msg']),Tcode))


    except:#接口异常的情况
        TResult={
            "T_id":TC_id,
            "T_name":TC_name,
            "method":"POST",
            "T_url": Turl,
            "T_param": "测试数据:"+str(Data),
            "T_hope": "code:"+str(Tcode),
            "T_actual": str(json.loads(resultJson.text)),
            "T_result": "错误"}
        ResultList.append(TResult)#把测试结果添加到数组里面
        # print(TC_name)
        # print('\n')
        # print("测试不通过")
        # print('\n')
        # print("返回的消息是："+str(resultJson.text))
        # 记录日志
        log_Title.info_log('inputdata>用例名称:%s, 参数:%s, url:%s ,返回:%s,预期:%s, 测试结果:失败'%(TC_name,Data,Turl,(json.loads(resultJson.text)),Tcode))
