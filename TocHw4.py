#!/usr/bin/python
#	-*-	coding:	utf-8	-*-	
import	sys,urllib,json,re,urlparse
class	piece:
	def	__init__(self,name,max,min,month):
		self.name	=	name
		self.max	=	max
		self.min	=	min	
		self.month	=	[month]
	def	update(self,price,month):
		if	self.max	<	price:
			self.max	=	price
		if	self.min	>	price:
			self.min	=	price
		self.month.append(month)	
url	=	str(sys.argv[1])	
data	=	urllib.urlopen(url)
js	=	json.load(data)
dataRoadName	=	'土地區段位置或建物區門牌'.decode("utf8")
dataMonth	=	'交易年月'.decode("utf8")
dataPrice	=	'總價元'.decode("utf8")
maximum	=	0
dataList	=	[]
for	show	in	js:
	new	=	1
	if		'路'.decode("utf8")	in	show[dataRoadName]:					#if	roadname	with	month	exist,	update	the	class	else	new	a	class
		dataName	=	show[dataRoadName][0:show[dataRoadName].find('路'.decode("utf8"),0)+1]
		for	search	in	dataList:
			if	search.name	==	dataName	and	not	show[dataMonth]	in	search.month:
				search.update(show[dataPrice],show[dataMonth])
				new	=	0
				break;
		if	new	==	1:
			dataList.append(piece(dataName,show[dataPrice],show[dataPrice],show[dataMonth]))
	elif	'街'.decode("utf8")	in	show[dataRoadName]:					#if	roadname	with	month	exist,	update	the	class	else	new	a	class
		dataName	=	show[dataRoadName][0:show[dataRoadName].find('街'.decode("utf8"),0)+1]
		for	search	in	dataList:
			if	search.name	==	dataName	and	not	show[dataMonth]	in	search.month:
				search.update(show[dataPrice],show[dataMonth])
				new	=	0
				break;
		if	new	==	1:
			dataList.append(piece(dataName,show[dataPrice],show[dataPrice],show[dataMonth]))
	elif	'弄'.decode("utf8")	in	show[dataRoadName]:					#if	roadname	with	month	exist,	update	the	class	else	new	a	class
		dataName	=	show[dataRoadName][0:show[dataRoadName].find('弄'.decode("utf8"),0)+1]
		for	search	in	dataList:
			if	search.name	==	dataName	and	not	show[dataMonth]	in	search.month:
				search.update(show[dataPrice],show[dataMonth])
				new	=	0
				break;
		if	new	==	1:
			dataList.append(piece(dataName,show[dataPrice],show[dataPrice],show[dataMonth]))					
	elif	'大道'.decode("utf8")	in	show[dataRoadName]:					#if	roadname	with	month	exist,	update	the	class	else	new	a	class
		dataName	=	show[dataRoadName][0:show[dataRoadName].find('大道'.decode("utf8"),0)+2]
		for	search	in	dataList:
			if	search.name	==	dataName	and	not	show[dataMonth]	in	search.month:
				search.update(show[dataPrice],show[dataMonth])
				new	=	0
				break;
		if	new	==	1:
			dataList.append(piece(dataName,show[dataPrice],show[dataPrice],show[dataMonth]))	
for	x	in	dataList:#search	max	price		for	every	piece	equal	the	max	print	the	data	
	if	maximum	<	len(x.month):
		maximum	=	len(x.month)
for	y	in	dataList:
	if	maximum	==	len(y.month):
		print	y.name	+	',','最高成交價:',str(y.max)	+	',','最低成交價:',y.min
