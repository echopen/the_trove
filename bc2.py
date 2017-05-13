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

Noms = ["Mehdi","Kelu","Olivier","Jerome","Jérôme","Jérome","Jerôme","Benoit","Vincent","Constant","Benoît","Pierre","Carlos","Farad","Laurel","Oliv","Luc"]
Family = ["Benchoufi","De Fresnoye","de Fresnoye", "De fresnoye", "Jonveaux","Vincent","Dubois","Bourdeloux"]

BigFile = ""

def Clean(txt):
	CleanTxt = str(txt)
	CleanTxt = html2text.html2text(CleanTxt)
	CleanTxt = CleanTxt.replace("<br/>","")
	for nom in Noms:
		CleanTxt = CleanTxt.replace(nom,"Hyacinthe")
		CleanTxt = CleanTxt.replace(nom.lower(),"hyacinthe")
	for family in Family:
		CleanTxt = CleanTxt.replace(family,"Lacenne")
		CleanTxt = CleanTxt.replace(family.lower(),"lacenne")

	CleanTxt = CleanTxt.replace("lacenne hyacinthe","Hyacinthe Lacenne")

	CleanTxt = CleanTxt.replace("`","")
	return CleanTxt



for root, directories, filenames in os.walk('./'):
	for directory in directories:
		print os.path.join(root, directory) 
	for filename in filenames: 
		print os.path.join(root,filename) 
		if (".html" in filename) and ("bc2-raw"  in root):
			Messages.append(os.path.join(root,filename) )	

for item in Messages:
	MessageBC2 = ""
	info = item.split("/")
	print info
	fileset = info[-2].split("-")[1]
	#print fileset
	filename = info[-1].split(".")[0]
	#print filename

	SaveFile = fileset+"-"+filename+".md"
	soup = BeautifulSoup(open(item))


	titre = soup.find_all('h2')[0]
	MessageBC2 += Clean(titre) +"\n\n"

	Contenu = soup.find_all('div', {'class' : 'content'})
	if len(Contenu):
	    MessageBC2 += Clean(Contenu[0]) +"\n\n"

	Comments = soup.find_all('div', {'class' : 'comments'})

	if len(Comments):
		realComment = Comments[0].find_all('div', {'class' : 'comment'})
		for comment in realComment:
		    MessageBC2 += "### "+Clean(comment.find_all('p')[0]) +"\n\n" 
		    MessageBC2 += Clean(comment.find_all('div', {'class' : 'content'})[0]) +"\n\n"
		    titre = ""
	BC2 = MessageBC2.replace("\n\n", "$$$$$$$")
	BC2 = MessageBC2.replace("\n", "")
	BC2 = MessageBC2.replace("$$$$$$$", "\n\n")

	BigFile += "\n\n"+MessageBC2
	file = open("./bc2-data/"+SaveFile, 'w')
	file.write(MessageBC2)
	file.close()

file = open("./bc2-data/Readme.md", 'w')
file.write(BigFile)
file.close()

#html2text.html2text()

