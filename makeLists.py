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

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


Messages = []
for root, directories, filenames in os.walk('./'):

	for filename in filenames: 
		#print os.path.join(root,filename) 
		if ((".md" in filename) or (".txt" in filename)) and ("-data" in root) and ("the_trove-raw" not in root):
			Messages.append(os.path.join(root,filename) )	

Wiki = "# Items in the Wiki\n\n"
BC2 = "# Items in Basecamp 2\n\n"
BC3 = "# Items in Basecamp 3\n\n"
Slack = "# Items in Slack\n\n"
PDF = "# Items in PDFs\n\n"

for item in Messages:
	
	item = item[2:]
	nom = item.split("/")[-1].split(".")[0]
	print item + " " + nom
	if "bc2-data" in item:
		
		BC2 += "* ["+nom+"](https://echopen.gitbooks.io/the_trove/content/"+item.split(".")[0]+".html)\n"
	if "bc3-data" in item:
		BC3 += "* ["+nom+"](https://echopen.gitbooks.io/the_trove/content/"+item.split(".")[0]+".html)\n"
	if "pdf-data" in item:
		PDF += "* ["+nom+"](https://echopen.gitbooks.io/the_trove/content/"+item.split(".")[0]+".html)\n"
	if "slack-data" in item:
		Slack += "* ["+nom+"](https://echopen.gitbooks.io/the_trove/content/"+item.split(".")[0]+".html)\n"

	if "wiki-data" in item:
		Wiki += "* ["+nom+"](https://echopen.gitbooks.io/the_trove/content/"+item.split(".")[0]+".html)\n"


file = open("wiki.md", 'w')
file.write(Wiki)
file.close()

file = open("bc2.md", 'w')
file.write(BC2)
file.close()

file = open("bc3.md", 'w')
file.write(BC3)
file.close()

file = open("pdf.md", 'w')
file.write(PDF)
file.close()

file = open("slack.md", 'w')
file.write(Slack)
file.close()







