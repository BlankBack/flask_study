
#运用模板时，需要导入render_templates
from flask import Flask, render_template

app =Flask(__name__)

# 1. 如何返回一个网页(模板)
# 2. 如何规模版填充数据
@app.route('/')
def index():

    # 比如需要传入一个网址

    url_str = 'www.heima.com'

    # 列表
    my_list = [1, 3, 5, 7, 9]

    # 字典

    my_dict ={
        'name': '程序猿',
        'url': 'www.itheima.com'
    }

    my_int = 38

    # 通常， 模板中使用的变量名要和传递的数据的变量名保持一致
    return render_template('index.html',
                           url_str=url_str,
                           my_list=my_list,
                           my_dict=my_dict,
                           my_int=my_int
                           )

if __name__ == '__main__':
    app.run()