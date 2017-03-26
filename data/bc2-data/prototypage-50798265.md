## echopen data format



Salut la communauté,  
  
Petite question à ouvrir: est ce que ca ne vaudrait pas le coup de
standardiser le format des fichiers pour ce qui est des images d'une part, les
signaux bruts de l'autre? On commence à acquerir des données sur lesquelles on
peut déjà travailler, ce serait top de capitaliser là dessus, et ca
permettrait à ceux qui veulent faire du traitement de l'image d'avoir une base
sur laquelle travailler pour traiter les ressources/fichiers qu'on peut mettre
à disposition.  
  
L'idée est d'avoir un format qui soit consistant dans le temps pour qu'on
puisse développer des outils qui n'aient pas besoin d'évoluer à chaque fois,
et d'avoir des données tagguées proprement, de manière à voir les évolutions
qu'on pourra avoir en fonction des kits et releases, et d'avoir ces données
propres.  
  
Il y aurait d'un côté des headers, de l'autre les données en tant que telles.  
  
Dans le header, on pourrait avoir:  
# la date/heure de l'image  
# la taille de l'image qui sera attendue  
# le serial du transducteur utilisé  
# la fréquence du transducteur  
# le pas entre deux points  
# la version du kit  
# la version du firmware embarqué  
# le serial de la board/kit/release  
# les parametres à passer dans le scan conversion if any (à lister)  
# les parametres de l'app (ex: organe en train d'etre imagé, user, timestamp
côté app, ...)  
# ... j'en passe et des meilleures.  
  
Ca permettrait d'avoir une continuité des données dans le temps, malgré les
évolutions qu'on pourrait avoir - un interêt certain.  
  
Si ca branche quelqu'un de définir le cadre du format, qu'il fasse signe!
Sinon, je peux créer la page de Challenge correspondant.  
  
Topette et bonne fin de week end =)  
  
Hyacinthe



### **Hyacinthe Lacenne** on November 9, 2015:



hey, c intéressant, ce d'autant que Hyacinthe Hyacinthe, sans le formuler de  
cette manière, semble partant sur une réflexion de cette nature.  
  
d'un autre côté, à des fins de standardisation, il y a l'option dicom - on  
pourrait regarder des points d'intersections avec orthanc  
&lt;[http://www.orthanc-server.com/&gt;](http://www.orthanc-server.com/>)  
  
@hyacinthe quels sont selon toi les pros/cons ?  
  
[image: photo]  
*Hyacinthe Lacenne*  
Club JADE  
+33630371100 | [lacenne@clubjade.fr](mailto:lacenne@clubjade.fr) | [www
.club-jade.fr](http://www.club-jade.fr) | 10 rue Gustave  
Rouanet, 75018  
&lt;[http://www.facebook.com/pages/Club-
Jade/281050951907640?fref=ts&gt;](http://www.facebook.com/pages/Club-
Jade/281050951907640?fref=ts>)  
&lt;[http://twitter.com/club_jade&gt;](http://twitter.com/club_jade>)  
Get a signature like this: Click here!  
&lt;[http://ws-
promos.appspot.com/r?rdata=eyJydXJsIjogImh0dHA6Ly93d3cud2lzZXN0YW1wLmNvbS9lbWFpbC1pbnN0YWxsP3dzX25jaWQ9NjcyMjk0MDA4JnV0bV9zb3VyY2U9ZXh0ZW5zaW9uJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPXByb21vXzU3MzI1Njg1NDg3Njk3OTIiLCAiZSI6ICI1NzMyNTY4NTQ4NzY5NzkyIn0=&gt;](http
://ws-
promos.appspot.com/r?rdata=eyJydXJsIjogImh0dHA6Ly93d3cud2lzZXN0YW1wLmNvbS9lbWFpbC1pbnN0YWxsP3dzX25jaWQ9NjcyMjk0MDA4JnV0bV9zb3VyY2U9ZXh0ZW5zaW9uJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPXByb21vXzU3MzI1Njg1NDg3Njk3OTIiLCAiZSI6ICI1NzMyNTY4NTQ4NzY5NzkyIn0=>)  
  
Le dim. 8 nov. 2015 à 22:38, Hyacinthe Lacenne (Basecamp) &lt;



### **Hyacinthe Lacenne** on November 9, 2015:



Yop  
  
Pour il ne serait pas abérrant de partir sur notre propre format  
échographie, sur la base des points ci-dessus, et d'avoir un bout de code  
qui convertisse notre format en format DICOM. Notre format pourrait  
contenir les raw data et parametres internes de prise d'image, que DICOM ne  
prendrait pas forcément en compte a priori.  
Pour nous en effet, et ce à des vues encore une fois de péréniser notre  
historique d'images, il faudrait pouvoir dumper toutes les données  
importantes relatives à la prise d'image dans le même fichier image, ce qui  
ne se reflete pas forcément dans le DICOM.  
  
Wala =)  
  
2015-11-09 0:25 GMT+01:00 Hyacinthe Lacenne (Basecamp) &lt;



### **Hyacinthe Lacenne** on November 9, 2015:



gat it  
  
tintopette  
  
[image: photo]  
*Hyacinthe Lacenne*  
Club JADE  
+33630371100 | [lacenne@clubjade.fr](mailto:lacenne@clubjade.fr) | [www
.club-jade.fr](http://www.club-jade.fr) | 10 rue Gustave  
Rouanet, 75018  
&lt;[http://www.facebook.com/pages/Club-
Jade/281050951907640?fref=ts&gt;](http://www.facebook.com/pages/Club-
Jade/281050951907640?fref=ts>)  
&lt;[http://twitter.com/club_jade&gt;](http://twitter.com/club_jade>)  
Get a signature like this: Click here!  
&lt;[http://ws-
promos.appspot.com/r?rdata=eyJydXJsIjogImh0dHA6Ly93d3cud2lzZXN0YW1wLmNvbS9lbWFpbC1pbnN0YWxsP3dzX25jaWQ9NjcyMjk0MDA4JnV0bV9zb3VyY2U9ZXh0ZW5zaW9uJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPXByb21vXzU3MzI1Njg1NDg3Njk3OTIiLCAiZSI6ICI1NzMyNTY4NTQ4NzY5NzkyIn0=&gt;](http
://ws-
promos.appspot.com/r?rdata=eyJydXJsIjogImh0dHA6Ly93d3cud2lzZXN0YW1wLmNvbS9lbWFpbC1pbnN0YWxsP3dzX25jaWQ9NjcyMjk0MDA4JnV0bV9zb3VyY2U9ZXh0ZW5zaW9uJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPXByb21vXzU3MzI1Njg1NDg3Njk3OTIiLCAiZSI6ICI1NzMyNTY4NTQ4NzY5NzkyIn0=>)  
  
Le lun. 9 nov. 2015 à 09:16, Hyacinthe Lacenne (Basecamp) &lt;



