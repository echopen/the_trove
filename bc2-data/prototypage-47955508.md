## Taille de l'image



Hello!  
  
Petite challenge sur la définition de l'image: step 1: vérifier les conditions  
  
**Hypothèses : **  

  * Notre transducteur focalise sur une zone de 1x1mm
  * On acquiert une image sur un angle de 60°
  * On cherche à aller jusqu'à 10cm
  * On utilise 3 transducteurs

  
**Calculs**  

  1. Si on a une ouverture de 60°, on a à la louche 10cm d'ouverture à 10cm de profondeur (triangle équilateral). Ca veut dire qu'on doit avoir une image brute à la louche de 100x100 pixels. Arrondissons à une image brute de 128 lignes de 1x128 pixels.
  2. 128px de profondeur est bien, mais on overkill l'image à profondeur moyenne si on prend 128 lignes/image, puisque sur la moitié supérieure de l'image on aura un suréchantillonage. Prenons donc 64 lignes par image.
  3. A notre fréquence de travail, prenant 1500m/s, 1mm représente 0,67µs. Un pixel couvre donc 0.67µs. Ca veut dire que pour nos 128px, on a une durée d'acquisition de 2x128x0,67µs ~ 170µs. Le x2 vient du fait qu'un point à 128px donne un signal due à un écho qui fait deux fois la distance  (aller puis retour)
  4. Pour du 10img/s avec 1 transducteur, acceptable pour le proto of course), on fait donc une image sur 1/6eme du temps, donc pour faire 1/6eme de tour il faut 16ms. 16ms pour 64 lignes, ca donne 0.26ms/ligne, ou encore 260µs/ligne.
  5. Ca veut donc dire qu'on a un tir qui est fait toutes les 260µs, et qu'on écoute le retour sur 170µs.

  
A priori, les conditions de prise d'image à 10cm, sont bien de prendre une
image de 64x128px, sur un moteur qui tourne à 10trs/s (ce qui est déjà .. pas
mal).  
  
Que pensez vous du calcul? Discussion ouverte :)  
  
Bon we !  
  
Hyacinthe



### **Hyacinthe Lacenne** on September 14, 2015:



Ping pour des questions si besoin ce soir :)



