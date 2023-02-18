from lxml import html
from lxml import etree
import requests
import json


xml_sample = """<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"
    xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:wfw="http://wellformedweb.org/CommentAPI/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:atom="http://www.w3.org/2005/Atom"
    xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"
    xmlns:slash="http://purl.org/rss/1.0/modules/slash/"
    
    xmlns:georss="http://www.georss.org/georss"
    xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#"
    >
""".encode("utf-8")

"""
# some bad results from algorithmic solution
page = requests.get(address9to5mac)
tree = html.fromstring(page.content)
publisherTitle = tree.xpath('//*/text()')
#print "Publisher: ", publisherTitle[2]
#articleTitle = tree.xpath('//*/text()')

articleTitleFirstLine = 19
articleLinkFirstLine = 21
publicationDateFirstLine = 26
nextArticleIteration = 36

articleTitle = tree.xpath('//*/text()')
articleLink = tree.xpath('//*/text()')
#articleLink = articleLink.replace("\n","").replace("\t","")
publicationDate = tree.xpath('//*/text()')

articlesToLoad = 50

rssFeedRaw = []
rssFeedRaw.append([publisherTitle[2], articleTitle[articleTitleFirstLine], articleLink[articleLinkFirstLine], publicationDate[publicationDateFirstLine]])
counter = 1
while (counter < articlesToLoad):
    rssFeedRaw.append([publisherTitle[2], articleTitle[articleTitleFirstLine + (nextArticleIteration * counter)], articleLink[articleLinkFirstLine + (nextArticleIteration * counter)], publicationDate[publicationDateFirstLine + (nextArticleIteration * counter)]])
    counter += 1
"""
    
"""
articleTitle = tree.xpath('//*/text()')
print "Article Title: ", articleTitle[19]
articleLink = tree.xpath('//*/text()')
#print "Link: ", articleLink[21]
articleLink[21] = articleLink[21].replace("\n","").replace("\t","")
print "Link: ", articleLink[21]
publicationDate = tree.xpath('//*/text()')
print "Publication Date: ", publicationDate[26]
print "\n"

print "Article Title: ", articleTitle[55]
articleLink = tree.xpath('//*/text()')
#print "Link: ", articleLink[21]
articleLink[57] = articleLink[57].replace("\n","").replace("\t","")
print "Link: ", articleLink[57]
publicationDate = tree.xpath('//*/text()')
print "Publication Date: ", publicationDate[62]
print "\n"

print 55-19
print 57-21
print 62-26
"""

"""
for line in rssFeedRaw:
    print(line[0].replace("\n","").replace("\t","").replace("\u2019", "'"), line[1].replace("\n","").replace("\t","").replace("\u2019", "'"),
        line[2].replace("\n","").replace("\t","").replace("\u2019", "'"),
        line[3].replace("\n","").replace("\t","").replace("\u2019", "'"))
"""

publisher = "ABCNews"
addressABCNews = 'https://abcnews.go.com/abcnews/topstories'
page = requests.get(addressABCNews)
tree = html.fromstring(page.content)
abcNewsDump = tree.xpath('//*/text()')

firstArticleTitle = abcNewsDump[16].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
firstArticleLink = abcNewsDump[18].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
firstArticleDate = abcNewsDump[21]

secondArticleTitle = abcNewsDump[30].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
secondArticleLink = abcNewsDump[32].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
secondArticleDate = abcNewsDump[35]

thirdArticleTitle = abcNewsDump[44].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
thirdArticleLink = abcNewsDump[46].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
thirdArticleDate = abcNewsDump[49]

fourthArticleTitle = abcNewsDump[58].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
fourthArticleLink = abcNewsDump[60].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
fourthArticleDate = abcNewsDump[63]

fifthArticleTitle = abcNewsDump[72].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
fifthArticleLink = abcNewsDump[74].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
fifthArticleDate = abcNewsDump[77]

sixthArticleTitle = abcNewsDump[86].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
sixthArticleLink = abcNewsDump[88].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
sixthArticleDate = abcNewsDump[91]

seventhArticleTitle = abcNewsDump[100].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
seventhArticleLink = abcNewsDump[102].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
seventhArticleDate = abcNewsDump[105]

eighthArticleTitle = abcNewsDump[114].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
eighthArticleLink = abcNewsDump[116].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
eighthArticleDate = abcNewsDump[119]

ninthArticleTitle = abcNewsDump[128].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
ninthArticleLink = abcNewsDump[130].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
ninthArticleDate = abcNewsDump[133]

tenthArticleTitle = abcNewsDump[142].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
tenthArticleLink = abcNewsDump[144].replace("\n","").replace("\t","").lstrip('<![CDATA[ ').rstrip(']]>')
tenthArticleDate = abcNewsDump[147]


abcNewsBundle = []
abcNewsBundle.append([firstArticleTitle, firstArticleLink, publisher, firstArticleDate])
abcNewsBundle.append([secondArticleTitle, secondArticleLink, publisher, secondArticleDate])
abcNewsBundle.append([thirdArticleTitle, thirdArticleLink, publisher, thirdArticleDate])
abcNewsBundle.append([fourthArticleTitle, fourthArticleLink, publisher, fourthArticleDate])
abcNewsBundle.append([fifthArticleTitle, fifthArticleLink, publisher, fifthArticleDate])
abcNewsBundle.append([sixthArticleTitle, sixthArticleLink, publisher, sixthArticleDate])
abcNewsBundle.append([seventhArticleTitle, seventhArticleLink, publisher, seventhArticleDate])
abcNewsBundle.append([eighthArticleTitle, eighthArticleLink, publisher, eighthArticleDate])
abcNewsBundle.append([ninthArticleTitle, ninthArticleLink, publisher, ninthArticleDate])
abcNewsBundle.append([tenthArticleTitle, tenthArticleLink, publisher, tenthArticleDate])

for line in abcNewsBundle:
    print line
print "\n"


publisherFox = "FoxNews"
addressFOXNews = 'https://moxie.foxnews.com/google-publisher/latest.xml'
pageFox = requests.get(addressFOXNews)
treeFox = html.fromstring(pageFox.content)
foxNewsDump = treeFox.xpath('//*/text()')

articleTitlesFox = treeFox.xpath('//channel//item//title/text()')
articleLinksFox = treeFox.xpath('//channel//item//guid/text()')
articleDatesFox = treeFox.xpath('//channel//item//pubdate//text()')

foxNewsBundle = []
firstArticleTitleFox = articleTitlesFox[0]
firstArticleTitleFox.replace("\u2018","'").replace("\u2019","'")
firstArticleLinkFox = articleLinksFox[0]
firstArticleDateFox = articleDatesFox[0]
foxNewsBundle.append([firstArticleTitleFox, firstArticleLinkFox, publisherFox, firstArticleDateFox])

secondArticleTitleFox = articleTitlesFox[2]
secondArticleTitleFox.replace("\u2018","'").replace("\u2019","'")
secondArticleLinkFox = articleLinksFox[1]
secondArticleDateFox = articleDatesFox[1]
foxNewsBundle.append([secondArticleTitleFox, secondArticleLinkFox, publisherFox, secondArticleDateFox])

thirdArticleTitleFox = articleTitlesFox[4]
thirdArticleTitleFox.replace("\u2018","'").replace("\u2019","'")
thirdArticleLinkFox = articleLinksFox[2]
thirdArticleDateFox = articleDatesFox[2]
foxNewsBundle.append([thirdArticleTitleFox, thirdArticleLinkFox, publisherFox, thirdArticleDateFox])

fourthArticleTitleFox = articleTitlesFox[6]
fourthArticleTitleFox.replace("\u2018","'").replace("\u2019","'")
fourthArticleLinkFox = articleLinksFox[3]
fourthArticleDateFox = articleDatesFox[3]
foxNewsBundle.append([fourthArticleTitleFox, fourthArticleLinkFox, publisherFox, fourthArticleDateFox])

fifthArticleTitleFox = articleTitlesFox[8]
fifthArticleTitleFox.replace("\u2018","'").replace("\u2019","'")
fifthArticleLinkFox = articleLinksFox[4]
fifthArticleDateFox = articleDatesFox[4]
foxNewsBundle.append([fifthArticleTitleFox, fifthArticleLinkFox, publisherFox, fifthArticleDateFox])

sixthArticleTitleFox = articleTitlesFox[10]
sixthArticleTitleFox.replace("\u2018","'").replace("\u2019","'")
sixthArticleLinkFox = articleLinksFox[5]
sixthArticleDateFox = articleDatesFox[5]
foxNewsBundle.append([sixthArticleTitleFox, sixthArticleLinkFox, publisherFox, sixthArticleDateFox])

seventhArticleTitleFox = articleTitlesFox[12]
seventhArticleTitleFox.replace("\u2018","'").replace("\u2019","'")
seventhArticleLinkFox = articleLinksFox[6]
seventhArticleDateFox = articleDatesFox[6]
foxNewsBundle.append([seventhArticleTitleFox, seventhArticleLinkFox, publisherFox, seventhArticleDateFox])

eighthArticleTitleFox = articleTitlesFox[14]
eighthArticleTitleFox.replace("\u2018","'").replace("\u2019","'")
eighthArticleLinkFox = articleLinksFox[7]
eighthArticleDateFox = articleDatesFox[7]
foxNewsBundle.append([eighthArticleTitleFox, eighthArticleLinkFox, publisherFox, eighthArticleDateFox])

ninthArticleTitleFox = articleTitlesFox[16]
ninthArticleTitleFox.replace("\u2018","'").replace("\u2019","'")
ninthArticleLinkFox = articleLinksFox[8]
ninthArticleDateFox = articleDatesFox[8]
foxNewsBundle.append([ninthArticleTitleFox, ninthArticleLinkFox, publisherFox, ninthArticleDateFox])

tenthArticleTitleFox = articleTitlesFox[18]
tenthArticleTitleFox.replace("\u2018","'").replace("\u2019","'")
tenthArticleLinkFox = articleLinksFox[9]
tenthArticleDateFox = articleDatesFox[9]
foxNewsBundle.append([tenthArticleTitleFox, tenthArticleLinkFox, publisherFox, tenthArticleDateFox])

for line in foxNewsBundle:
    print line
print "\n"

publisherDailyMail = "Daily Mail"
addressDailyMail = 'https://www.dailymail.co.uk/news/index.rss'
pageDailyMail = requests.get(addressDailyMail)
treeDailyMail = html.fromstring(pageDailyMail.content)
dailyMailDump = treeDailyMail.xpath('//*/text()')
#print dailyMailDump
articleTitlesDailyMail = treeDailyMail.xpath('//channel//item//title/text()')
articleLinksDailyMail = treeDailyMail.xpath('//channel//item//guid/text()')
articleDatesDailyMail = treeDailyMail.xpath('//channel//item//pubdate//text()')
#print articleTitlesDailyMail

dailyMailBundle = []
firstArticleTitleDailyMail = articleTitlesDailyMail[0]
firstArticleTitleDailyMail = firstArticleTitleDailyMail.lstrip('<![CDATA[ ').rstrip(']]>')
firstArticleLinkDailyMail = articleLinksDailyMail[0]
firstArticleDateDailyMail = articleDatesDailyMail[0]
dailyMailBundle.append([firstArticleTitleDailyMail, firstArticleLinkDailyMail, publisherDailyMail, firstArticleDateDailyMail])

secondArticleTitleDailyMail = articleTitlesDailyMail[1]
secondArticleTitleDailyMail = secondArticleTitleDailyMail.lstrip('<![CDATA[ ').rstrip(']]>')
secondArticleLinkDailyMail = articleLinksDailyMail[1]
secondArticleDateDailyMail = articleDatesDailyMail[1]
dailyMailBundle.append([secondArticleTitleDailyMail, secondArticleLinkDailyMail, publisherDailyMail, secondArticleDateDailyMail])

thirdArticleTitleDailyMail = articleTitlesDailyMail[2]
thirdArticleTitleDailyMail = thirdArticleTitleDailyMail.lstrip('<![CDATA[ ').rstrip(']]>')
thirdArticleLinkDailyMail = articleLinksDailyMail[2]
thirdArticleDateDailyMail = articleDatesDailyMail[2]
dailyMailBundle.append([thirdArticleTitleDailyMail, thirdArticleLinkDailyMail, publisherDailyMail, thirdArticleDateDailyMail])

fourthArticleTitleDailyMail = articleTitlesDailyMail[3]
fourthArticleTitleDailyMail = fourthArticleTitleDailyMail.lstrip('<![CDATA[ ').rstrip(']]>')
fourthArticleLinkDailyMail = articleLinksDailyMail[3]
fourthArticleDateDailyMail = articleDatesDailyMail[3]
dailyMailBundle.append([fourthArticleTitleDailyMail, fourthArticleLinkDailyMail, publisherDailyMail, fourthArticleDateDailyMail])

fifthArticleTitleDailyMail = articleTitlesDailyMail[4]
fifthArticleTitleDailyMail = fifthArticleTitleDailyMail.lstrip('<![CDATA[ ').rstrip(']]>')
fifthArticleLinkDailyMail = articleLinksDailyMail[4]
fifthArticleDateDailyMail = articleDatesDailyMail[4]
dailyMailBundle.append([fifthArticleTitleDailyMail, fifthArticleLinkDailyMail, publisherDailyMail, fifthArticleDateDailyMail])

sixthArticleTitleDailyMail = articleTitlesDailyMail[5]
sixthArticleTitleDailyMail = sixthArticleTitleDailyMail.lstrip('<![CDATA[ ').rstrip(']]>')
sixthArticleLinkDailyMail = articleLinksDailyMail[5]
sixthArticleDateDailyMail = articleDatesDailyMail[5]
dailyMailBundle.append([sixthArticleTitleDailyMail, sixthArticleLinkDailyMail, publisherDailyMail, sixthArticleDateDailyMail])

seventhArticleTitleDailyMail = articleTitlesDailyMail[6]
seventhArticleTitleDailyMail = seventhArticleTitleDailyMail.lstrip('<![CDATA[ ').rstrip(']]>')
seventhArticleLinkDailyMail = articleLinksDailyMail[6]
seventhArticleDateDailyMail = articleDatesDailyMail[6]
dailyMailBundle.append([seventhArticleTitleDailyMail, seventhArticleLinkDailyMail, publisherDailyMail, seventhArticleDateDailyMail])

eighthArticleTitleDailyMail = articleTitlesDailyMail[7]
eighthArticleTitleDailyMail = eighthArticleTitleDailyMail.lstrip('<![CDATA[ ').rstrip(']]>')
eighthArticleLinkDailyMail = articleLinksDailyMail[7]
eighthArticleDateDailyMail = articleDatesDailyMail[7]
dailyMailBundle.append([eighthArticleTitleDailyMail, eighthArticleLinkDailyMail, publisherDailyMail, eighthArticleDateDailyMail])

ninthArticleTitleDailyMail = articleTitlesDailyMail[8]
ninthArticleTitleDailyMail = ninthArticleTitleDailyMail.lstrip('<![CDATA[ ').rstrip(']]>')
ninthArticleLinkDailyMail = articleLinksDailyMail[8]
ninthArticleDateDailyMail = articleDatesDailyMail[8]
dailyMailBundle.append([ninthArticleTitleDailyMail, ninthArticleLinkDailyMail, publisherDailyMail, ninthArticleDateDailyMail])

tenthArticleTitleDailyMail = articleTitlesDailyMail[9]
tenthArticleTitleDailyMail = tenthArticleTitleDailyMail.lstrip('<![CDATA[ ').rstrip(']]>')
tenthArticleLinkDailyMail = articleLinksDailyMail[9]
tenthArticleDateDailyMail = articleDatesDailyMail[9]
dailyMailBundle.append([tenthArticleTitleDailyMail, tenthArticleLinkDailyMail, publisherDailyMail, tenthArticleDateDailyMail])

for line in dailyMailBundle:
    print line
print "\n"


publisherTimcast = "TIMCAST"
addressTimcast = 'https://timcast.com/feed/'
pageTimcast = requests.get(addressTimcast)
treeTimcast = html.fromstring(pageTimcast.content)
timcastDump = treeTimcast.xpath('//*/text()')
#print timcastDump
articleTitlesTimcast = treeTimcast.xpath('//channel//item//title/text()')
articleLinksTimcast = treeTimcast.xpath('//channel//item//guid/text()')
articleDatesTimcast = treeTimcast.xpath('//channel//item//pubdate//text()')
#print articleTitlesTimcast

timcastBundle = []
firstArticleTitleTimcast = articleTitlesTimcast[0]
firstArticleLinkTimcast = articleLinksTimcast[0]
firstArticleDateTimcast = articleDatesTimcast[0]
timcastBundle.append([firstArticleTitleTimcast, firstArticleLinkTimcast, publisherTimcast, firstArticleDateTimcast])

secondArticleTitleTimcast = articleTitlesTimcast[1]
secondArticleLinkTimcast = articleLinksTimcast[1]
secondArticleDateTimcast = articleDatesTimcast[1]
timcastBundle.append([secondArticleTitleTimcast, secondArticleLinkTimcast, publisherTimcast, secondArticleDateTimcast])

thirdArticleTitleTimcast = articleTitlesTimcast[2]
thirdArticleLinkTimcast = articleLinksTimcast[2]
thirdArticleDateTimcast = articleDatesTimcast[2]
timcastBundle.append([thirdArticleTitleTimcast, thirdArticleLinkTimcast, publisherTimcast, thirdArticleDateTimcast])

fourthArticleTitleTimcast = articleTitlesTimcast[3]
fourthArticleLinkTimcast = articleLinksTimcast[3]
fourthArticleDateTimcast = articleDatesTimcast[3]
timcastBundle.append([fourthArticleTitleTimcast, fourthArticleLinkTimcast, publisherTimcast, fourthArticleDateTimcast])

fifthArticleTitleTimcast = articleTitlesTimcast[4]
fifthArticleLinkTimcast = articleLinksTimcast[4]
fifthArticleDateTimcast = articleDatesTimcast[4]
timcastBundle.append([fifthArticleTitleTimcast, fifthArticleLinkTimcast, publisherTimcast, fifthArticleDateTimcast])

sixthArticleTitleTimcast = articleTitlesTimcast[5]
sixthArticleLinkTimcast = articleLinksTimcast[5]
sixthArticleDateTimcast = articleDatesTimcast[5]
timcastBundle.append([sixthArticleTitleTimcast, sixthArticleLinkTimcast, publisherTimcast, sixthArticleDateTimcast])

seventhArticleTitleTimcast = articleTitlesTimcast[6]
seventhArticleLinkTimcast = articleLinksTimcast[6]
seventhArticleDateTimcast = articleDatesTimcast[6]
timcastBundle.append([seventhArticleTitleTimcast, seventhArticleLinkTimcast, publisherTimcast, seventhArticleDateTimcast])

eigthArticleTitleTimcast = articleTitlesTimcast[7]
eigthArticleLinkTimcast = articleLinksTimcast[7]
eigthArticleDateTimcast = articleDatesTimcast[7]
timcastBundle.append([eigthArticleTitleTimcast, eigthArticleLinkTimcast, publisherTimcast, eigthArticleDateTimcast])

ninthArticleTitleTimcast = articleTitlesTimcast[8]
ninthArticleLinkTimcast = articleLinksTimcast[8]
ninthArticleDateTimcast = articleDatesTimcast[8]
timcastBundle.append([ninthArticleTitleTimcast, ninthArticleLinkTimcast, publisherTimcast, ninthArticleDateTimcast])

tenthArticleTitleTimcast = articleTitlesTimcast[9]
tenthArticleLinkTimcast = articleLinksTimcast[9]
tenthArticleDateTimcast = articleDatesTimcast[9]
timcastBundle.append([tenthArticleTitleTimcast, tenthArticleLinkTimcast, publisherTimcast, tenthArticleDateTimcast])

for line in timcastBundle:
    print line
print "\n"



def sort_newsBundle_Date_Descending(arr):
    sorted = []
    while (len(arr) > 0):
        latestDate = find_latest(arr)
        for line in arr:
            if line[3] == latestDate:
                sorted.append(line)
                arr.remove(line)
    return sorted

def find_latest(arr):
    temp = []
    for line in arr:
        temp.append(line[3])
    return max(temp)



fullNewsBundle = []
for line in abcNewsBundle:
    fullNewsBundle.append(line)
for line in foxNewsBundle:
    fullNewsBundle.append(line)
for line in dailyMailBundle:
    fullNewsBundle.append(line)
for line in timcastBundle:
    fullNewsBundle.append(line)

fullNewsBundle = sort_newsBundle_Date_Descending(fullNewsBundle)
for line in fullNewsBundle:
    print line
print "\n"

print "GO BACK AND FIX FOX NEWS"
print "\n"


# convert into JSON:
#y = json.dumps(fullNewsBundle)

# the result is a JSON string:
#print(y)

response={'Price':54,'Cost':'99'}
    print(json.JSONEncoder().encode(response))
