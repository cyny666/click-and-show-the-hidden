import csv
from jinja2 import Environment, FileSystemLoader
input_name = input("输入csv文件:")
title = []
answer = []
# 打开CSV文件
with open(input_name, 'r',encoding='gbk',errors="ignore") as csvfile:
    # 创建CSV读取器
    reader = csv.reader(csvfile)
    # 逐行读取CSV文件内容
    for row in reader:
        title.append(row[0])
        answer.append(row[1].replace("\n",""))

# 创建Jinja2环境
env = Environment(loader=FileSystemLoader('.'))

# 渲染HTML模板
template = env.get_template('template.html')
output = template.render(title=title,answer=answer,n=range(1,answer.__len__()))
output_html = input_name.replace(".csv",".html")
# 将生成的HTML写入文件
with open(output_html, 'w') as file:
    file.write(output)

print("HTML文件已生成。")