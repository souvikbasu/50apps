import urllib2
import re
from Queue import Queue
from BeautifulSoup import BeautifulSoup, SoupStrainer

class Url:
    def __init__(self, url, depth):
        self.url = url
        self.depth = depth

def getSoup(url):
    page = urllib2.urlopen(url)
    return BeautifulSoup(page)

def getLinks(url):
    links = []
    soup = getSoup(url)
    for link in soup.fetch('a'):
        if link.has_key('href') and 'http://' in link['href']:
            links.append(link['href'])
    return links

def hasContent(url, content):
    try:
        soup = getSoup(url)
        if(content in soup.text):
            return 1
        return 0
    except:
        return 0

def crawl(searchstring,url,depth):
    seedUrl = Url(url, 0)
    q = Queue()
    visited = []
    successlinks = []
    q.put(seedUrl)
    while(not q.empty()):
        currentUrl = q.get()
        if currentUrl.depth == depth:
            continue
        print 'Parsing Depth '+ str(currentUrl.depth) + '. Url:' + str(currentUrl.url)
        if hasContent(currentUrl.url,searchstring):
            successlinks.append(currentUrl.url)
        visited.append(currentUrl.url)

        links = getLinks(currentUrl.url)
        for link in links:
            if (link not in visited):
                q.put(Url(link, currentUrl.depth + 1))
    return successlinks

