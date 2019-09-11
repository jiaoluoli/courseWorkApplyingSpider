 #!/usr/bin/python
# -*- coding: UTF-8 -*-

#通过salalchemy模块连接数据库
import os
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import hashlib

Base = declarative_base()

class User(Base):
	__tablename__ = 't_user_1'
	id = Column(Integer, primary_key = True)
	name = Column(String(255))
	password = Column(String(255))
engine = create_engine('mysql+pymysql://root:0509gudu@localhost:3306/stu?charset=utf8')
# 创建表格
Base.metadata.create_all(engine)
# 插入数据
# DBSession = sessionmaker(bind = engine)
# session = DBSession()
# user = User(id = 2, name = '李俊杰')
# session.add(user)
# session.commit()
# session.close()

# 注册
def register(name, password):
	DBSession = sessionmaker(bind = engine)
	session = DBSession()
	usercount = session.query(User).filter(User.name == name).count()
	if usercount > 0:
		return '已注册'
	else:
		md5 = hashlib.md5()
		md5.update(password.encode("utf8"))
		password = md5.hexdigest()
		user = User(name = name, password = password)
		session.add(user)
		session.commit()
		return '注册成功'
	session.close()

# 登陆
def login(name, password):
	DBSession = sessionmaker(bind = engine)
	session = DBSession()
	user = session.query(User).filter(User.name == name).one()
	if hashlib.md5(password.encode("utf8")).hexdigest() == user.password:
		return "登录成功"
	else:
		return "登陆错误"
	session.close()

# print(register("lijunjie", "12345"))
print(login("lijunjie", "12345"))