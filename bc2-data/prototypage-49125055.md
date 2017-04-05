## scan conversion



hello,  
  
@loic : j'ai complété le code /* methode make_interpolation()*/ pour processer
les data  
  
j'ai corrigé de nombreux paramètres - j'obtiens une image de type echographie
mais très déformée.  
@hyacinthe : il faut donc régler les paramètres - on fait cela demain ?  
  
@loïc : j'ai isolé le code dans un module, ce qui permettra aux contributeurs
de tester leur solutions sans avoir à démarrer `Android`.  J'ai pushé sur une
branche `scan_conversion`. Qd on sera satisfait, on mergera  ou on l'isolera
dans un autre repo ;)  
  
  
a++



### **Loïc Fejoz** on October 6, 2015:



@medhi chouette !  
D'où venaient les erreurs de paramètres ? unités ou approximations ?



### **Hyacinthe Lacenne** on October 6, 2015:



oui essentiellement de variables en `float` qui ne suffisaient pas - je les  
ai passées en double - et je modifie asap le code pour passer les `float`  
en `double`.  
  
Ceci étant, j'ai encore un gros travail avec Hyacinthe pour ajuster finement  
les paramètres ;)  
  
Le mar. 6 oct. 2015 à 07:54, Loïc Fejoz (Basecamp) &lt;



### **Hyacinthe Lacenne** on October 7, 2015:



après ajustement de paramètres par @hyacinthe la scan conversion fonctionne  
  
le code est pushé  
  
en terme de perf on est à 83ms... j'ai indiqué le point de départ et de fin de
la mesure de façon qu'on soit cohérent  
  
il y a de la marge mais ca fonctionne  
  
@++



### **Hyacinthe Lacenne** on November 19, 2015:



Y'a un truc chouette aussi sur ce sujet :  
<http://www.engineeringtv.com/video/Texas-Instruments-Open-Source-2>  
=)



### **Hyacinthe Lacenne** on November 19, 2015:



yes, je connaissais, super initiative - de mémoire, il me semble que le  
code n'est plus entretenu, n'est plus up to date. Je contre-checke  
  
@++  
  
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
  
Le jeu. 19 nov. 2015 à 00:00, Hyacinthe Lacenne (Basecamp) &lt;



### **Hyacinthe Lacenne** on November 19, 2015:



C'est pas sur une puce dédiée leur SC ? Je crois que c'était sur  
<http://www.ti.com/lit/an/sprab32/sprab32.pdf>  
Jme trompe peut etre :/



