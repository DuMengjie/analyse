 # 根据创建合约数统计用户、根据调用合约次数统计用户、根据被调用次数统计合约
 # rank.py
import calendar
import json
from datetime import datetime, time, timedelta
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "1234qwer", "qsnark" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 用户调用合约次数
def countUserByCall():
    dataID={} #数据
    dataName={}

    sql = "SELECT user_id FROM transaction"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        if dataID.__contains__(str(row[0])):
            dataID[str(row[0])] += 1
        else:
            dataID[str(row[0])] = 1

    for key in dataID:
      sql = "SELECT user_name FROM user WHERE id = %d"%(int(key))
      cursor.execute(sql)
      result = cursor.fetchone()
      dataName[result[0]] = dataID[key]

    with open("./UserCall.json", 'w', encoding='utf-8') as json_file:
        json.dump(dataName, json_file, ensure_ascii=False)

# 用户创建合约数量
def countUserByCreate():
    dataApp={}
    dataID={} 
    dataName={}

    sql = "SELECT application_id FROM contract"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        if dataApp.__contains__(str(row[0])):
            dataApp[str(row[0])] += 1
        else:
            dataApp[str(row[0])] = 1

    for key in dataApp:
      sql = "SELECT user_id FROM application WHERE id = %d"%(int(key))
      cursor.execute(sql)
      result = cursor.fetchone()
      if dataID.__contains__(str(result[0])):
          dataID[str(result[0])] += dataApp[key]
      else:
          dataID[str(result[0])] = dataApp[key]

    for key in dataID:
      sql = "SELECT user_name FROM user WHERE id = %d"%(int(key))
      cursor.execute(sql)
      result = cursor.fetchone()
      dataName[result[0]] = dataID[key]

    with open("./UserCreate.json", 'w', encoding='utf-8') as json_file:
        json.dump(dataName, json_file, ensure_ascii=False)
  
# 合约被调用次数
def countContractByCall():
    dataID={} #数据
    dataName={}

    sql = "SELECT to FROM transaction"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        if row[0][0:4] == '0000':
            continue
        else:
            if dataID.__contains__(row[0]):
                dataID[row[0]] += 1
            else:
                dataID[row[0]] = 1

    for key in dataID:
      sql = "SELECT name, id FROM contract WHERE address = '%s'"%('0x'+key)
      cursor.execute(sql)
      result = cursor.fetchone()
      if result is None:
          continue
      else:
          dataName[result[0]+'-'+str(result[1])] = dataID[key]
    
    with open("./ContractCall.json", 'w', encoding='utf-8') as json_file:
        json.dump(dataName, json_file, ensure_ascii=False)
    
countUserByCreate()