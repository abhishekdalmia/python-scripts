#author : abhishekdalmia
import sys
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def printInfo(uname, wp):
    soup = BeautifulSoup(wp, 'html.parser')
    #print(soup)
    #print(uname + ' is a valid username.')
    crating = soup.find('div', attrs={'class': 'rating-number'})
    if (crating==None):
        print(uname + ' is a team handle!!')
        return
    crating = crating.text.strip()
    print("User : " + uname)
    print("Current Rating = " + crating)
    #print(type(soup))
    filtered = soup.find_all('small')
    #print(type(filtered))
    #filtered.reverse()
    #print(filtered)
    for each in filtered:
        s = str(each)
        #print(s)
        if ("Highest Rating" in s):
            #print(s)
            hrating = each.text.strip().split()[-1][:-1]
            print("Highest Rating = " + hrating)
            return
           
    """
    ind = len(filtered)-17
    hrating = filtered[ind]
    hrating = hrating.text.strip().split()[-1][:-1]
    """

args = sys.argv[1:]
count=len(args)
if (count==0):
    print("no username provided!!")
    exit()
for i in range(0,count):
    addr = 'https://www.codechef.com/users/'+args[i]
    #print(addr)
    req = Request(addr, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        wp = urlopen(req).read()
        printInfo(args[i], wp)
    except:
        print(args[i] + ' is not a valid username!!')
    print('<----------------------------------------->')
