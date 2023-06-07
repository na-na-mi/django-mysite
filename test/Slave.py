import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data = pd.read_csv(r"../static/data/导入订单utf8.csv", encoding='utf-8')
son_Series = data['子类别'].value_counts()
# print("一共有{}种类别".format(son_Series))
pivot_table = data.pivot_table(index=['客户名称'], columns=['子类别'], aggfunc='size', fill_value=0)
print(pivot_table)

# 将透视表中的计数值转换为布尔值
binary_table = pivot_table.applymap(lambda x: 1 if x > 0 else 0)

# 使用 Apriori 算法找到频繁项集
frequent_itemsets = apriori(binary_table, min_support=0.1, use_colnames=True)

# 基于频繁项集生成关联规则
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

print(rules)
# 将关联规则写入 CSV 文件
rules.to_csv("../static/data/rules.csv", index=False)




