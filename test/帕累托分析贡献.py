"""
计算总销售额和每个客户的销售额占比：计算所有客户的销售额总和，并计算每个客户的销售额占比。
对客户销售额进行排序：对客户销售额占比进行排序，从高到低排列。
计算累计百分比：计算每个客户的累计百分比。
筛选符合帕累托法则的客户：根据阈值筛选出符合帕累托法则的客户。
"""

import pandas as pd
data = pd.read_csv(r"../static/data/导入订单utf8.csv", encoding='utf-8')
sales_data = data['销售额']
total_sales = sales_data.sum()
customer_sales_percentage = (sales_data / total_sales) * 100
sorted_customers = customer_sales_percentage.sort_values(ascending=False)
cumulative_percentage = sorted_customers.cumsum()

threshold = 80  # 设置阈值
selected_customers = sorted_customers[cumulative_percentage <= threshold]
# print(selected_customers)
#
# selected_customer_names = data.loc[selected_customers.index, '客户名称']
# print(selected_customer_names)
selected_customer_data = data.loc[selected_customers.index, ['客户名称', '销售额']]
selected_customer_data['销售额占比'] = customer_sales_percentage.loc[selected_customers.index]

print(selected_customer_data)

# 将数据转换为 JSON 格式
json_data = selected_customer_data.to_json(orient='records')

# 指定保存的文件路径和文件名
output_file = '../static/data/ParetoAnalysis.json'

# 将数据写入 JSON 文件
with open(output_file, 'w') as file:
    file.write(json_data)

print("数据已成功写入 JSON 文件：", output_file)
