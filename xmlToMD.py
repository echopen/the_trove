#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------
# (c) kelu124
# cc-by-sa/4.0/
# -------------------------

from bs4 import BeautifulSoup
import re
import os
import urllib2
import html2text
from lxml import etree

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Setup the wiki file
dataset = "./wiki-raw/201512-wiki-backup.xml"
tree = etree.parse(dataset)
root = tree.getroot()
NbPages = len(root)
#NbPages = 4
for i in range(NbPages-2):
	NbItem = len(root[i+1])
	#print "NbItem: " + str(NbItem)
	Title = root[i+1][0].text
	if "File:" not in Title and "User:" not in Title:
		#print Title
		NbRevs = NbItem - 3
		#print "Revs: "+ str(NbRevs)
		Revs = root[i+1][NbRevs]
		LastRev = len(Revs)
		#print LastRev
		for k in reversed(range(LastRev)):
			if Revs[k].tag == "text":
				contenu = Revs[k].text
				break
		#print contenu


		contenu = contenu.replace("http://paglabs.com/echopen/index.php?","http://wiki.echopen.org/index.php/")

		file = open("./wiki-data/mediawiki/"+Title.replace(" ","_").replace("/","_")+".mediawiki", 'w')
		file.write("# "+Title+"\n\n"+contenu)
		file.close()

			
