#!/usr/bin/env python3
import urllib.request
import re

url='http://www.asciima.com/ascii/12.html'
response=urllib.request.urlopen(url)
html=response.read()
p=re.findall('src="([-_/0-9a-zA-Z]*?\.(?:gif))"',str(html))
for src in p:
	print('http://www.asciima.com'+src)
	urllib.request.urlretrieve('http://www.asciima.com'+src,"a.gif")
#print(html)

