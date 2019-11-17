#script to find running time of a youtube playlist
import re
import sys
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup

def get_soup(addr):
	req = Request(addr, headers={'User-agent': 'Mozilla/5.0'})
	wp = urlopen(req).read()
	soup = BeautifulSoup(wp, "html.parser")
	return soup

addr = sys.argv[1]
#print(addr)
soup = get_soup(addr)
tstamps = soup.find_all("div", attrs={"class": "timestamp"})
sec=0
for a in tstamps:
	#print(a)
	result = re.search(r">(.*)</span>", str(a))
	result = result.group(1)
	#print(result)
	temp = re.search(r">(.*)", result)
	temp = temp.group(1)
	temp = temp.split(":")
	#temp = int(temp)
	sing=0
	for ind in temp:
		sing *= 60
		sing += int(ind)
	sec += sing
	#print(sing)
	#print(temp)

print(str(sec//3600) + " hours " + str((sec%3600)//60) + " minutes " + str(sec%60) + " seconds")
