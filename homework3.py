#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 李俊杰 2018.11.25

# 爬天猫笔记本价格用ORM存储
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib import request
from bs4 import BeautifulSoup
import datetime
import os
import pymysql

Base = declarative_base()

class Computer(Base):
	__tablename__ = "computers1"
	id = Column(Integer, primary_key = True)
	productTitle = Column(String(255))
	productShop = Column(String(255))
	productPrice = Column(String(255))
	productStatus = Column(String(255))
	policy = Column(String(255))
	dateTime = Column(DateTime())
	
engine = create_engine('mysql+pymysql://root:0509gudu@localhost:3306/homework?charset=utf8')	
Base.metadata.create_all(engine)	
DBSession = sessionmaker(bind = engine)


def creatmysql(productTitle, productPrice, productShop, productStatus, policy, dateTime):
	session = DBSession()	
	count = session.query(Computer).filter_by(productTitle = productTitle, productPrice = productPrice, productShop = productShop).count()
	if count > 0:
		computer = session.query(Computer).filter_by(productTitle = productTitle, productPrice = productPrice, productShop = productShop).one()
		computer.dateTime = dateTime
		computer.policy = policy
		computer.productStatus = productStatus
	else:
		computer = Computer(productTitle = productTitle, productPrice = productPrice, productShop = productShop, productStatus = productStatus, policy = policy, dateTime = dateTime)
		session.add(computer)
		session.commit()
	session.close()
	

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