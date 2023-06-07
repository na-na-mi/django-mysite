import pandas as pd
from datetime import datetime

data = pd.read_csv(r"../static/data/导入订单utf8.csv", encoding='utf-8')
data['订单日期'] = pd.to_datetime(data['订单日期'])

today = datetime.now().date()
data['Recency'] = today - data['订单日期'].dt.date

rfm_data = data.groupby('客户名称').agg({'Recency': 'min', '数量': 'sum', '销售额': 'sum'})

rfm_data['R'] = pd.qcut(rfm_data['Recency'], 5, labels=False)
rfm_data['F'] = pd.qcut(rfm_data['数量'], 5, labels=False)
rfm_data['M'] = pd.qcut(rfm_data['销售额'], 5, labels=False)

rfm_data['RFM'] = rfm_data['R'].astype(str) + rfm_data['F'].astype(str) + rfm_data['M'].astype(str)

print(rfm_data['RFM'])
rfm_data.reset_index(inplace=True)
# 写入csv文件
columns = ['客户名称', 'Recency', '数量', '销售额', 'R', 'F', 'M', 'RFM']
rfm_data = rfm_data[columns]

# rfm_data.to_csv('../static/data/RFM.csv', index=False)
rfm_data.to_json('../static/data/rfm_data.json', orient='records', force_ascii=False)

# rfm_data.to_csv("../static/data/RFM.csv", index=False)
