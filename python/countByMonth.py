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
        min = results[0].replace(day=1).date()
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
        max = add_months(results[0].date(), 1).replace(day=1)
        return max
    except:
        print("Error: unable to fetch data")

# 增加月份
def add_months(dt, months):
    month = dt.month - 1 + months
    year = dt.year + int(month / 12)
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)

def countUserByMonth():
    max = getMax('user')
    min = getMin('user')
    gap = (max.year - min.year)*12 + (max.month - min.month)
    data={} #数据

    for i in range(gap):
        sql = "SELECT * FROM user WHERE register_time >= '%s' AND register_time < '%s'"%(add_months(min, i), add_months(min, i+1))
        cursor.execute(sql)
        results = cursor.rowcount
        data[add_months(min, i).strftime("%Y-%m")] = results        

    with open("./UserByMonth.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

def countApplicationByMonth():
    max = getMax('application')
    min = getMin('application')
    gap = (max.year - min.year)*12 + (max.month - min.month)
    data={} #数据

    for i in range(gap):
        sql = "SELECT * FROM application WHERE create_time >= '%s' AND create_time < '%s'"%(add_months(min, i), add_months(min, i+1))
        cursor.execute(sql)
        results = cursor.rowcount
        data[add_months(min, i).strftime("%Y-%m")] = results        

    with open("./ApplicationByMonth.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

def countContractByMonth():
    max = getMax('contract')
    min = getMin('contract')
    gap = (max.year - min.year)*12 + (max.month - min.month)
    data={} #数据

    for i in range(gap):
        sql = "SELECT * FROM contract WHERE create_time >= '%s' AND create_time < '%s'"%(add_months(min, i), add_months(min, i+1))
        cursor.execute(sql)
        results = cursor.rowcount
        data[add_months(min, i).strftime("%Y-%m")] = results        

    with open("./ContractByMonth.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

def countTransactionByMonth():
    max = getMax('transaction')
    min = getMin('transaction')
    gap = (max.year - min.year)*12 + (max.month - min.month)
    data={} #数据

    for i in range(gap):
        sql = "SELECT * FROM transaction WHERE create_time >= '%s' AND create_time < '%s'"%(add_months(min, i), add_months(min, i+1))
        cursor.execute(sql)
        results = cursor.rowcount
        data[add_months(min, i).strftime("%Y-%m")] = results        

    with open("./TransactionByMonth.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

countUserByMonth()
countApplicationByMonth()
countContractByMonth()
countTransactionByMonth()
