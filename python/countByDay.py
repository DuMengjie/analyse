import calendar
import json
from datetime import datetime, time, timedelta
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "1234qwer", "qsnark" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 获取最小日期
def getMin(scheme_name):
    if scheme_name == 'user':
        sqlMin = "SELECT min(register_time) FROM %s"%(scheme_name)
    else:
        sqlMin = "SELECT min(create_time) FROM %s"%(scheme_name)
        
    try:
        cursor.execute(sqlMin)
        results = cursor.fetchone()
        min = datetime.combine(results[0], time.min)
        # print('输出：{}'.format(min))
        return min
    except:
        print("Error: unable to fetch data")

# 获取最大日期
def getMax(scheme_name):
    if scheme_name == 'user':
        sqlMax = "SELECT max(register_time) FROM %s"%(scheme_name)
    else:
        sqlMax = "SELECT max(create_time) FROM %s"%(scheme_name)
    try:
        cursor.execute(sqlMax)
        results = cursor.fetchone()
        max = datetime.combine(results[0], time.max)
        # print('输出：{}'.format(max))
        return max
    except:
        print("Error: unable to fetch data")

# 增加天数
def add_days(dt, days):
    return dt + timedelta(days=days)

def countUserByDay():
    max = getMax('user')
    min = getMin('user')
    gap = (max.date() - min.date()).days
    data={} #数据

    for i in range(gap+1):
        sql = "SELECT * FROM user WHERE register_time >= '%s' AND register_time < '%s'"%(add_days(min, i), add_days(min, i+1))
        cursor.execute(sql)
        results = cursor.rowcount
        data[add_days(min, i).strftime("%Y-%m-%d")] = results        

    with open("./UserByDay.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

def countApplicationByDay():
    max = getMax('application')
    min = getMin('application')
    gap = (max.date() - min.date()).days
    data={} #数据

    for i in range(gap+1):
        sql = "SELECT * FROM application WHERE create_time >= '%s' AND create_time < '%s'"%(add_days(min, i), add_days(min, i+1))
        cursor.execute(sql)
        results = cursor.rowcount
        data[add_days(min, i).strftime("%Y-%m-%d")] = results        

    with open("./ApplicationByDay.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

def countContractByDay():
    max = getMax('contract')
    min = getMin('contract')
    gap = (max.date() - min.date()).days
    data={} #数据

    for i in range(gap+1):
        sql = "SELECT * FROM contract WHERE create_time >= '%s' AND create_time < '%s'"%(add_days(min, i), add_days(min, i+1))
        cursor.execute(sql)
        results = cursor.rowcount
        data[add_days(min, i).strftime("%Y-%m-%d")] = results        

    with open("./ContractByDay.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

def countTransactionByDay():
    max = getMax('transaction')
    min = getMin('transaction')
    gap = (max.date() - min.date()).days
    data={} #数据

    for i in range(gap+1):
        sql = "SELECT * FROM transaction WHERE create_time >= '%s' AND create_time < '%s'"%(add_days(min, i), add_days(min, i+1))
        cursor.execute(sql)
        results = cursor.rowcount
        data[add_days(min, i).strftime("%Y-%m-%d")] = results        

    with open("./TransactionByDay.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

countUserByDay()
# countApplicationByDay()
# countContractByDay()
# countTransactionByDay()
