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

import pyPdf

Messages = []

for root, directories, filenames in os.walk('./'):
	for directory in directories:
		print os.path.join(root, directory) 
	for filename in filenames: 
		print os.path.join(root,filename) 
		if (".pdf" in filename) and ("pdf-raw"  in root):
			Messages.append(os.path.join(root,filename) )	

for item in Messages:
	MessageBC2 = ""
	info = item.split("/")
	print info
	#print fileset
	filename = info[-1].split(".")[0]
	#print filename

	SaveFile = "./pdf-data/"+filename+".md"

	pdf = pyPdf.PdfFileReader(open(item, "rb"))
	for page in pdf.pages:
	    PDFTxt = page.extractText()

	file = open(SaveFile, 'w')
	file.write(PDFTxt)
	file.close()




