#!/usr/bin/python3
 
import pymysql
from datetime import datetime, time, timedelta
# 打开数据库连接
db = pymysql.connect("localhost","root","1234qwer","qsnark" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)

# SQL查询语句
# sql = "SELECT * FROM application WHERE create_time > DATE_ADD('2018-09-07 14:01:45', INTERVAL 1 HOUR)"
sql = "SELECT max(create_time) FROM application"
# sql = "SELECT * FROM application WHERE create_time > DATE_ADD('2018-09-07 14:01:45', INTERVAL '%d' DAY)"%(2)
# sql = "SELECT COUNT(*) FROM application WHERE create_time > '2018-11-07 14:01:45'"
# sql = "SELECT COUNT(*) FROM application"``

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchone()
    # max = datetime.combine(results[0], time.max)
    print('输出：{}'.format(results[0] + timedelta(days=1)))
    # for row in results:
    #     print('输出：{}'.format(row))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close() 