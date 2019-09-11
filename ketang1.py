 #!/usr/bin/python
# -*- coding: UTF-8 -*-

# 爬天猫笔记本价格
# from urllib import request
# from bs4 import BeautifulSoup

# response = request.urlopen('https://list.tmall.com/search_product.htm?cat=50024399')
# html = response.read()
# soup = BeautifulSoup(html, 'lxml')

# computerList = soup.find(id = 'J_ItemList').find_all("div", {"class" : "product item-1111 "})
# for co in computerList:
# 	wrap = co.select('.product-iWrap')[0]
# 	print("价格:" + wrap.select('.productPrice')[0].select('em')[0].get_text())



# 登陆注册 salites
# import sqlite3
# import hashlib

# 基本操作
# sa = "create table t_user (id integer primary key autoincrement, name varchar(255), username varchar(255), password varchar(255))"
# cursor.execute(sa)
# sql = "insert into t_user (name, username, password) values ('lijunjie' , 'LiJunjie', '123456')"
# cursor.execute(sql)
# print(cursor.rowcount)
# cursor.execute("select password from t_user where name='lijunjie'")
# values = cursor.fetchall()[0][0]
# cursor.close()
# connection.commit()
# connection.close()
# print(values)

# 注册
# def register(name, username, password):
# 	connection = sqlite3.connect('test.db')
# 	cursor = connection.cursor()
# 	user = cursor.execute('select * from t_user where name = ?',(name,))
# 	if len(user.fetchall())>0:
# 		cursor.close()
# 		connection.close()
# 		return '已注册'
# 	else:
# 		md5 = hashlib.md5()
# 		md5.update(password.encode("utf8"))
# 		password = md5.hexdigest()
# 		sql = "insert into t_user (name, username, password) values (?,?,?)"
# 		cursor.execute(sql, (name, username, password))
# 		cursor.close()
# 		connection.commit()
# 		connection.close()
# 		return '注册成功'

# 登陆
# def login(name, password):
# 	connection = sqlite3.connect('test.db')
# 	cursor = connection.cursor()
# 	cursor.execute("select password from t_user where name = ?", (name,))
# 	values = cursor.fetchall()[0][0]
# 	if hashlib.md5(password.encode("utf8")).hexdigest() == values:
# 		cursor.close()
# 		connection.close()
# 		return "登录"
# 	else:
# 		cursor.close()
# 		connection.close()
# 		return "错误"
# print(register('lijunjie1', 'lijunjie1', '12345'))
# print(login('lijunjie1', '12345'))



# 存储数据到mysql
import os
import pymysql

connection = pymysql.connect(host = 'localhost', port=3306, user='root', passwd='0509gudu', db='homework', charset='utf8')
cursor = connection.cursor()
sql = "insert into t_user (name, username, password) values ('李俊杰' , 'lijunjie' , '123456')"
cursor.execute(sql)
connection.commit()	
sq = 'select * from t_user where id = %d'
cursor.execute(sq % (1,))
connection.close()
values = cursor.fetchall()
print(values)

# 获取时间测试
# import datetime
# print(datetime.datetime.now())