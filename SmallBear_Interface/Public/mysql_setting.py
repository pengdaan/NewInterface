# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import pymysql.cursors
import time
host="localhost"
user="root"
password=""
db="test_db"

class MySQLOperating():
    def __init__(self):
        try:
            self.connection=pymysql.connect(host=host,
                                            user=user,
                                            password=password,
                                            db=db,
                                            charset="utf8mb4",
                                            cursorclass=pymysql.cursors.DictCursor
                                            )
        except pymysql.err.OperationalError as e:
            print ('Mysql Error %d:$s'%(e.args[0],e.args[1]))



# clear table data
    def clear(self,table_name):
        real_sql="delete from "+table_name+";"
        with self.connection.cursor()as cursor:
           #cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
           cursor.execute(real_sql)
        self.connection.commit()


#insert test data
    def insert(self,table_name,data):
        for key in data:
            data[key]="'"+str(data[key])+"'"
        key=','.join(data.keys())
        value=','.join(data.values())
        # real_sql1="select COLUMN_NAME from information_schema.COLUMNS where table_name =" +table_name+";"#获取表列字段
        real_sql="INSERT INTO "+table_name+"("+key+")VALUE("+value+")"

        with self.connection.cursor()as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    def close(self):
            self.connection.close()

if __name__=='__main__':
    times= int(time.time())  #获取当前时间戳
    db=MySQLOperating()
    table_name="orderdp"
    data={
        'api_key':'8d46b75a4a0456a35302d2893ed072a3',
        'uid':'43507844',
        'consignee':'么么22',
        'mobile':'13728142737',
        'shop_id':'123456',
        'products':'[{"product_id":10749,"number":1}]',
        'timestamp':times,

    }
    #data={'id':'2','question_test':'66666'}
    #db.clear(table_name)
    db.insert(table_name,data)
    db.close()


#这个方法类是处理测试用例数据的：之前的想法是，建立一个测试用例数据库，然后把数据存在里面，
#后面我发现好像没什么用，用例数据代码已经有了，我写死了。暂时弃用了