## Workshop 24.11 - Update



Hello all,  
  
Suite à notre réunion ce matin avec Muriel, voici le lien de la page du wiki
mise à jour :
<http://echopen.org/index.php?title=CAPTech#16.00_-_17.00_.7C_Enjeux_communautaires>  
  
Il manque encore le détail des critères / contraintes techniques (sur lesquels
Hyacinthe travaille actuellement).  
  
Globalement, son approche est :  
1\. L'atelier du matin : Spec image + critères généraux + critères médicaux +
risques médicaux =&gt; Spéc de la sonde =&gt; Solution-s technique-s (livrable
sous forme d'un matrice)  
2\. Architecture en 6 meta-modules + 16 modules =&gt; Challenger =&gt; \+
critères / contraintes tech =&gt; Architecture fonctionnelle et architecture
d'interface validée =&gt; Arbre de développement + balises + plan de release
=&gt; ROADMAP  
  
Voilà en résumé les deux phases tech du 24, qui reprennent exactement ce que
nous avions dit avec un brin de méthode en sus. Les détails des critères /
contraintes générales, médicales, risques, etc. sont sur la page wiki du
workshop.  
  
**LES BESOINS : **  

  1.  Définir les besoins médicaux (spéc de l'image) - MEB + PIB
  2. Finir de lister les contraintes / critères techniques - JED

  
Vos remarques sont le bienvenues et si vous avez des incompréhensions, dites
le moi.  
  
@+



### **Hyacinthe Lacenne** on November 17, 2015:



top !  
  
on est d'accord que l'arbre de dev et le plan de release sera un output de  
la synthèse du workshop, soit un peu après ?  
  
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
  
Le mar. 17 nov. 2015 à 15:20, Hyacinthe Lacenne (Basecamp) &lt;



### **Hyacinthe Lacenne** on November 17, 2015:



Oui, si consensus à la fin =&gt; On a une solution. Si pas consensus =&gt; On
se  
laissera le temps d'affiner et de choisir la solution tech.  
  
Le mar. 17 nov. 2015 à 15:40, Hyacinthe Lacenne (Basecamp) &lt;



### **Hyacinthe Lacenne** on November 17, 2015:



perfect  
  
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
  
Le mar. 17 nov. 2015 à 15:53, Hyacinthe Lacenne (Basecamp) &lt;



### **Hyacinthe Lacenne** on November 17, 2015:



Voilà le premier jet du schéma de Hyacinthe remis en forme pour montrer l'impact
des critères de l'image sur les autres éléments. Ce sont les impacts directs
uniquement ;)  
  
Bravo à Hyacinthe,  
  
Vos remarques sont les bienvenues... Dès qu'on a les info, on complète et
ensuite on liste les critères... Et on est bon pour un envoi des ressources
rapidement.  
  
@+



### **Hyacinthe Lacenne** on November 17, 2015:



Je dirais, à rajouter pour clarifier,  
adc: fréquence d'échantillonnage  
Display: paramétres physiques pour scan conversion !  
Le 17 nov. 2015 18:20, "Hyacinthe Lacenne (Basecamp)" &lt;



### **Hyacinthe Lacenne** on November 18, 2015:



Merci Hyacinthe,  
Peux tu préciser ?  
En noir =&gt; Un critère image  
En couleur =&gt; Le critère impacté du module considéré.  
  
Du coup,  
  
Fréquence d'échantillonnage est impacté par quel info sur l'image ? idem pour
les paramètres physique du scan conversion ?  
  
Merci



### **Hyacinthe Lacenne** on November 18, 2015:



ADC: fréquence d'échantillonnage - en rouge car spec du module  
Display: paramétres physiques pour scan conversion, au même niveau que
affichage, en bleu =)



### **Hyacinthe Lacenne** on November 18, 2015:



Je n'ai pas mis la fréquence d'échantillonnage car c'est un impacte de second
niveau (résolution -&gt; fréquence du transducteur -&gt; fréquence
d'échantillonnage). Et les paramètres physiques sont redondant avec la
position pour moi.



### **Hyacinthe Lacenne** on November 18, 2015:



Merci Hyacinthe, en effet, ce ne sont que les impacts de niveau 1 =&gt; direct  
impacts  
  
@Hyacinthe, du coup, je te laisse imaginer :  
\- Les impacts de niveau 2 et + si besoin  
\- Finir la liste des questions  
  
Merci.  
  
Le mer. 18 nov. 2015 à 10:39, Hyacinthe Lacenne (Basecamp) &lt;



### **Hyacinthe Lacenne** on November 18, 2015:



Je vais faire pour chaque module le même type de schéma pour montrer l'impacte
de chaque décision sur chaque élément.



### **Hyacinthe Lacenne** on November 18, 2015:



Top. Merci. tu me l'envois dès que tu as fini et je mets en forme ?  
  
@+  
  
Le mer. 18 nov. 2015 à 10:47, Hyacinthe Lacenne (Basecamp) &lt;



### **Hyacinthe Lacenne** on November 18, 2015:



  
Hello All,  
  
Voilà la nouvelle version du schéma des impacts directs revue et corrigé avec
vos remarques + ajout des éléments de définition de l'image  
  
A vos remarques.  
  
=&gt; Objectif : finaliser le programme pour relance des participants d'ici
demain soir et re-mobilisation des participants hésitants.



### **Hyacinthe Lacenne** on November 18, 2015:



Dans cette image, tu ne fais pas de distinction entre focal et profondeur de
mesure. Ce n'est pas la peine de mettre la focale ici.  
La valeur du frame rate n'est pas bonne (Hyacinthe à confondu avec l'échelle
d'affichage de la puissance).



### **Hyacinthe Lacenne** on November 18, 2015:



Merci.  
  
@Hyacinthe, c'est corrigé. btw, qu'entends tu par "Une typo though"  
@Hyacinthe, merci, Hyacinthe m'a donné l'info. J'ai pas saisie ce que je dois  
changer suite à ta remarque : "Dans cette image, tu ne fais pas de  
distinction entre focal et profondeur de mesure. Ce n'est pas la peine de  
mettre la focale ici."  
  
Merci.  
  
Le mer. 18 nov. 2015 à 14:48, Hyacinthe Lacenne (Basecamp) &lt;



### **Hyacinthe Lacenne** on November 18, 2015:



Ici profondeur et focale sont identiques. En fait pour faire une mesure entre
5 et 20 cm, ta focale devrait être de 12.5 cm. C'est à peu près le centre de
ta mesure.



### **Hyacinthe Lacenne** on November 19, 2015:



Yo all,  
  
Voilà la nouvelle version. A priori on est bon.  
  
On fini avec Hyacinthe ce matin de caler l'ensemble des éléments et questions
pour le 24 et on envoie.  
  
@+  
O.



### **Hyacinthe Lacenne** on November 19, 2015:



top !  
  
Le jeu. 19 nov. 2015 à 10:12, Hyacinthe Lacenne (Basecamp) &lt;



### **Hyacinthe Lacenne** on November 19, 2015:



Bonsoir à tous,  
  
Voici le lien du programme et des ressources pour le workshop de mardi. Dites
moi ce que vous en pensez !!  
  
<http://echopen.org/index.php?title=CAPTech>  
  
L'idée est d'envoyer ça demain pour relance des participants.



### **Hyacinthe Lacenne** on November 19, 2015:



yes ca a de la gueule ;)  
  
l'effet de style pyramidal était voulu ;) ?  
  
\- size  
\- weight  
\- autonomy  
\- image quality  
\- probe ergonomy  
\- software ergonomy  
  
@++  
  
Le jeu. 19 nov. 2015 à 19:09, Hyacinthe Lacenne (Basecamp) &lt;



### **Hyacinthe Lacenne** on November 19, 2015:



C'est un pure hasard, je n'avais même pas fait gaffe... C'est marrant



### **Hyacinthe Lacenne** on November 20, 2015:



Lolz =)  
  
BTW, comment se cloture la journée? Remerciements entre 17:00 et 17:30 ?  
  
Bonne nuit!



### **Hyacinthe Lacenne** on November 20, 2015:



Je ne sais pas encore comment on clôture mais globalement, j'imagine qu'on  
peut en effet faire un remerciement ;) In peut aussi penser que certains  
auront envi de continuer à discuter... Mais gardons en tête que notre point  
principal est d'obtenir des solutions tech et dans l'idéal un consensus sur  
une orientation.  
  
J'ai eut la confirmation que Chiraz serait la à 14.00 pour l'atelier  
principal.  
  
Le ven. 20 nov. 2015 à 01:34, Hyacinthe Lacenne (Basecamp) &lt;



