# Django-mysite

这是采用django实现的网页可视化项目。  
采用echarts为主要展示途径。

## git 传输命令
```   echo "# django-mysite" >> README.md  
# 初次推送
git init  
git add README.md  
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:na-na-mi/django-mysite.git
git push -u origin main   
```

## 在tool包中进行数据分析挖掘
关联规则分析子类别：`Association Rule Mining`   
在slave中实现了关联规则的导出，导出内容为 `/mysite/static/data/rules.csv `    
在RFMmodel中导出了RFM的数值，导出内容为`/mysite/static/data/rfm_data.json `  
----------------
rfm通常是指：      
- Recency（最近购买时间）：表示客户最近一次购买产品或服务的时间。较短的最近购买时间通常表示客户更有可能再次购买。
- Frequency（购买频率）：表示客户在一段时间内购买产品或服务的频率。购买频率高的客户可能是忠实客户或高价值客户。
- Monetary Value（购买金额）：表示客户在一段时间内购买产品或服务的总金额。购买金额高的客户通常是高价值客户。

帕累托分析贡献分析：  
本质上就是二八定律，找出那百分之二十。