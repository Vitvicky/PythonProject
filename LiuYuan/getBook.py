import urllib2
from download import download
from bs4 import *

url_header = 'http://www.springerlink.com'

def down_task(url):
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    webpage = urllib2.urlopen(req)
    soup = BeautifulSoup(webpage.read( ))
    #download the book chapter
    for i in soup.find_all('li', {'class':'primitive contribution bookChapter'}):
        link=i.find_all('p',{'class':'title'})[0].a
        url=url_header+link.get('href') + 'fulltext.pdf'
        name=link.contents
        name=name[0].replace(":"," -")+".pdf"
        download(url,name)
        
    index=0
    for  i in  soup.find_all('li', {'class':'primitive primitiveResource Frontmatter'}):
         link=url_header+i.a.get('href')
         download(link,'Front Matter '+str(index)+'.pdf')
         index=index+1
         
    index=0
    for  i in  soup.find_all('li', {'class':'primitive primitiveResource Backmatter'}):
         link=url_header+i.a.get('href')
         download(link,'Front Matter '+str(index)+'.pdf')
         index=index+1
         
down_task('http://www.springerlink.com/content/978-1-4471-4053-5/contents/')     

         