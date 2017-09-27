# -*- coding: utf-8 -*-
__author__ = 'leo'
import pymysql
from Public.Config import *
class Mysql(object):
    __db=None
    def __init__(self):
        # 创建数据库连接方法
        self.__connect()

    def __del__(self):
        if(self.__db is not None):
            self.__db.close()

    def __connect(self):
        if (self.__db == None):
            self.__db = pymysql.connect(
                db=MysqlConfig['db'],
                host=MysqlConfig['host'],
                port=MysqlConfig['port'],
                user=MysqlConfig['user'],
                passwd=MysqlConfig['passwd'],
                charset=MysqlConfig['charset'],
            )

        return self.__db

    def query(self,_sql):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.__connect().cursor()
        try:
            # 使用 execute()方法执行SQL
            cursor.execute(_sql)
            # 接收全部的返回结果行
            data = cursor.fetchall()
            # 提交到数据库执行
            self.__connect().commit()
        except:
            # 如果发生错误则回滚
            self.__connect().rollback()
            return False
        #print(data[0][0])
        return data[0][0]




    def select(self,data='',table='',where='',limit='',order='',group=''):
        """
        查询sql语句

        data - 查询的字段，默认 * 或 id,name,email,...
        table - 表名
        where - 查询条件语句
        limit - 结果范围
        order - 排序

        Returns Lists.
        """

        sql = self._sql_contact(data,table,where,limit,order,group)
        result = self._sql_query(data,sql)
        return result

    def get_one(self,data='',table='',where='',order=''):
        """
        获取单行记录

        data - 查询的字段，默认 * 或 id,name,email,...
        table - 表名
        where - 查询条件语句
        order - 排序

        Returns Sets or None.
        """
        sql = self._sql_contact(data,table,where,'1',order)
        result = self._sql_query(data,sql)
        return result[0] if result else None

    def insert(self,data,table):
        """
        新增一条数据

        data - 数据集合 {field:value...}
        table - 表名

        Returns insert_id
        """
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.__connect().cursor()
        fields = ','.join(data.keys())
        inputs = ','.join(("%s", ) * len(data))
        values = tuple(data.values())
        sql = "INSERT INTO %s (%s) VALUES ("%(table, fields) + inputs + ")"
        cursor.execute(sql,values)
        insert_id = cursor.lastrowid
        self.__connect().commit()
        return insert_id

    def insert_many(self,data,table):
        """
        新增多条数据

        data - 数据列表 [{field:value...}...]
        table - 表名

        Returns rowcount 影响到行数
        """
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.__connect().cursor()
        fields = ','.join(data[0].keys())
        inputs = ','.join(("%s", ) * len(data[0]))
        values = []
        [values.append(tuple(item.values())) for item in data]

        sql = "INSERT INTO %s (%s) VALUES ("%(table, fields) + inputs + ")"
        cursor.executemany(sql,values)
        insert_id = cursor.lastrowid
        self.__connect().commit()
        return cursor.rowcount

    def update(self,data,table,where):
        """
        修改数据

        data - 数据集合 {field:value...}
        table - 表名
        where - 条件

        Returns rowcount 影响到行数
        """
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.__connect().cursor()
        fields = (",".join(map(lambda k: k+"=%s", data.keys())))
        values = tuple(data.values())
        sql = "UPDATE %s SET "%table + fields + " WHERE " + where
        cursor.execute(sql,values)
        self.__connect().commit()
        return cursor.rowcount

    def delete(self,table,where):
        """
        删除数据

        table - 表名
        where - 条件

        Returns rowcount 影响到行数
        """
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.__connect().cursor()
        where = ' WHERE '+where if where else ''
        sql = 'DELETE FROM ' + table + where
        cursor.execute(sql)
        self.__connect().commit()
        return cursor.rowcount


    def close(self):
        """关闭游标和数据库连接"""
        cursor = self.__connect().cursor()
        cursor.close()
        self.__db.close()

    def _sql_contact(self,data='',table='',where='',limit='',order='',group=''):
        """构造和拼接sql语句"""
        where = ' WHERE '+where if where else ''
        limit = ' LIMIT '+limit if limit else ''
        order = ' ORDER BY '+order if order else ''
        group = ' GROUP BY '+group if group else ''
        data = data if data else '*'
        sql = 'SELECT '+data+' FROM ' + table + where + group + order +limit
        return sql

    def _sql_query(self,data,sql):
        """执行sql并返回结果集"""
        cursor = self.__connect().cursor()
        #print(sql)
        cursor.execute(sql)
        result = []
        column_names = cursor.column_names if data=='*' else tuple(data.split(','))
        [result.append(dict(zip(column_names,item))) for item in cursor]
        #print(result)
        return result


if __name__ == '__main__':
    test=Mysql()
    test.query(_sql="SELECT attr_id FROM mall_attribute WHERE attr_name='规格'")
    Code=test.select(data='attr_id',table='mall_attribute',where="attr_name='规格'")
    print(Code[0].get('attr_id'))
    api_key='9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o'
    api_secret = test.select(data='api_secret',table='mall_app',where="api_key='%s'"%api_key)

