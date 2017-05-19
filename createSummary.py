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
import datetime
import html2text

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

SUMMARYMD = "# Summary\n\n"



def GetFiles(folder,extension):
	Messages = []
	for root, directories, filenames in os.walk('./'):
		for filename in filenames: 
			#print os.path.join(root,filename) 
			if (extension in filename) and (folder+"-data"  in root) and ("the_trove-raw" not in root) and ("Readme" not in filename):
				Messages.append(os.path.join(root,filename) )	
	return Messages



## Wiki

BC3MDs = GetFiles("wiki",".processed.md")
SUMMARYMD += "\n"+"* [Wiki](wiki.md)\n"

for item in BC3MDs:
	print item
	SUMMARYMD += "    * ["+item.split("/")[-1].split(".")[0]+"]("+item.split("./")[-1]+")\n"

## BC3

BC3MDs = GetFiles("bc3",".md")
SUMMARYMD += "* [Basecamp 3](bc3.md)\n"

for item in BC3MDs:
	print item
	SUMMARYMD += "    * ["+item.split("/")[-1]+"]("+item.split("./")[-1]+")\n"

## Writing

file = open("SUMMARY.md", 'w')
file.write(SUMMARYMD)
file.close()

