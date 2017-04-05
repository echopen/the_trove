## Multiplicateur de tension



@Na voici un petit document sur des circuits pour multiplier la tension.



### **Hyacinthe VINCENT** on November 19, 2015:



J'avais aussi trouvé des choses autour de circuits spécialisés (boost
controllers, DC-DC converters) comme le MAX1522 de chez MAXIM:  
  
<https://www.maximintegrated.com/en/products/power/switching-
regulators/MAX1522.html/tb_tab0>  
  
[http://uk.rs-online.com/web/c/semiconductors/power-management-ics/boost-
converters/#esid=4294957842&amp;applied-
dimensions=4294442347,4294486807,4294506514](http://uk.rs-
online.com/web/c/semiconductors/power-management-ics/boost-
converters/#esid=4294957842&applied-
dimensions=4294442347,4294486807,4294506514)  
  
<https://www.maximintegrated.com/en/app-notes/index.mvp/id/3425>  (juste le
deuxième étage)  
  
Il me manque une donnée :  

  * un ordre de grandeur du courant absorbé par le piezo.  

  * contrainte de temps de monté et surtout du temps de descente du créneau d'excitation. Peut-être qq chose comme 1/4 de la période propre ?

  
Hyacinthe



### **Hyacinthe Lacenne** on November 19, 2015:



Tu vas trouver des infos ici :
<http://echopen.org/index.php?title=Category:Transducer>.  
  
On veut un pulse d'environ -100 V et un durée de la moitié de la période (100
ns) idéalement.



### **Hyacinthe VINCENT** on November 20, 2015:



Est-ce que l'on doit comprendre, d'après le document (Re(Z) = 9.29 Ohms), que
l'on aurait un pic de 10A sous 100V ?



### **Hyacinthe Lacenne** on November 21, 2015:



Attention, impédance complexe, il faut prendre la partie reelle, imaginaire,
et la fréquence en compte pour faire les calculs =)



### **Hyacinthe VINCENT** on November 23, 2015:



Alors, à la louche, ça donne quoi ?



