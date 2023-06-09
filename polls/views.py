import json

from django.shortcuts import render
from pyecharts import options as opts
from pyecharts.charts import Graph

def test(request):
    return render(request, "test.html")

# def product_recommendation(request):

def index(request):
    return render(request, "index.html")

def visualize_rules(request):
    # 获取关联规则数据（假设数据存储在 rules 变量中）
    with open('./static/data/rules.json', 'r') as file:
        rules_data = json.load(file)

    # 提取规则数据中的关联规则
    rules = rules_data['associations']
    # 构建节点和边的数据
    nodes = []  # 节点列表
    links = []  # 边列表

    # 根据关联规则构建节点和边
    for rule in rules:
        # 添加节点
        nodes.append({"name": rule.antecedents})  # 添加前项节点
        nodes.append({"name": rule.consequents})  # 添加后项节点

        # 添加边
        links.append({"source": rule.antecedents, "target": rule.consequents})  # 添加边连接前项和后项

    # 创建关系图
    graph = (
        Graph()
        .add("", nodes, links, repulsion=8000)
        .set_global_opts(title_opts=opts.TitleOpts(title="关联规则关系图"))
    )

    # 渲染图表并将图表保存为 HTML 文件
    graph.render("graph.html")

    # 将图表文件名传递给模板进行渲染
    return render(request, "visualize.html", {"graph_file": "graph.html"})