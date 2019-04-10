
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/mysql_flask"
    #设置salalcchemy自动更新数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

# 导入
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象

db = SQLAlchemy(app)

class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'

    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 在一的一方，写关联
    # users = db.relationship("User", backref="role")表示和User模型发生了关联，增加了一个users属性
    # backref="role"：表示role是User要用的属性
    users = db.relationship("User", backref="role")

    # repr() 方法显示一个可读字符串
    def __repr__(self):
        return '<Role: %s %s>' % (self.name, self.id)



# 表名的常见规范
# ihome -> ih_user  数据库缩写_表名
# tbl_user  ->      tbl_表名

# 创建数据库模型类
class User(db.Model):
    __tablebame__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    # unique 表示数据是否唯一
    name = db.Column(db.String(10), unique=True)
    email = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(32))
    # ForeignKey 表示外键，使用时需要传参数：表名.id
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # User希望有role属性，但是这个属性的定义，需要在另一个模型中定义,见class Role

    # repr() 方法显示一个可读字符串
    def __repr__(self):
        return '<Role: %s %s %s %s>' % (self.name, self.id, self.email, self.password)

if __name__ =='__main__':

    db.drop_all()
    db.create_all()

    # 插入一条数据
    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()
    # 再次插入一条数据
    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123465', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@163.com', password='453783453', role_id=ro2.id)
    us3 = User(name='chen', email='chen@163.com', password='78634538', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='123786465', role_id=ro2.id)
    us5 = User(name='tang', email='tang@163.com', password='87645', role_id=ro1.id)
    us6 = User(name='wu', email='wu@163.com', password='1378786', role_id=ro1.id)
    us7 = User(name='qian', email='qian@163.com', password='974538', role_id=ro2.id)
    us8 = User(name='liu', email='liu@163.com', password='334578', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com', password='789546', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com', password='6428647', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()



