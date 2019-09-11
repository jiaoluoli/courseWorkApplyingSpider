 #!/usr/bin/python
# -*- coding: UTF-8 -*-
# 李俊杰 2018/10/18

from urllib import request
from bs4 import BeautifulSoup

# 获取微人大登录页面中class为itemdesc-2的第二个div标签中的p标签的文本内容
response1 = request.urlopen("https://v.ruc.edu.cn")
html1 = response1.read()
soup1 = BeautifulSoup(html1, 'lxml')
text = soup1.select('div.itemdesc')[1].select('p')[0].get_text()
print(text)



# 获取豆瓣电影的《纯洁心灵·逐梦演艺圈》电影名，评分，导演，编剧，主演等信息，并依次输出
response2 = request.urlopen("https://movie.douban.com/subject/26322774/") 
html2 = response2.read()
soup2 = BeautifulSoup(html2, 'lxml')
outDiv = soup2.find(id = 'content')
movieName = outDiv.find('h1').find("span").get_text()
def has_no_class(tag):
	return tag.name == 'span' and not tag.has_attr('class')

interDiv = outDiv.find(id = 'info')
di_sc = interDiv.find_all(has_no_class)
direct = di_sc[0].find('a').string
screenwriter = di_sc[1].find('a').string
actors = interDiv.find('span', class_ = 'actor').find('span',class_ = 'attrs')
actorlist = ""
for actor in actors.children:
	actorlist += actor.string

score = outDiv.select('#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > strong')[0].get_text()
print("电影名:" + movieName)
print("评分:" + score)
print("导演:" + direct)
print("编剧:" + screenwriter)
print("主演:" + actorlist)
