# import pandas as pd
# import sqlite3
#
# # 连接到SQLite数据库
# conn = sqlite3.connect('../db.sqlite3')
#
# # 执行SQL查询并将结果加载到DataFrame中
# query = 'SELECT * FROM polls_salesdata'
# df = pd.read_sql(query, conn)
#
# # 关闭数据库连接
# conn.close()
#
# # 打印DataFrame的内容
# print(df)

import pymysql

# 连接到 MySQL 数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='djangodb',
    cursorclass=pymysql.cursors.DictCursor
)

# 创建游标对象
cursor = conn.cursor()

# 执行查询语句
query = "SELECT * FROM salesdata"
cursor.execute(query)

# 获取查询结果
results = cursor.fetchall()

# 输出查询结果
for row in results:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()

