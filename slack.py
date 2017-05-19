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







def GetFiles(folder,extension):
	Messages = []
	for root, directories, filenames in os.walk('./'):
		for filename in filenames: 
			#print os.path.join(root,filename) 
			if (extension in filename) and (folder+"-data"  in root) and ("the_trove-raw" not in root) and ("Readme" not in filename):
				Messages.append(os.path.join(root,filename) )	
	return Messages

LotsOfLogs = GetFiles("slack",".log")

for item in LotsOfLogs:
	with open(item) as f:
		print item
		content = ""
    		for line in f:
			TmpLine = line.split(">")
			value = int(TmpLine[0].split(".")[0]) # 


			TmpLine[0] = "* _"+str(datetime.datetime.fromtimestamp(int(value)).strftime('%Y-%m-%d %H:%M:%S'))+"_"

			lineBack = ">".join(TmpLine)
			content +=  lineBack

		file = open("slack-data/"+item.split("/")[-1].split(".")[0]+".md", 'w')
		file.write(content)
		file.close()







