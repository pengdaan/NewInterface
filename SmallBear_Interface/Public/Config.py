# -*- coding: utf-8 -*-
"""
#
# Authors: limanman
# OsChina: http://my.oschina.net/pydevops/
# Purpose:
#
"""

MysqlConfig = {
    'port': 3306,
    # 启动时连接池中创建的的连接数
    'mincached': 5,
    # 连接池中最大允许创建的连接数
    'maxcached': 20,
    'user': 'testxiaoshuxiong',
    'charset': 'utf8',
    'db': 'mama_mall',
    # 所有允许的最大连接数上限设置
    'maxconnections': 5,
    'passwd': '9bo0388lAxA4XsCY',
    'host': '10.0.0.100'
}

MysqlConfigPay = {
    'port': 3306,
    # 启动时连接池中创建的的连接数
    'mincached': 5,
    # 连接池中最大允许创建的连接数
    'maxcached': 20,
    'user': 'testxiaoshuxiong',
    'charset': 'utf8',
    'db': 'mama_pay',
    # 所有允许的最大连接数上限设置
    'maxconnections': 5,
    'passwd': '9bo0388lAxA4XsCY',
    'host': '10.0.0.100'
}

SupplierConfig = {
    'port': 3306,
    # 启动时连接池中创建的的连接数
    'mincached': 5,
    # 连接池中最大允许创建的连接数
    'maxcached': 20,
    'user': 'testxiaoshuxiong',
    'charset': 'utf8',
    'db': 'supplier',
    # 所有允许的最大连接数上限设置
    'maxconnections': 5,
    'passwd':'9bo0388lAxA4XsCY',
    'host':'10.0.0.100'
}

if __name__ == '__main__':
    print ('Found Errors: the module can only be imported, not run!')