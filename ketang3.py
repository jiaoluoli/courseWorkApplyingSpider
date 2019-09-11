#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 用wsgi开启监听
# import os
# from wsgiref.simple_server import make_server

# def application(environ, start_response):
# 	start_response('200 OK', [('Content-Type', 'text/html')])
# 	body = '<h1>Hello,%s</h1>'  % (environ['PATH_INFO'][1:] or 'web')
# 	return [body.encode('utf-8')]

# httpd = make_server('localhost', 8000, application)
# print('Serving')
# httpd.serve_forever()

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world'

# 通过<name>传递参数
# @app.route('/post/<name>')
# @app.route('/post/')
# def show_post(name = None):
# 	return render_template('templates/ketang3.html', name = name)
@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('uname')
		password = request.form.get('pword')
		return 'post method, uname is %s and pword is %s' % (username, password)
	else:
		return render_template('ketang3.html')
app.run(debug = True)
