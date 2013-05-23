#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import csv
import urllib
import numpy as np
from BeautifulSoup import BeautifulSoup

def getTop25ReginalSites(region):
    url = "http://www.alexa.com/topsites/countries/" + region
    #url="http://beijing.homelink.com.cn/ershoufang/xqcj/BJHD85587502.shtml"
    try:
        html = urllib.urlopen(url).read()
        parser = BeautifulSoup(html)
        tt = unicode(parser)
        tt = tt.encode('ascii','ignore')
        p = np.array(re.findall('/siteinfo/.+\</a', tt))
        #p = np.array(re.findall('/ershoufang/BJHD.+\</a', tt))
        condlist = np.array(map(len, p)) < 60
        p0 = p[condlist]
        sites = []
        for i in range(len(p0)):
            site = re.split('">',re.split('info/',p0[i])[1])[0]
            sites.append(site)
        final=np.array(sites)
        return (final)
    except:
        return (np.array(["na","na"]))

if __name__ == '__main__':    
    websites = getTop25ReginalSites("US")
    print websites
#file = open('D:/sitelist.csv','w')
#w = csv.writer(file,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#w.writerows(websites)
#file.close()