#!/usr/bin/env python3


import urllib
from BeautifulSoup import *
import sys 
import wget

url = "http://www.asambleanacional.gob.ve/documento/show2/id/64"
#url  = raw_input('Enter URL -> ')
#pattern = raw_input('Enter search pattern-> ')
pattern = 'documentos'

html = urllib.urlopen(url).read()


dir_download = "./download/"

if html.find("400 Bad Request") != -1:
	print ("Bad Request")
	sys.exit()

soup = BeautifulSoup(html)
#print soup.prettify()

tags = soup('a')

for tag in tags:
	urldownload = "http://www.asambleanacional.gob.ve/"
	url = tag.get('href',None)
	text = str(url)
	if text.find(pattern) == -1: continue
	urldownload +=  text
	print "Retrieve: ", tag.contents[0],  urldownload
	file = 	text.split("/")[-1]
	path_and_file = dir_download + file
	wget.download(urldownload)		
	

