# Script for getting all XKCD images
# Done as a project from 'Automate the Boring Stuff With Python' book 


import requests as r
import bs4, os, shutil


url = 'https://www.xkcd.com/'




def getAll(url):
	num = 1799 # this is how much images script will download
	for i in range(num): 
		url = url + str(i+1)
		print("Getting {}".format(url))
		res = r.get(url)
		s = bs4.BeautifulSoup(res.text,'lxml')
		img = s.select('#comic img')
		url = 'https://www.xkcd.com/'
		source = 'https:' + img[0]['src']
		imageFile = r.get(source, stream=True)
		if imageFile.status_code == 200:
			with open(str(i+1) + '.jpg', 'wb') as f:
				imageFile.raw.decode_content = True
				shutil.copyfileobj(imageFile.raw, f)




getAll(url)
