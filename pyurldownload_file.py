#!/usr/bin/python3

import requests
from bs4 import *
import sys 
import wget

url  = raw_input('Enter URL -> ')
pattern = raw_input('Enter search pattern-> ')

html = requests.get(url)




if html.text.find("400 Bad Request") != -1:
	print ("Bad Request")
	sys.exit()

soup = BeautifulSoup(html.text)

tags = soup('a')

for tag in tags:
	urldownload = "http://www.asambleanacional.gob.ve/"
	url = tag.get('href',None)
	text = str(url)
	if text.find(pattern) == -1: continue
	urldownload +=  text
	print ("Retrieve: {0},{1}".format(tag.contents[0],urldownload))
	file = 	text.split("/")[-1]
	path_and_file = dir_download + file
	wget.download(urldownload)		
	