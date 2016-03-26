#!/usr/bin/python3

import requests
from bs4 import *
import sys 


url  = input('Enter URL -> ')
pattern = input('Enter search pattern-> ')

html = requests.get(url)

dir_download = "./download/"


if html.text.find("400 Bad Request") != -1:
	print ("Bad Request")
	sys.exit()

soup = BeautifulSoup(html.text)

tags = soup('a')

for tag in tags:
	url_path = tag.get('href',None)
	text = str(url_path)
	if text.find(pattern) == -1: 
		continue
	domain = url.split("http://")[1].split("/")[0]
	urldownload = "http://" + domain + text
	print ("Retrieve: {0},{1}".format(tag.contents[0],urldownload))
	file = 	text.split("/")[-1]
	path_and_file = dir_download + file
	try:
		r = requests.get(urldownload)
		with open(path_and_file, "wb") as f:
			f.write(r.content)
	except ConnectionError:
		print("I can't download file: {0}".format(file))
	except HTTPError:
		print("I can't download file: {0}".format(file))
	f.close()