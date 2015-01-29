import time
import urllib
import re
from bs4 import BeautifulSoup

STARTYEAR = 2009
ENDYEAR = 2015
STARTMONTH = 12
ENDMONTH = int(time.strftime("%m"))
listOfBBUrls = []

def listOfYearMonths(startyear,startmonth,endyear,endmonth):

	moyr = map(lambda x: [x,range(1,13)],range(startyear,endyear+1))
	moyr[0][1] = moyr[0][1][startmonth-1:]
	moyr[-1][1] = moyr[-1][1][0:endmonth]
	return moyr

def generateUrls(yrmo,url_stub,_format = '{}/{}/{:0>2d}'):
    #return a formatted list of urls
    #yrmo is a datastructure with the format [[yr, [mo,mo,...]],[yr, [mo, mo, ...], ...]
    for yr in yrmo:
        for mo in yr[1]:
            yield _format.format(url_stub,yr[0],mo)


def getRecipesFromBBURL(url):
    try:
        html_data = urllib.urlopen(url).read()
        regex = 'post-\d\d\d\d\d'
        recipeLinks = []

        soup = BeautifulSoup(html_data)

        content = soup.find(id="content")
        divs = content.find_all(class_=re.compile(regex))

        for recipe in divs:
            rec_data = []
            rec_divs = recipe.find_all("div")
            for rec_div in rec_divs:
                if rec_div.get('class')[0] == 'recipe-cost':
                    #print rec_div.contents
                    if not rec_div.contents:
                        rec_data.insert(0,False)
                    else:
                        rec_data.insert(0,True)
                if rec_div.get('class')[0] == 'entry-content':
                    #print rec_div.a.get('href')
                    try:
                        rec_data.insert(1,rec_div.a.get('href'))
                        rec_data.insert(2,rec_div.a.img.get('src'))
                    except:
                        rec_data.insert(1,'')
                        rec_data.insert(2,'')
                        pass
            if rec_data[0]:
                recipeLinks.append(', '.join([rec_data[1],rec_data[2]]))
        return recipeLinks
    except:
        print "Something broke"
        print url
        print rec_div

#getRecipesFromBBURL('http://www.budgetbytes.com/2009/05')
fo = open('./output.txt','wb')
for u in generateUrls(listOfYearMonths(STARTYEAR,STARTMONTH,ENDYEAR,ENDMONTH), 'http://www.budgetbytes.com'):
    listForThisUrl = getRecipesFromBBURL(u)
    listOfBBUrls += listForThisUrl
    print listForThisUrl
fo.write('\n'.join(listOfBBUrls))
fo.close()
