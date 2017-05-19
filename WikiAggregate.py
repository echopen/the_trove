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

#<Category:Mechanics>
Pages = ["RetroEngineering","TechTeam","BBB","Servomotor","Mechanics","Historique","Sonde","Balayage","Transducer","Electronics","Microcontroller","Challenge","Arduino","Display","Software","RedPitaya","Network"]
FullContent = {"Tmp":""}
for Category in Pages:
	FullContent[Category]= ""

def GetFiles(folder):
	Messages = []
	for root, directories, filenames in os.walk('./'):
		for filename in filenames: 
			#print os.path.join(root,filename) 
			if (".md" in filename) and (folder+"-data"  in root) and ("the_trove-raw" not in root) and ("Readme" not in filename):
				Messages.append(os.path.join(root,filename) )	
	return Messages

WikiMDs = GetFiles("wiki")

for item in WikiMDs:
	f = open(item, 'r')
	contenu = f.read()
	f.close()

	contenu = contenu.replace("1.  ","# ") 

	for Category in Pages:
		if "<Category:"+Category+">" in contenu:
			FullContent[Category]+= "\n\n"+contenu+"\n"

#print FullContent

for Category in Pages:

	file = open("./wiki-data/"+Category+".processed.md", 'w')
	file.write(FullContent[Category])
	file.close()
