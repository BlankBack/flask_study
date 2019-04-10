
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app =Flask(__name__)

# 用来做加密混淆
app.secret_key = 'itheima'
"""
目的：实现一个简单的登录的逻辑处理
1. 路有需要有get和post两种请求方式 --> 需要判断请求方式
2. 获取请求的参数
3. 判断参数是否填写 & 密码是否相同
4. 如果判断都没有问题，就返回一个success
"""

"""
给模板传递消息用 flash ————>需要对内容加密，因此需要设置 secret_key，做加密消息的混淆
但是
在模板（index.html）中需要去遍历消息
"""

"""
使用WTF实现表单
自定义一个表单类
"""

class LoginForm(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired()])
    password = PasswordField('密码:', validators=[DataRequired()])
    password2 = PasswordField('确认密码',validators=[DataRequired(), EqualTo('password', '密码填入的不一致')])
    submit = SubmitField('提交')

@app.route('/form', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    # 1. 判断请求方式
    if request.method == 'POST':
        # 2. 获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 3. 判断参数是否填写 & 密码是否相同，WTF可以一句话实现所有的校验
        if login_form.validate_on_submit():
            print(username, password)
            return 'success'
        else:
            flash('参数有误')



    return render_template('index_WTF.html', form=login_form )


@app.route('/', methods=['GET', 'POST'])
def index():
    # request 是请求对象 --> 获取请求方式、数据

    # 1. 判断请求方式
    if request.method == 'POST':

        # 2. 获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 3. 判断参数是否填写 & 密码是否相同
        if not all([username, password, password2]):
            # print('参数不完整')
            flash('参数不完整')

        elif password !=password2:
            # print('密码不一致')
            flash('密码不一致')
        else:
            return 'success'

    return render_template('index_WTF.html')





if __name__ == '__main__':
    app.run(debug=True)