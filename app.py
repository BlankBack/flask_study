# 1. 导入flask扩展
from flask import Flask

# 2. 创建Flask应用程序实例
# 需要传入__name__,作用是为了确定资源所在的路径
app = Flask(__name__)

# 3. 定义路由及视图函数
# flask中定义路由是通过装饰器来实现的
# 路由默认只支持GET，如果需要增加，需要自行指定
@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello Flask!'

# 使用同一个视图函数 来显示不同用户的订单信息
# <> 来定义路由的参数，<> 需要起一个名字
# 使用 int/float 来限定输入的类型，其他类型如何实现百度
@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
    # 需要再视图函数括号内填入参数名，那么后面的代码才能够使用
    return 'order_id %s' % order_id

# 4. 启动程序
if __name__ == '__main__':
    # 执行了app.run(),就会将Flask程序运行在一个简易的服务器（Flask提供的，用于测试的）
    app.run()
