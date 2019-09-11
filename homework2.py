#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 李俊杰 2018.10.25

# 爬天猫笔记本价格
from urllib import request
from bs4 import BeautifulSoup
import datetime
import os
import pymysql

def creatmysql(productTitle, productPrice, productShop, productStatus, policy, dateTime):
	connection = pymysql.connect(host = 'localhost', port=3306, user='root', passwd='0509gudu', db='homework', charset='utf8')
	cursor = connection.cursor()
	sql = "select * from computers where productTitle = %s AND productPrice = %s AND productShop = %s"
	cursor.execute(sql, (productTitle, productPrice, productShop,))
	if len(cursor.fetchall())>0:
		sql = "update computers set dateTime = %s where productTitle = %s AND productPrice = %s AND productShop = %s"
		cursor.execute(sql, (dateTime, productTitle, productPrice, productShop))
	else:
		sql = "insert into computers (productTitle, productPrice, productShop, productStatus, policy, dateTime) values (%s,%s,%s,%s,%s,%s)"
		cursor.execute(sql, (productTitle, productPrice, productShop, productStatus, policy, dateTime))
	cursor.close()
	connection.commit()	
	connection.close()

def spider():
	response = request.urlopen('https://list.tmall.com/search_product.htm?cat=50024399')
	html = response.read()
	soup = BeautifulSoup(html, 'lxml')

	computerList = soup.find(id = 'J_ItemList').find_all("div", {"class" : "product item-1111 "})
	for co in computerList:
		wrap = co.select('.product-iWrap')[0]
		productPrice = wrap.select('.productPrice')[0].select('em')[0].get_text()
		policy = wrap.find('p', {'class' : 'icon-srp-1111'}).get_text()
		productShop = wrap.select('div.productShop > a')[0].string
		productStatus = wrap.find('p', {'class' : 'productStatus'})
		if productStatus:
			productStatus = productStatus.find('span').get_text()
		productTitle = ""
		for a in wrap.find('div', {'class' : 'productTitle'}).find_all('a'):
			productTitle += a.string
		dateTime = datetime.datetime.now()
		creatmysql(productTitle.replace('\n', '').replace(' ', ''), productPrice, productShop.replace('\n', ''), str(productStatus), str(policy), dateTime)
spider()
