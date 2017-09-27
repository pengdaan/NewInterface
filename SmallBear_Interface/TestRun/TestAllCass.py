# -*- coding:utf-8 -*-

'''
Created on 2017年7月29日
@author: leo
'''

#导入测试用例
from Test_Case.TestCase_Dp import *

def Test_01DpOrderCass():
    print('开始测试')
    now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    print(now)
    #添加需要测试测试用例
    test_Create_Order()
    test_applyRefund()
    test_cancelOrder()
    test_UpdateComment()
    test_OrderBySnDp()
    test_UserOrderListDP()
    print('结束测试')

    
# def Test_02PermissionCass():
#     print("开始测试")
#     now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
#     print(now)
#     TestCass.TestCassPermission_02.test_1add_permission()
#     TestCass.TestCassPermission_02.test_2del_permission()
#     TestCass.TestCassPermission_02.test_3find_permission()
#     TestCass.TestCassPermission_02.test_4exists_permission()
#     print('结束测试')
#
# def Test_03AdminroleCass():
#     print("开始测试")
#     now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
#     print(now)
#     TestCass.TestCassAdminrole_03.test_1relate_permissions()
#     TestCass.TestCassAdminrole_03.test_2get_permissions()
#     print("结束测试")



 

