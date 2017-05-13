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

	oldPath = "./../../echopen-155345/all%20files%20-%20images%20pdfs%20spreadsheets%20etc/"
	newPath = "bc3-raw/files/"
	CleanTxt = CleanTxt.replace(oldPath,newPath)

	return CleanTxt.strip()



for root, directories, filenames in os.walk('./'):
	for filename in filenames: 
		#print os.path.join(root,filename) 
		if (".html" in filename) and ("bc3-raw"  in root):
			Messages.append(os.path.join(root,filename) )	

for item in Messages:
	MessageBC2 = ""
	info = item.split("/")
	print info
	fileset = info[-2].split("-")[1]
	#print fileset
	filename = info[-1].split(".")[0].split("-")[-1]
	print filename

	SaveFile = filename+".md"
	soup = BeautifulSoup(open(item), "lxml")



	titre = soup.find_all('h1', {'class' : 'flush--top'})[0]
	MessageBC2 += Clean(titre) +"\n\n"

	MessageBC2 += str(Clean(soup.find_all('small', {'class' : 'metadata'})[0]))+"\n\n"

	Contenu = soup.find_all('div', {'class' : 'formatted_content'})
	if len(Contenu):
	    MessageBC2 += Clean(Contenu[0]) +"\n\n"

	Comments = soup.find_all('div', {'class' : 'thread__entries'})

	if len(Comments):
		realComment = Comments[0].find_all('article', {'class' : 'thread-entry'})

		for comment in realComment:
			if comment.find_all('strong', {'class' : 'thread-entry__author'}):
			    MessageBC2 += "### "+Clean(comment.find_all('strong', {'class' : 'thread-entry__author'})[0])
			    MessageBC2 += " - "+ Clean(comment.find_all('span', {'class' : 'thread-entry__metadata__time'})[0])
			    MessageBC2 += "\n\n" 
			    MessageBC2 += Clean(comment.find_all('div', {'class' : 'formatted_content'})[0]) +"\n\n"


		#print MessageBC2


	file = open("./bc3-data/"+SaveFile, 'w')
	file.write(MessageBC2)
	file.close()
	BigFile += "\n\n"+MessageBC2

file = open("./bc3-data/Readme.md", 'w')
file.write(BigFile)
file.close()

#html2text.html2text()


