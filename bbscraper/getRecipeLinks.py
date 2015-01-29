import time
import urllib
import re
import collections
from bs4 import BeautifulSoup

STARTYEAR = 2009
ENDYEAR = 2015
STARTMONTH = 5
ENDMONTH = int(time.strftime("%m"))

def ListOfYearMonths(startyear,startmonth,endyear,endmonth):

	moyr = map(lambda x: [x,range(1,13)],range(startyear,endyear+1))
	moyr[0][1] = moyr[0][1][startmonth-1:]
	moyr[-1][1] = moyr[-1][1][0:endmonth]
	return moyr

def listOfUrls(yrmo,url_stub,_format = '{}/{}/{:0>2d}'):
    #return a formatted list of urls
    #yrmo is a datastructure with the format [[yr, [mo,mo,...]],[yr, [mo, mo, ...], ...]
    for yr in yrmo:
        for i,mo in enumerate(yr[1]):
            print i,
            print _format.format(url_stub,yr[0],mo)

def getRecipesFromBBURL(url, )
    data = urllib.urlopen(url).read()
    reg = 'post-\d\d\d\d\d'
    #class="post-##### post
    #class id="content"
    links = collections.defaultdict(list)


    soup = BeautifulSoup(data)

    rec = soup.find(id="content")

    divs = rec.find_all(class_=re.compile('post-\d\d\d\d\d'))
    for m,k in enumerate(divs):
        #print "POST %s => " % (m)
        #print ""
        #print k.get('class')
        r = k.find_all("div")
        for a,j in enumerate(r):
            if j.get('class')[0] == 'entry-content':
                print j.a.get('href')
                print "___________________________________"
