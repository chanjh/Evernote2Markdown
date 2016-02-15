#coding=utf-8
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import xml.dom.minidom
from  xml.dom  import  minidom

def index():
	# 统计文章数量
	dom = xml.dom.minidom.parse('index.html')
	root = dom.documentElement

	aTags = root.getElementsByTagName('a')
	i = 0
	while 1:
		try:
			aTags[i].firstChild.data
			# print aTags[i].firstChild.data
			i+=1
		except:
			break
	# print "There are",i,"articles"

	# 引导开始进入文章处理
	k = 0
	while (k!=i):
		link = aTags[k].firstChild.data
		article(link)
		k+=1

def article(link):
	# 获取基本信息
	dom = xml.dom.minidom.parse( link+".html" )
	root = dom.documentElement
	title = root.getElementsByTagName('title')[0].firstChild.data
	meta = root.getElementsByTagName('meta')
	author = meta[3].getAttribute('content')
	createdTime = meta[4].getAttribute('content')
	updateTime = meta[8].getAttribute('content')
	# 得到正文
	bodys = root.getElementsByTagName('body')
	for b in bodys:
		body = b.toxml()
	body = body.replace('<body>','').replace('</body>','')


	# 从头按顺序检索正文中的标签
	# i=0
	# while 1:
	# 	try:
	# 		bodys[i].firstChild.data
	# 		i+=1
	# 	except:
	# 		break
	# print i

	body = ul(root,body)
	# print body
	# print "UL translate over"

	body = ol(root,body)
	print body

def ul(root,body):
	print "----------"
	title = root.getElementsByTagName('title')[0].firstChild.data
	print title

	# 处理无序标签
	# 计算无序标签数量
	ulTags = root.getElementsByTagName('ul')
	i = 0
	while 1:
		try:
			ulTags[i].firstChild.data
			i+=1
		except:
			break
	# 转换 HTML 为 Markdown
	k = 0
	while  k!=i:
		j=0
		liTags = ulTags[k].getElementsByTagName('li')
		liContent = "<ul>\n"	# 储存 ul 标签内的内容
		while 1:
			try:
				liTags[j].firstChild.data
				liContent += "<li>" + liTags[j].firstChild.data + "</li>\n"
				j+=1
			except:
				liContent += "</ul>"
				body = body.replace(liContent,"<Loading......>")	# 暂时替换掉
				liContent = ulLiContentTrans(liContent)				# 处理
				body = body.replace("<Loading......>",liContent)	# 替换回来
				# print body
				break
		k+=1
	return body

def ulLiContentTrans(liContent):
	liContent = liContent.replace("<li>","*")
	liContent = liContent.replace("<ul>\n","").replace("</li>","").replace("\n</ul>","")
	# print liContent
	return liContent
	
def ol(root,body):
	print "----------"
	title = root.getElementsByTagName('title')[0].firstChild.data
	# print title

	olTags = root.getElementsByTagName('ol')
	i = 0
	while 1:
		try:
			olTags[i].firstChild.data
			i+=1
		except:
			# print "There are",i,"ol tags"
			break

	k = 0
	while k!=i:
		j=0
		liTags = olTags[k].getElementsByTagName('li')
		liContentForTrans = "<ol>\n"
		liContent = "<ol>\n"
		while 1:
			try:
				liTags[j].firstChild.data
				liContent += "<li>" + liTags[j].firstChild.data + "</li>\n"
				liContentForTrans +="<li"+str(j)+">"+liTags[j].firstChild.data + "</li>\n"
				j+=1
			except:
				liContent += "</ol>"
				liContentForTrans += "</ol>"
				body = body.replace(liContent,"<Loading......>")			# 暂时替换掉
				liContentForTrans = olLiContentTrans(liContentForTrans,j)	# 处理
				body = body.replace("<Loading......>",liContentForTrans)	# 替换回来
				break
		k+=1
	return body

def olLiContentTrans(liContentForTrans,j):
	z=0
	while z<j:
		liContentForTrans = liContentForTrans.replace("<li"+str(z)+">","*"+str(z)+".")
		z+=1
	liContentForTrans = liContentForTrans.replace("<ol>\n","").replace("</li>","").replace("\n</ol>","")
	return liContentForTrans


index()