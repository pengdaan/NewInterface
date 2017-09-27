__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import hashlib

def api_signs(payload,api_secret):
   # print type(payload)
    api_sign=[]
    for (key,value) in payload.items():
        api_sign.append( key +str(value))
    #print api_sign
    api_sign.sort()#获取所有键值对，并升序排列
   # print  api_sign
    api_signs = "".join(api_sign)
   # print '获取HTTP请求的所有键值对，并升序排列 :'  + api_signs #获取HTTP请求的所有键值对，并升序排列
   # api_secret='RjdQPmDvyaysmolFPG3hpFa2UrMmCKVG'#这个参数在mall_app
    pj=api_secret+api_signs+api_secret
   # print '字符串拼接：       '+ pj
   #拼接后字符串反转义
    pj = pj.replace("\\n", "\n")
    pj = pj.replace("\\r", "\n")
    pj = pj.replace("\\", "")

    #print'拼接后字符串反转 :'+ pj
    md5jm= hashlib.new("md5", pj).hexdigest()
    #m=hashlib.md5(pj.encode(encoding='utf-8'))#python3 写法
    #md5jm=m.hexdigest()



    #print (md5jm)
   # print md5jm.upper()#然后把加密内容转换为大写
    return md5jm.upper()
    #return md5jm



























def DPapi_signs(payload):

    api_sign=[]
    for (key,value) in payload.items():
        api_sign.append( key +str(value))
    #print api_sign
    api_sign.sort()#获取所有键值对，并升序排列
  #  print  api_sign
    api_signs = "".join(api_sign)
   # print '获取HTTP请求的所有键值对，并升序排列 :'  + api_signs #获取HTTP请求的所有键值对，并升序排列
    api_secret='4a5c4b33f83f6a41efed0f36d01e407e'#这个参数在mall_app
    pj=api_secret+api_signs+api_secret
   # print '字符串拼接：       '+ pj
   #拼接后字符串反转义
    pj = pj.replace("\\n", "\n")
    pj = pj.replace("\\r", "\n")
    pj = pj.replace("\\", "")

   # print'拼接后字符串反转 :'+ pj
    md5jm= hashlib.new("md5", pj).hexdigest()
    #print md5jm
   # print md5jm.upper()#然后把加密内容转换为大写
    return md5jm.upper()



