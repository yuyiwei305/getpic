#! /usr/bin/env  python
# _*_ coding: utf-8 _*_

import os
import sys
import requests
from bs4 import BeautifulSoup
import re



reload(sys)
sys.setdefaultencoding("utf-8")

# 需要爬的url eg :搜狗壁纸
sougouurl = "http://bizhi.sogou.com/park"

# http 请求头

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}

def GetDownloadUrl(url):
	downloadurl = []
	r = requests.get(url,headers)
	soup = BeautifulSoup(r.content)
	for preimg in soup.find_all("img"):
		
		imgre = re.compile('^http:.*')
		imgtrue = re.findall(imgre,preimg["src"])
		for i in range(len(imgtrue)):
			downloadurl.append(imgtrue[i])

	return downloadurl

def downloadpic(url):
	pic_list_url = GetDownloadUrl(url)
	for i in range(len(pic_list_url)):
		pic_url = pic_list_url[i]
		refilename = re.compile('.*/(.*)')
		filematch = re.search(refilename,pic_url)
		filename =  filematch.group(1)
		r = requests.get(pic_url,headers = headers)	
		path = os.getcwd()
		path = os.path.join(path,"pictures")
		if not os.path.exists(path):
			os.mkdir(path)
		file_path = os.path.join(path,filename)
		f = open(file_path, 'wb')
		print "downloading " + filename + "......"
		f.write(r.content)
		f.close()
			
downloadpic(sougouurl)
