import sqlite3
from django.shortcuts import render
import pandas as pd


class GetData:
    def index(self):
        # print(777)
        # 连接到数据库
        conn = sqlite3.connect('../db.sqlite3')

        # 执行SQL查询语句
        query = "SELECT * FROM main.polls_salesdata;"
        df = pd.read_sql_query(query, conn)
        conn.close()
        print(df)
        # 将查询结果传递给模板
        return render(self, 'index.html', {'results': df})


