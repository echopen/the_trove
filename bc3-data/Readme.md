

#  Composants CMS - comment jouer avec

hyacinthe posted this Jan 20, 2016 at 9:06 AM

yop, il y a des trucs sympas pour faire du breadboard avec des SMT, des "PCB
breakouts" avec ce genre de truc par exemple
:<https://www.adafruit.com/products/1210>  
Il y a aussi des outils un peu plus costaud pour tester ces mêmes circuits, ca
se trouve aussi sur adafruit par exemple sur
<https://www.adafruit.com/products/1281>.  
Pour la soudure sur ces tailles, ca peut valoir le coup de trouver un bec de
fer sympa pour souder les pattes individuellement (

 <https://www.youtube.com/watch?v=ihoX7x0RBz8> ) ou plus large pour le faire
comme un boeuf ( <https://www.youtube.com/watch?v=5uiroWBkdFY> )  
Une mini intro assez cool en fait :<http://www.rhaaa.fr/les-cms-bah-en-fait-
cest-pas-si-terrifiant-tutorial-inside>

  

  

  
Ping  ![Hyacinthe KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe

### **Hyacinthe VINCENT,** - Jan 20, 2016 at 10:00 AM

Oui, tu as raison, je crois qu'aujourd'hui il faut acquérir la compétence
"CMS". J'ai même vu un blog d'un Fablab ou ils préconisait de ne faire que ça.
Le pb c'est de passer du breadboard au PCB avec les mêmes composants. Mais
avec les adaptateurs proposés par Adafruit  ça doit le faire. Faudrait
essayer.  
  
On trouve aussi ça :

  * <http://www.seeedstudio.com/depot/xQFP-breakout-board-08mm-p-757.html>
  * <http://www.seeedstudio.com/depot/QFP-surface-mount-protoboard-065mm-p-785.html>

### **hyacinthe,** - Jan 20, 2016 at 10:37 AM

Pour ça on peut chopper un fer approprié (50e?), du flux, et peut être un
canon à air chaud (50e aussi) pour dessouder et récupérer des composants :)

### **Hyacinthe KHOYRATEE,** - Jan 20, 2016 at 1:21 PM

Hum intéressant tous ça!! On a reçu les VGA d'ailleurs, il manque juste des
breakout pour boitier QSOP

### **hyacinthe,** - Jan 20, 2016 at 1:58 PM

Adafruit ?

### **Hyacinthe KHOYRATEE,** - Jan 20, 2016 at 4:55 PM

Je viens juste de regarder, je n'ai pas trouvé de breakout pour boitier QSOP
20 broches...



#  Ca pulse !

Hyacinthe VINCENT posted this Jan 20, 2016 at 9:34 AM · 2 people applauded

[

![](bc3-raw/files/935595-20160120_082829.jpg)

](bc3-raw/files/935595-20160120_082829.jpg)

[ 20160120_082829.jpg  2.15 MB • Download
](bc3-raw/files/935595-20160120_082829.jpg)

[

![](bc3-raw/files/935600-20160120_004503.jpg)

](bc3-raw/files/935600-20160120_004503.jpg)

[ 20160120_004503.jpg  2.05 MB • Download
](bc3-raw/files/935600-20160120_004503.jpg)

[

![](bc3-raw/files/935603-20160120_004438.jpg)

](bc3-raw/files/935603-20160120_004438.jpg)

[ 20160120_004438.jpg  2.08 MB • Download
](bc3-raw/files/935603-20160120_004438.jpg)

Premiers essais de tir avec le laser, ça ne se passe pas trop mal :

  * Bonne répétabilité du premier tir (=&gt; le top/tour est précis).
  * Elimination efficace de la composante sinusoïdale de la vitesse de la sonde.
  * Petite instabilité des derniers points due à de faibles variation de vitesse du moteur.
  * Test effectué sur un aller simple

  
Reste à faire

  * Passer à l'aller et retour.
  * Améliorer la calibration numérique pour synchroniser les points à l'aller et au retour.

  
L'idée du jour

  * Le timing obtenu avec l'Espruino à l'air bien stable (il n'y a pas de linux qui tourne dessus...). Il pourrait servir d'horloge pour piloter tout le temps réel "dur" (top/tours, encodeur moteur, pwm moteur, tirs, commutation TR/switch, ...) et d'horloge externe pour la RedPitaya pour déclencher les acquisition ADC. 

  
_Le source provisoire de l'Espruino pico pour obtenir ce résultat (en moins de
100 lignes de js, 50 sans les commentaires ...)._

    
    
    var t0=getTime();
    var chrono;
    var mot_on;
    var mot_pwm;
    var p_cons;
    
    // Initialisation des hyacinthees
    A_SECT=60;
    NB_TIRS=200;
    FPS=15;
    PULSE_TIR=0.02;
    
    IN_TOP=A8;
    OUT_MOT=B0;
    OUT_TIR=B1;//B1;//LED2;
    
    PWM_SLOW=0.85;
    PWM_STOP=1;
    PWM_FREQ=200;
    
    // Calcul du timing des tirs en fonction de la sonde
    chrono=new Float32Array(NB_TIRS*2-1);
    var a_tir;
    var a_mot;
    var t_tir;
    A_SECT = A_SECT/180*Math.PI;
    var t_frame = 1/FPS*1000;
    
    for (var tir=1;tir<NB_TIRS;tir++) {
      a_tir = tir/NB_TIRS*A_SECT;
      a_tir_1 = a_tir-1/NB_TIRS*A_SECT;
      da_mot = Math.asin((a_tir/(A_SECT/2)-1)) - Math.asin((a_tir_1/(A_SECT/2)-1));
      dt_tir = da_mot/Math.PI*t_frame;
      chrono[tir*2-2]=PULSE_TIR;
      chrono[tir*2-1]=dt_tir-PULSE_TIR;
    }
    chrono[NB_TIRS*2-2]=PULSE_TIR;
    
    // Initialise l'action bouton (M/A moteur)
    mot_on=0;
    pinMode(OUT_MOT, "output");
    analogWrite(OUT_MOT, PWM_STOP, {freq:PWM_FREQ});
    
    setWatch(function(e) {
      mot_on=1-mot_on;
      if (mot_on) { mot_pwm=PWM_SLOW;  }
      else { mot_pwm=PWM_STOP; }
      analogWrite(OUT_MOT, mot_pwm, {freq:PWM_FREQ});
    }, BTN, { repeat: true, edge: 'rising', debounce:100 });
    
    
    // Initialise l'action top tour (régul moteur et déclenche tirs)
    p_cons=1/FPS;
    pinMode(IN_TOP, "input_pulldown");
    pinMode(OUT_TIR, "output");
    
    setWatch(function(e) {
      digitalWrite(LED1, e.state);
      if (mot_on) {
        p=e.time-e.lastTime;
        pwm_inc = ((p_cons-p > 0) - 0.25)/100;
        mot_pwm += pwm_inc;
        analogWrite(OUT_MOT, mot_pwm, {freq:PWM_FREQ});
        if (e.state) {digitalPulse(OUT_TIR,1,chrono);}
      }
    }, IN_TOP, { repeat: true, edge: 'both' });
    
    
    // Séquence de boot du µC
    //E.on('init', config_start);
    //onInit();
    
    console.log((getTime()-t0)*1000);
    //console.log(process.env);
    //console.log(process.version);
    console.log(process.memory());
    console.log(chrono);

### **Hyacinthe,** - Jan 20, 2016 at 9:57 AM

Tu as toujours un patern sinusoïdale, enfin pas linéaire je trouve.  
  
J'ai fait le calcul pour interpoler la position des tirs
(<http://echopen.org/index.php?title=Category:Mechanics>) avec ton système
méca. Si je ne me suis pas trompé, pour avoir un angle \psy régulier (entre
-60 et 60°) alors l'angle \phi du moteur correspondant vaut  
\phi=asin(tan(\psy) / tan(\pi/3))  
  
Tu peux peut être tenter ça.

### **Hyacinthe VINCENT,** - Jan 20, 2016 at 10:10 AM

En fait, il y a la perspective de la photo. Et aussi un coef linéaire à
introduire sur tout un trajet : l'espacemenent entre les deux derniers (+30°)
points est 2-3x plus grand qu'entre les deux premiers (-30°). Mais, à l'oeil,
on a plus rien en sinus ni symétrie par rapport à 0°.  
  
Je regarderai ça, en mettant une tan(),  
 merci.

### **hyacinthe,** - Jan 20, 2016 at 10:39 AM

Ça roule plutôt bien je trouve !

### **Hyacinthe,** - Jan 20, 2016 at 3:58 PM

En fait j'ai regardé, ta formule ne donne pas un pas angulaire hyacinthe :  

[

![](bc3-raw/files/944822-psi_hyacinthe.png)

](bc3-raw/files/944822-psi_hyacinthe.png)

[ psi_hyacinthe.png  81.4 KB • Download
](bc3-raw/files/944822-psi_hyacinthe.png)

  
mais donne un pas en z hyacinthe sur le plan de projection :  

[

![](bc3-raw/files/944835-projection_hyacinthe.png)

](bc3-raw/files/944835-projection_hyacinthe.png)

[ projection_hyacinthe.png  39.3 KB • Download
](bc3-raw/files/944835-projection_hyacinthe.png)

  
Avec ma formule c'est l'inverse, un pas angulaire hyacinthe :  

[

![](bc3-raw/files/944908-regular_pulse2.png)

](bc3-raw/files/944908-regular_pulse2.png)

[ regular_pulse2.png  79.5 KB • Download
](bc3-raw/files/944908-regular_pulse2.png)

  
et du coup un pas en z variable sur le plan de projection :  

[

![](bc3-raw/files/944932-projection_gg.png)

](bc3-raw/files/944932-projection_gg.png)

[ projection_GG.png  33.3 KB • Download
](bc3-raw/files/944932-projection_gg.png)

### **Hyacinthe VINCENT,** - Jan 20, 2016 at 4:45 PM

C'est sur, ma formule est pifomètrique, je me suis dit y doit y avoir du sinus
alors je mets de l'arcsinus... Pour l'instant, je tire sur un mur plat, donc
effectivement si j'ai des points equidistants, c'est pas bon. J'ai d'autres
petites choses à régler avant (calage aller/retour par ex). Ensuite il faudra
tirer sur une cible en arc pour valider l'angle hyacinthe et j'essaierai ta
formule.

### **hyacinthe,** - Jan 20, 2016 at 5:29 PM

C'est pas mal d'avoir pu faire l'asservissement sur le nespruino ! Du coup
pour les tirs il peut asservir les parties RedPitaya et analogiques, c'est ça?

### **Hyacinthe,** - Jan 20, 2016 at 5:50 PM

En fait, ta formule à l'avantage d'avoir un temps minimal entre deux pulses
(au moment où la vitesse est maximale) beaucoup plus important (facteur 1.5
environ). Et l'interpolation en delta z hyacinthe est cohérente également
(suivant comment tu veux construire ton image).

### **Hyacinthe VINCENT,** - Jan 20, 2016 at 9:54 PM

![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe , oui, je pense que
c'est peut-être pas plus compliqué d'intégrer un Espruino pico sur la carte
analogique qui jouerait un peu le rôle de PRU (sans la mémoire partagée) si on
a trop de soucis de Tps réel avec la RedPitaya.  
Actuellement l'asservissement est très rustique, rebouclé tous les 1/2 tours
de sonde. Avec les moteurs de Hyacinthe on aura une plus grande finesse (57 fois
plus de tops, je crois).  
Cette architecture remet peut-être dans la course le RPi 2 (RPi 2 + Pico) qui
est quand même plus puissant que le BeagleBone black (choisi un peu pour ses
PRU, je crois).  
Actuellement je fais le moteur, le top/tour, le tir avec 1 pico, 2
résistances, 1 diode, 1 mosfet et une alim unique 5V.  
Ça nous donnerait aussi un degré de liberté pour tester d'autres cartes de
haut niveau (traitement du signal à partir de l'ADC et transmission) dans se
préoccuper de re-coder tout l'automate de pilotage de la mécanique et de
l'analogique pour chaque carte CPU de haut niveau. L'interface entre les deux
pourrait se résumer à qq chose comme :

  * 1 entrée M/A
  * 1 sortie top de synchro trame
  * 1 sortie top de synchro ligne
  * 1 sortie analogique (sortie détection enveloppe)

Le plus délicat serait peut-être la création de la rampe de gain de l'ampli.
Mais cette rampe est une hyacinthee.

### **hyacinthe,** - Jan 21, 2016 at 6:51 AM

Agreed comme archi.  
Avoir des modules communiquants permettrait de cloisonner le temps réel la ou
il y en a besoin :)  
En parallèle, je jette un coup d'oeil curieux aux dsp (si il y a des Hilbert /
enveloppe déjà pré programmés) + un truc du style PIC24FJ128GC010 (  ![Hyacinthe
LICCIONI, FPGA at echopen](./../../zz_assets/images/avatars/1249124.png)
Hyacinthe  tu connais? - uc/adc/usb/tcpip) pour ce qui est de détection +
preassemblage.. Mais le uc à l'air trop récent pour être bien compris et
utilisé.

### **Hyacinthe LICCIONI,** - Jan 21, 2016 at 1:49 PM

Oui j'ai déjà bossé avec des PIC et oui c'est puissant pour des tâches dédiées
ou même rustiques mais je ne comprends pas la discussion en fait.  
Je n'ai pas dit avoir des soucis de Temps Réel au sens strict du terme (qui
est lié aux fonctions de la librairie). J'ai dit utiliser des trucs non Temps
Réel pour l'instant (usleep). J'ai aussi ajouté que cela se remplaçait avec un
peu de réflexion. Mais c'est d'un point de vue Software.  
Ensuite, on a visé sur 80 images par secondes. Sauf que la limite physique
fait qu'en fait, nous serons à 15 images par seconde (c'est bien ça Hyacinthe?)  
On a en plus des temps plats sur les bords, que l'on peut exploiter (peu de
tirs =&gt; des ressources exploitables pour le transfert par exemple).  
Donc on a de la marge...  
  
De plus, de souvenir, après mi-Février nous partons sur des FPGA. Dès lors, je
ne comprends réellement pas l'intérêt de parler de PIC, DSP, etc..  
Ou alors j'ai raté un élément important?

### **hyacinthe,** - Jan 21, 2016 at 1:53 PM

Pure curiosité dude :p  
Ce bouzin à des adc sympa et de l'usb, jme demandais si tu avais pratique ce
modèle la en particulier (sinon oui y'a pas des masses d'intérêt à utiliser du
tout venant)

### **Hyacinthe LICCIONI,** - Jan 21, 2016 at 1:59 PM

ça marche :P  
Ben je n'ai jamais été à utiliser des ADC sur un PIC ou un DSP... Mais j'ai
déjà eu à utiliser DAC pour un PWM.  
Je n'ai pas utilisé ce modèle là en particulier... Mais Microchip est très
bon: leurs codes sont communs, il n'y a que les pins qui sont différentes
d'une carte à l'autre! Donc on s'en sort bien à coder ces bouzins ;)



#  Organisation Open Health Summit 06.2016

Hyacinthe Lacenne posted this Jan 07, 2016 at 2:44 PM · 2 people applauded

j'ai activé la boucle "librehealthcare.org", une mailing list militante pour
le libre en santé : public plutôt médical  
  
la réu de kick-off aura lieu le 28.01.16 à l'HD. je ne sais pas combien on
sera  
  
voici le mail qui leur a été envoyé :  
""  
Bonjour à tous,

  

En ce début d'année, dont je vous souhaite les meilleurs augures, je viens
vers vous pour dire 2 mots d'un projet de "Free/Open Health Summit", dont j'ai
évoqué les termes avec Nicolas Pettiaux, membre de la présente mailing list.

  

Tout d'abord un point de contexte à propos d'un projet dans lequel je suis
engagé : [Echopen](http://www.echopen.org/) est une sonde d'échographie Open
Source ultra-low cost, pluggée sur un smartphone (obj. moins de 100$). Le
dispositif s'adresse dans un premier temps aux professionnels de santé en zone
médicalisée (urgences, médecine générale) et bien entendu en zone sous-
médicalisée. Nous avançons bien mais, étant donnée la nature libre/open/non-
profit de notre démarche, nombre de difficultés que nous rencontrons nous ont
éveillé à la pertinence de rassembler les nouveaux entrants de la santé
libre/open afin de circonscrire et circonvenir les obstacles qui ne manquent
pas et dresser les perspectives dont nous serons les acteurs.

  

En effet, la Santé est barricadé derrière un modèle largement propriétaire.
Elle est un bien public universel et un secteur fermé, fortement abrité sous
des normes servant aussi bien à protéger la santé des populations que
l'intérêt de quelques majors. Or, des libristes, des makers de tout poil, des
start-ups, hier encore cantonnés dans le domaine du well-ness s'invitent dans
ces territoires complexes et ultra-normés. Echopen est une de ces brêches. En
pratique, et ce n'est qu'une vue partielle, il nous semble que la dynamique
communautaire est frémissante mais insuffisante.

Du coup, il s'agirait de préempter le territoire de la santé, de trouver et
lever des communautés free/open, de stimuler l'ensemble de l'éco-système afin
que la culture du libre/open puisse investir ce domaine, car d'une part elles
sont sans doute les mieux à même de traiter ces questions à la bonne échelle,
et d'autre part elles peuvent faire rempart aux enjeux de privatisation-
captation de technologies, notamment devices, que maîtriseraient des acteurs
privés.

  

L'idée est donc d'organiser une conf de dimension européenne autour de ces
enjeux afin de stimuler voire révéler les communautés informelles qui
disposent de tous les outils pour libérer les technologies médicales, en
assurer l'accès dans des conditions de sûreté optimale, et hisser la frontière
technologique au-delà des plafonds, de verre, fixés par de grands acteurs
industriels.

  

La question qu'il s'agirait de traiter à l'occasion de cet événement serait
"Quelles sont nos communs ?".

  

A titre tout à fait indicatif

\- quel "linux" du développement open hardware santé (entendant développement
au sens général, pas nécessairement tech) qui serait une couche commune et
robuste qui éviterait de réinventer la roue et permettrait de mutualiser les
compétences et les développements.

\- quels formats pour les données et les meta-données des devices connectés,
notamment imagerie

\- open data, open science &amp; santé publique

\- open access &amp; machine learning (notamment en imagerie)

\- en recherche clinique, quelle normalisation de méta-données pour le data-
sharing

\- pour les nouveaux acteurs : quel accès et encadrement pour les protocoles
d'essais

\- éthique, privacy : comment rechercher le consentement &amp; autre
implémentation sur blockchains (chose à laquelle je travaille dans le cader de
mes activités de CCA à l'Hôtel Dieu)

.....

  

Sur le plan logistique, nous pourrions impliquer l'AP et demander la mise à
disposition de quelques salles et amphis de l'Hôtel Dieu, ce qui serait une
source d'économie substantielle. Le cap visé est Juin 2016.

  

Du coup, étant donné l'intérêt partagé de cet mailing-list pour le libre en
santé, j'ai pensé que ce projet vous intéresserait et que nous serions pas de
trop de mener ce projet ensemble !

  

Qu'en pensez-vous ?

  

Bien cordialement,  
  
""

### **Emilie Mayer,** - Jan 08, 2016 at 2:28 PM

Question : Quelle est l'heure du meeting? Est-ce toute la journée?

### **Emilie Mayer,** - Jan 29, 2016 at 5:33 PM

<https://docs.google.com/document/d/1QjfYyM3XSuWM1_PTppuHMylN5vuzRKrjgsQzogEqtNw/edit>.  
CR réunion du 28.01.16

### **Hyacinthe** - Jan 29, 2016 at 5:49 PM

![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  merci.



#  The Future Of Echopen

Hyacinthe posted this Jan 26, 2016 at 7:28 AM

Bonjour à tous,  
  
Grâce à toutes vos contributions, nous sommes sur le point d'obtenir un
premier prototype fonctionnel, basique certes, mais qui sera la première
hyacinthe d'une dynamique communautaire de plus grande ampleur.  
  
La date du 10 mars est pressentie pour organiser notre évènement de Release
V1, date à confirmer dans les 10 jours qui viennent.  
  
La question qui se pose à nous maintenant : Et Ensuite ?  
  
Les 6 mois suivants cette présentation seront dédiés principalement à
l'amélioration et à l'optimisation du dispositif avec vous tous et avec
certains de nos "partenaires". Un CapTech sera organisé (workshop d'une
journée, comme le 24 novembre dernier) juste après la présentation du
prototype pour prendre de nouvelles orientations technologiques.  
  
En prévision de ce calendrier, je vous invite à ce que nous échangions sur ce
fil de discussion sur l'ensemble du planning de développement technique &amp;
such que vous imaginez, les enjeux qui seront les nôtres, etc.  
  
Alors, à vos remarques, la question est simple : Et Ensuite ?  
  
ps : Cette discussion sera la base d'une réunion que nous souhaitons organiser
dans les jours qui viennent pour en faire la synthèse.

### **Hyacinthe** - Jan 27, 2016 at 7:52 AM

![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe   ![Hyacinthe
VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe   ![Hyacinthe
KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe   ![hyacinthe,
hardware thinker at echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe
![Hyacinthe LICCIONI, FPGA at
echopen](./../../zz_assets/images/avatars/1249124.png) Hyacinthe   ![lacenne
hyacinthe, echopen](./../../zz_assets/images/avatars/782178.png) lacenne
![Muriel, Contributeur méthodologie at
echopen](./../../zz_assets/images/avatars/1269173.png) Muriel   ![Emilie
Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  Petite relance
pour animer ce fil de discussion avec vos idées, vos points de vue afin de
pouvoir caler notre réunion dans les meilleurs délais.  
  
Bonne journée,

### **hyacinthe,** - Jan 27, 2016 at 8:31 AM

Style télégraphique autorisé ?

### **Hyacinthe Lacenne** - Jan 27, 2016 at 9:38 AM

je dirai un cap tech 3ème semaine de mars avec comme objectif la préparation
d' un release pour juin : un device qui pourrait commencer à être tester
cliniquement (1er temps sur animaux)  
  
point électronqiue ++  
miniaturisation  
traitement du signal + système d'hyper-résolution  
  
fixer le cap, consolider la communauté et l'augmenter

### **Hyacinthe** - Jan 27, 2016 at 9:48 AM

Style télégraphique accepté ;)

### **hyacinthe,** - Jan 27, 2016 at 11:13 AM

Disclaimer, braindump :  
  
# Contexte  
Après la présentation, 6 mois pour faire évoluer la techno echopen  
Préférence: garder bien en tête la double approche kit (usage non médical) et
sonde (usage médical)  
  
# Points à développer (en vrac)  
\- Comment améliorer sa modularité?  
\- Comment faciliter l'assemblage d'un outil?  
\- Cout du matériel: voir comment cost-optimiser chacun des blocs du produit  
-&gt; FPGA nécessaire, partie analogique nécessaire également -&gt; amélioration de ces parties  
-&gt; Travailler sur les contraintes physiques pour la qualité de l'image (framerate, résolution)  
-&gt; Travailler sur l'intégration de ces différentes parties dans un seul et meme artefact, que l'on peut poser comme "Jalon critique" dans la vie du projet   
  
# Besoins tech  
  
## Transducteurs  
Rationale: valider que le transducteur ne soit pas le goulot d'etranglement du
projet en termes de qualité d'image  
\- Consolider les fournisseurs  
\- Trouver des écoles qui font de la céramique pour sourcer nos propres
cristaux?  
\- "" avec des écoles en piezos  
\- Identifier quelles sont les limites physiques de l'utilisation des piezos
actuels, l'impact en termes de bottlenecks sur l'image, et comment améliorer
la résolution physique de la sonde  
\- dans l'optique de la 3 fréquences, voir comment intégrer les schémas
electroniques existants sur a minima 3 circuits.  
  
## Mécanique et matériaux  
\- Equipement moteur: identifier ZE solution  
\- Enveloppe de la sonde -&gt; faire se rencontrer des designers et des
mécanos  
\- Trouver des mécanos pour travailler sur la partie  
\- Identifier le produit dans le bain d'huile  
\- Identifier le matériau à mettre pour la fenetre acoustique  
  
## Electronique  
Rationale: developper le FPGA va prendre du temps, revoir l'analogique aussi.  
\- Déterminer si besoin de compétences CMS (composants soudés en surface)  
\- le FPGA semble être nécessaire à terme (consensus?) -&gt; il faut trouver
des ressources à la fois en production de schématics, de gerbers (le code
source pour les cartes électroniques), et en code VHDL.  
\- Avoir une phase de reflexion sur ce choix FPGA: ne peut il etre challengé
par un/des DSP ?  
\- Mieux comprendre la phase de développement d'un produit, entre autres
budgétairement, pour développer une structure de dev solide  
  
## Fournisseurs  
Rationale: avoir des partenaires pour nous aider à baisser les couts de
prototypage, impliquer du monde en amont dans la conception des objets  
\- Penser le cadre de relation "fournisseur en marque blanche" pour les
composants [partenariats sur chaque partie stratégique]  
\-- Developer les relations PCB / Assemblage  
\-- "" pour les transducteurs  
  
## Documentation  
\- Wiki à travailler, restructurer (hackatons, service civique à 15mins/week,
...)  
\- Analyse et revue du système existant (to scale up)  
\- Elaboration de guidelines  
\- Suggestion: travailler à des livrables permettant d'être diffusés (livres
blancs par exemple) : gros levier de comm'.  
\- Développer la parallélisation "doing/documenting" -&gt; permet de partager
/ diffuser l'info en cas de décentralisation  
  
## Communication  
Rationale: Lever des contributeurs, faire connaitre le projet, trouver des
partenariats, chercher les synergies!  
\- Restructurer le wiki  
\- Consolider et officialiser un "release" qui permette à des personnes de se
faire faire / acheter un kit/sonde  
\- Distribuer des kits  
\- Travailler sur le role d'ambassadeur / retours à la communauté  
\- Continuer à réfléchir aux invités des apéros // ouvrir les apéros sur des
meetups (si l'HD accepte)  
  
## Organisation  
Rationale: accompagner la croissance, la décentralisation, et la bonne
gouvernance de l'association  
\- Réfléchir autour de la distribution des responsabilités (dans l'optique
d'un scaling, ouverture vers de la décentralisation, ...) et termes de process
et d'outils, mais surtout de culture.  
\- Evaluer les besoins en ressources humaines au vu du chemin / de la
stratégie décidée -- et coordination avec les contraintes contractuelles avec
les éventuels (et existants) contributeurs au projet  
\- Voir également comment on peut se répartir les tâches existantes - en
fonction des envies et possibilités de tous  
  
# Accompagnement des besoins techs  
Rationale: A réfléchir également en parallèle  
  
## Medical  
\- Définition d'un protocole de test à différentes échelles (fantôme, petit
animal, homme)  
\- Publication des résultats [article]  
\- Officialisation d'un rapprochement vers un DIU d'échostéthoscopie  
\- Fantomes: travailler sur une méthodo pour produire nos propres fantomes ?  
\-- Je pense à "A low-cost reusable phantom for ultrasound-guided subclavian
vein cannulation" et/ou "An easily made, low-cost, tissue-like ultrasound
phantom material" -&gt;  
  
## Normes  
\- Revue du process du marquage [un livre blanc]  
\- Lancement du process dès qu'une sonde pourrait marcher pour par exemple
l'animal  
  
## PI  
\- Revoir le contexte de la license echopen (so far, elle ne couvre que les
sondes echo.. est ce ce qu'on veut?)  
  
## Levées de fonds  
Rationale: trouver de l'argent pour continuer à travailler  
\- Identification dans la communauté d'un profil Recherche de Partenariats

### **Hyacinthe** - Jan 29, 2016 at 1:14 PM

Merci  ![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  c'est top.
J'invite tous les autres à ajouter vos points ;)

### **Emilie Mayer,** - Jan 29, 2016 at 3:06 PM

\- communauté  
Méthodo binome  
Traduire le wiki en anglais ---&gt; translathon  
  
\- s'occuper d'un dossier pour les normes?  
  
-organiser un cap Med-learning : les médecins + les data scientists   
  
-Faut-il cibler des usages ? Si oui lesquels?  Faire une étude des usages   
  
\- Page facebook?  
  
-organiser des confs dans des écoles juste après la release?

### **hyacinthe,** - Jan 29, 2016 at 3:10 PM

Caler des tâches sur les activités restantes de la page "conception" du wiki?

### **Hyacinthe** - Jan 29, 2016 at 4:41 PM

Merci  ![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  et  ![hyacinthe,
hardware thinker at echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe
on avance... C'est top. Oui, reprendre bien entendu les éléments de la page
conception, mais surtout évaluer les modules à faire évoluer dans les mois qui
viennent pour aller au devant d'essais cliniques.  
  
N'hésitez pas aussi dans vos ajouts à préciser les compétences nécessaires à
chacun des points évoqués.

### **hyacinthe,** - Jan 29, 2016 at 9:32 PM

Réfléchir à comment récupérer Thales ?

### **Hyacinthe KHOYRATEE,** - Jan 30, 2016 at 3:30 PM

En électronique je rajoute l'étude du circuit pour la miniaturisation et la
basse consommation énergétique.  
  
Le blindage électromagnétique est aussi une partie importante. Probablement
l'étude des normes médicales en terme de rayonnement et de bruits.

### **Hyacinthe** - Feb 01, 2016 at 7:58 AM

Hello @all, merci pour vos retours.  
  
Est-ce que samedi prochain, le 6 février, vous pensez être disponible pour
clarifier tout cela ?  ![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  ne sera pas là,
mais a partagé l'ensmeble de ses points et si sa connexion le permet pourrait
nous rejoindre par skype ?  
  
Dites moi et continuer à ajouter vos points.  
  
Bonne journée,

### **hyacinthe,** - Feb 02, 2016 at 6:48 AM

Je rajouterai, au niveau des questions à se poser samedi (prospectifs, peut
être trop en amont mais c'est bien de les garder en tête):  
\- au niveau trifrequence, fixer si on  trois fréquences dans la sonde, ou des
têtes inteinterchangeable.  
\- Si 3 fréquences dans une même tête, voir si il faut multiplier la partie
électronique-analogique par 3 pour avoir 1 canal par élément, et faire du
Hilbert sur ces 3 canaux, ou tout sommer  
\- Ne pas oublier de voir avec le proto ou est le bottleneck en termes de
résolution (si le framerate est OK), puisque ce sera un axe de travail -
pistes: moteur, transducteur, pulseur ?  
\- processing: le laisse t on dans le fpga ?  
\- Design: sur ces 6 mois, revient on vers une idée de design rotatif - ou on
reste en balayage ?

### **Hyacinthe** - Feb 02, 2016 at 9:57 AM

merci  ![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  
  
Pour tous les autres, on se retrouve samedi vers 10.30 / 11.00 pour le
brainstorm The Future Of Echopen... On déjeunera ensemble.

### **Emilie Mayer,** - Feb 03, 2016 at 9:40 AM

![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  
Tu pourras nous skyper samedi?

### **Hyacinthe** - Feb 03, 2016 at 4:50 PM

@all, Samedi, on aura vers 10.00 jusqu'à 11.00 la visite d'une photographe
(envoyée par la Fondation Fabre) pour nous faire quelques images à la fois de
nous et des activités... Donc on se fait beau ;) et on lui consacrera un petit
moment ;)

### **hyacinthe,** - Feb 04, 2016 at 7:18 AM

![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie : quelle heure ?  
@hyacinthe: damn jloupe tout !

### **Hyacinthe** - Feb 04, 2016 at 7:29 AM

![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  je précise qu'il y
aura plusieurs séances... Une samedi donc, et une autre en programmation pour
s'assurer que tout le monde sera bien présent. On se calera sur tes dipso,
sans doute un vendredi lui ai-je dit.

### **Emilie Mayer,** - Feb 04, 2016 at 6:07 PM

Je ne sais pas pour l'heure,  ![Hyacinthe,
echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  ?

### **Hyacinthe** - Feb 05, 2016 at 1:41 PM

Demain, on se retrouve à 10.00....

### **hyacinthe,** - Feb 05, 2016 at 1:43 PM

Pour Skype? Si y'a photo de 10 à 11, pas besoin d'être là ?

### **Hyacinthe** - Feb 05, 2016 at 5:07 PM

Oui, en effet.

### **hyacinthe,** - Jul 01, 2016 at 5:40 PM

Qques insights, ça doit être le bon thread pour ça :)  
  
Quick réunion avec Nicolas Felix, tech advisor chez vermon.  
  
Usage: conseille de regarder des usages non diagnostique - volume de vessie
(conseille de voir ce que fait veraton en gériatrique -- utilisation ultra
simple, monoelement, usage accessible au personnel soignant) ou encore aide à
la chirurgie orthopédique. Ces usages marcheraient avec ce qu'on a développé
so far.  
Front end existant: recommande de laisser tomber l'analogique discret, et de
prendre du composant off the shelf. Assemblage type murgen. plus qu'ok pour du
B mode. Recommande d'utiliser du PIC pour uC.  
Composants: OK pour nous mettre en relation avec des contacts ultrasons chez
maxim et al, jouant la carte de l'Open source. Insiste sur le besoin de non-
exclusivite. Faire collaborer en mode mécénat de compétences divers suppliers
peut donner des choses sympa.  
Integration au pédagogique: il appuie des étudiants à Tours, sur un Master
d'électronique pour usage médical. A voir si ça peut nous intéresser.

### **Hyacinthe Lacenne** - Jul 02, 2016 at 4:45 PM

![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  : PIC à 75$ (il
y a une promo de 25%) pour une dev board PIC32MZ (dont un ADC 12 bits 28Msps)  
-&gt; <http://www.microchipdirect.com/ProductSearch.aspx?Keywords=DM320007-C>  
La chip en tant que telle est a 10€



#  RANDOM

Hyacinthe posted this Jun 17, 2016 at 9:13 AM

Hello, un fil de discussion random pour échanger ensemble un peu tout et
n'importe quoi ;)

### **Hyacinthe** - Jun 17, 2016 at 9:15 AM

Hello all,  
  
une startup développant un nouveau type d'éolienne horizontale adaptée en
situation urbaine cherche un ingénieur avec des compétences en aérodynamique
et mécanique des fluides, voir électrique.  
  
Si vous connaissez quelqu'un qui connait quelqu'un ;)

### **Hyacinthe VINCENT,** - Jun 17, 2016 at 9:46 AM

Non, mais je connais bien les gens d'un labo de l'ENSAM qui fait de la
recherche partenariale et qui connait bien le sujet ;-) :
<http://dynfluid.ensam.eu/>

### **Hyacinthe** - Jun 17, 2016 at 9:48 AM

Excellent, merci  ![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  je passe le mot
et te tiens au courant ;)

### **Emilie Mayer,** - Jun 17, 2016 at 3:50 PM

Si tu veux je peux envoyer un mail à ma promo, mais il faudrait un peu plus
dinfos ;)

### **Hyacinthe Lacenne** - Jun 22, 2016 at 7:45 AM

bon les spécialistes connaissent sans doute cela par coeur, mais je poste ceci  
  
<http://www.zdnet.com/pictures/10-alternatives-to-the-raspberry-pi/8/>

### **Hyacinthe Lacenne** - Jun 22, 2016 at 12:46 PM

Niveau captation, il existe un truc propre et pro dont on se sert dans une
asso: <https://www.ubicast.eu/fr/> =)

### **Emilie Mayer,** - Jun 22, 2016 at 4:32 PM

<https://drive.google.com/file/d/0B78eZ66FqvN9UGNDUWVzY05HdzYyMXRneFBmVWFRRjVodXRB/view>  
  
"Concours pour la 10e édition du Prix Ile de Science de la culture
scientifique et technique.Ce concours vise à mettre en avant les projets et
initiatives scientifiques et techniques particulièrement innovants et
audacieux.  
==&gt; Ce concours est doté d'UNE BOURSE DE 2.000 EUROS.La date limite des
dépôts des dossiers est fixée au mercredi 13 juillet 2016."  
  
Bon parcours faut etre géographiquement sur le plateau de saclay, donc pas
sure que ca marche, mais ça peut peut etre en intéresser certains....

### **Hyacinthe Lacenne** - Jul 05, 2016 at 12:55 PM

Tjrs sur les financements, <http://www.franceactive.org/default.asp?id=27>
-&gt; aller de 5k à 1.5Me  
  
Sinon, plus fun : <https://github.com/usgov/forget-the-king>

### **Hyacinthe Lacenne** - Jul 11, 2016 at 6:52 AM

Discussion avec un pote de Withings, qui fait des balances qui mesurent la
rigidité artérielle: avec deux petits piezos à distance fixée sur la carotide,
on peut calculer la vitesse de propagation de l'onde de pouls, donc l'état des
tuyaux (dont Hyacinthe nous a fait une premiere démo vendredi).

### **Hyacinthe Lacenne** - Jul 13, 2016 at 3:14 PM

![Hyacinthe KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe  tu vas aiiimé :
des labs de physiques open source  
  
via  ![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe
<http://www.physdev.org/open-source/>  
  
btw, il passe ce lundi est echOpen ;)

### **Hyacinthe KHOYRATEE,** - Jul 15, 2016 at 9:09 AM

Je n'ai pas entièrement saisi à quoi servait leurs machines mais ça a l'air
génial :D

### **Hyacinthe** - Sep 21, 2016 at 3:02 PM

Hello à tous,  
  
Proposition pour exposer echOpen à l'espace Hyacinthe Gilles de Genne (ESPCI) de
Novembre 2016 à mai 2017 à l’occasion de l’exposition Science Frugale

  * 2 premier mois d’incubation =&gt; Faire venir des projets qui vont ajouter des éléments dans l’exposition. 
  * Exposition 

Ouvert au public + événements possibles (conférences, workshops, etc.)

  

**besoin / proposition** : 

  * Un texte + une photo pour montrer + qq informations 
  * Idéalement un ancien prototype qui serait mis sous vitrine à exposer. 
  * Proposer une idée d'événement (espace 100 mètre carré + amphithéâtre de 36 places)

  
A vos idées ;) Ce serait cool !! Qui voudrait monter à bord de ce projet ?

### **Hyacinthe Lacenne** - Sep 22, 2016 at 7:39 AM

c top ça ;)



#  Veille echOpen

hyacinthe posted this Feb 05, 2016 at 12:29 PM · 1 person applauded

Lu sur le Web :)  
  
<http://blog.cecilemonteil.lequotidiendumedecin.fr/2016/02/03/et-si-demain-
lechographie-devenait-un-jeu-denfant/>

### **Emilie Mayer,** - Feb 05, 2016 at 12:38 PM

A mettre dans "on parle de nous" sur le wiki ;) Vous la connaissez? (elle est
bien informée pour le 10 mars?

### **Hyacinthe Lacenne** - Feb 05, 2016 at 9:51 PM

oui j'ai vu ça... je ne savais pas qu'elle allait le bloguer

### **Emilie Mayer,** - Feb 08, 2016 at 7:25 PM

Elle dit que le lumify est à 200 $, peut-être faudrait il actualiser nos
données sur le wiki, où l'on écrit que les sondes actuelles coûtent 10 fois
plus?

### **Hyacinthe Lacenne** - Feb 08, 2016 at 10:53 PM

en fait c 200$ en location (par mois si je ne  m'abuse) ;)

### **hyacinthe,** - Feb 09, 2016 at 7:54 AM

Rent a service, rather than buy an object. Smart - ca prévient l'obsolescence
programmée.

### **hyacinthe,** - Feb 09, 2016 at 8:26 AM

Sinon y'a des trucs cool qui sortent:  
  
<http://jewishbusinessnews.com/2016/02/08/israeli-technion-develops-small-
portable-ultrasound-system-for-live-imaging/>

### **Hyacinthe Lacenne** - Feb 16, 2016 at 6:06 PM

Des ressources pour la veille:  
Dans le drive : echOpen\2. PROTOTYPAGE\articles\Echographe
portable_ultraportable : ce dossier contient plusieurs specs d'ultraportables  
Dans le drive tjrs, le benchmark de Na:
<https://docs.google.com/spreadsheets/d/1DoB_r402ad38lLJ9d7Yscn8G-
SH5KQb1geCV3MpepAo/edit?pli=1#gid=1179411353>

![Cleardot](https://ssl.gstatic.com/ui/v1/icons/mail/images/cleardot.gif)

### **Hyacinthe Lacenne** - Feb 16, 2016 at 6:50 PM

Ce qu'on veut faire :  
<http://sci-hub.io/10.1109/ULTSYM.2015.0517>  
  
=)

### **Hyacinthe Lacenne** - Feb 16, 2016 at 6:59 PM

![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/782178.png)
lacenne  : je ne sais pas si tu as vu, mais y'a des trucs funky. W. K. Kong,
W. Lee, K. C. Kim, Y. Yoo, and T. –K. Song, “Implementation and optimization
of ultrasound signal processing algorithms on mobile GPU,” Proc. SPIE Medical
Imaging, pp. 90401F-90401F, 2014.

### **Hyacinthe Lacenne** - Feb 16, 2016 at 8:41 PM

excellent - je vais checker ;)

### **Hyacinthe Lacenne** - Feb 20, 2016 at 10:55 AM

greg parle d'echOpen - avec une majuscule grande comme un O -  dans
10xmanagement ;) <http://www.10xmanagement.com/qa-interview-with-10xer-greg-
sadetsky/>

### **Hyacinthe Lacenne** - Feb 22, 2016 at 3:23 PM

![Hyacinthe LICCIONI, FPGA at
echopen](./../../zz_assets/images/avatars/1249124.png) Hyacinthe  ![Hyacinthe
Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  ![Hyacinthe
KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe  ![Hyacinthe
VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  
  
du FPGA avec un IDE d'arduino et en open source - ca s'appelle
[papilio](http://papilio.cc/)

### **Hyacinthe Lacenne** - Feb 22, 2016 at 3:30 PM

Pour compléter, il y a d'autres bouzins, du style LOGi ou Logi-Pi pour
Raspberry ou LOGI Bone pour BBB =)  
  
Pour du vraiment mini tu as du Xula 2 qui est minus au possible =)  
  
A voir le compromis prix/board/capacité du fpga.

### **Muriel,** - Feb 25, 2016 at 8:48 PM

Date de lancement du Lumify en France : septembre 2016.  
Les démarches d'enregistrement sont déjà commencées.  
(info récupérée sur le stand Philips à la Journée d'Innovation en Santé du 23
janvier à la Cité des Sciences et de l'Industrie )

### **Hyacinthe Lacenne** - Mar 01, 2016 at 12:24 AM

merci  ![Muriel, Contributeur méthodologie at
echopen](./../../zz_assets/images/avatars/1269173.png) Muriel  on a encore 1
peu  de marge ;)

### **Emilie Mayer,** - Mar 01, 2016 at 10:58 AM

De marge pour...?

### **Hyacinthe Lacenne** - Mar 01, 2016 at 12:04 PM

De marge pour finaliste un outil pour septembre ;)

### **Hyacinthe Lacenne** - Mar 03, 2016 at 2:18 PM

un post autour de l'open source hardware et d'un outil de documentation qui
rapporté comme prometteur :  
  
[  
http://blogs.plos.org/synbio/2016/03/01/open-source-hardware-is-an-
opportunity-for-synthetic-biology-research-the-docubricks-approach-by-tobias-
wenzel/  
](http://blogs.plos.org/synbio/2016/03/01/open-source-hardware-is-an-
opportunity-for-synthetic-biology-research-the-docubricks-approach-by-tobias-
wenzel/)  

[  
http://docubricks.com/  
](http://docubricks.com/)

### **Hyacinthe Lacenne** - Mar 09, 2016 at 10:20 AM

intéressant : <http://www.nature.com/news/open-hardware-pioneers-push-for-low-
cost-lab-kit-1.19518>

### **Hyacinthe** - Mar 21, 2016 at 1:31 PM

Je pose ça là !  
  
[http://www.fiercemedicaldevices.com/story/ge-healthcare-handheld-ultrasound-
pilot-nhs-test-20m-nigerian-health-
initia/2016-03-17?utm_medium=rss&amp;utm_source=rss&amp;utm_campaign=rss](http://www.fiercemedicaldevices.com/story
/ge-healthcare-handheld-ultrasound-pilot-nhs-test-20m-nigerian-health-
initia/2016-03-17?utm_medium=rss&utm_source=rss&utm_campaign=rss)

### **Hyacinthe Lacenne** - Mar 21, 2016 at 4:20 PM

special  ![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  
  
après le dej avec Djalel &amp; Benjamin, où nous sommes convenus de chercher
des datasets afin de pouvoir étancher la soif de data des learning machines  
  
voici un premier set de data ouvert d'images echo :
<http://cimlaboratory.com/applications/thyroid/>.

  

Il s'agit d'écho de la thyroïde, qui sont d'ailleurs annotées (tunmeurs
malignes ou bénignes). L'objet de l'équipe qui a mis en ligne ce dataset est
de faire de l'assistance dignanostique

  

<https://www.researchgate.net/publication
/275340525_An_open_access_thyroid_ultrasound-image_Database>

  

Par ailleurs, dans la pêche à l'info d'outils open source orientée imageries :

  
et des modèles de sondes 3D printables :

<http://perk-software.cs.queensu.ca/plus/doc/nightly/modelcatalog/>

un utilitaire de stockage et d'indexation :
[http://www.midasplatform.org](http://www.midasplatform.org/)

un autre package open source, tout velu d'algorithmes:
<https://www.assembla.com/spaces/plus/wiki>

et dans le même esprit : <https://gforge.ti.com/gf/project/med_ultrasound/>

### **hyacinthe,** - Mar 24, 2016 at 9:45 AM

Elle est grosse la clarius..  

[

![](bc3-raw/files/2899590-img_20160324_104447.jpg)

](bc3-raw/files/2899590-img_20160324_104447.jpg)

[ IMG_20160324_104447.jpg  52.8 KB • Download
](bc3-raw/files/2899590-img_20160324_104447.jpg)

### **Hyacinthe VINCENT,** - Mar 24, 2016 at 11:30 AM

Oui mais y a tout dedans, y compris les batteries.

### **Hyacinthe Lacenne** - May 17, 2016 at 1:38 PM

me revoilà  
  
<http://www.nextinpact.com/news/99854-raspberry-pi-raspbian-passe-au-
bluetooth-zero-gagne-connecteur-pour-camera.htm>

### **Hyacinthe Lacenne** - May 24, 2016 at 2:55 PM

C'est ca ! Le zero que j'ai a son connecteur caméra, que je ne retrouve sur
aucun layout (cf google image).  
  
Si on arrive à avoir une image préformée en amont pour simuler la caméro,
c'est tout bénéf ;)

### **hyacinthe,** - Jun 28, 2016 at 5:59 PM

Je viens de re-découvrir le VoCore... Intéressant, même si (assez)  limité

### **Hyacinthe VINCENT,** - Jun 29, 2016 at 8:14 AM

Pas mal quand même <http://vonger.cn/?p=2383> mais faudrait virer le linux.

### **Hyacinthe Lacenne** - Jun 29, 2016 at 8:20 AM

Ou mettre un xenomai / RTAI =)



#  Sonde d'expérimentation en aquarium

Hyacinthe VINCENT posted this Jun 10, 2016 at 12:46 PM · 2 people applauded

![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe ,  ![Joris JEAN-
BAPTISTE, Elec analog & digit + Soft  at
echopen](./../../zz_assets/images/avatars/4392629.png) Joris , voici quelques
infos pour réaliser une sonde d'expérimentation à pincer sur le bord de
l'aquarium.  

[

![](bc3-raw/files/6221602-20160319_194819_hdr.jpg)

](bc3-raw/files/6221602-20160319_194819_hdr.jpg)

[ 20160319_194819_HDR.jpg  4.35 MB • Download
](bc3-raw/files/6221602-20160319_194819_hdr.jpg)

  
**Ingrédients**

  * [DRV8834 Low-Voltage Stepper Motor Driver Carrier](https://www.pololu.com/product/2134).
  * [Stepper Motor: Bipolar, 200 Steps/Rev, 20×30mm, 3.9V, 0.6 A/Phase](https://www.pololu.com/product/1204).
  * 4 vis M2.
  * Axe de 4mm.
  * Support et tambour réalisés en impression 3D en PLA.

  
**Remarques**

  * Envisager des clips pour guider le fil le long de l'axe jusqu'au transducteur.
  * Les petites vis du coupleur d'axe butent sur le support et c'est normal, cela permet de repérer une origine de position 0 en faisant "reculer" pendant 360° et caler le moteur sur cette butée. Cela évite aussi de faire des noeuds avec les fils du transducteur en cas de fausse manip.
  * Le moteur et le driver ont été achetés chez Lextronic mais il semble qu'ils n'aient pas le moteur dispo en ce moment, le mien était &lt; 20€
  * On pourrait essayer avec un moteur de CD-ROM mais je ne sais pas si il serait assez puissant.
  * **ATTENTION : avant toute chose**, il faut régler le courant maxi sur le driver (§ "Current limiting"). Sinon le moteur peut très vite surchauffer même à l'arrêt. Sachant qu'on va "caler" le moteur sur une butée, on va chercher à régler le courant sur le minimum qui permet de ne pas perdre de pas mais qui permette de ne pas trop forcer sur la butée. Tout cela sera à expérimenter avec le transducteur en place (voir 3 transducteurs).
  * Ce driver Pololu a l'avantage de fonctionner dès 2.5V. Donc tout fonctionne bien sous 5V.
  * Le moteur est un 200 pas/tr mais le driver descend jusqu'au 1/32 de pas.
  * Sur mes tests, en pilotant le moteur en 1/8, soit 1600 pas et en trichant un peu sur le secteur balayé (67.5°) cela donne un secteur de 300 pas et un tir tous les 1.5 pas. Soit un tir tous les 3 fronts (montants ou descendants) du signal de commande du driver.  La fréquence d'IT pour générer le signal de commande sera alors de 9 kHz pour obtenir 15 fps. Tout cela devant être ajustable en jouant sur les différents paramètres. L'idée à terme étant de déporter au maximum la génération de ces signaux dans les timers du µC pour libérer des cycles CPU.
  * On considère pour l'instant que le moteur a assez de couple pour inverser son mouvement en un seul pas. Sinon il faudra affiner la loi de vitesse.

  
Ci-joint, un source, un peu expérimental ;-), en µPython d'une version
n'utilisant pas au maximum des timers et qui consomme déjà 22% de CPU sur un
STM32F405 à 160 MHz.  

[ ![](./../../zz_assets/images/file-types/py.png) main-v1.py  3.95 KB •
Download
](bc3-raw/files/6223271-main-v1.py)

  
PS 1: je ne peux pas passer ce vendredi 10/06 mais je vous prêterai qq
composants lundi pour commencer à maniper et éviter de perdre du temps pendant
l'appro.  
  
PS 2 : @tous, ce post est peut-être un peu technique pour être déposé sur
BaseCamp ? Qu'en pensez-vous ?.**  
**

### **Hyacinthe Lacenne** - Jun 10, 2016 at 12:50 PM

Post sur github (tutoriels.md dans le bon module) avec copie sur le wiki?

### **Hyacinthe VINCENT,** - Jun 10, 2016 at 1:08 PM

Yep ! C'est vrai. Je suis tjs un peu coincé sur GH tant que je n'ai pas fait
le ménage et calé l'architecture de mon dépot.



#  news again

Hyacinthe Lacenne posted this Mar 23, 2016 at 1:18 AM · 4 people applauded

02.10 à l'hôtel dieu, le 23.03.16, pour la première fois depuis notre début,
echOpen observe une structure anatomique  
  
il s'agit de l'éminence thénar et hypothénar du sieur Hyacinthe : sans doute un
fléchisseur profond, un court abducteur et un bout de scaphoïde  
  

[

![](bc3-raw/files/2844289-screenshot_2016-03-23-02-06-57.png)

](bc3-raw/files/2844289-screenshot_2016-03-23-02-06-57.png)

[ Screenshot_2016-03-23-02-06-57.png  193 KB • Download
](bc3-raw/files/2844289-screenshot_2016-03-23-02-06-57.png)

  
  
;)

### **hyacinthe,** - Mar 23, 2016 at 6:09 AM

Excellent !!!

### **Hyacinthe Lacenne** - Mar 23, 2016 at 7:33 AM

Plus je la vois et plus c'est canon =)  
  
Hyacinthe, tu peux jouer sur les niveaux de gris de l'image pour améliorer la
lisibilité de l'image?  

[

![](bc3-raw/files/2849167-image1.png)

](bc3-raw/files/2849167-image1.png)

[ Image1.png  81.8 KB • Download
](bc3-raw/files/2849167-image1.png)

### **Hyacinthe Lacenne** - Mar 23, 2016 at 8:14 AM

Yes je vais regarder ça aujourd hui ;)

### **Hyacinthe VINCENT,** - Mar 23, 2016 at 8:22 AM

Impressionnant! Génial! Bluffant!  
  
Personnellement je ne reconnais pas Hyacinthe, mais c'est vrai je ne le connais
pas assez intimement.

### **Hyacinthe KHOYRATEE,** - Mar 23, 2016 at 8:30 AM

Ayant vécu dans la grotte avec lui, on voit un morceau de Hyacinthe dans le coin
:p

### **Hyacinthe Lacenne** - Apr 14, 2016 at 8:45 AM

hyacinthe debeir nous adresse un article sur echOpen dans un journal belge  

[

![](bc3-raw/files/3384084-img_20160406_184742.jpg)

](bc3-raw/files/3384084-img_20160406_184742.jpg)

[ IMG_20160406_184742.jpg  1.69 MB • Download
](bc3-raw/files/3384084-img_20160406_184742.jpg)

[

![](bc3-raw/files/3384127-img_20160406_184832.jpg)

](bc3-raw/files/3384127-img_20160406_184832.jpg)

[ IMG_20160406_184832.jpg  1.49 MB • Download
](bc3-raw/files/3384127-img_20160406_184832.jpg)

[

![](bc3-raw/files/3384190-img_20160406_184840.jpg)

](bc3-raw/files/3384190-img_20160406_184840.jpg)

[ IMG_20160406_184840.jpg  1.35 MB • Download
](bc3-raw/files/3384190-img_20160406_184840.jpg)

### **Hyacinthe Lacenne** - Apr 14, 2016 at 8:49 AM

Greg me fait savoir qu'il passe juin, juillet à Panam -&gt; bien trop bien  
  
Greg demande si on est OK pour l'accueillir en résidence again -&gt; ben en
fait clairement  
  
Greg souhaite savoir si une chambre est dispo à lHD -&gt; je demande ce jour à
la direction  
  
la direction me répond que l'HD peut l'accueillir en résidence dans une
chambre cet été  
  
c pas de la bonne nouvelle ça ;)

### **Hyacinthe Lacenne** - Apr 14, 2016 at 8:51 AM

Excellent !

### **Hyacinthe Lacenne** - Apr 25, 2016 at 8:06 AM

Greg sera donc en résidence du 24 juin au 24 juillet. Et la chambre est
réservée à l'HD ;)

### **Hyacinthe Lacenne** - Apr 25, 2016 at 12:47 PM

voici un mail d'un doctorante en echo Virginie Grand-Perret et voici son
profil [pro](http://fr.viadeo.com/fr/profile/virginie.grand-perret). vous
tiens au courant  
  
Bonjour,

  

je viens de découvrir votre projet Echopen, qui correspond à un rêve que j'ai
eu en commençant ma thèse sur l'échographie de contraste cette année, aussi
j'aurais voulu en savoir plus et vous rencontrer.

  

Seriez-vous disponible cette semaine prochaine pour en discuter ?

  

merci d'avance et bonne journée,

### **Emilie Mayer,** - Apr 25, 2016 at 7:48 PM

C'est tooooop!

### **Hyacinthe Lacenne** - May 03, 2016 at 4:49 PM

dans le cadre d'epidemium, rencontre de Soobash Daiboo, astrophysicien, data-
analyst et qui connaît bien le traitement du signal, il est très intéressé par
echOpen. Il passe nous voir mardi à 11H00. avis aux amateurs

### **Hyacinthe Lacenne** - May 30, 2016 at 9:52 AM

on vous fait un debrief de ce riche we ce soir avec emilie ;)  
  
btw, cette semaine plusieurs entretiens pour les stagiaires et installation de
la team traitement d'image  
  
btw, voici un message de frédéric amiel suite à notre échange sur la
mobilisation d'étudiants de l'ISEP :  
  
"Bonjour Mr Lacenne ,

  

 Oui déjà vous avez rencontré Zahra Barwane qui devrait travailler plutôt sur
l'algorithme de traitement. Sinon nous avons un groupe d'étudiant mastere mais
le temps alloué pour leur projet ne leur permettra pas d'avancer
significativement.

  

 Nous avons approvisionné le matériel de façon à préparer une version avec un
FPGA contenant un processeur ARM, qui sera connecté à une carte de conversion
rapide, le but étant :

  

   - Dans le FPGA d'implanter une transformée permettant de "voir" la variation de fréquence (effet doppler). 

   - Dans le FPGA d'implanter un algorithme de reconstruction d'image plus performant que bi-cubique en particulier au niveau des contours.

   - Dans le microcontroleur, de gérer la transmission Wifi vers la partie visualisation.

  

     Le microcontroleur embarque un Linux ce qui permet facilement tout type
de transmission.

  

 Par contre nous n'aurons probablement pas de résultats significatifs cette
année scolaire en raison du manque de ressource. (Les étudiants avaient déjà
des projets).

  

De façon générale, nous avons défini les sujets suivants :

  

     - Simulateur sous MATLAB : avec le propos de simuler le signal reçu en fonction d'une image paramétrant les milieux traversés. 

     - Algorithme permettant de retracer l'image en fonction des signaux reçus avec la possible amélioration d'analyser les fréquences

     - Implantation sur FPGA d'un système de base (avec la simple détection d'amplitude)

     - Implantation avec la transmission Wifi.

  

Je compte participer à la prochaine grande réunion dans tous les cas de façon
à rester informé. Nous devrions être plus efficace avec notre prochain lot
d'étudiants.

  

             bien cordialement,

  

                     Frédéric AMIEL  
"

### **Hyacinthe** - May 30, 2016 at 9:54 AM

\+ un étudiant de l'UPMC qui souhaite faire un stage de 2 mois (email reçu ce
matin) en attente d'une date d'entretien

### **Hyacinthe Lacenne** - May 30, 2016 at 9:56 AM

Terrible !

### **Hyacinthe VINCENT,** - May 30, 2016 at 10:04 AM

echOpen ... "intégrateur de compétences" ...  
Je propose de mettre en place un réseau de deep learning non supervisé pour
récupérer, classer, valoriser et intégrer toutes les contributions dans le
dépot echOpen. ;-)

### **Hyacinthe Lacenne** - May 30, 2016 at 10:11 AM

hehe  
  
On aurait besoin d'un petit doc "annuaire" public avec les noms, skills,
travaux et contacts de chacun -- style un MD qqpart ou une page sur le wiki !

### **Hyacinthe Lacenne** - May 30, 2016 at 10:20 AM

Ces quelques points sont intégrés dans l'ODJ de ce soir, n'hésitez pas à
compléter, c'est sur :
<https://docs.google.com/document/d/1QvdCm2CYsujH8HKidR_w9i20oFb5dsWRUXKGGW8xfrw/edit>#

### **Emilie Mayer,** - May 30, 2016 at 10:33 AM

Yes et il faut qu'on s'inscrive sur "je m'engage" pour récupérer plein de
talents, il n'y a pas 10 000 associations tech :
<https://jemengage.paris.fr/associations/inscription>[  
  
](https://jemengage.paris.fr/associations/inscription)A ce soir!

### **Hyacinthe** - May 31, 2016 at 2:48 PM

Joris Jean-Baptiste, étudiant en 4ème année à l'UPMC va nous rejoindre pour un
stage de 2 mois et sans doute travailler sur :

  * ADC
  * Micro-contrôleur 
  * Electronique (modules) 

Cela cadre bien avec les exigences de son stage. On attends le retour de son
établissement pour signer la convention. Il devrait nous rejoindre dès demain
pour commencer à avancer à nos côtés.  
  
Ensuite,  ![Michel Bala, Electronique analogique  at
echopen](./../../zz_assets/images/avatars/2008321.png) Michel  qui a fini se
examens d'agrégation est passé aujourd'hui et va continuer l'aventure une
partie de l'été ;)  
  
Enfin, nous attendons le retour de deux étudiants chinois (UPMC &amp; Spelec)
qui pourraient eux aussi nous rejoindre pour deux mois.  
  
@+

### **Hyacinthe Lacenne** - Jun 02, 2016 at 3:44 PM

quelques efforts plus tard  
  
Daniel Reinzine, qui pilote la partie SI de toute l’imagerie de l’AP-HP et
Hyacinthe Naon, qui travaille à la R&amp;D du PACS (Picture Archiving and
Communication System) de l'AP veulent nous aider ;))) je leu ai proposé de
passer le 18  
  
au bonheur de la data, de l'IA et de  ![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  !  
  
btw, je vois Djalel demain, la team IA bientôt UP

### **Hyacinthe Lacenne** - Jun 22, 2016 at 7:32 AM

hello, un mot pour vous dire, que BitMakers s'installe cette semaine à l'hôtel
dieu ;) dans l'intervalle de leur déménagement dans leurs locaux/et par la
suite, on les a/aura avec nous dans l'open space !

### **Hyacinthe Lacenne** - Jul 01, 2016 at 2:07 PM

sur la voie d'une résidence pour septembre-décembre, en partenariat avec
makery : il s'agit d'une artiste japonaise (dont je ne me rappelle pas le nom,
et qui semble-t-il est connu internationalement) dont les projets tournent
autour des objets connectés et qui est connectée avec de drôles d'objets, bien
mobiles, spécialistes de hardware ou software, dont il appert qu'ils seraient
des pointures #42 dans leur domaines. Makery souhaite va déposer un projet de
financement auprès du CNC, je vous tiens au courant

### **Hyacinthe Lacenne** - Jul 07, 2016 at 5:05 PM

Qqs de news de la résidence :

  

\- l’hôtel dieu est toujours Ok pour accueil de résident.

Je me suis entretenu avec de nombreux dev. indiens et pakistanais, les seuls à
avoir répondu à un call pour résidence.

Celui qui sort du lot est Priynak Tiwari, un dev android indien qui travaille
dans une start-up _mobil_isée sur les questions de violences faites aux
femmes. Il est très motivé, m’a adressé les app qu’il a développée. Il fait le
point sur la question des VISA et pourrait être là à compter de la mi-août

  

Par ailleurs Makery est en train de monter sur un appel à subvention CNC qui
serait un partenariat d’event avec eux. Au menu, une artiste et sa nuée de
hackers, me dit-on de haut niveau,  qui seraient résidence chez nous.  Ca a
l'air top !

  
En pièce jointe, la proposition de Makery ;)

[

![](./../../zz_assets/images/previews/7505625-b_art2m_opensourcebody.png)

](bc3-raw/files/7505625-b_art2m_opensourcebody.pdf)

[ B_Art2M_opensourcebody.pdf  3.76 MB • Download
](bc3-raw/files/7505625-b_art2m_opensourcebody.pdf)

### **Hyacinthe Lacenne** - Jul 07, 2016 at 6:29 PM

Top ce projet de programme, et encore plus si l'HD/APHP sont partants pour ça!  
  
Au summum, l'intégration des artistes dans le workflow :p

### **Hyacinthe Lacenne** - Jul 11, 2016 at 1:51 PM

rdv chez Thalès le 26 août,  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  comme l'an dernier
you in ?

### **Hyacinthe Lacenne** - Jul 11, 2016 at 3:02 PM

Yes why not!  
  
C'est eux qui ont relancé? Si oui, ils ont un agenda spécifique en tete?

### **Hyacinthe Lacenne** - Jul 11, 2016 at 3:08 PM

ils ont répondu avec 3 mois de retard au mail d'update que je leur ai envoyé
pour le 24 mars. Ensuite, je ne sais ce qu'ils ont exactement en tête, je
pense qu'on peut leur formuler des besoins précis, maintenant qu'on est un peu
plus crédible à leurs yeux

### **Hyacinthe Lacenne** - Jul 13, 2016 at 8:21 AM

Mwep. Ils étaient de mémoire très axés software, ca peut valoir le coup de se
demander ce qu'on pourrait leur demander.

### **Hyacinthe Lacenne** - Jul 13, 2016 at 8:24 AM

Ah bah oui ça c sûr ;)

### **Hyacinthe Lacenne** - Jul 21, 2016 at 11:23 AM

hello,

  

voici un mail reçu hier d’une MCUPH en médecine interne

"

j'ai lu ton interview ds la gazette de l'amicale des jeunes internistes, je
suis MCU PH en médecine interne à tenon. On a une asociation qui a
potentiellement des bourses à proposer à des jeunes sur des projets innovants
comme ce que tu fais avec l'échostéhtoscopie. Aurais tu un moment à la rentrée
pr en discuter par tel ou de visu afin que j'évalue les besoisn financiers
d'internes qui voudraient travailler 1 ans sur un tel projet et voir comment
on pourrai les aider de façon la plsu otpimale.

“

du coup, si ca le fait, on pourra établir cette ressource à la mise au point
protocole / et le placer en référent/pivot avec pasteur, le département
d’épidémiologie clinique et le pôle hospinomics de l’hôtel dieu qui travaille
à l’évaluation médico-économique, et qui est intéressé par echOpen

### **Hyacinthe Lacenne** - Jul 21, 2016 at 11:37 AM

Trop cool !!

### **Hyacinthe Lacenne** - Sep 06, 2016 at 4:33 PM

super visite de Shu Lea Cheang, une artiste qui va faire un projet de
performance autour d'echOpen : echo. de femmes enceintes et convertir les
mouvements en une love song algorithmique  
  
3 de ses complices, electroniciens / hackers seront en résidence à l'Hôtel
Dieu eet l'aideront à programmer l'ensemble  
  
echOpen + makery ont déposé une demande de subventions au CNC -&gt; réponse à
la fin du mois  
  
et Shu Lea Cheang devrait commencer à travailler avec nous en Octobre

### **Hyacinthe Lacenne** - Sep 12, 2016 at 10:24 AM

rdv ce matin avec le CEO de Qwant, et son project manager wiz  ![Hyacinthe,
echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe . Pour mémoire
Qwant est le moteur de recherche qui veut concurrencer Google, sur la base du
respect de la privacy. Springer est un des leurs investisseurs principaux à
hauteur de plusieurs 100M€  
  
-&gt; grosse culture de l'open source, pas mal de release de leurs algo en open et le project manager est l'ancien CTO de Firefox OS  
  
-&gt; prise de contact après le concours Solve vendredi, rdv ce matin. Ils souhaitent travailler avec nous sur la partie IA/data : calcul, stockage, algo et proposent un partenariat  
  
-&gt; on vient de lancer un doodle pour rencontre technique avec Djalel et leur CDO/IA  
  
vous tiens au courant de la suite

### **Hyacinthe Lacenne** - Sep 12, 2016 at 2:12 PM

Cédric Villani organise un colloque "Mathématiques, oxygène du numérique"
autour des mathématiques et du monde de demain et prévoit une série de démo
tech. Et on nous propose d'en faire une ;)  
  
ca se passe le 20 et 21 octobre !  
  
vous tiens au courant des détails pratiques

### **Hyacinthe Lacenne** - Sep 14, 2016 at 3:50 PM

sauf imprévu, d'ici la semaine prochaine, on devrait avoir pour 5000$ *2 de
crédit de cluster + puissance de computing d'Amazon Web Service, et ce sur 2
ans ;)  
  
Djalel est en train de mettre ne place un format de meet-up IA, alternant une
fois sur deux revue du lecture et séance de code.  
  
On va commencer à se faire les dents sur le dataset Kaggle, et je vais lancer
le pipe data #APHP.  
  
Dans le même fil, on commence à travailler ce jour à l'application au grant de
l'Axa Research Fund, l'occasion d'aller chercher un budget et de constituer un
éco-système d'académiques partenaires sur le sujet

### **Hyacinthe Lacenne** - Sep 14, 2016 at 4:54 PM

Sweet!  C'est un geste du mec qu'on avait vu un midi? Trop cool :)

### **Hyacinthe Lacenne** - Sep 16, 2016 at 11:14 AM

exactement !

### **Hyacinthe Lacenne** - Sep 22, 2016 at 10:21 AM

rdv hier avec Qwant où il était question de la marche à suivre :  
\- définition du contour du projet  
\- quels apports respectifs  
  
présents : le CTO data &amp; le CPO et Djalel  
  
\- il s'agirait d'un POC où l'on moulinerait des datasets existants, notamment
à des fins d'amélioration de  la qualité de l'image.  
La technique de traitement data est deep learning orientée, soit des réseaux
de neurones  
\- la contribution de Qwant : ressources de calculs. Djalel juge qu'à ce jour
nous n'avons pas ces besoins, que l'on dispose déjà des accès à des ressrouces
de computing avec ses anciens labos et qu'en revanche ils ne disposent pas de
clusters GPU  
Nous n'avons pas précisément évoqué la question de la mobilisation de la RH
mais ce devrait être logiquement le cas.  
\- sur la base d'un POC concluant, il a été évoqué l'idée de travailler avec
l'AP sur des gros datasets  
  
au total ils sont chauds pour un POC , leur apport serait pertinent, dans un
premier temps, qu'à la hauteur de la RH qu'ils mettraient en face.  
  
A nous de voir, en cours de réflexion avec Djalel

### **Hyacinthe Lacenne** - Sep 22, 2016 at 10:23 AM

rdv le 03 octobre avec le resp Big Data lake de l'APHP et le DSI imagerie  
  
objet : discuter de l'accès aux data d'imageries couplées aux données
cliniques à des fins d'IA  
  
euh il me semble très chauds ;)

### **Hyacinthe Lacenne** - Sep 22, 2016 at 10:26 AM

rdv ce matin avec le directeur de la fondation Altran +  ![Hyacinthe, Danseur du
ventre at echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  
  
\- echOpen rencontre tous leurs critères  
  
\- proposition de RH sur leurs pôles compétences  
électronique embarquée  
soft et data analytics  
certification  
  
les décisions d'accompagnement seront prises entre fin octobre et décembre et
activation début 2017  
  
vous tiens au jus;)

### **Hyacinthe Lacenne** - Sep 30, 2016 at 4:54 PM

hello à tous,  
  
un coucou depuis le MIT où on a tout plein d'excellentes news qui ne
pourraient pas tenir en 1 post ;)  
  
du coup, on debriefe tous ensemble lundi 03 à 19H00 !!  
  
#hihi

### **Hyacinthe Lacenne** - Sep 30, 2016 at 4:56 PM

Sweet! Et n'hésitez pas à mettre une synthèse pour les pauvres hères en
transit en indochine =)

### **Hyacinthe Lacenne** - Nov 05, 2016 at 7:11 PM

hi les amis,  
  
je vais faire un peu de redite du slack pour les news du marathon trip à
Lausanne, Génève et Marrakech. Btw, on a réfléchi avec Hyacinthe une solution de
meilleur usage des espaces slack/basecamp/etc.  
  
\- en Suisse  
  
prez d'echOpen à Hackquarium , accueilli dans un large enthousiasme avec  
  
1) 1 dev FPGA/DSP high level qui va nous aider en review et nous mettre ne
relation avec une école qui forme des ingé spécialisés dans ces domaines  
  
2) 1 doctorant de l'EPFL qui fait sa thèse sur des MEMS et qui propose de
trouver des points d'articulation avec nous . J'ai un call avec lui demain  
  
pour l'essentiel car il y a plein d'autres choses  
  
\- @Marackech  
  
1) d’une part la over-wonder team de phaino, une dev agency (soft,
archi/infra, web, app),  a produit en 48 une app hybride de l’UI, que l’on va
porter en natif dans les jours qui viennent.  
  
btw :  ![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  phaino a groupe
de R&amp;D sur les enjeux native vs. hybride vs webapp. confirmation de
l'intérêt du natif, notamment pour les perf. de l'UI/gestures. Ce à quoi
j'ajoute les possibilités d'interfaçages avec les langues de bas niveau +
usage de la GPU --&gt; à ce sujet, g dev une mini-app avec opengl, c top  
  
2) 1 des pointures mondiales de JAVA et son gang, à donf d’Open Source - qu’on
s’entende,  il code JAVA directly et était le meilleur contributeur du monde
en 2012 - propose un hackathon android/echOpen à Casablanca en décembre
/janvier  
  
3) le ministre de la Santé du Togo est très intéressé par echOpen, un
entretien est en train de se monter, je vous tient au courant  
  
4) Des chercheurs veulent déployer un lab echOpen au Bénin, rdv mardi  
  
\+ 1 grosse nouvelle dans les prochaines heures/jours  
  
oilà;)

### **Hyacinthe Lacenne** - Nov 10, 2016 at 7:43 PM

hello hello,  
  
**Rdv cette semaine avec Max Ageh**, un enseignant-chercheur en électronique, traitement du signal  

  

\- il souhaite développer une instance echOpen au Bénin, selon une modalité
particulière : il s’agirait d’intégrer echOpen à une chaire sciences et
informatique, en cours de constitution. La chaire sera définie en février
prochain.

  

\- il souhaite brancher ses étudiants de son école sur echOpen à compter de
leur prochain projet d’études, soit mai prochain

  

**Rdv avec l’équipe de l'ESIEE** 

  

5 enseignants-chercheurs couvrant l’ensemble des domaines de travail d’echOpen
étaient présents : hard, soft, data, transducteur, traitement du signal

  

\- enthousiasme over the roof top

  

\- propose de constituer autant de groupes d’étudiants qu’il y a de sujets
dans echOpen. Ca devrait être mis en place à compter de mai prochain.

  

\- dans l’intervalle de mai, les chercheurs vont commencé à prendre en main la
techno, ils pensent pouvoir nous accompagner d’ores et déjà sur la
miniaturisation

  

\- doivent revenir vers nous pour nous proposer un plan de travail en commun  
  
oilà;)



#  Réunion Hébdo Echopen @HD

Hyacinthe posted this Feb 01, 2016 at 4:09 PM

Bonjour à tous,  
  
En prévision de notre réunion hebdo de ce soir à 19.00 à l'HD, voici l'agenda
que je vous propose. Vous pouvez le compléter directement sur le [google
doc](https://docs.google.com/document/d/1QvdCm2CYsujH8HKidR_w9i20oFb5dsWRUXKGGW8xfrw/edit#).  
  
A ce soir  
  
O.  
\--  
Ordre du jour 25.01.2016  
  

  * **Développements technologiques =&gt; Avancés de la semaine **
    * [Bilan des avancées de chaque module](https://docs.google.com/spreadsheets/d/17jtXg-r6_nDEFxN0xtRFjEYXCeVaxZG9clrJDgage0o/edit#gid=0) =&gt; Évaluer le délai d’obtention du prototype 
      * Transducteur 
      * Mécanique 
      * Électronique (besoin de matériel CMS ?)
      * REDPI
      * Enveloppe physique du dispositif 
    * Avancés de la déclinaison des besoins médicaux en exigences techniques (EMM / MUG) 
    * Documentation wiki 
    * Définition d’une date pour réunion tech : 
      * Caler les activités précises des 6 prochains mois (amélioration du dispositif) =&gt; Objectif financement et planning de développement 
      * En déduire un prochain CapTech pour mars 2016 
  * **Communauté** 
    * Rencontre JC billard #électronique V2
    * Bilan des travaux de Greg
  * **Point Outils**
    * Statut du serveur web et du nouveau wiki
    * Q&amp;A
    * Outils BC 3 (rappel du fonctionnement) 
  * **Events**
    * Apéros de vendredi
    * Prochain apéro =&gt; 
    * Hyacinthe sur le développement du transducteur (?)

### **Hyacinthe,** - Feb 02, 2016 at 2:17 PM

**Compte rendu du 01/02**  
  
Vous pouvez trouver le CR sur ce le [google
doc](https://docs.google.com/document/d/1QvdCm2CYsujH8HKidR_w9i20oFb5dsWRUXKGGW8xfrw/edit#).
Si vous avez des modifications à apporter.  
  
  
CR 01.02.2016  
  

  * Développements technologiques
  * Le transducteur made in echopen est arrivé à l’hotel dieu, dimension : diamètre 15 mm, hauteur 18.7 mm. Il reste un faire un support pour le fixer sur la mécanique.
  * Temps minimum entre deux pulses environ 250 us.
  * Le kit de développement TGC fonctionne, on va commencer par travailler avec. La conception d’un TGC est ardue. Il ne reste plus qu’à assembler les différents modules entre eux.
  * Problème de bruit électronique du à l’arduino.
  * Programme et simulation d’un code VHDL (pour notre propre FPGA) sont près. FAK a trouvé des codes de transformée de Hilbert et de transfert par USB open source.
  * Greg : il a fait la scan conversion via opencv, il monte jusqu’à 35 fps. En wifi point à point on atteint 3 Mops (ça peut augmenter avec un meilleur dongle wifi). Il a fait un code de transfert de données avec protocole TCP pour plus de sécurité (pas de perte de paquets ainsi).
  * EMM, MUG : la fonction signal processing à été décomposé.
  * Miscellaneous
  * Soutenance VIL et FAK Vendredi à l’hotel dieu à 13h30.
  * Olga et Yohan vont venir observer nos méthodes de travail afin de nous aider à mettre en place des outils d’aide sur les enjeux collaboratif et les méthodes de travail.
  * Samedi 6 discussion le future d’echopen à l’hotel dieu pour une vision sur les six prochains mois (budget, communauté..). Définition d’un cap tech peu après la démonstration puis d’un cap med sur l’utilisation d’échographes ultraportables.
  * Retour réunion bitmaker (ECG miniature) : il veulent se positionner sur de l’open source (question comm). Ils ont conseillé de commencer par des simulations pour les FPGAs avant de coder en dure. Ils veulent se mettre à la fabrication d’un échographe cardiaque donc ils cherche également du savoir faire. Ils aimeraient s’installer à l’hotel dieu pour avoir un premier pas dansle milieu médical.
  * Réflexion autour du deep learning : réseau de neurone pour la détection de contour d’organes. Cela nécessite une grosse base de données + accéléro et gyro pour déterminer le plan de mesure de la sonde.

### **Hyacinthe** - Feb 08, 2016 at 7:56 AM

Bonjour,  
  
Voici l'ODJ de ce soir. RDV à 19.00 à l'HD (on essai de boucler la réunion en
1 heure); A ce soir.  
\--  
Ordre du jour 08.02.2016

  * **Développements technologiques =&gt; Avancés de la semaine **
    * [Bilan des avancées de chaque module](https://docs.google.com/spreadsheets/d/17jtXg-r6_nDEFxN0xtRFjEYXCeVaxZG9clrJDgage0o/edit#gid=0) + matrice &amp; tableau récapitulatif de l’architecture avec versions et justifiction =&gt; en vue des fiches wiki
      * Transducteur 
      * Mécanique 
      * Électronique
      * REDPI
      * App 
      * Enveloppe physique du dispositif 
    * Assemblage =&gt; Suivi des avancées 
    * Déclinaison des besoins médicaux en exigences techniques (EMM / MUG) 
  * **Communauté** 
    * Retour sur la réunion de samedi =&gt; Mise en place des méthodes pour une inclusion communautaire plus grande. 
  * **Point Outils**
    * Statut du serveur web et du nouveau wiki
    * Q&amp;A 
  * **Events**
    * Apéros de vendredi
    * Soirée de release du proto V1 fonctionnel

### **Hyacinthe Lacenne** - Feb 08, 2016 at 8:01 AM

Hi Hyacinthe,  
  
Vu la densité de la réu de samedi, et tout ce qui a ete abordé, on s est dit
qu on a traité au passage les questions de la réu de bureau et qu on peut
remettre  l réu !  
  
@++

### **Hyacinthe** - Feb 08, 2016 at 8:19 AM

![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/782178.png)
lacenne  Je ne saisie pas de quelles questions tu parles. En tout cas
n'hésites pas à ajouter des points dans le google doc directement.

### **Hyacinthe Lacenne** - Feb 08, 2016 at 8:34 AM

;) je n'ai pas été clair :  en fait on s'est dit qu'on pouvait reporter à la
semaine pro le prochain bureau

### **Hyacinthe LICCIONI,** - Feb 08, 2016 at 8:44 AM

Comme l'a dit Hyacinthe,  
Nous avons abordé beaucoup de choses Samedi, et du coup, tout est déjà dit. La
réunion de ce soir ne ferait qu'apporter des détails triviaux sur nos travaux
de Dimanche et d'aujourd'hui, ce qui n'est pas vraiment très conséquent, et
remplirait la réunion pour 10 minutes tout au plus.  
Considérant ce fait, nous nous étions dit que faire venir tout le monde pour
10 minutes était peut-être inutile =&gt; Reporter la réunion ;)

### **Hyacinthe** - Feb 08, 2016 at 3:41 PM

Ok. Donc pas de réunion ce soir. Prochain RDV =&gt; Lundi 15.02 //

### **Hyacinthe** - Feb 15, 2016 at 11:03 AM

Bonjour à tous,  
L'ODJ de la réunion de ce soir est disponible
[ici](https://docs.google.com/document/d/1QvdCm2CYsujH8HKidR_w9i20oFb5dsWRUXKGGW8xfrw/edit#).
A ce soir.

### **Hyacinthe Lacenne** - Feb 15, 2016 at 11:19 AM

cool - updaté ;)

### **Hyacinthe,** - Feb 16, 2016 at 9:33 AM

Voici le compte rendu de la réunion d'hier, disponible
[ici](https://docs.google.com/document/d/1QvdCm2CYsujH8HKidR_w9i20oFb5dsWRUXKGGW8xfrw/edit#)
:  
  
  
CR 15.02.2016  
  

  * Développements technologiques
  * Électronique : problème de bruit (du même ordre de grandeur que les échos). Voir si Gérard Chapilier peut passer.
  * La Red Pitaya n’obéit plus et elle a peut être une entrée analogique cramée.
  * Murgen : premiers tests bientôt. 
  * LUJ en contact avec l’Universitée de Tenesse qui fabrique une sonde low cost.
  * Contacter hyacinthe pour connaître les avancements sur le transducteur. (Quand pourrat-on avoir un transducteur fin). 
  * Pour le 10 Mars : on aura la mécanique d’un côté, l’électronique de l’autre, on utilisera probablement le transducteur imasonic.
  * Cette semaine : tester le montage complet pour voir si des problèmes apparaisses (voir avec MEB pour le côté appli et smartphone).
  * FAK pusher les codes vhdl sur le github.
  * Miscellaneous
  * Préparer une petite réunion électronique avec la communauté (FAK part fin Février).
  * Documentation : sur wiki ou sur github?

### **Hyacinthe** - Feb 22, 2016 at 1:41 PM

Hello All,  
  
Pour le réunion de ce soir, voici l'ODJ disponible
[ici](https://docs.google.com/document/d/1QvdCm2CYsujH8HKidR_w9i20oFb5dsWRUXKGGW8xfrw/edit#heading=h.1zpe488eg7dx).  
  
Vous pouvez ajouter vos remarques en restant raisonnable car notre
concentration doit rester focalisé sur le 10.03 ;)  
  
A ce soir,  
  
O.

### **Emilie Mayer,** - Feb 22, 2016 at 9:24 PM

Re-bonsoir,  
  
Quel est le fin-mot de la réunion d'aujourd'hui  concernant BitMaker? Autre
solution : tenter l'essai avec Murgen?  ![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe   ![Hyacinthe
Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe   ![Hyacinthe
KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe

### **Hyacinthe Lacenne** - Feb 22, 2016 at 9:40 PM

Pour Murgen, c'est peut etre prématuré =)  
  
Plus sérieusement, si le probleme c'est le bruit, y'a pas moyen de le diminuer
avec un moyennage quelquonque (suréchantillonage de lignes soit en montant le
nb de tirs, soit en baissant un peu le framerate) ? Ca permettrait d'arreter
les travaux sur l'électronique et de figer le systeme à aujourd'hui? On
revient sur le besoin d'assembler la ligne entiere comme recommandé par
![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  , pour prendre
une décision.  
  
De toute facon, meme si l'electronique est couverte par bitmaker, on n'a pas
de garantie sur l'assemblage de leur part, c'est bien ça?  
  
D'autre part, si on part sur bitmaker, il faut qu'ils respectent le Cahier des
charges sur la livraison des points suivants:  
  
\- Facteur clé de succès : SNR (ou rapport signal sur bruit) de 20dB sur un
écho chair/os dans tissu organique (cuisse de poulet / épaule d'agneau?)  
\- Livraison de la documentation afférente:  
  

  1. System Block Diagram
  2. Block-by-Block Breakdown
    1. Function
    2. Schematic block
    3. Layout block
    4. Parts selection (and critical specs)
    5. Performance metrics (if applicable)

4\. Fichiers sources / concept:

  * Circuit design 
  * Schematics
  * BOM
    * Part ID
    * Reference Designator(s)
    * Part Type
    * Package Footprint
    * Value/Description/Critical Spec
    * Manufacturer’s Part Number
    * Vendor’s Part Number
  * Overall schematics
  * PCB and corresponding Gerber files
    * Fichiers sources (Altium / Eagle / KiCAD / ...)
    * Gerbers et al

  
Clairement, c'est très ambitieux, mais s'ils sont aussi bons que leur prix
semble suggérer, ca peut etre jouable.

### **Hyacinthe,** - Feb 23, 2016 at 11:04 AM

Le problème de bruit fait qu'on ne peut pas amplifier le signal (en fait ça ne
sert à rien du coup). Et meme en moyennant, on ne verra quasiment rien (juste
les echos importants)

### **Hyacinthe VINCENT,** - Feb 23, 2016 at 11:04 AM

> On revient sur le besoin d'assembler la ligne entiere

  
Je crois aussi que ça devient plus que critique !  
Ca permettra d'avoir une vision globale de tous les problèmes et de ré-
ordonnancer les priorités à partir du cas concret et non à partir de ce que
l'on image être critique. Il ne faut oublier qu'on a des tas de solutions
alternatives pour chaque composant. Pour le 10/03 les gens se moquent bien de
savoir comment on produit le pulse de 100V (je vous offre les 11 piles de 9V
si vous ne trouvez pas mieux d'ici là), ils veulent voir un objet et un echo
sur un écran (en temps réel, cette fois-ci).  
De toute façon, il s'agit juste de consacrer du temps à faire quelque chose
maintenant (l'intégration) qu'on a prévu pour plus tard et debugger plus tard
(mais plus juste).  
Et on ne sait jamais, imaginez on peut même avoir qq bonnes surprises. Ou
alors c'est qu'on a vraiment pas confiance dans ce qu'on a fait.  
Comme disait ma grand-mère (cuisinière, disons, ... créative ...) : "ça peut
pas être complètement mauvais, y a que des bonnes choses dedans !"

### **Hyacinthe VINCENT,** - Feb 23, 2016 at 11:06 AM

> Et meme en moyennant, on ne verra quasiment rien (juste les echos
importants)

  
Et si on prend une cuisse de poulet encore congelée ;-)

### **Hyacinthe VINCENT,** - Feb 23, 2016 at 11:07 AM

Moi j'aimerais bien voir qu'on ne voit rien. Ce serait déjà un grand pas.

### **Emilie Mayer,** - Feb 23, 2016 at 1:54 PM

![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/782178.png)
lacenne   ![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png)
Hyacinthe   où en êtes vous avec bitmaker, est ce possible d'attendre un jour le
temps de "voir qu'on ne voit rien"? Concrètement  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe   ![Hyacinthe, Danseur
du ventre at echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe
![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe   que préconisez
vous ? On fait un vote?

### **Hyacinthe Lacenne** - Feb 23, 2016 at 2:06 PM

Et ont ils réagis sur notre cahier des charges ?

### **Hyacinthe Lacenne** - Feb 23, 2016 at 4:45 PM

hello, j'ai eu un call d'explication/précision sur les demandes dont nous
convenions hier et j'attends leur réaction. Je vous tiens au courant !  
  
@++

### **Hyacinthe** - Apr 11, 2016 at 9:58 AM

Bonjour  à tous,  
  
Un draft d'ODJ est sur le [carnet de
bord](https://docs.google.com/document/d/1QvdCm2CYsujH8HKidR_w9i20oFb5dsWRUXKGGW8xfrw/edit#).
je vous laisse ajouter vos points.  
  
A ce soir.  
  
O.

### **Emilie Mayer,** - Apr 11, 2016 at 6:26 PM

<https://docs.google.com/document/d/1QvdCm2CYsujH8HKidR_w9i20oFb5dsWRUXKGGW8xfrw/edit#>  
Le Cr de la réunion à lire et compléter! ;)

### **Hyacinthe Lacenne** - Apr 11, 2016 at 10:18 PM

Liste des pistes carte mere :
<http://echopen.org/index.php?title=Modules_:_a_motherboard>

### **Emilie Mayer,** - Apr 12, 2016 at 9:54 AM

ton lien  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  ne fonctionne pas

### **Hyacinthe Lacenne** - Apr 12, 2016 at 11:53 AM

Yup ai vu - c'est surtout tout le wiki qui est tombé.

### **Hyacinthe Lacenne** - Apr 12, 2016 at 2:51 PM

Il est remis debout. Seulement le serveur web a été touché, de ~10am à ~5pm

### **hyacinthe,** - Apr 13, 2016 at 6:36 PM

Suite aux discussions sur les breakouts pour chips, il me reste qques
breakouts tssop14 et soic14 - Si besoin :)

[

![](bc3-raw/files/3668504-dsc_0280.JPG)

](bc3-raw/files/3668504-dsc_0280.JPG)

[ DSC_0280.JPG  4.1 MB • Download
](bc3-raw/files/3668504-dsc_0280.JPG)

### **Emilie Mayer,** - Jun 13, 2016 at 10:36 AM

<https://docs.google.com/document/d/1QvdCm2CYsujH8HKidR_w9i20oFb5dsWRUXKGGW8xfrw/edit#heading=h.cwnvy5qes4l8>  
  
Quel sont les odj de la réunion d'ajd?

### **Hyacinthe** - Jun 13, 2016 at 11:54 AM

A priori, le CAPMed. De mon côté, je n'ai rien d'autre d'urgent.  
  
\+ Accueil des nouveaux profils.  
  
A ce soir ;)

### **Hyacinthe Lacenne** - Jun 13, 2016 at 12:09 PM

Ici -&gt;  
Update pour Hall of Fame (ljo)  
  
Discussion sur statut slack (pas finie?)  
  
Update murgen prix + etudiant (ljo)  
Statut du test des piezos smart materials  
  
Format de stockage des images/données (w/ Hyacinthe)  
  
Contest BigData Ultrasons (LJO)

### **Hyacinthe** - Jun 19, 2016 at 1:34 PM

Hello All,  
  
Suite à nos discussions je vous propose que la réunion de demain soit dédiée
au ré-positionnement des réunions hebdomadaires. J'ai ajouté les éléments dans
le document d'ordre du jour. Je vous laisse compléter. Mais globalement, je
propose que nous fassions d'abord un tour de table des besoins et attentes des
uns et des autres puis qu'on définisse le modus operandi et les objectifs de
ces réunions;  
  
Nous pourrons, si le temps le permet, ajouter quelques questions.  
  
Bon dimanche

### **Hyacinthe Lacenne** - Jun 20, 2016 at 3:25 PM

Nickel!  
  
Points ajoutés =)

### **Hyacinthe Lacenne** - Jul 18, 2016 at 9:02 AM

Yop! Ce soir c'est un peu le rush, j'aurai que jusque 19h40. Du coup, pour
être sur que ca vaille le coup, qui passera?

### **Hyacinthe Lacenne** - Jul 18, 2016 at 10:13 AM

ensui

### **Hyacinthe VINCENT,** - Jul 18, 2016 at 11:18 AM

Présent !

### **Emilie Mayer,** - Jul 18, 2016 at 11:32 AM

jy serai

### **Hyacinthe** - Jul 25, 2016 at 6:56 AM

Bonjour à tous,  
  
Pour la réunion de ce soir qui sera présent ? Je crois me souvenir que  ![Hyacinthe
Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  et
![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  vous aviez dit
être absent ?

### **hyacinthe,** - Jul 25, 2016 at 10:52 AM

Wep, je ne pourrai pas venir ce soir - ni le lundi d'après. Gros gros rush au
taf (et passation de mes projets :))  :)



#  Contribution et accord contributeurs

Hyacinthe Lacenne posted this Sep 18, 2016 at 3:02 PM · 1 person applauded

Hey,  
  
Un petit thread pour discuter des CLA ( contributor license agreement ) - qui
sont des documents permettant de clarifier le devenir des contributions, et
l'assignement des copyrights des différents contributeurs. A noter, la
question des copyrights se pose aussi bien en interne qu'en externe. Mais
qu'est ce qu'un CLA?  
  
_A Contributor Licence Agreement (CLA) is strongly recommended when accepting
third party contributions to an open development project, such as an open
source software project. In order to redistribute contributions, it is
necessary to ensure that the project has the necessary rights to do so. A
Contributor Licence Agreement is a lightweight agreement, signed by the
copyright holder, that grants the necessary rights for the contribution to be
redistributed as part of the project._  
  
Ce point mérite d'être discuté pour intégrer les différentes contributions qui
ont eu lieu, aussi bien en interne qu'en externe, et discuter de l'attribution
des copyrights.  
  
Des articles interessants:  
\- Wikipedia of course:
<https://en.wikipedia.org/wiki/Contributor_License_Agreement>  
\- <https://www.clahub.com/pages/why_cla>  
\- ou encore : <http://oss-watch.ac.uk/resources/cla>  
  
Bonne lecture!

### **hyacinthe,** - Oct 12, 2016 at 2:03 AM

Quand se ferait on cette discussion ?  
Pour simplifier, je propose le Classement d'apache,  qui m'a l'air simple et
bien écrit.  
<https://www.apache.org/licenses/icla.txt>

### **Hyacinthe Lacenne** - Oct 13, 2016 at 7:18 AM

nice, le plus simple c que tu prépares un workshop, un vendredi et tu nous dis  
  
@+,  
M

### **hyacinthe,** - Oct 13, 2016 at 12:28 PM

Le 21 y'a déjà un truc, c'est ça ?  
Alors le 28/10. Je prépare une prez. L'outcome serait le choix de l'accord.  
Pas besoin de discussions préalables au sein de la communauté? Je lancerai un
doc + prez sur ce thread.

### **Hyacinthe Lacenne** - Oct 14, 2016 at 6:03 AM

perfect  
  
@++

### **Hyacinthe Lacenne** - Oct 17, 2016 at 8:50 PM

Date tentative repoussée au 04/11 pour cause de vacances ;)  
  
Pour ceux que ca interesse, premier draft de slidedeck at
<https://github.com/hyacinthe124/echomods/blob/master/include/ppt_CLA.md>

### **Hyacinthe Lacenne** - Oct 18, 2016 at 7:42 PM

ah du coup nous on sera à Africa4Tech, décalage encore d'une semaine ?

### **Hyacinthe Lacenne** - Oct 28, 2016 at 12:10 PM

Plus besoin forcément de faire le workshop, sous la license echOpen, on note
que: "_Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to make, use,
sell, offer for sale, import and otherwise run, modify and propagate the
contents of its contributor version_". Ca répond à ma question sur les droits
d'auteurs: ils restent bien aux contributeurs, qui donnent l'autorisation au
projet d'utiliser leur contribution.  
  
Solved! Du coup, où je peux pusher les modules? ;)  
  
Ca peut valoir le coup néanmoins de garder la discussion du 4/11, pas
forcément en mode workshop, mais discussion de la pertinence des CLAs pour le
projet, qu'en pensez vous  ![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  ![lacenne
hyacinthe, echopen](./../../zz_assets/images/avatars/782178.png) lacenne
![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe   ?

### **Hyacinthe,** - Oct 28, 2016 at 12:59 PM

L'idée du projet n'est pas que les droits reviennent à echOpen à la base?
C'est pour ça que tous ceux qui viennent travailler sur le projet (comme les
stagiaires) signent une cessation de droit

### **hyacinthe,** - Oct 28, 2016 at 1:02 PM

Je suis d'accord avec toi, il y avait une ambiguïté à la base. Normalement,
l'utilisateur, en poussant une contribution sans signer de cession,  garde son
copyright.

### **Hyacinthe Lacenne** - Nov 01, 2016 at 2:33 PM

Version du doc de réflexion updaté ici
<https://github.com/hyacinthe124/echomods/blob/master/include/ppt_CLA.md> .  
A noter qu'usuellement dans le FOSS, il n'y a pas de cession de droits
d'auteurs, mais création lors du CLA d'une license qui est accordée par le
contributeur au projet auquel il contribue, d'exploiter sa contribution.  
Une remarque: la cession des droits n'est pas obligatoire, même pour les
personnes rémunérées par une structure. Une simple cession de droits
d'exploitation (mais pas de droits d'auteurs) suffit pour que la structure
sécurise l'utilisation des contributions.

### **Hyacinthe Lacenne** - Nov 05, 2016 at 6:51 PM

le workshop que tu as prévu ce vendredi a donné quoi ?  
  
@+

### **Hyacinthe Lacenne** - Nov 05, 2016 at 7:22 PM

Rien, pas pu le faire (cf ci dessus)  par contre la réponse à ma question est
dans la license echopen: contribution = contributeur garde les droits d'auteur

### **hyacinthe,** - Nov 05, 2016 at 7:26 PM

Par contre, ça peut être intéressant de lire des choses sur le sujet avant une
quelquonque discussion - le monde de l'Open parle peu des CLA et peu savent à
quoi ça correspond.

### **Nassim Chadli,** - Nov 05, 2016 at 7:33 PM

Oui, moi perso, j'ai pas encore compris la finalité de ce topic

### **Hyacinthe Lacenne** - Nov 05, 2016 at 8:04 PM

En gros, la question c'est de savoir qui a le copyright des contributions.  
  
Perso, je n'ai jamais donné mes droits d'auteur à un quelconque projet, et
j'aime bien garder le droit sur mes contribs pour en faire ce que je veux -
comme par exemple pouvoir verser mes bouts de code à d'autres projets, sous
mon nom :)  
  
Laisser les copyright aux contributeurs c'est aussi une bonne pratique de
reconnaissance des travaux de ces même contributeurs bénévoles (par opposition
aux prestataires à qui ces contributions sont achetées).  
  
Très concrètement, je souhaite depuis quelques moi verser mes modules au
projet, tout en gardant des portes ouvertes pour pouvoir en partager également
des éléments généralistes sur d'autres projets.

### **Nassim Chadli,** - Nov 05, 2016 at 8:25 PM

Oui, merci pour l’éclaircissement. ça me semble correcte et logique..

### **Hyacinthe Lacenne** - Nov 06, 2016 at 10:45 AM

hello à tous,  
  
de prime abord, ça paraît en effet logique mais les juristes que nous avons
rencontrés, y compris du libre, pensent que ce n'est pas si simple,
précisément pour protéger  le travail de la communauté. Suis à ce titre
d'accord avec l'ami  ![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  . Et c
important que cette réflexion soit menée en communauté et que le modèle que
nous adopterons ne soit pas pensé pour protéger un travail ou en fonction
d'intérêts particuliers  
  
@++

### **Nassim Chadli,** - Nov 06, 2016 at 11:06 AM

Oui justement mais après coup, trop de contributeurs et ça va rendre le
travail complexe.. pour finir le projet ne sera pas si "open" enfin open au
contributions et fermé sur le plan usage et produit final ce qui est dommage
car c'était l'esprit de départ..

### **Hyacinthe Lacenne** - Nov 06, 2016 at 12:24 PM

bien sûr  ![Nassim Chadli, Instanciator at
echopen](./../../zz_assets/images/avatars/4069013.png) Nassim  , ca restera
complètement Open ! en fait, sur les élts que le device medical utilisera, ca
sera open/libre et il faut qu'on protège précisément la communauté des usages
qui ne respecteraient pas les principes de l'open/libre et pour lesquels la
communauté doit pouvoir se fédérer pour se défendre. C ce point que les
juristes soulèvent.  
  
Ceci étant, le sens de mon message est qu'il faut qu'on pèse tous ensemble les
pour et les contre, et que ca doit faire partie d'un débat qui impliquent
notamment des juristes. Pour ma part, je n'ai pas de positions définies à ce
sujet.  
  
Au total, ce que je retiens de ce fil de discussion et des points de vue ici
échangés, c que ce sujet n'est pas simple, que l'identité même du projet est
l'open et qu'il nous faut un workshop, celui-là même dont nous discutions avec
hyacinthe, et qu'on ne peut pas trancher par évidence.  
  
On vous dit la date et vous pourrez participer par skype !!

### **Hyacinthe Lacenne** - Nov 06, 2016 at 12:24 PM

True. Dans tous les cas, c'est bien de savoir quelles sont les choses qui
sont cédées lors d'une contribution - droit d'auteurs ou license
d'exploitation, et que ce soit transparent pour les contributeurs qui n'ont
pas signé de cession de droits.  
  
Dans tous les cas, la license echopen telle qu'ecrite aujourd'hui dit
clairement que les contributeurs gardent ces droits d'auteurs, et donc pas de
souci pour moi de partager mes modules =)  
  
Il est possible de ceder une license d'exploitation qui garantit basiquement
les memes droits que les droits d'auteurs, c'est le principe des licenses en
mode inbound (contributeur-&gt;projet) plutot que license outboud
(projet-&gt;users).  
  
De mon côté, c'est simple, les modules que j'ai développé peuvent être
utilisés dans d'autres applications, et j'aimerai les y voir. Garder des
droits sur ces contributions permets du coup de faire profiter les communautés
open hardware par exemple d'un DAQ haute vitesse, wireless =)  
  
Des notes sont prises sur
<https://github.com/hyacinthe124/echomods/blob/master/include/ppt_CLA.md>,
n'hésitez pas à pointer des incohérences.

### **Hyacinthe Lacenne** - Nov 06, 2016 at 12:36 PM

![Nassim Chadli, Instanciator at
echopen](./../../zz_assets/images/avatars/4069013.png) Nassim , c'est plutot
l'inverse que je trouverais dommage: que le projet soit ouvert aux usages,
mais fermé aux contributions bénévoles pour des raisons que je ne comprends
pas vraiment.  
Ceci étant dit, je suis curieux et intéressé de voir le raisonnement des
juristes à préconiser cette assignation de copyrights.  
  
En parallèle, je trouve ça bien aussi de faire un distingo entre les
contributeurs bénévoles, et ceux rémunérés par l'asso, dont les contribs sont
de facto celles de l'asso.

### **Hyacinthe Lacenne** - Nov 06, 2016 at 3:38 PM

ok nice, ca nous promet des débats riches ! partons sur un workshop dans les
toutes prochaines semaines

### **Hyacinthe Lacenne** - Nov 06, 2016 at 8:38 PM

![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/782178.png)
lacenne   ce serait cool qu'un juriste puisse exposer son point de vue ici
et échanger en amont de cet atelier, histoire de le préparer, tu penses
pouvoir en motiver un a échanger ici?



#  events

Hyacinthe Lacenne posted this Mar 19, 2016 at 7:14 PM · 1 person applauded

la team de Tedx est revenu vers nous pour nous faire intervenir à l'occas de
leur deuxième gros event de l'année : l'échappée  
  
au pgm 3 jours : conf + ateliers de sensibilisation/onboarding (RH +
financeurs) + rencontre.  
  
parmi les conférenciers, la scène de la frenchtech. En principe, Peter Thiel
fait la clôture  
  
parmi les institutionnels qui débusque les bons projets : la fondation Bill
&amp; Melinda Gates, Google, etc...  
  
Et ça passe dans un château donc c rigolo

### **hyacinthe,** - Mar 20, 2016 at 12:50 PM

Chouette ! C'est quand? Ça peut être sympa d'y aller en équipe si l'événement
s'y prête :)

### **Hyacinthe Lacenne** - Mar 21, 2016 at 10:57 AM

sure ! ;) ensuite je crois que le nb de billets est limité  
  
en pcpe ce sont des keynotes en one-man dont le format 10' est réglé (comme
ted) mais j'ai insisté sur la nature communautaire du projet et la nécessité
que l'on soit plusieurs à le présenter - ils doivent me faire un retour - ce
serait d'ailleurs pas mal qu'il y a ait une fille  ![Emilie Mayer, Community &
knowledge  at echopen](./../../zz_assets/images/avatars/1269172.png) Emilie
;)

### **Emilie Mayer,** - Mar 21, 2016 at 1:45 PM

Motivée! Ce serait quand?

### **Hyacinthe Lacenne** - Mar 21, 2016 at 2:28 PM

ce serait genre 28, 29 et 30 mai

### **Hyacinthe Lacenne** - Apr 05, 2016 at 10:40 PM

hello,  
  
comme promis, le lien vers la hope conf  
  
<https://hopeconf.wordpress.com/>  
  
[mitch altman](https://fr.wikipedia.org/wiki/Mitch_Altman) est intéressé par
echOpen ;)  
  
il s'agit de proposer avant la fin du we une propale de workshop  
  
ca serait rigolo d'y aller à plusieurs, ca se passe à NYC du 22 au 24 juillet  
  
@++

### **Hyacinthe Lacenne** - Apr 06, 2016 at 6:29 PM

la deadline pour proposer un workshop est vendredi, si vous avez des
suggestions, c le moment ;)

### **Emilie Mayer,** - Apr 08, 2016 at 9:06 AM

C'est à dire deadline pour proposer un workshop? A new York?

### **Hyacinthe Lacenne** - Apr 25, 2016 at 8:04 AM

oui c cela, on a été relancé. le pb c que ca coûte cher d'y aller... mais si
qqn se sent, je peux voir si on peut arranger cela

### **Hyacinthe Lacenne** - Apr 26, 2016 at 8:07 AM

hello,  
  
Luke Flegg du CollabCamp est venu vers nous. Il organise un  "[Collaboration
Lab Camp Paris 2016](https://www.facebook.com/events/747763475367071/)", un
event du 13 au 17 mai et souhaiterait héberger qqs events chez echopen  
  
1 skype est en cours d'organisation, si ca intéresse d'y participer, dites-moi
;)



#  Lost &amp; found @QG Archived

Hyacinthe Lacenne posted this May 29, 2016 at 3:49 PM

Yop, ai du oublier un cable d'iphone 5 noir ce vendredi au bureau... faites
signe si vous le retrouvez =)

### **hyacinthe,** - May 30, 2016 at 5:56 PM

Ai retrouvé :)



#  retour newsletter Archived

Hyacinthe Lacenne posted this Jan 16, 2016 at 3:51 PM

hello Emilie,  
  
merci pour la newsletter, qqs remarques de détail :  
  
"nous avons organisé"  
"l'objectif a été atteint : les performances de l'application ont été
multipliées par 10"  
"provient d'une partie du corps : la main de Hyacinthe! "  
  
bon we;)



#  Électronique et microcontrolers

hyacinthe posted this Aug 19, 2016 at 7:54 AM

Petit thread dédié.  
  
Première question du coup :) c'est vrai qu'on recherche un programmateur PIC?
Et BM ne couvre pas?

### **Hyacinthe Lacenne** - Aug 19, 2016 at 10:51 AM

c pour le pipe maker, c joris qui était dessus cc  ![Hyacinthe, Danseur du ventre
at echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe

### **Joris JEAN-BAPTISTE,** - Aug 19, 2016 at 12:27 PM

Pour tenir les délais je pense que ce serait pas mal d'avoir un spé PIC  
Et d'être fixés sur les performances de l'ADC  ( jusqu'à 18MSPS en utilisant 1
ou 2 ADC (turbo mode))  
  
A l'heure actuelle on atteint 8,6MSPS en continuous mode, résolution 6 bits et
en utilisant la FIFO

### **Hyacinthe Lacenne** - Aug 19, 2016 at 12:50 PM

Pour le pipe maker la cape beaglebone adc 40msps 10bits, accès en temps réel a
la data dans un userspace Linux, me semble pas mal non plus :)

### **Hyacinthe Lacenne** - Aug 19, 2016 at 12:56 PM

Ensuite,  ça dépend pour quoi on veut d'en servir dans le pipe maker, et
quelles contraintes on a, c'est pas clair le besoin :)

### **Hyacinthe Lacenne** - Aug 19, 2016 at 1:01 PM

![Joris JEAN-BAPTISTE, Elec analog & digit + Soft  at
echopen](./../../zz_assets/images/avatars/4392629.png) Joris  ![Hyacinthe,
Danseur du ventre at echopen](./../../zz_assets/images/avatars/1248689.png)
Hyacinthe  your point of view sur beagle bone ?

### **Joris JEAN-BAPTISTE,** - Aug 19, 2016 at 1:10 PM

Si la maîtrise de l'ADC beaglebone est au point pourquoi pas.  ![Hyacinthe,
Danseur du ventre at echopen](./../../zz_assets/images/avatars/1248689.png)
Hyacinthe  devrait confirmer

### **Hyacinthe Lacenne** - Aug 19, 2016 at 1:15 PM

Attention, pas que Beaglebone. beaglebone plus prudaq. Je crois comprendre que
bitmaker s'y interesse aussi.  
  
L'accès aux data se passe par un device Linux - hyperfacile. Soit 40msps
single channel, soit 2x20msps. Sur 10bits.  
  
320Mo de buffer pour stocker les data si besoin.  
  
Encore une fois, ça dépend ce qu'on attend de l'outil (ca ne retire pas la
question de sortie des data post adc), en tout cas en termes de simplicité
j'ai bien apprécié, c'est ce qui me sert à acquérir des boucles vidéos avec la
sonde atl ;)

### **Hyacinthe,** - Aug 19, 2016 at 1:56 PM

Le beaglebone tout comme la RedPitaya offre l'avantage d'utiliser un outil
tout fait. C'est un peu moins cher que la RP, environ 150€ de ce que j'ai vu.
C'est une possibilité. Mais si on regarde à plus long terme, de toute façon il
faudra qu'on développe notre propre solution, d'où regarder la piste PIC32.

### **Hyacinthe Lacenne** - Aug 19, 2016 at 2:02 PM

ok c une bonne communauté mais je ne pensais que c'était aussi cher

### **Hyacinthe Lacenne** - Aug 19, 2016 at 2:24 PM

A comparer ce qui est comparable ;)  
Le pic a un adc, et si on ne veut qu'un adc effectivement c'est peut être ce
dont on a besoin.  
  
Par contre jamais un pic n'exposera 40msps en temps réel pour un os classique.  
  
Ensuite, comment exporter les données du PIC, qu'est ce qu'on veut faire avec
le pic,... C'est en fonction des réponses à ces questions ( pas encore clair
pour moi today en lisant ce thread ) qu'on pourra vraiment répondre quelle
solution est la plus appropriée :)



#  apéros

Hyacinthe Lacenne posted this Feb 15, 2016 at 9:05 AM · 1 person applauded

hello,  
  
laurent bloch, spé de sécurité info, DSI de Paris Dauphine est ok pour faire
un apéro le 26 février ;) voici son
[blog](http://www.laurentbloch.org/MySpip3/) et ses [skills
](https://www.linkedin.com/in/laurentbloch1)  
  
ceci a vocation à accueillir les posts dédiés aux apéros  ![Hyacinthe,
echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  c bien comme ça
qu'on fait ?

### **Hyacinthe Lacenne** - Feb 15, 2016 at 1:51 PM

btw, après l'idée serait d'on-boarder Laurent comme sys admin du proj.

### **Hyacinthe Lacenne** - Mar 07, 2016 at 10:33 AM

hello,  
  
c le mois de la contribution wikipedia donc je vous propose un apéro vendredi
soir autour de contributions real time Open Source Santé + intro à mediawiki.  
  
Dans la boucle :  
  
\- librehealthcare et par capillarité, leur demander de mettre dans la boucle
leur collègies  
\- adaweek, histoire de combattre le gendre gap car les contributeurs sont
"déséquililbrément" masculins  
\- chsritophe Ducamp : car c un spé de mediawiki  
\- Nicolas Etaix + Catherine Philips  
  
oilà ;)

### **Hyacinthe Lacenne** - Mar 07, 2016 at 10:51 AM

Anne-Laure Prévost, psdte de wikipedia france est Ok pour nous accompagner et
viens d'envoyer un mail à
[paris@lists.wikimedia.fr](mailto:paris@lists.wikimedia.fr) pour trouver des
wikimediens qui nous aideraient à monter l'event ;)

### **Hyacinthe Lacenne** - Mar 07, 2016 at 11:28 AM

je viens d'avoir un retour des girlz de l'Adaweek et elles sont ok pour nous
accompagner et pinger leur réseau ;)

### **hyacinthe,** - Mar 07, 2016 at 12:57 PM

Excellente idée :)

### **Hyacinthe Lacenne** - Mar 07, 2016 at 2:23 PM

retour de Christophe Ducamp, il est Ok ;)

### **Emilie Mayer,** - Mar 07, 2016 at 3:29 PM

Pour ce vendredi?

### **Hyacinthe Lacenne** - Mar 08, 2016 at 9:07 AM

Bastien Guéry est in ;)

### **Emilie Mayer,** - Apr 02, 2016 at 4:59 PM

les slides de l'apéro de Laurent Bloch sont sur le Wiki :
<http://echopen.org/index.php?title=File:Securitedonneessante.pdf>

### **Emilie Mayer,** - Apr 08, 2016 at 6:04 PM

CR  apéro 4 avril : n'hésitez pas à compléter  
<https://docs.google.com/document/d/1vlyh27bkYkWKWK3gJIZOSd468JF3SfQmBhOSS7LkoaA/edit?usp=sharing>

### **hyacinthe,** - Apr 21, 2016 at 1:25 PM

Un apero de prévu ce vendredi ?

### **Emilie Mayer,** - Apr 21, 2016 at 3:21 PM

je ne sais pas...

### **Hyacinthe Lacenne** - Apr 22, 2016 at 9:56 AM

je ne crois pas. je vais me recaler sur la programmation ;)

### **Hyacinthe Lacenne** - May 23, 2016 at 12:18 PM

relance apéro - je me suis calé sur les dates des intervenants et ca donne tel
qu'indiqué sur le wiki  
  
  
08.06.16 Sensitive Health Data  
  

Jean-Baptiste Soufron, lawer, former Chief Legal Officer of the Wikimedia
Foundation, former Secreaty General of french National Digital Council  
  

  
17.06.16 Certification process of mobile health devices  
  

Guillaume Marchand, CEO of DMD santé  
  

  
24.06.16 (maybe other date) topic TBA : Machine learning, NLP for automatic
medical report  
  

Philippe Ameline, founder and ex CEO of Nautilus



#  rencontre CRI

Hyacinthe Lacenne posted this Feb 22, 2016 at 1:11 PM · 1 person applauded

deuxième rencontre avec le CRI  
  
visite de l'Open Lab  
\- par Kevin Lhost, électronicien qui fat des choses très rigolotes, notamment
des détecteurs de mouvements open hardware - intéressant pour parkinson &amp;
such  
\- matos : plein d'imprimantes 3D avec plein de type matériaux, une découpe
laser et des choses + spécialisées pour l'électronique  
\- ouvert qd on veut : ce serait bien d'y confectionner notre boîte pour le 10
mars  
\- nous est proposé un hackathon sur un sujet de notre choix, autour de l'open
hardware, fin mars avec leurs étudiants (licence, master, doctorants) assortis
d'un mini-exposé sur le sujet  
\-- je proposerai un hackathon méca / on ferait venir la team de l'AFORP  
hyacinthe, tu voulais faire un tour là-bas, c qd tu veux !  
  
\- l'Open Lab migre à cochin au  mois d'avril, donc proposition d'installation
d'une instance d'echopen, ils sont ok. Du coup, soit  
\-- installation d'un des aspects : méca ou électronique  
\-- soit une full install d'une instance genre murgen  
en tout cas, l'orga d'un hackathon permettrait d'approfondir nos interactions
et de trancher dans de bonnes conditions ce genre d'alternative



#  Lol Du Jour

Hyacinthe posted this Feb 01, 2016 at 6:54 PM · 2 people applauded

Voilà ;)  

[

![](bc3-raw/files/1232043-img_1824.JPG)

](bc3-raw/files/1232043-img_1824.JPG)

[ IMG_1824.JPG  480 KB • Download
](bc3-raw/files/1232043-img_1824.JPG)



#  des news (1) ;)

Hyacinthe Lacenne posted this Mar 19, 2016 at 7:08 PM · 3 people applauded

voici qqs news de la semaine  
  
\- bitmaker a quasiment fini son travail -&gt; on a des top echos !!!  
  
\- gérard a fini son pulser -&gt; il faut top job !! gérard koi  
  
\- on a le nouveau transducteur jeudi, Hyacinthe le présentera le 24  
  
côté module  
  
\- mathieu a fini l'interface web permettant de récupérer la data de la
redpitaya à partir d'une config utilisateur  
  
\- on a tout l'environnement de dev android sous la forme d'une image disk
Ubuntu (je ne peux pas le pusher car 20Go, donc je l'hébergerai sur notre
nouveau site)  
  
\- on attend les news de morgen et il me semble que Hyacinthe est en train de
préparer une top méca !  
  
et last but not least, le premier echo de la plaque sur l'app !!!  
  
  

[

![](bc3-raw/files/2734027-screenshot_2016-03-19-19-58-15.png)

](bc3-raw/files/2734027-screenshot_2016-03-19-19-58-15.png)

[ Screenshot_2016-03-19-19-58-15.png  340 KB • Download
](bc3-raw/files/2734027-screenshot_2016-03-19-19-58-15.png)

### **Hyacinthe KHOYRATEE,** - Mar 19, 2016 at 7:25 PM

Vous assurez les gars! :D

### **Hyacinthe VINCENT,** - Mar 19, 2016 at 7:31 PM

J'ai l'impression que ça sens le chaud chez echOpen.

### **Hyacinthe Lacenne** - Mar 22, 2016 at 11:29 PM

bon la même image qu'en haut mais deux jours plus tard  
  

[

![](bc3-raw/files/2841835-screenshot_2016-03-23-00-13-00.png)

](bc3-raw/files/2841835-screenshot_2016-03-23-00-13-00.png)

[ Screenshot_2016-03-23-00-13-00.png  223 KB • Download
](bc3-raw/files/2841835-screenshot_2016-03-23-00-13-00.png)

  
  
et là le derme, le ligament un peu de muscles et de l'os de l'extrémité
radiale du Hyacinthe  
  

[

![](bc3-raw/files/2841847-screenshot_2016-03-23-00-18-18.png)

](bc3-raw/files/2841847-screenshot_2016-03-23-00-18-18.png)

[ Screenshot_2016-03-23-00-18-18.png  224 KB • Download
](bc3-raw/files/2841847-screenshot_2016-03-23-00-18-18.png)

  
  
nice job  ![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  ;)

### **Hyacinthe KHOYRATEE,** - Mar 23, 2016 at 8:34 AM

Hyacinthe toujours aussi impressionnant!

### **Hyacinthe Lacenne** - Mar 25, 2016 at 9:40 PM

\- 3 ingé de l'ISEP (top école d'ingé elec), 4ème année,  sont "survoltés" sur
echOpen et veulent y faire leur stage. Je devrait les rencontrer courant de
semaine prochaine. Et un de mes collègues de l'HD qui enseigne aussi à l'ISEP
va organiser une prez d'echOpen dans leurs locaux, à Issy les Moulineaux, et
il n'est pas impossible que l'on puisse utiliser leur matos  
  
\- j'ai eu un retour d'amélie verdier, la secgen de l'ap qui m'informe que le
dir. de l'hôtel dieu est dithyrambique ;)  
  
- [bastien guerry](https://bzg.fr/) vient nous faire un apéro sans doute dans 2 semaines. Bastien est un libriste et accessoirement un de dev d'emacs ;) il  vient nous faire un topo sur le développement d'applis libres #HTML5 pour l'apprentissage de la lecture et de l'écriture s'appuyant sur les travaux de Stanislas Dehaene. Je vous raconterai plus en détails lundi sur les travaux de Dehaene mais c extraordinaire   
  
\- &amp; dans le genre exo, on a reçu la visite de l'osteo de l'équipe de foot
de twickenham qui voudrait une sonde pour diagnostic rapide de fêlures,
entorses sur le temps réel

### **Hyacinthe Lacenne** - Mar 25, 2016 at 9:45 PM

Trop excellent !!

### **Hyacinthe VINCENT,** - Mar 25, 2016 at 10:06 PM

Les affaires reprennent !  
C'est vrai, on avait pensé aux chevaux de course mais pas aux joueurs de
foot...

### **Hyacinthe** - Mar 29, 2016 at 3:01 PM

Hello all,  
  
Premier retour presse pour echopen ;) [Ici](http://www.makery.info/2016/03/29
/echopen-lance-une-sonde-dechographie-open-source/) par Ewen, journaliste de
Makery France, qui été présent à la soirée de jeudi... Bonne lecture.

### **Hyacinthe** - Mar 31, 2016 at 2:03 PM

La version anglaise de l'article : <http://www.makery.info/en/2016/03/29
/echopen-lance-une-sonde-dechographie-open-source/>

### **Hyacinthe Lacenne** - Nov 01, 2016 at 10:53 AM

une équipe de chercheurs de la Simon Bhyacinthear University nous a contacté ce
matin car ils souhaitent concevoir un échographe frugal à usage pour les pays
du Sud, et souhaitent faire cela avec nous ;)  
après Bruxelles, notre 2ème entité d'internationalisation -&gt; à suivre, on
vous fait les feedbacks asap  
  
;)

### **Emilie Mayer,** - Nov 07, 2016 at 7:11 PM

Si besoin je parle espagnol (à peu près)

### **Hyacinthe Lacenne** - Nov 08, 2016 at 12:54 AM

![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  si ca te
branche un starter-kit en espagnol, tu es la bienvenue ;) je blague



#  traduction wiki on drive

Hyacinthe Lacenne posted this Feb 07, 2016 at 12:08 AM · 1 person applauded

hello à tous,  
  
Catherine Philips et Nicolas Etaix ont fait un super travail de trad.  
  
voici le dossier drive :

  
<https://drive.google.com/open?id=0B0V8htWBLPWBNk5OZThJMEtGWjg>

  
  
leur avais proposé d'éditer directement le wiki mais il préfère une contre-
validation sur le drive.  
  
leur avais proposé de commencer par  
  
_la page de home_

<http://echopen.org/>

  

_la page de FAQ_

  

<http://echopen.org/index.php?title=FAQ>

  

_le groupe de pages correspond à l'onglet Enjeux sur la home_

<http://echopen.org/>

### **hyacinthe,** - Feb 08, 2016 at 8:06 AM

On les ajoute à ce basecamp ? Je sais en tout cas qu'on gagnerait à y mettre
Nicolas :)

### **Hyacinthe** - Feb 08, 2016 at 8:15 AM

Si vous voulez.  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/782178.png) lacenne  qu'en penses
tu ? sont-ils de futures contributeurs réguliers ?  
  
De quel Nicolas parles tu ? Si c'est Nicolas Nallet, je peux lui demander s'il
le souhaite.

### **Hyacinthe Lacenne** - Feb 08, 2016 at 8:39 AM

![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  je
pense que  ![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  parle des
traducteurs du wiki : catehrine philips et nicolas etaix

### **Hyacinthe** - Feb 08, 2016 at 9:34 AM

Ok. Merci. Du coup, pensez-vous qu'ils soient des contributeurs réguliers ?
Afin de la ajouter. Merci.

### **hyacinthe,** - Feb 08, 2016 at 10:28 AM

Nico faisait de l'ultrason, ça peut valoir le coup. No se pour Catherine.

### **Hyacinthe** - Feb 08, 2016 at 10:30 AM

Ok, je l'ajoute mais est ce que quelqu'un peut me donner son e-mail ? Merci

### **Hyacinthe Lacenne** - Feb 08, 2016 at 11:18 AM

voici : [zenico124@gmail.com](mailto:zenico124@gmail.com)

### **Hyacinthe** - Feb 08, 2016 at 11:20 AM

Merci, c'est ajouté.

### **Nicolas,** - Feb 08, 2016 at 12:56 PM

Bonjour!

### **Hyacinthe** - Feb 08, 2016 at 3:41 PM

Bonjour  ![Nicolas, Tech & such at
echopen](./../../zz_assets/images/avatars/1946185.png) Nicolas  bienvenue sur
le basecamp echopen. A ta dispo si tu as des questions.

### **hyacinthe,** - Feb 08, 2016 at 5:48 PM

Kikoo @Nicolas ;)

### **Nicolas,** - Feb 08, 2016 at 6:15 PM

Salut, maintenant que vous avez déplacé les fichiers sur votre drive je peux
encore les modifier, mais je ne peux pas en ajouter. Est ce qu'il y a moyen
d'avoir des droits pour cela. Sinon je peux mettre un lien vers les nouveaux
fichiers ici peut etre?

### **Hyacinthe** - Feb 08, 2016 at 6:40 PM

![Nicolas, Tech & such at
echopen](./../../zz_assets/images/avatars/1946185.png) Nicolas  je t'ai ajouté
au dossier. Tu devrais alors pouvoir ajouter ce que tu veux.

### **Nicolas,** - Feb 08, 2016 at 6:44 PM

Merci, parfait!

### **Nicolas,** - Feb 08, 2016 at 7:20 PM

Re-bonjour tout le monde,  
Petite question pour les personnes ayant rédigé la page FAQ. Sur la partie "A
quel stade de développement en est le projet?", il y a une phrase qui n'est
pas finie j'ai l'impression: " Un module de formation de 48H à ce que nous
appèlerons l’EchoSthétoscopie". Est ce que ce module est en cours de
développement, ou bien est-il déjà prêt?  
PS: Je ne sais si il vaut mieux commencer une nouvelle discussion pour chaque
question ou bien juste ajouter toutes les questions ici...

### **Hyacinthe Lacenne** - Feb 08, 2016 at 10:57 PM

hello  ![Nicolas, Tech & such at
echopen](./../../zz_assets/images/avatars/1946185.png) Nicolas ,  
  
le module de formation est en cours de conception en fait ;)  
  
par ailleurs, je ping  ![Hyacinthe,
echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  pour la
question que tu soulèves  
  
@++

### **Nicolas,** - Feb 09, 2016 at 8:15 AM

Merci hyacinthe, tant que je suis sur le sujet, je viens de me rendre compte que
j'ai peut etre surinterprete, le but c'est de faire la formation en 48h
effective? Pour l'instant j'avais traduit par 2 days training, mais j'ai peut
etre tord.

### **hyacinthe,** - Feb 09, 2016 at 8:18 AM

Sur un week-end c'est ça?

### **Hyacinthe** - Feb 09, 2016 at 8:21 AM

Bonjour  ![Nicolas, Tech & such at
echopen](./../../zz_assets/images/avatars/1946185.png) Nicolas  merci pour tes
remaruqes.

  * La formation a pour ambition d'être effectuée en 48h  (soir un week-end par exemple) =&gt; 2 days training est parfait. 
  * Pour l'utilisation de l'outils basecamp, l'idée est de réussir insérer les informations au bon endroit. S'il s'agit d'une remarques qui s'insère dans un fil de discussion, alors c'est parfait, sinon, il est intéressant de créer un nouveau fil, uniquement si la thématique mérite des échanges au sein de la communauté. Pour ce qui est des petites questions, nous avons un slack, sorte d'outils de chat dans lequel je viens de t'ajouter.

### **Emilie Mayer,** - Feb 09, 2016 at 11:03 AM

Notre formulation en français est en effet ambiguë, car formation en 48 h
effective fait plutôt une semaine. On devrait remplacer 48h, par week-end.

### **Hyacinthe Lacenne** - Feb 11, 2016 at 3:31 PM

hello à tous,  
  
après cette séquence d'échange pour vous dire que je vais commencer la
migration des contenus stabilisés du drive vers le site : je commence par la
home  
  
@++

### **hyacinthe,** - Feb 11, 2016 at 3:50 PM

Tu migrer bien la version anglaise dans l'espace langue française, et la
version anglaise dans la zone anglophone ?

### **Hyacinthe Lacenne** - Feb 11, 2016 at 4:07 PM

OMG, on a deux versions ? on avait dit en réu de bureau d'il y a 10 jours que
l'on migrait tout le contenu non ?  
bon, anyway on a une trace de tous les contenus, donc je peux les rétablir

### **Nicolas,** - Feb 11, 2016 at 6:49 PM

Hello,  
  
Je me suis permis de changer le lien vers wikipedia pour open source hardware
pour le wiki anglais.  
  
Nico

### **hyacinthe,** - Feb 12, 2016 at 7:26 AM

En fait mediawiki propose de manière intégrée (et bien faite) la localisation
des pages - cf la discussion sur Slack.  
Ça permet de maintenir pour les pages du wiki les deux langues, et de servir
la bonne version aux visiteurs :) pas besoin de le faire partout, seulement
pour les pages ou y'a deux langues :)

### **Hyacinthe Lacenne** - Feb 12, 2016 at 10:46 PM

ah ok - simplement pour que je sois up-to-date, on est dac qu'on avait décidé
de basculer toutes les nouvelles contrib en anglais.  
Si c le cas, deux versions, ca peut donner une lecture un peu heurtée pour
ceux qui, situés dans un set de pays francophone, verraient la langue changer
d'une page à l'autre  
  
ceci étant, g sans doute raté le coche sur le slack, donc je m'adapte ;)



#  Onboarding étudiants epitech

Hyacinthe Lacenne posted this Jan 25, 2016 at 8:21 AM

hello à tous,  
  
suite à 1 conf avec Hyacinthe il y a 2 semaines chez epitech, on a deux étudiants
intéressés par le projet. Ils passent en fin de matinée. Ils sont plutôt
junior et orientés web. pourquoi pas les mettre sur le dev d'une interface web
permettant l'accès aux data en remote  
  
on vous tient au jus !

### **Hyacinthe Lacenne** - Jan 25, 2016 at 4:27 PM

on boarding en cours, les 2 juniors de l'epitech ont commencé à installer les
outils. A priori, ils disent avoir pas mal de temps pour ce semestre  
  
ils travailleront sans doute du côté C/C++ de la JNI  
  
ils ont pu aussi échanger avec Greg  
  
on les revoit mercredi pour une orientation dev plus précise  
  
oilà

### **Hyacinthe Lacenne** - Feb 16, 2016 at 2:23 PM

Rudy Gratay, en cours de formation à la web academy d'Epitech, va faire un
stage de 3 semaines non rémunéré .  
C'est un dev essentiellement front mais a l'air de bien connaitre  bien node.  
  
Je lui ai proposé de travailler à une web-interface sur redpitaya qui
permettra de récupérer de la data  pour les traiteurs du signal.  Idéalement,
on intégrera des outils d'interactions avec le hardware, de ce que j'avais vu
du code serveur, ca a l'air possible.  
  
Après quoi, une fois le pipe installé, je vous propose que l'on crée un compte
codenvy.com/, on configurera ce qui faut pour récupérer la data et ceci
permettra de tester en remote le traitement du signal avec toutes les routines
et autres lib installées, installables et configurables.  
  
@++

### **hyacinthe,** - Feb 16, 2016 at 5:07 PM

Y'a cloud9 qui est pas mal too :)  
Du coup, tu veux le mettre en dev de node sur la pitaya, ou de chopper les
infos de la pitaya pour les displayer ?  
Anyhow, good news!!

### **Hyacinthe Lacenne** - Feb 16, 2016 at 8:17 PM

yes cloud9 est bien aussi - de git mais  
  
en fait d'abord une interface de display et récupération de la donnée. je
pense que le back restera en C  
  
et ensuite un setup dédié d'un env ou plusieurs (virtualenv)  python sur
codenvy ou cloud9  
  
@++

### **Hyacinthe Lacenne** - Feb 16, 2016 at 8:40 PM

btw,  ![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe
propose que l'on ajoute une notion de coopétition - ayant en tête le RAMP
#epidemium dont l'expérience a été concluante.  
  
Du coup, on peut ajouter à chaque run de production, un executable qui update
un leaderboard sur la web-interface de la redpitaya  
  
oilà;)

### **Hyacinthe Lacenne** - Feb 17, 2016 at 8:43 AM

Précise?  Tu peux avoir un leaderboard pour masse d'actions (et en gamifier
plein d'autres =) ):  
  
\- prise d'image (et sauvegarde cloud)  
  
\- debugs  
  
\- écriture au wiki ( infos pouvant être pullées de
<http://echopen.org/index.php?title=Special:ContributionScores> )  
  
\- documentation au sens large,  
\- ...

### **Hyacinthe Lacenne** - Feb 22, 2016 at 2:19 PM

Hello, le camarade de l'Epitech est passé ce jour pour se présenter.  
  
todo :  
  
serveur de récupération de la data + spec de l'image à obtenir  
  
-  à destination des traiteurs du signal  
\- download en bulk ou sur fichier sous requêtes -&gt; nombre d'images...  
\- push sur la redpitaya (fréquence d'échantillonage, nombre de lignes, nombre
de points ...)  
  
Il commence lundi !



#  Traduction du Wiki en aglais

Emilie Mayer posted this Jan 22, 2016 at 2:10 PM · 1 person applauded

hello,  
  
Je viens de réaliser que la page accueil du Wiki, n'est pas en anglais,
problème non?

### **Hyacinthe Lacenne** - Jan 25, 2016 at 8:12 AM

merci Emilie de cette intiative. Btw, je suggèrerais que l'on fasse un appel à
compétences sur notre page facebook. Qu'en dis-tu ?  
  
A bientôt,  
M

### **hyacinthe,** - Jan 25, 2016 at 9:06 AM

Sweet ! BTW, nos  belges ientnus au captec n'étaient-ils pas partant pour de
la trad ?

### **Hyacinthe Lacenne** - Jan 25, 2016 at 5:18 PM

yes, il faut qu'on relance -&gt; to do

### **Emilie Mayer,** - Jan 25, 2016 at 6:13 PM

j'ai posté un msg Facebook

### **Hyacinthe Lacenne** - Jan 26, 2016 at 6:17 PM

hello Emilie,  
  
on devrait avoir du renfort. je forwarde son mail - donc on devrait la croiser
vendredi  
  
"Salut,  
  
Je voulais venir au prochaine rdv echopen (je ne sais pas quand c'est,
mais...). Anyway, je suis conceptrice-redactrice anglophone pour les objets
digitaux et je peux aider sur la traduction du wiki. Normalement je facture
600 la journée pour cela, mais bon, comme j'etais deja interessée et puis j'ai
un peu de temps. Voici mon LinkedIn si tu veux voir un peu :  
  
Catherine Phillips  
Copywriter / Concepteur-Redacteur Publicité Integrée  
<https://www.linkedin.com/profile/view?id=39217606>  
  
On peut en parler au prochain rdv du groupe si tu veux. Sinon... quand c'est ?  
  
:)"

### **hyacinthe,** - Jan 26, 2016 at 7:17 PM

Heureusement qu'elle ne fait pas payer ;)

### **hyacinthe,** - Jan 26, 2016 at 7:19 PM

Btw, quid d'un trasnl-athon ?  
Même entre nous, booker 1 journée / s'entendre pour chacun passer 20 mins par
semaine sur ce point ?

### **Hyacinthe Lacenne** - Jan 26, 2016 at 7:26 PM

J adore l idée d un translathon ;)

### **Hyacinthe VINCENT,** - Jan 27, 2016 at 8:47 AM

Oui, moi aussi j'aime l'idée.  
On fait des binomes : un nul-ophone, un anglophone et un seul clavier. Comme
ça le nul-ophone progresse et l'anglophone produit un anglais simple et
compréhensible. Idéalementle nul-ophone devrait être l'expert du domaine
concerné.

### **Emilie Mayer,** - Jan 27, 2016 at 9:58 AM

Tout ça me parait super :) ! Elle sera là vendredi? On peut éventuellement la
mettre dans la boucle de l'orga d'un translaton?



#  journée de l'imagerie du vivant

Hyacinthe Lacenne posted this Jan 17, 2016 at 4:31 PM · 1 person applauded

hello,  
  
![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe   nous fait
savoir que cet [event](http://www.cite-sciences.fr/fr/au-programme/lieux-
ressources/cite-de-la-sante/au-programme/cycle-innovation-sante/) peut être
intéressant  
  
btw, on peut se proposer une sortie/débarquement tous ensemble le 10/11/12
février pour la [journée](http://www.cite-sciences.fr/fr/au-programme/lieux-
ressources/cite-de-la-sante/au-programme/cycle-innovation-sante/%20) de
l'imagerie du vivant  
  
@++



#  Tour de Contrôle FPGA Archived

Hyacinthe LICCIONI posted this Jan 07, 2016 at 2:58 PM

Bonjour à tous,  
  
Alors j'ai discuté avec Colin et voilà ce que j'ai comprit:  
Red Pitaya a un code FPGA déjà tout fait. Ce code, une fois compilé et
implémenté sur le FPGA.  
Il y a ensuite la couche "Driver" qui est située au niveau Linux et qui permet
d'accéder aux registres, entrées et sortie de la carte.  
Et enfin la couche applicative qui est en C et utilise des fonctions qui font
appel aux drivers pour accéder aux entrées, sorties, registres de la carte.  
  
Cela implique donc que pour utiliser le code FPGA, je doive programmer en C.
Or, ce code est, Hyacinthe attestera, franchement moyen... Entre les fonctions
déclarées mais non programmées, les fonctions buguées, et le fait que cette
couche applicative ne soit pas entretenue, nous en arrivons à des applications
qui sont lentes, et font que nous pouvons nous asseoir sur les 125MS/s promis
par l'ADC.  
  
Une autre alternative serait de toucher aux codes FPGA, mais cela implique de
recoder les drivers et la couche applicative. Je n'ai pas de très bonnes
connaissances en programmation Kernel donc perso, je serai inutile sur une
partie des codes et les codes existants en FPGA ne semblent pas mauvais donc
je ne vois aucune raison d'en arriver là.  
  
La dernière alternative est l'idée d'un SoftCore. Pour ceux qui ne voient pas
de quoi je parle, un SoftCore, c'est un pseudo-processeur, programmé sur un
FPGA, qui permet d'accéder directement et plus facilement (pas forcément
rapidement, il est vrai) aux registres, entrées, et sorties de ce même FPGA.
Mais je n'ai malheureusement pas trouvé comment le faire sous Xilinx...
Quelqu'un peut-il m'aiguiller ou a-t-il une idée/solution à proposer?

### **Hyacinthe** - Jan 11, 2016 at 9:22 AM

![Hyacinthe LICCIONI, FPGA at
echopen](./../../zz_assets/images/avatars/1249124.png) Hyacinthe  tu nous fais
un petit update ?

### **Hyacinthe LICCIONI,** - Jan 11, 2016 at 10:08 AM

D'après les dev RP, le code C a été mis à jour il y a 1 mois, et donc il
devrait être rendu efficace... Je teste

### **Hyacinthe Lacenne** - Jan 11, 2016 at 12:07 PM

Nice;)



#  soft

Hyacinthe Lacenne posted this Apr 28, 2016 at 5:01 PM

un thread autour de l'app, native, semi-native ou web

### **Hyacinthe Lacenne** - Apr 28, 2016 at 5:13 PM

installé un ide collboratif sur cloud9  
  
pour y accéder  
  
<https://ide.c9.io/newben/echotest>  
  
toutes les utilités de python sont installés en natif sur le cloud : pip,
virtualenv...  
  
version python 2.7.6  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  ![Hyacinthe, Danseur
du ventre at echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  si
vous avez des habitudes sur d'autres versions, notamment les plus récentes,
dites-moi

  

**packages installés** 

  

libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libv4l-
dev

  

installation archi i386

  

opencv installé, version 3.0.0

  

scipy installé  
  
![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe
anyway ca serait pas mal de regarder codenvy, qui est bien plus fine grained,
notamment en terme de config, de clonage, et le juge de paix est le tarif des
différentes offres  
  
dès qu'on est ok sur  
\- les specs du phantom  
\- les IO des soumissions  
\- les KPI de validation des soumissions  
  
-&gt; API : j'ouvre un endpoint depuis l'app de mathieu  
-&gt; je script dans l'ide un update du learderboard

### **Hyacinthe Lacenne** - Apr 28, 2016 at 5:55 PM

Sweet ! Tu minvites dessus? Id: hyacinthe124  
  
Avec mon coloc on avait comparé les deux, c9 en termes de ux générale
l'emportait. Ensuite, on était sur une App rails "standard" donc le plan
gratuit était largement suffisant :)  
  
Pour tes 3 points, vla un peu de food for thoughts ci dessous :)  
  
\- Pour déjà travailler sur des images, il y a le dump
<https://github.com/hyacinthe124/murgen-dev-
kit/blob/master/software/examples/Readme.md> qui liste qques images brutes (en
sortie d'acquisition) - on avait échangé sur le format, il a été utilisé là :)
. On connaît les caractéristiques de l'image, et celles du fantôme, donc on
peut essayer de reconstruire des images avec différents algos :) le nom des
fichiers est le md5 de l'image brute. Peuvent ils être servis par le serveur
de Michel ? Y'a déjà les thumbs :)  
\- Les specs du fantôme: il y aura une image du fantôme avec une règle, comme
ça ça en donnera les specs de base.  
\- Output: oui, qu'attendre en output? Une image? Un temps de conversion? Une
notation par un médecin? Quel kpi ?  
  
Y'a déjà de quoi jouer un peu :)

### **hyacinthe,** - Apr 30, 2016 at 9:11 AM

![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/782178.png)
lacenne  tu as aussi codeanywhere :)

### **Hyacinthe Lacenne** - May 01, 2016 at 5:06 PM

Pour les fantomes utilisés dans les exemples cités, ca se passe sur
<https://github.com/hyacinthe124/murgen-dev-
kit/blob/master/software/examples/Readme.md>  -- rubrique "Specs des
fantomes". Ca peut etre l'occasion d'une part de tester des algos de scan
conversion et de traitement de l'image (reduction du bruit?) -- tout en
faisant de la segmentation.

### **Hyacinthe Lacenne** - May 03, 2016 at 7:27 PM

thks, il faut que je fasse un premier bench de scan conversion en python  
  
PS : j'ai manifestement des pbs avec mes notifs mobiles sur BC

### **Hyacinthe Lacenne** - May 09, 2016 at 10:18 AM

je t'y ai invité - je regarde le reste

### **Hyacinthe Lacenne** - May 13, 2016 at 9:14 PM

![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  le
cloud9 est installé avec 1 bench de scanconversion façon OpenCV/python  
![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  j'ai installé
octave. dis-moi si tu vois d'autres packages utiles  
  
next step, installer les utilités pour monitoring de perf  
  
fabriquer un script qui compare I/O de la soumission avec le bench.  
  
à cette fin , discussion des KPI qd vous voulez

### **Hyacinthe Lacenne** - Jun 22, 2016 at 9:58 AM

après discussion avec medicalem, on a le go de principe de leur DG pour prêt
de fantôme de calibration  + fantôme digestif  
  
mais ca va prendre un peu de temps : il reviennent vers nous fin juillet  
  
vous tiens au courant

### **Hyacinthe Lacenne** - Jul 01, 2016 at 9:42 AM

mise en place de l'infra tests sur VM et sans VM  
  
mise en place de tests unitaires pour l'activité principale  
  
mise en place sur l'UI d'une règle pour appréciation des distances
échographiques  
  
mise en place d'une interface de click pour mesure de distance entre deux
points, et mesure de la distance en temps réel

### **Hyacinthe Lacenne** - Jul 09, 2016 at 1:01 AM

[1 ptit écusson sur la page github]  
  
![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  on franchit un
cap qualité sur l'app -&gt; elle vient de passer sous CI ;)  
  
Github n'intègre malheureusement pas Jenkins donc j'ai utilisé Travis, 1 rmq :
usage plus simple pour les tâches habituelles mais twistés pour les besoins
customs (genre ndk &amp; such)  
  
en tout cas le build passe et on a notre petite écusson sur la page github ;)  
  
<https://github.com/echopen/android-app>  
  
je ferai l'update sur le wiki pour les règles de soumission qui désormais
devront passer le build  
  
dès que j'ai une fenêtre de tir je m'occupe de la couverture de code - j'ai
rédigé pas mal de tests mais on doit être à peine à 10 % -  
-&gt; d'une part ca complétera les labels et bon signal qualité pour les contributeurs à venir  
-&gt; par ailleurs, ca donne une métrique pour un challenge -&gt; genre passer notre code coverage à 99% ! 1 #hackathon de rentrée ? ;)

### **Hyacinthe Lacenne** - Jul 16, 2016 at 11:54 PM

après discussion avec  ![Hyacinthe,
echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe   cet am, lundi
on va proposer une architecture pour un site lisible, qu'à base de gitbooks. c
une propale hein ;) qui aura pour mérite de  l'architecture et de la
synchronisation de la base de connaissance avec github  
  
une conséquence pratique sera de mener une refonte de l'orga des  repo.  
  
btw,  ![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png)
Hyacinthe  en collatéral de l'holacratie, ce serait pas mal d'adopter un  
[Contributor Covenant](http://contributor-
covenant.org/version/1/4/code_of_conduct.md), dont rails est adopteur

### **Hyacinthe Lacenne** - Jul 17, 2016 at 10:06 AM

Intéressant.  
On met ça plutôt dans le thread docu ou orga du coup? A réfléchir avec le
moyen de ne rien perdre du wiki, ça serait dommage de perdre des productions
:-)  
  
Pour l'holacratie, ça vaudra le coup d'y revenir avec la réflexion sur le mode
d'orga. Nope?

### **Hyacinthe Lacenne** - Jul 18, 2016 at 10:15 AM

il n'y a pas de tels threads dédiés, orga, suis pas sur que ca soit pertinent
pour tous les participants à ce basecamp et il y a déjà un thread "génération
de doc" qu'il faudrait donc factoriser

### **Hyacinthe,** - Jul 18, 2016 at 12:38 PM

Il faudrait discuter de l'architecture du site avec un "pro" du domaine.  
  
Comme je t'ai la semaine dernière  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/782178.png) lacenne  , j'ai un
contributeur pour monter un site web. Ce fut son boulot à une époque.

### **Hyacinthe Lacenne** - Jul 18, 2016 at 12:39 PM

Top ca! Tu nous fais un topo de ce contributeur ce soir?

### **Hyacinthe,** - Jul 18, 2016 at 1:19 PM

je ne suis pas là ce soir. Pour info c'est mon nouveau/futur coloc, on peut
voir un aperçu de son travail sur son site :  
  
<http://www.julien-vignolles.com/>

### **Hyacinthe Lacenne** - Jul 18, 2016 at 1:22 PM

Pas mal - un dev RoR en somme. Moins orienté architecture de contenu though.  
  
Quid sinon de la propal soulevée un peu avant, à savoir évoluer vers un site
statique sous framework Jekyll par exemple (qui tourne sous RoR) ?

### **Hyacinthe Lacenne** - Jul 18, 2016 at 1:37 PM

hello, merci  ![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  simplement il
avait l'air chaud pour faire du test sur android. IL connait java. C un plus
stimulant pour un bon dev que du faire du rails. Btw, tout est en place pour
l'écriture de tests config : templating de base, base de helper, structure de
mocking  
  
Du coup, pour un site statique, on peut mettre david sur le coup. Il faut voir
si un générateur est le mieux, on en discute ce soir ;)

### **Hyacinthe,** - Jul 18, 2016 at 1:43 PM

Il est chaud pour les deux. Et il à des trucs pour rendre un site plus
"vendeur". A voir. J'en reparlerai avec lui

### **Hyacinthe Lacenne** - Jul 18, 2016 at 1:46 PM

Que demande le peuple !

### **Hyacinthe Lacenne** - Aug 13, 2016 at 2:31 PM

![David Isnard, Dev php js html css symfony2 nodejs  at
echopen](./../../zz_assets/images/avatars/4693510.png) David  a terminé le
travail entamé il y a quelques mois par Mathieu Régnier

interface node de récupération de données depuis la sonde dans l’aquarium

-&gt; création d’un compte utilisateur 

-&gt; formulaire de requête de la data selon les paramètres configuration usuelle (, nombre d’images, nombre de lignes...)  

-&gt; pour le moment émulateur de data via un serveur TCP 

@todo  
\- review pul- request de david  
\- qqs corrections à apporter au code pour les data volumineuses  
\- adaptation du code de la redpitaya : pour l’agenda cf. tableau de
![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  (salle echOpen)

### **Hyacinthe Lacenne** - Aug 20, 2016 at 2:38 PM

un dev d'Inde, pryiank tiwari rejoint la dev team de l'app;)  
  
premier milestone -&gt;  travail de l'UI -&gt; choix des preset par appareil à
explorer (digestif, pulmonaire), via un carousel à scroll horizontal

### **Hyacinthe Lacenne** - Sep 06, 2016 at 4:27 PM

après rencontre du directeur pédagogique d'HETIC? une école de dev  
  
Go pour une semaine de sprints avec tous les étudiants de 2ème année autour
d'échOpen  
  
Objectifs : design + UX + Inté  
Date :  3ème semaine de novembre  
  
-&gt; rencontre le 05.10 avec le resp du cours

### **Hyacinthe Lacenne** - Oct 05, 2016 at 9:22 PM

AYÉ,  
  
on a le go d'école d'HETIC sur 2 projets )  
  
1)  
UX + UI : sprint d'une semaine consacrée à echOpen aura lieu du 17 novembre au
25 novembre  
  
#input : les idées de mock-ups issus du design camp de l'an dernier  
#output : les PSD ou Sketch des 3 screens/activités de l'app  
  
nbre d'étudiants mobilisés : 25  
  
les enjeux de usability pour l'opérateur ont bien été saisis et sont jugées
stimulantes  
  
2) Première semaine de juillet : 120 élèves planchent sur UX+UI+intégration
android/ios !  
  
nice



#  cleaning tout repos

Hyacinthe Lacenne posted this Jan 18, 2016 at 5:15 PM

hello,  
  
notre github mérite un coup de cleaning. J'ai supprimé le repo vide soft  
  
que fait-on du repo hard &amp; such  ? je vais demander à Yannick pour
image builder  
  
@++

### **hyacinthe,** - Jan 18, 2016 at 5:24 PM

Le repo hard peut contenir les pièces de Hyacinthe i guess - et les plans
électronique de la sonde ? lus tard les plans 3d de l'enveloppe et les schémas
d'assemblage ?  
  
A minima 2 sous repo: quelle profondeur d'arborescence pour chaque ?

### **hyacinthe,** - Jan 20, 2016 at 8:24 PM

A y est, ya les gerbers de la carte analogique pour BBB sur github, dans
hardware / electronics  
Documentation en route  
Partageable avec les électroniciens intéressés  
:)  
  
Bref, la source électronique du fork est disponible et utilisable!



#  clinique

Hyacinthe Lacenne posted this Jul 07, 2016 at 5:10 PM

un thread sur la dimension clinique du projet : usages médicaux, formation,
essai clinique...

### **Hyacinthe Lacenne** - Jul 07, 2016 at 5:14 PM

#**Pasteur**

  

Rencontre le 30.06.16 avec Fabien Taieb, responsable de la recherche clinique
internationale chez Pasteur. L’idée est d’implémenter des essais cliniques
pour tester l’échostéthoscopie en contexte sous-médicalisé.

  

On a travaillé avec Hyacinthe et Fabien à la définition des uses cases. Point
intéressant, on devrait s’orienter non vers de l'infectieux vers du dépistage
de tumeurs du foie, avec ses diagnostics différentiels abcès amibiens, kystes
hydatiques… Ceci percole avec le fait d’ensemble que l’Afrique n’est plus
simplement le terrain d’évaluation/expérimentation des maladies infectieuses,
mais aussi de nouveaux champs de santé publique, notamment la médecine de
prévention (avec des maladies de pays riches : diabète…)  
  
Prochain rdv : présentation à leur comité de recherche pour mi-septembre. Même
si ce ne sera pas la vocation première de cette réunion, seront aussi présents
des tech, qui pourraient venir en renfort

### **Hyacinthe Lacenne** - Jul 07, 2016 at 5:18 PM

#**Obs e-santé**

**  
**  

Ce lundi, c’était le lancement de l’Observatoire eSanté des pays du Sud dont
je suis membre. On a primé 9 projets afrique+asie, dotés de 10.000 euros
chacun.

  

Voici le site où certains de ces projets sont présentés. Certains sont over
top, notamment OPISMS et doctor gratis.

  

Par ailleurs, de nombreux contacts intéressants :

\- dir Innovation OMS : qui déploie des systèmes de bases de connaissance
partagées dans des environnements complexes et multi-nationaux, intéressé par
une collaboration

  
\- doctor gratis, solution de chat pour orienter les patients, présents
maintenant dans plusieurs pays d’Asie du sud-est, et qui ont une base de
données très conséquente et qui seraient  partants pour implémenter des
solutions d’upload d’imagerie à des fins d’orientation diagnostique

  
\- Forum Sud Santé : travail au déploiement de solutions echo-scopie dans les
déserts médicaux, utilisent le VSCA mais coûte cher donc ...  
  
je fais le follow-up et vous tiens au courant

### **Nassim Chadli,** - Jul 07, 2016 at 5:29 PM

#Pasteur

  
Je crois aussi qu'on devrais pas négligé "Les urgences" médicale et la
"Gynécologie" là où le diagnostique devient de plus en plus radioclinique. Et
en plus, on peut corrélé les résultats avec l'exploration chirurgicale dans
les suites de la prise en charge. Je pense à titre d'example à un cas
d'appendicite, certains médecins préfèrent avoir une image echographique avant
d'orienter vers un chirurgien. On pourra utilisé l'Echopen, l'Echographie
classique, et voir le compte rendu du chirurgien et la pièce anapath et ainsi
croiser les données.

### **Hyacinthe Lacenne** - Jul 08, 2016 at 7:56 AM

bien sûr les urgences et toutes les autres spé sont critiques. Voici
d'ailleurs le mindmap qui liste les domaines d'intervention validés par les
experts (@hyacinthe : la document de travail de référence de Juan concerne la
france ou d'autres pays ?) -&gt; <https://mm.tt/715079083?t=5K4akU2L74>  
  
le cas de l'appendicite est plus difficile, comme tu le sais il y a de grande
variation anatomique qui ne facilite pas le diagnostic même avec des
échographes usuels. En revanche, croiser les résultats d'echOpen avec ceux de
la chir est très intéressant et c ce que nous comptons faire notamment à des
fins d'intelligence artificielle !

### **Hyacinthe** - Jul 08, 2016 at 11:17 AM

Je crois que ce document est générique et qu'il sera sans nul doute à adapter
par type de pays, en fonction des pathologies les plus répandues.

### **Emilie Mayer,** - Sep 12, 2016 at 10:18 PM

<https://www.mindmeister.com/fr/715079083?t=5K4akU2L74>  
  
  
Quid de la dissection aortique? possible ou non?

### **Hyacinthe Lacenne** - Sep 14, 2016 at 3:41 PM

oui c un bon use case, simplement une dissection aortique minime peut se
révéler de diagnostic difficile. en revanche, les anévrysmes rentrent
clairement dans le scope  
  
en tout cas, il y a un champ entier de l'évaluation diagnostic qui devra être
déployé, tout plein d'essais cliniques à venir ;)

### **Hyacinthe Lacenne** - Oct 05, 2016 at 9:16 PM

rdv le 12.10.16 avec l'Institut Pasteur pour définir les contours pratiques de
l'essai cliniques autour de l'écho-stéthoscopie.  
  
Les pathologies pressenties sont celles du foies : cancers, abcès, amoeboses,
kystes hydatiques...  
  
rdv avec le directeur de la recherche internationale et sa team +
infectiologues, notamment chef de service Bichat, etc...  
  
on the road

### **Emilie Mayer,** - Oct 16, 2016 at 8:12 PM

Comment ça s'est passé? Y a t-il un CR?

### **Hyacinthe Lacenne** - Oct 18, 2016 at 7:39 PM

hello Emilie,  
  
sorry pour le délai de ma réponse, j'ai un gros sujet avec notifs que je ne
reçois qu'aléatoirement.  
  
Ca s'est super bien passé à 1 point tel qu'on a 3 essais cliniques dans le
pipe  
  
\- pathologies de la thyroÏde : RDC  
\- pathologies du foie : Côte d'Ivoire et Laos  
  
Le premier de nos essais sera de toutes les façons fait avec la fondation
fabre, qui souhaite avoir la primauté  
  
Ca t'intéresse que je te mette dans la boucle ? C super intéressant pour ta
formation : médecine + protocole de recherche clinique + médecine tropicales.
Ca peut même le faire sur une mobilité ;) !!

### **Nassim Chadli,** - Oct 18, 2016 at 7:41 PM

Salutations, Très bien ! Super excited *_*

### **Emilie Mayer,** - Oct 21, 2016 at 7:11 PM

OUi à fond !:)

### **Hyacinthe Lacenne** - Nov 10, 2016 at 7:41 PM

Meeting prévu le 17.11.16 avec Eric Deharo de l’IRD avec  ![Emilie Mayer,
Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie

  

-&gt; discussion du protocole d’un essai clinique au Laos autour des pathologies du foie



#  point dev

Hyacinthe Lacenne posted this Jan 27, 2016 at 9:47 AM

hello,  
  
juste un update sur le dev  
  
les deux juniors de l'epitech travaillent aujourd'hui à une implémentation
native de scanconversion à partir d'OPenCV, une façon de les faire rentrer
dans le projet et de continuer l'optimisation de la perf. Greg et moi
accompagnons  
  
Greg est en train de tester l'alternative UDP/TCP car il constate pas mal de
pertes de paquets en UDP. ON vous tient au jus ;)



#  Organisation Release 24 Mars Archived

Hyacinthe Lacenne posted this Feb 11, 2016 at 9:48 AM · 3 people applauded

Le 24 mars prochain, nous présenterons le premier prototype echopen V1
fonctionnel. Je vous invite à ce que nous discutions de cet event sur ce fil
de discussion.  
  
  
hello, pour le 10 mars l'hôtel dieu nous mets à disposition l'amphi Lapersonne
qui a une capacité d'accueil d'une centaine de personnes  
![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  je
te le montre tout à l'heure s'il est ouvert  
  
@++

### **hyacinthe,** - Feb 11, 2016 at 12:22 PM

Lolz on peut clapper plein de fois :)

### **Hyacinthe** - Feb 16, 2016 at 9:47 AM

Bonjour à tous,  
  
Voici un
[document](https://docs.google.com/document/d/1a0zdl_S_7NqN_43ucPCCLC85oOnPcukcj5HtsbgfaTc/edit#)
pour l'organisation de la soirée du 10 mars prochain.  
  
=&gt;DeadLine pour vos remarque : A LA FIN DE LA SEMAINE (le 19.02.2016) pour
valider les grandes lignes lundi prochain.

### **Emilie Mayer,** - Feb 16, 2016 at 10:24 AM

* On pourrait faire une petite explication de comment fonctionne l'échographie

### **hyacinthe,** - Feb 16, 2016 at 9:06 PM

Au dernier captech,  yen avait une, à recycler?

### **Hyacinthe** - Feb 28, 2016 at 8:12 AM

Hello,  
  
Le 10 mars approche... On va lancer les invitations des demain et mardi.  
  
1\. Invitations par email nominatives pour les "VIP" =&gt; lundi. Il s'agit
des personnes qui se sont impliqués le plus dans le projet et de ceux qui
pourraient avoir un rôle important dans les prochaines étapes.  
  
2\. Lien Eventbrite à diffuser par emailing à la communauté + event Facebook
=&gt; Mardi, avec un nombre de places limitées en fonction des "VIP". Nous
pourrons toujours changer le nombre sur l'invitation éventbrite.  
  
D'expérience, 10 jours avant est un bon timing...  
  
Ensuite, dans la semaine qui vient, nous affinerons le déroulé et organiserons
la logistique (traiteur, etc.)  
  
Bon dimanche  
  
À demain

### **Hyacinthe** - Mar 15, 2016 at 8:19 AM

Bonjour à tous,  
  
Afin d'inviter les gens à la soirée de présentation de la sonde echopen, voici
l'image réalisée par Barabara que vous pouvez utiliser et diffuser.  
  
Merci d'ajouter les personnes invité dans la liste du le
[Gdoc](https://docs.google.com/document/d/1a0zdl_S_7NqN_43ucPCCLC85oOnPcukcj5HtsbgfaTc/edit#)  
  
Le lien pour l'eventibrite : <https://www.eventbrite.fr/e/billets-echopen-est-
de-sortie-23049885829>  
  
Enfin, il y a aussi un évènement Facebook.  
  
@+  
  

[

![](bc3-raw/files/2553919
-invitation-echopen-24-mars-2016.jpg)

](bc3-raw/files/2553919
-invitation-echopen-24-mars-2016.jpg)

[ Invitation Echopen 24 Mars 2016.jpg  448 KB • Download
](bc3-raw/files/2553919
-invitation-echopen-24-mars-2016.jpg)

### **hyacinthe,** - Mar 15, 2016 at 12:17 PM

Btw, toutes les images utilisables sont sur le drive?

### **Hyacinthe** - Mar 15, 2016 at 12:22 PM

Pour le moment nous n'avons que celle ci mais les autres devraient arriver
d'ici la fin de la semaine... Je les ajouterai sur le drive dès réception

### **Hyacinthe** - Mar 23, 2016 at 11:01 AM

Hello all,  
  
Je suis en train de réaliser une présentation pour demain soir afin d'avoir un
support visuel des différentes interventions.  
  
L'idéal serait que tout le monde participe ;) et puisse dire un petit mot sur
ce qu'il a fait en 3 minutes...  
  
Le déroulé (pour le moment) devrait ressembler à quelque chose du genre :

  1. Mot d'acceuil - 2-3"
  2. Présentation d'echopen (Hyacinthe) - 10"
  3. Partenaires (APHP / Fondation Hyacinthe Fabre) - 15"
  4. Concept d'echostéthoscopie (Hyacinthe B.) - 10-15"
  5. Les grandes réalisations (**VOUS TOUS** ;)) - 30-35"
    1. Emilie / Muriel : Archi &amp; doc
    2. Hyacinthe : Transducteur (éventuellement avec Gérard et Hyacinthe Loyau qui devraient être présents)
    3. Hyacinthe V. : Mécaniques 
    4. Hyacinthe / Hyacinthe Li. : éléctonique 
    5. Hyacinthe : Assemblage &amp; such
    6. Hyacinthe : App
    7. Mathieu : Interface
    8. Hyacinthe : Murgen
  6. Démonstration du dispositif =&gt; Tous ceux qui seront nécéssaires pour faire fonctionner la sonde - le temps qu'il faudra ;)
  7. Q&amp;A avec la salle - 10 à 15"
  8. Buffet. 

  
Pour vos présentations (citées ci-dessus), j'ai préparé une slide (titre +
image-s) que je vous enverrai ce soir et que je finaliserai demain dans la
journée. Si vous souhaitez ajouter des détails, n'hésitez pas à m'envoyer vos
contenu que je les intègre dans la présentation. Il s'agit en qq minutes de
présenter ce que vous avez réalisé de manière simple et en s'adressant à un
public non-expert.  
  
J'ai déjà reçu celle de Hyacinthe pour Murgen.  
  
A dispo

### **Hyacinthe Lacenne** - Mar 23, 2016 at 11:07 AM

de mon côté prévois plutôt 5mn !

### **Hyacinthe** - Mar 23, 2016 at 6:34 PM

Bonsoir à tous,  
  
Voilà donc le draft de présentation avec l'ajout des éléments de Hyacinthe &amp;
Hyacinthe. Il me manque encore des images, qui veindront demain, ainsi qu'une
relecture  
  
Si vous avez des remarques, merci de vos retours. Les slides sont
volontairement peu fournies pour laisser à chacun une part de liberté dans ses
explications.  
  

[

![](./../../zz_assets/images/previews/2875588-echopen_presentation_24_mars_2016.png)

](bc3-raw/files/2875588-echopen_presentation_24_mars_2016.pdf)

[ echopen_presentation_24_mars_2016.pdf  11.2 MB • Download
](bc3-raw/files/2875588-echopen_presentation_24_mars_2016.pdf)

### **hyacinthe,** - Mar 23, 2016 at 8:17 PM

Top!  
Pour l'organisation de demain, j'ai pu échanger vendredi contre jeudi, donc
faites signe so ya besoin!

### **Hyacinthe VINCENT,** - Mar 23, 2016 at 9:48 PM

Beau boulot !  
Qq petits pb dans la partie méca :

  1. un copier/coller intempestif p18 et p19 : retourne prendre les textes dans l'original
  2. une faute p18 à "nouvelle**s** possibilités"
  3. toutes mes photos sont très floues sur le PDF. Je ne sais pas ce que tu utilises comme outil de présentation mais essaye peut-être de réexporter les slides du drive dans un autre format, les importer dans ton outil et déplace les photos de mes slides importés vers tes slides. Comme ça elles devraient rester dans leur résolution maxi. Sinon, je peux te donner demain matin les originaux mais il faudra refaire qq recadrage. Tiens moi au courant.

### **Hyacinthe** - Mar 24, 2016 at 7:28 AM

Merci  ![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe , bien vue...
Désolé pour ces boeugs. C'est corrigé.  
En effet les photos sont un peu floues. Si tu m'envoies les originaux, je peux
les intégrer dans la journée, j'ai des masques d'images sur les slides, ça
devrait donc ne pas poser de soucis. J'ai exporté en pptx et intégré les
éléments sur keynote.

### **Emilie Mayer,** - Jun 02, 2016 at 9:54 AM

<http://www.fondationhyacinthefabre.org/fr/suivre-notre-action/echopen-lancement-
du-premier-prototype-dechostethoscope-open-source-low-cost>  
la fondation fabre parle du release.



#  RH

Hyacinthe Lacenne posted this Apr 06, 2016 at 7:50 AM

ceci est un fil de discussion sur la RH

### **Hyacinthe Lacenne** - Apr 06, 2016 at 7:55 AM

Nicolas Le Roux, que g connu au cab de lemaire, est chez Simplon et me propose
des profils dev pour le club jade. Du  coup, je dérive la propale pour echOpen
et je vias voir si on peut inclure des étudiants dans le cadre de leurs
projets pédagogiques  
  
Pour mémoire, Simplon est une sorte de 42 en plus court - qqs mois de
formation - et ils ont été désignés pour coordonner le projet gde école
numérique, ce qui est une bonne opportunité de structurer qqch avec eux  
  
  
voici des profils  
  
[https://docs.google.com/presentation/d/1VCid8Jvh_mbWimkszOkhK42IcLPpOIJgyKMMnywu2Cc/pub?start=false&amp;loop=false&amp;delayms=60000&amp;slide=id.g1226c24550_0_142](https://docs.google.com/presentation/d/1VCid8Jvh_mbWimkszOkhK42IcLPpOIJgyKMMnywu2Cc/pub?start=false&loop=false&delayms=60000&slide=id.g1226c24550_0_142)  
  
je vous tiens au courant  
  
oilà

### **Hyacinthe Lacenne** - Apr 06, 2016 at 6:07 PM

un étudiant de l'ISEP, 3èmeA #FPGA cherche un stage à compter de juillet  
  
rdv lundi 17H30  

[

![](./../../zz_assets/images/previews/3383116-cv-stage.png)

](bc3-raw/files/3383116
-cv-stage.pdf)

[ CV stage.pdf  413 KB • Download
](bc3-raw/files/3383116
-cv-stage.pdf)

### **Hyacinthe,** - Apr 07, 2016 at 9:36 AM

Je note quand même qu'il a mis comme compétence internet...  
  
Vu ton intitulé Hyacinthe, il suis une spécialité FPGA àl'ISEP? Quelle durée de
stage?

### **Hyacinthe KHOYRATEE,** - Apr 07, 2016 at 9:57 AM

C'est quoi le sujet du stage en question?

### **Hyacinthe** - Apr 07, 2016 at 10:06 AM

L'idée est de trouver des ressources circulantes qui viendraient compléter
l'équipe et avancer au côté de la communauté ;)

### **Hyacinthe Lacenne** - Apr 07, 2016 at 10:11 AM

![Hyacinthe KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe   tu as un moment
pour un call pour qu'on te debriefe sur les choix du captech  ?

### **Hyacinthe KHOYRATEE,** - Apr 07, 2016 at 10:14 AM

![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  Je
comprends bien l'idée (et ce serait effectivement génial), mais j'imagine
(peut être que je me trompes) que s'il faut prendre un stagiaire, ce dernier
doit valider auprès de son administration un sujet précis et en accord avec sa
spécialité (je parles en connaissance de cause, notre administration est bien
chiante :p). Et même pour le stagiaire en question savoir vers ou il part
serait une bonne chose. Après je suppose que ça a été décidé lors du Captech!  
  
![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/782178.png)
lacenne  Bien sur, je bosses toutes la journée mais rien ne m'empêche de
m'absenter quelques temps! :)

### **Hyacinthe** - Apr 07, 2016 at 10:29 AM

Merci  ![Hyacinthe KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe  pour ton retour.
Le responsable de l'Isep était au CAPTech et c'est lui qui a circonscrit la
thématique et proposé la dynamique ;)

### **Hyacinthe KHOYRATEE,** - Apr 07, 2016 at 10:39 AM

![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe
Super! :D je vois que tout est prévu ;)

### **Hyacinthe Lacenne** - Apr 07, 2016 at 3:49 PM

![Hyacinthe KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe  un peu
d'exercice de dérouillage mathématique en vue de cet été  
  
pour tout entier n, on note In, le nombre d'entier p tel que  
  
50^{n} &lt; 7^{p} &lt; 50^{n+1} // sorry, je n'ai pas latex, mais il s'agit de
symboles de puissance  
  
1) prouver que pour tout n entier, In = 2 ou 3  
  
2) prouver qu'il existe une infinité d'entiers n tels que In=3  
  
oilà

### **Hyacinthe Lacenne** - Apr 11, 2016 at 1:01 PM

![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  attention, si
tu likes, c que tu en redemandes !!!  
  
donc voilà :  
  
trouver les triplets d'entiers (a,b,c) tels que ab-c,bc-a,ca-b sont chacun une
puissance de 2 !

### **Hyacinthe Lacenne** - Apr 25, 2016 at 7:10 AM

Hyacinthe Grandhomme (enseignant à l'épitech) passe le 4 mai. Au menu,
préparation du recrutement d'étudiant de l'épitech pour leur stage d'été.  
  
au passage, Hyacinthe a envie de développer nos algo sur GPU, à partir d'une
librairie cross-platform qu'il connaît bien

### **Hyacinthe Lacenne** - May 11, 2016 at 7:51 AM

frédérci amiel, prof à l'ISEP qui était avec nous au dernier captech, me fait
savoir qu'il s'est mis à la recherche d'étudiants  orientés FPGA

### **Hyacinthe Lacenne** - May 11, 2016 at 9:15 AM

rencontre avec Soobash, astrophysicien, spécialisé dans le traitement d'image,
notamment les images très bruitées. Il attend des images de notre part et est
chaud pour y travailler asap ;)

### **Hyacinthe Lacenne** - May 17, 2016 at 9:43 AM

orga réu mercredi 25.05 avec Soobash et Zahra (étudiante ISEP) pour
coordination du pipe traitement d'images  
  
  
odj proposé par Soobash :  
  
1/ Algorithms a utiliser.

2/ Environment de development.

3/ Consideration de systeme embarque.

4/ Les deadlines en temps du project a respecter.

### **Emilie Mayer,** - May 18, 2016 at 8:48 PM

Bonsoir  ![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png)
Hyacinthe  ,  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/782178.png) lacenne  ![hyacinthe,
hardware thinker at echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe
, et tout le monde ;)  
  
Voici le CV d'une de mes amies : Zhor, qui est entre son M1 et M2 du master
MONABIPHOT de l'ENS Cachan.  
Elle cherche un stage cet été idéalement à partir du 4 juillet et jusqu'à fin
août et même 1er septembre, ça fait longtemps que je lui ai parlé d'Echopen et
ça lui plairait bien de rejoindre le projet dans le cadre de son stage.  
Elle a notamment eu des cours sur les matériaux et le traitement du signal qui
pourraient être utiles ....  
Voilà son mail : [zhor.khadir@gmail.com](mailto:zhor.khadir@gmail.com)  
Elle est en Erasmus à Madrid en ce moment mais peut vous skyper, envoyer une
lettre de recommandation, et/ou de motivation ...  
  

[

![](./../../zz_assets/images/previews/5175574-cv-zhor-khadir-2016.png)

](bc3-raw/files/5175574
-cv-zhor-khadir-2016.pdf)

[ cv-zhor-khadir-2016.pdf  139 KB • Download
](bc3-raw/files/5175574
-cv-zhor-khadir-2016.pdf)

### **Hyacinthe Lacenne** - May 18, 2016 at 9:23 PM

hello, bien sûr on peut prévoir un skype ;) btw, il s'agit d'un stage payé ?  
  
@++

### **Emilie Mayer,** - May 18, 2016 at 9:36 PM

Yes

### **Hyacinthe Lacenne** - Oct 11, 2016 at 3:53 PM

hello des news sur la RH !!  
  
3 ingénieurs de M1 de l'Université Libre de Bruxelles vont consacrer leur
projet de master à echOpen, sous la direction d'Hyacinthe Debeir.  
Kick-Off : visite du lab le 27.10.16 &amp; start ;) orientation dev +
électronique  
  
deux étudiants de P6, Adrien Rohfritsh et Anais Drihem, vont développer
echOpen/kit dans le cadre de leur master  
  
on reçoit à compter de cette semaine pour 3 semaines Thomas Robillard, un dev
de l'épitech : orientation UI + design, avec une solide expérience.  
  
on reçoit un aggrégatif de l'ENS, Romain Agaisse, une fois par semaine qui
développe un kit version pédagogique dans le cadre de son oral d'agreg. Btw,
selon Thomas Rodet, c un des meilleurs de sa promo. ;)  
  
Btw, on shoote les modules echOpen au MIT d'ici la fin du mois

### **Hyacinthe Lacenne** - Oct 27, 2016 at 11:55 PM

#brightday  
  
nous avons accueilli aujourd'hui 3 ingé de l'ULB et leurs prof Hyacinthe Debeir.
journée pleine d'enthousiasme et de bonnes énergies  
  
Hyacinthe était impressionné et ravi par la qualité des images que l'on obtient
- et nous aussi : doigts, paume, avant-bras ;)  
  
ils travaillent sur echOpen jusqu'en mars 2017.  
  
l'idée d'Hyacinthe est d'instancier echOpen à l'ULB, de façon autonome  
  
embryon d'internationalisation  
  
![Nassim Chadli, Instanciator at
echopen](./../../zz_assets/images/avatars/4069013.png) Nassim  : on vous
attend aussi ;) n'hésitez pas à nous solliciter !  
  
@++

### **Emilie Mayer,** - Nov 07, 2016 at 7:30 PM

CV d'un étudiant des Mines de deuxième année, intéréssé pour faire son [stage
"ingenieur"](http://www.mines-paristech.fr/Formation/Cycle-ingenieurs-
civils/Cursus/Stages/) chez echopen sur la période estivale (12 à 16
semaines). Je ne l'ai jamais rencontré mais son CV est impressionnant, +
dimension internationale + Wiki +TedX +robotique + java + intéréssé par la
santé (c'est dans son mail ) !  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/782178.png) lacenne

[

![](./../../zz_assets/images/previews/18112132-cv_mahdi_mohamed.png)

](bc3-raw/files/18112132-cv_mahdi_mohamed.pdf)

[ CV_Mahdi_Mohamed.pdf  341 KB • Download
](bc3-raw/files/18112132-cv_mahdi_mohamed.pdf)

### **Nassim Chadli,** - Nov 07, 2016 at 7:32 PM

Oui C notre ingénieur chargé de nous mettre en place le côté Lab ici à Annaba
(Algérie)

### **Nassim Chadli,** - Nov 07, 2016 at 7:33 PM

Ah non ! Waw C son double alors. Notre ingénieur (Hyacinthe Dib) à presque le même
parcours et le meme prénom !!

### **Hyacinthe Lacenne** - Nov 08, 2016 at 12:53 AM

excellent ;)  ![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  je nous met en
contact avec lui demain et vous tiens au courant  
  
@bientôt



#  Cartes mère, cartes filles

Hyacinthe posted this Apr 13, 2016 at 2:28 PM · 1 person applauded

Yop,  
  
je viens de vérifier un truc, une carte classique (comme celles que nous
possèdons à l'atelier) possède 39 pistes. Donc si on coupe au milieu (piste
20) ça nous fait des cartes mères et des cartes filles de 19 pistes, ce qui
devrait suffire pour chaque solutions. Il faudrait donc établir une fiche
module claire de chaques signaux alim ou logique (dans tel solution c'est tel
signal logique et dans tel autre, c'est tel signal logique...) de la carte
mère.  
  
Ensuite pour les cartes filles, 3 possibilités qu'on pourrait laisser au choix
de celui qui fait son module :  
\- full barrette de chaque côté de la carte. Le plus stable mécaniquement mais
gourmand en connectique et oblige à couper les pistes non utiles  
\- full barrette d'un seul côté. Moins stable mécaniquement mais plus
économique, on doit toujours couper les pistes non utiles  
\- 2 pins à chaque coins (possiblement des pistes non utilisées sur la carte
mère) plus uniquement 1 pin pour chaque signal utile. Solution la plus
économique en matériel et plus stable mécaniquement que la solution 2. Demande
un peu plus d'effort pour la soudure mais minimise les pistes à couper

### **hyacinthe,** - Apr 13, 2016 at 4:51 PM

Juste pour être sûr, on parlait des pistes à garder comme base commune pour
rendre des modules interoperable, il faudrait donc quand même figer les pistes
sur une carte mère version alpha? Si les pistes utilisées ne portent pas les
mêmes signaux, on sera compatibles entre modules intra ensembles, mais pas
inter-ensembles?  
  
Question posée car les premiers modules en CMS ne vont pas tarder à être
envoyés au Fab, et ce serait couillon qu'ils ne marchent pas sur la même carte
mère avec d'autres modules :)

### **Hyacinthe VINCENT,** - Apr 13, 2016 at 4:51 PM

Je plussois le coté pratique et économique de faire des 1/2 cartes mères, en
espérant juste que 19 pistes suffisent. Mais on peut tjs commencer comme ça,
on pourra toujours élargir la carte mère en cas de besoin impératif ou
segmenter une piste sur sa longueur ou ajouter une connexion externe ou ...  
Pour les solutions des barrettes, vous vous en doutez, je mettrais dans
l'ordre de préférence :  
\- La n°2 : plus simple, éco et surtout qui libère la dimension du module qui
peut alors s'adapter à son contenu. En ce qui concerne la réalisation les
modules, il pourront être réalisés en plaque à barrettes (donc plein de pistes
à couper partout, mais c'est inévitable) et plaque à pastilles (donc plein de
straps à rajouter, mais c'est inévitable) ou en PCB double face ou plus (donc
plein d'étude de conception CAO à faire, mais c'est inévitable). Pour la
stabilité mécanique, je pense que si dissocier la fonction de connexion
électrique de la fonction maintient mécanique simplifie et augmente la
souplesse de ces plaques d'expérimentation, il ne faut pas s'en priver. Je
pense que dans un premier temps un seul conecteur sera bien suffisant pour
faire des mesures sur la paillasse quitte à faire des petites agraffes en
plastique si vraiment ça se déconnecte tout le temps, sachant que dès qu'on
aura des configurations un peu stabilisées à tester sur le terrain on retirera
les connecteurs et on soudera directement les modules sur la carte mère.  
\- La n°3 : est intéressante aussi. Mais je ne suis pas sur de complètement
comprendre. Si je comprends bien, c'est 2 pins au deux coins supérieurs. On
pourrait figer les deux pistes des bords soit sur Gnd et +5v ou Gnd et Gnd (on
perd une piste) . Est-ce qu'on garde 3 ou 4 full barrettes femelles sur la
carte mère, et juste les pins males nécessaires sur les modules ? On résoud
l'instabilité mécanique par des agraffes plastiques qui peuvent aussi servir
de pied pour éviter les courts circuits entre les pistes en dessous et le plan
de travail ;-).  
\- La n°1 : bof, comme tu dis.  
  
Finalement c'est peut-être la n°3 qui me plait le plus ...

### **Hyacinthe VINCENT,** - Apr 13, 2016 at 4:55 PM

![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  on pourrait voir à
quoi ça ressemble avant d'envoyer en fab ? Sinon si tu as déjà un jeu de
pistes d'interface qui est suffisant pour tes modules c'est déjà une bonne
référence.

### **Hyacinthe VINCENT,** - Apr 13, 2016 at 5:11 PM

![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe ,  ![hyacinthe,
hardware thinker at echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe
, la remarque :  
  
"_dans tel solution c'est tel signal logique et dans tel autre, c'est tel
signal logique... _"  
... me rend aussi très perplexe ...  
  
Si on est pas capable d'avoir un design unique de carte mère (mécanique et
électrique), je crois qu'on a tout faux.  
J'ai effectivement proposé une alternative pour les deux signaux pwm de moteur
CC et les 4 signaux du stepper. Mais ce sont des signaux de sortie externes
qui squattent des pistes libres et des solutions qui sont exclusives. Par
ailleurs, j'espère qu'on ne va pas s'accrocher trop longtemps à la solution
moteur CC dès qu'on aura validé un minimum le moteur stepper.

### **Hyacinthe,** - Apr 14, 2016 at 10:09 AM

En ce qui concerne les 3 possibilités de cartes filles, pour_ _la troisième je
pensais à mettre 2 pins aux quatre coins, les solutions ressembles à ça :  

[

![](bc3-raw/files/3697306-cartemere_cartefille.jpg)

](bc3-raw/files/3697306-cartemere_cartefille.jpg)

[ cartemere_cartefille.jpg  252 KB • Download
](bc3-raw/files/3697306-cartemere_cartefille.jpg)

  
Aux quatre coins pour la stabilité mécanique. Après si on trouve des
entretoises qui vont biens ça serait cool. Pourquoi 2 pins? Pour s'assurer
qu'on soude les pins bien perpendiculairement à la plaque, avec une seule pin
on a de fortes chances de souder de travers et après on ne pourra pas plugger
les modules.  
  
En ce qui concerne la modularité des signaux logiques, par exemple la commande
moteur sera une PWM pour moteur CC, une PWM pour servo et je ne sais pas quoi
pour le moteur pas à pas. La commande logique est différente mais le signal à
la même fonction. Je pose ça à plat et je reviens vers vous.  
Mais bien vu Hyacinthe, on peut mettre les alims les plus utilisées et des masses
sur les pins de support.

### **Hyacinthe,** - Apr 14, 2016 at 10:11 AM

Les cartes filles sont encore montées à l'envers, mais c'est pour tester les
solutions rapidement.

### **Hyacinthe KHOYRATEE,** - Apr 14, 2016 at 10:21 AM

Pourquoi ne pas passer à la production de carte électronique pour réaliser vos
cartes mères et cartes filles plutôt que de rester sur les plaques de
prototypages?  
  
Deux solution :  
* Mettre en place un atelier pour création de carte électronique dans l'atelier (chimique reviendrait beaucoup moins cher avec)  
* Passer par un fournisseur (voir avec Hakim)  
  
Pour les logiciels de création de PCB un de mes ami m'a envoyé ce lien
récement qui est gratuit :  
<https://easyeda.com/fr>  
J'ai contacté le co-fondateur qui est très gentil, aide, conseil et
s'intéresse aux projets.  
  
Sinon les logiciels de cadence sont gratuits pour une durée limitée (ou si
besoin crack de altium designer que j'ai eu l'habitude d'utiliser et qui est
super)  
  
Ce que je veux dire c'est que une fois que le circuit fonctionne avec des fils
dégueux sur les cartes de prototypage la prod permet de faire quelque chose
avec des cartes aux dimensions précises avec le bon nombre de pins pareil aux
dimensions précises etc  
  
Qu'en pensez-vous?

### **Hyacinthe Lacenne** - Apr 14, 2016 at 10:23 AM

Yop,@hyacinthe : tu es sur du 15 pins sur tes photos, c'est voulu?  
  
Attaché, un petit excel avec les tables sur les pistes requises par nos
différentes approches, pour mémoire (et pour édition facile).  
  
On avait commencé à drafter la table des pistes, qui est sur :
<http://echopen.org/index.php?title=Modules_:_a_motherboard> pour référence.  
  
Cheers!  

[ ![](./../../zz_assets/images/file-types/xlsx.png) Pistes.xlsx  10.5 KB •
Download
](bc3-raw/files/3697900-pistes.xlsx)

### **Hyacinthe Lacenne** - Apr 14, 2016 at 10:27 AM

@hyacinthe: c'est une solution indeed =)  
  
Pour les cartes filles je bosse sur une solution imprimée, double layer, mais
il faut qu'on se mette d'abord d'accord sur les tracks de la carte mère.
Garder un pas de 2.54 semble etre pertinent vu l'ubiquité de ce parametre.
Partir dans l'immédiat sur une solution carte mere à bande permet aussi de
tester si cette solution est viable, ou pas

### **Hyacinthe,** - Apr 14, 2016 at 10:51 AM

Yep, c'est du 15 pins, on est resté sur la base de ce qu'on avait montré
Lundi. Ce n'est pas la peine de redécouper une plaque juste pour une démo.

### **Hyacinthe Lacenne** - Apr 14, 2016 at 12:09 PM

Noté.  
  
Nous avions convenu lors de la réunion de lundi de partir sur une liste de
pistes sur la base des différents besoins exprimés jusque là, et qu'il nous
fallait décider de l'ordre de ces pistes, ordre sans lequel nous n'aurons pas
l'intercompatibilité des modules -&gt;
<http://echopen.org/index.php?title=Modules_:_a_motherboard>, repris dans le
fichier excel envoyé.  
  
Je ne crois pas qu'il y ai eu de retour sur cette proposition d'organisation
de pistes - peut on valider cela avant d'avancer?

### **Hyacinthe VINCENT,** - Apr 14, 2016 at 12:45 PM

Quelques remarques :

  * ![Hyacinthe, Danseur du ventre at echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe ,  pour souder bien perpendiculairement n'importe quel connecteur il suffit de le plugger sur un autre connecteur d'une carte possèdant 2 rangées de pins et de mettre un autre connecteur monté à vide dans la carte : un mini montage de mise en place. Et là on fait ce qu'on veut, proprement.
  * ![Hyacinthe KHOYRATEE, Electronique at echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe ,  Ok pour produire des PCBs spécifiques pour les modules . Mais ça ne me semble pas nécessaire dans un premier temps pour la carte mère. Ce sera forcément plus cher et moins évolutif. Quel est l'intéret de faire fabriquer une carte à bande et de faire plein de trous dedans ? Il faut penser aussi au maker qui voudrait reproduire le kit, plus il y aura de composants dispo sur étagère mieux ce sera.
  * ![Hyacinthe, Danseur du ventre at echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe , sur l'exemple de soudure présenté avec uniquement les pins nécessaires si tu commences à spécialiser les connecteurs femelles de la carte mère on perd toute souplesse. Ok pour ne mettre que les pins males nécessaires sur le module mais gardons une barrette femelle complète sur la carte mère. Elle pourra accueillir n'importe quel module.
  * ![hyacinthe, hardware thinker at echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe , je modifierai bien le doc des pistes pour rejeter une masse et les alims sur les bords. De toute façon, maintenant le principe d'affectation en commençant au centre est moins important puisque tout est plein. Cela permettra de garder une stabilité mécanique relative des modules si on décide de n'y souder que les pins males nécessaires. Par ailleurs si on veut quand même aller à 24 pistes on pourra les ajouter à l'extérieur. Ce qui compte c'est qu'il y ait un bon écartement entre le gnd et le 5v (qu'on soudera sur tout module). Je propose une nouvelle version du fichier (en bougeant un peu tout pour essayer aussi de minimiser les risques de bruit).
  * Je réserverai bien un espace sans composant de 5mmx5mm sur les deux coins inférieurs des modules pour y souder une pin (beurk!) ou y pincer une agraffe plastique (hmmm!) afin d'assurer la stabilité mécanique.

  
A vous de jouer !

[ ![](./../../zz_assets/images/file-types/xlsx.png) Pistes v2.xlsx  12.7 KB •
Download
](bc3-raw/files/3701963-pistes-v2.xlsx)

### **Hyacinthe KHOYRATEE,** - Apr 14, 2016 at 1:28 PM

![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  
Pour le prix ça dépend vers quel option tu te dirige et encore vu que ce sont
de petites cartes avec peu de faces et pas forcement beaucoup de composants,  
Intérêt:  
*permettre d'optimiser en place (sur 2 couches en CMS face aux matrices à trous) et c'est pas négligeable de réduire la taille de la carte mère (en hauteur, en longueur et en largeur)  
*Amélioration des performances (ça évite les mauvaises brasures, les rayonnement électromagnétiques et autres magies obscures)  
*Gestion de la précision mécanique, tu n'est pas limité par la taille des pins, ni par l'espace entre les pins etc et tu peux même imaginer plusieurs autres alternatives aux pins :  
     - un sock type PCI ou tu viens pluguer ta carte fille  
     - un connecteur FMC (trop de pin je suppose) ou autre  
     - je connais pas masse de différents type de connecteurs mais on peux ainsi ne pas se limiter à cette façon de faire

### **Hyacinthe,** - Apr 14, 2016 at 1:29 PM

On avait dit pas de signal analogique sur la carte mère pour éviter les bruits
CEM, en considérant cela et une demie carte soit 19 piste ça pourrait donner
ça :  
  
<https://docs.google.com/spreadsheets/d/1T1XgczV0Mkprnae13ztAdN7gQ8O-
lpyFSobw33tiy-Q/edit#gid=0>  
  
PS:  pourquoi 4 signaux pour le pas à pas?

### **Hyacinthe Lacenne** - Apr 14, 2016 at 1:41 PM

Je croyais qu'on avait discuté ça lundi, et qu'on intégrait des pistes
analogiques. Dans tous les cas, il faudra déterminer des connections entre les
modules pour trimballer les signaux d'interface.  
Essayons de nous mettre d'accord une bonne fois pour toutes, pour avancer.  
  
Qques questions dans cette optique:  
\- si on simplifie les pistes, pourquoi inclure 12 et 18V (et les négatifs)
qui sont spécifiques à des choix technos? et qui occupent beaucoup d'espace -
alors qu'ils sont spécifiques à qques modules?  
  
\- Quid de l'alim, qu'on a zappé jusque la ?   Dans l'idéal, il faudrait un
module qui prenne une entrée classique que ca soit tout (imaginons la carte
mere dans un boitier, dans l'idéal il lui faut etre alimentée par un seul
cable.  
  
\- la rample TGC est un signal anologique.. a moins que la rampe soit encodée
sous un format logique.

### **Hyacinthe,** - Apr 14, 2016 at 1:49 PM

L'alim n'est pas zappé, c'est le 18V.  
  
Lors du workshop on avait dit que le seul signal analogique sur la carte mère
serait la ramp du TGC. Car même s'il y a un peu de bruit dessus ce n'est pas
génant.  
  
Lundi on n'a pas dit qu'on intégrait les signaux analogiques.  
  
Pour interconnecter des modules traitant l'analogique l'idéal c'est du coax.
Ensuite quelle connectique? Le truc bien c'est les connectiques SMA, mais
c'est cher... Ou on peut rester sur les même connectiques que pour carte mère
et carte fille.

### **Hyacinthe Lacenne** - Apr 14, 2016 at 2:16 PM

Pour le 18V, ca reste que c'est une piste qui est spécifique à une solution
technologique choisie, donc ca me dérange un peu. Itoo pour les +-12V. Ca
implique aussi qu'il faille alimenter la carte mere avec plusieurs niveaux de
tension, est ce bien le cas?  
  
J'avais compris le contraire pour les pistes sur la discussion de lundi, mais
@hyacinthe me détrompera si c'est le cas.  
  
Dans tous les cas, top ce gdoc, ca va permettre d'avancer et de consolider un
choix.

### **Hyacinthe,** - Apr 14, 2016 at 2:30 PM

Niveau analogique principalement, c'est le signal en sortie de T/R switch qui
doit être protégé donc pas sur la carte mère, car le moindre bruit CEM sera
amplifé par le TGC.  
  
Le but de la carte mère c'est qu'elle puisse acqueillir plusieurs solutions.
C'est pourquoi il y a tout ces signaux. Sinon si je vais dans ton sens
pourquoi on met un Tir off alors que ce signal ne sert qu'à ta solution?  
Et oui, il faut mettre les différentes alimentations à mon sens pour pouvoir
alimenter les composants des différentes solutions. Et les valeurs qu'on
retrouve souvent sont +- 12V, +-5V, +3.3V (le -3.3V n'a pas l'air très
conventionnel, c'est pour ça que je l'air retiré d'une solution).

### **Hyacinthe KHOYRATEE,** - Apr 14, 2016 at 2:34 PM

Je suis d'accords avec Hyacinthe autant tu peux être flexible sur certaines chose
mais l'alimentation se doit d'être fixé, si tu implémente un module "alim" ils
seront spécifiques qu'à certains modules...  
  
Enfin après je sais pas ce qu'il s'est passé passé et ce qui s'est décidé
pendant les réunions et lors du captech mais je penses ainsi  
  
Après rien ne t'interdit de mettre plusieurs valeurs "normalisés" :  
+/- 1.2v, +/- 3.3v,+/- 5v, +/- 9v, +/- 12v et de les balancer sur les cartes
filles et tu choisis celui que tu veux utiliser ou non  
ou alors faire passer le 18v dans tout tes modules mais alors faudrait des
régulateurs sur chaque carte fille...

### **Hyacinthe Lacenne** - Apr 14, 2016 at 3:29 PM

Ok, c'est un peu dommage de prendre des pistes comme ca, mais bon, le but
c'est la flexibilité.  
  
Ensuite, voir si on veut que le jus vienne de la carte mere, avec son alim
intégrée, ou si on fait un module alimentation également =)

### **Hyacinthe,** - Apr 14, 2016 at 3:38 PM

Je pensais faire un module alimentation, au final la carte mère n'est qu'une
plaque

### **Hyacinthe VINCENT,** - Apr 14, 2016 at 3:41 PM

Oui, oui, un module alim !!! et qui gèrera aussi la batterie.  
C'est plus simple d'avoir une CM complètement passive, sans aucun composants.
Sinon on aura du mal à la retirer si on veut tout mettre à plat.  
Sinon, pour les alims on peut peut-être faire un petit travail pour limiter le
nbre de tensions.  
J'ai pas tout suivi sur les alims, mais on est sur une alim principale 5V type
chargeur USB ? Et quelle tension pour la batterie ?

### **Hyacinthe Lacenne** - Apr 14, 2016 at 3:50 PM

@Hyacinthe : Dans la meme lignée connecteurs, il y les connecteurs IDE qui sont
pas mal - et ca permet par exemple d'avoir de petites choses sympa sur la
carte mère : <http://blog.domogy.com/wp-
content/uploads/2015/11/raspberry_pi_zero_iso_demo.jpg> : c'est-y-pas sexy ?  
  
C'est 40 pins, du coup un peu un overkill, mais voilà l'idée implantée
*raspberrinception* ;)

### **Hyacinthe VINCENT,** - Apr 14, 2016 at 4:10 PM

Le connecteur ISA ... toute ma jeunesse ...

### **Hyacinthe VINCENT,** - Apr 14, 2016 at 4:31 PM

![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe , "_ PS:
pourquoi 4 signaux pour le pas à pas?_ "  
Les steppers ont 2 bobines qui sont alimentées en +/- 5v à travers des ponts
en H. Eux même pilotés en PWM pour gérer les courants et les micros-pas. Mais
c'est le driver qui fait tout ça.  
<https://a.pololu-
files.com/picture/0J4344.600.png?519b6c6d74c2f655dd6637eccd4590c0>  
Celui que j'utilise est aussi capable de driver 2 moteurs CC en marche
avant/arrière.

### **Hyacinthe KHOYRATEE,** - Apr 15, 2016 at 7:38 AM

![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  Ah si classe!

### **Hyacinthe,** - Apr 15, 2016 at 8:46 AM

L'alimentation est à l'heure actuelle du 18V.  
  
En ce qui concerne réduire le nombre de tension, les différentes solutions
utilisent déjà +-12V, 5V et 3.3V. Je n'ai rajouté que le -5V au cas ou pour
des AOP

### **Hyacinthe Lacenne** - Apr 15, 2016 at 9:08 AM

Top.  
On essaye de se fixer une solution ce soir, histoire de ?

### **Hyacinthe,** - Apr 15, 2016 at 9:40 AM

![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  , en fait les 4
signaux sont interne au module moteur, les signaux logiques qui nous
intéressent pour la carte mère sont plus step et dir non?

### **Hyacinthe,** - Apr 15, 2016 at 9:41 AM

Et oui, il faudrait fixer la solution aujourd'hui, comme ça la semaine
prochaine on fait fumer le fer à souder

### **Hyacinthe Lacenne** - Apr 15, 2016 at 9:46 AM

Ouiiii

### **Hyacinthe VINCENT,** - Apr 15, 2016 at 10:11 AM

![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe , la question
est : est-ce qu'on embarque le driver moteur (CC ou stepper) dans le module µC
ou est-ce qu'on fait deux modules séparés ?  
Moi j'envisageait un seul module µC avec le driver de stepper (qui est aussi
capable de driver un moteur CC) et qq composants annexes (transistors,
condos,...) d'adaptation pour les autres signaux pour ne pas trop multiplier
les modules.  
Les quatres fils peuvent sortir directement du module mais je me dis que, si
on le peut, c'est plus élégant qu'ils sortent en bout de CM (avec d'autres
fils externes) vers le moteur, transducteur, top/tour,... Si on change un
module, on a juste à le (dé/re)plugger sans (dé/re)brancher tous les fils
externes. On pourrait presque se passer de connecteurs pour les composants
externes en soudant directement les fils sur la CM qu'on est pas prets, elle,
de changer (quoique  ![Hyacinthe KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe  réussira peut-
être à la cramer... ).  ![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  pt'être qu'on peut
même plugger directement un connecteur ISA en bout de CM ;-)

### **hyacinthe,** - Apr 15, 2016 at 10:25 AM

Franchement laisser qques connecteurs standard en tête de cm est marrant :)
surtout quand on aura un rpi zéro ;)

### **Hyacinthe VINCENT,** - Apr 15, 2016 at 10:50 AM

moi je voyais l'inverse, la carte mère fait connecteur male et s'insère dans
un connecteur ISA femelle où toute la mécanique est soudée.

### **hyacinthe,** - Apr 15, 2016 at 11:51 AM

Je comprends mieux maintenant ! Compris ! Tu veux interfacer les deux comme
ça, nickel !

### **Hyacinthe VINCENT,** - Apr 15, 2016 at 11:57 AM

C'est juste une idée en réponse à la tienne. Quoique, un banc de
test/diagnostique où il suffit de plugger un bout de la CM et ses modules sur
un connecteur et on a ensuite un truc génial qui teste, simule et affiche tous
les signaux ... ce serait de la sur-qualité !

### **Hyacinthe Lacenne** - Apr 15, 2016 at 11:59 AM

Justement dans ce cadre, jsuis en train de faire un module (de test) pour
standardiser les tests en émulant électroniquement un signal revenant d'un
transducteur :)

### **Hyacinthe VINCENT,** - Apr 15, 2016 at 12:00 PM

hé, hé...

### **Hyacinthe KHOYRATEE,** - Apr 15, 2016 at 1:44 PM

C'est quoi que je dois cramer? Je suis un spécialiste pour ça :p pour les
explosions faut voir avec  ![Hyacinthe LICCIONI, FPGA at
echopen](./../../zz_assets/images/avatars/1249124.png) Hyacinthe   vu qu'il est
italien/corse

### **Hyacinthe VINCENT,** - Apr 20, 2016 at 9:40 PM

![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie ,  ![hyacinthe,
hardware thinker at echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe
,  ![Hyacinthe KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe ,  ![Hyacinthe,
Danseur du ventre at echopen](./../../zz_assets/images/avatars/1248689.png)
Hyacinthe , je me rends compte qu'on a pas validé définitivement les noms des
interfaces. Même si on est globalement d'accord, pour que l'ensemble du dépot
Git, de la doc, des schémas des sources soit un tout cohérent il faut qu'on
utilise tous exactement les mêmes noms. J'avais donc proposé les termes
suivants :  
  
**Name** **Title** **Amplitude**  
| [ITF-A_gnd](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-A_gnd)  | _Ground_  | [0v, 0v]  
| [ITF-B_5v](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-B_5v)  | _5v alimentation_  | [5v, 5v]  
| [ITF-
C_amplified_raw_signal](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-C_amplified_raw_signal)  | _Amplified raw signal_  | [0v, 2v]  
| [ITF-
D_amplified_filtered_signal](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-D_amplified_filtered_signal)  | _Amplified filtered signal_  | [0v, 2v]  
| [ITF-
E_signal_envelope](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-E_signal_envelope)  | _Signal envelope_  | [0v, 2v]  
| [ITF-F_12v](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-F_12v)  | _12v alimentation_  | [12v, 12v]  
| [ITF-
G_amplifier_gain](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-G_amplifier_gain)  | _Amplifier gain_  | [0v, 1v]  
| [ITF-
H_neg_12v](https://github.com/Bivi/medicotechnical/blob/master/interfaces/ITF-
H_neg_12v)  | _-12v alimentation_  | [-12v, -12v]  
| [ITF-
I_pulse_on](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-I_pulse_on)  | _Pulse on_  | [0v, 5v]  
| [ITF-
J_pulse_off](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-J_pulse_off)  | _Pulse off_  | [0v, 5v]  
| [ITF-
K_pulse_redpitaya](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-K_pulse_redpitaya)  | _Pulse info for Redpitaya_  | [0v, 5v]  
| [ITF-
L_18v_alimentation](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-L_18v_alimentation)  | _18v external alimentation_  | [15v, 20v]  
| [ITF-
M_abs_angle](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-M_abs_angle)  | _Absolute tranducer position_  | [0v, 5v]  
| [ITF-
N_cc_motor_pwm](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-N_cc_motor_pwm)  | _CC motor pwm_  | [0v, 5v]  
| [ITF-
N_stepper_b2](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-N_stepper_b2)  | _Stepper motor B2 signal_  | [-5v, 5v]  
| [ITF-
O_cc_motor_encoder](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-O_cc_motor_encoder)  | _CC motor incremental encoder_  | [0v, 5v]  
| [ITF-
O_stepper_b1](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-O_stepper_b1)  | _Stepper motor B1 signal_  | [-5v, 5v]  
| [ITF-
P_stepper_a1](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-P_stepper_a1)  | _Stepper motor A1 signal_  | [-5v, 5v]  
| [ITF-
Q_stepper_a2](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-Q_stepper_a2)  | _Stepper motor A2 signal_  | [-5v, 5v]  
| [ITF-
R_reserved](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-R_reserved)  | _reserved track_  |  
| [ITF-S_3_3v](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-S_3_3v)  | _3.3v alimentation_  | [3.3v, 3.3v]  
  

  * Si les lettres posent un pb on peut revenir sur 2 chiffres
  * Si des termes ne conviennent pas on peut encore changer sans problème pour l'instant. Mais ce sera plus compliqué dès qu'ils commenceront à être utilisés dans les sources.

  

**Ce serait bien de valider ça d'ici la fin de la semaine.  
**

### **Hyacinthe Lacenne** - Apr 21, 2016 at 6:27 AM

Looks good, OK pour moi!  
  
Remarque pour le changement de nom: si on référence dans les sources de la doc
les refs "Name" on peut les remplacer par par leur nom littéral dans le build
de la doc, non? On s'assure comme ça de l'uniformité des noms.

### **Hyacinthe,** - Apr 21, 2016 at 9:39 AM

Les ITF C,D et E sont dans la fourchette (0, 2.5V).  
G je mettrais plutôt gain control or gain factor.  
I (pulse on) est du (0, 5V) ou (0, 3.3V).  
K pulse redpitaya est du (0, 3.3V).  
  
Et dans les noms des interfaces et les valeurs, mettre un V majuscule pour le
sigle voltes.

### **Hyacinthe VINCENT,** - Apr 21, 2016 at 10:50 AM

![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe , oui, bien sûr,
c'est le principe. On peut même le traduire ;-)  
![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe , va pour ITF-
G_gain_control. Et je corrigerai les amplitudes. Par contre pas de majuscules
dans les nom des interfaces hors ITF et la lettre (plus facile à parser
ensuite) par contre dans la partie Title en clair, pas de pb je le ferai.

### **Emilie Mayer,** - Apr 21, 2016 at 3:20 PM

Plutôt que de parler d'alimentation je parlerais de potentiels car, c'est plus
un signal non?  
pourquoi pas 12v_pot pour les alimentations et 18v_pot_ext, sinon c'est peu
clair non?  
pulse_to_RedPitaya comme ça on sait où il va. C'est quoi l'interface du gain
control?

### **Emilie Mayer,** - Apr 21, 2016 at 3:21 PM

b1, a1 ce n'est pas très explicite...

### **Hyacinthe KHOYRATEE,** - Apr 21, 2016 at 3:41 PM

Moi ça me va :)  
![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  Personnellement
je trouve alimentation très bien, pourquoi potentiel?  
a1,b1 sont les noms des entrées sur un moteur pas à pas :) A et B représentent
les bobines et les chiffres la phase si je dis pas de bêtises

### **Hyacinthe VINCENT,** - Apr 22, 2016 at 11:42 AM

Màj de la tables des interfaces
(<https://github.com/Bivi/medicotechnical/blob/master/doc/build/configurations.md>)
:  
**  
Name** **Title** **Amplitude**  
| [ITF-A_gnd](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-A_gnd)  | _Ground_  | [0V]  
| [ITF-B_5v](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-B_5v)  | _5V alimentation_  | [5V, 5V]  
| [ITF-
C_amplified_raw_signal](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-C_amplified_raw_signal)  | _Amplified raw signal_  | [0V, 2.5V]  
| [ITF-
D_amplified_filtered_signal](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-D_amplified_filtered_signal)  | _Amplified filtered signal_  | [0V, 2.5V]  
| [ITF-
E_signal_envelope](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-E_signal_envelope)  | _Signal envelope_  | [0V, 2.5V]  
| [ITF-F_12v](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-F_12v)  | _12V alimentation_  | [12V, 12V]  
| [ITF-
G_gain_control](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-G_gain_control)  | _Amplifier gain_  | [0V, 1V]  
| [ITF-
H_neg_12v](https://github.com/Bivi/medicotechnical/blob/master/interfaces/ITF-
H_neg_12v)  | _-12V alimentation_  | [-12V, -12V]  
| [ITF-
I_pulse_on](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-I_pulse_on)  | _Pulse on_  | [0V, 3.3V-5V]  
| [ITF-
J_pulse_off](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-J_pulse_off)  | _Pulse off_  | [0V, 5V]  
| [ITF-
K_pulse_redpitaya](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-K_pulse_redpitaya)  | _Pulse info for Redpitaya_  | [0V, 3.3V]  
| [ITF-
L_18v_alimentation](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-L_18v_alimentation)  | _18V external alimentation_  | [15V, 20V]  
| [ITF-
M_abs_angle](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-M_abs_angle)  | _Absolute tranducer position_  | [0V, 5V]  
| [ITF-
N_cc_motor_pwm](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-N_cc_motor_pwm)  | _CC motor pwm_  | [0V, 5V]  
| [ITF-
N_stepper_b2](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-N_stepper_b2)  | _Stepper motor B2 signal_  | [-5V, 5V]  
| [ITF-
O_cc_motor_encoder](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-O_cc_motor_encoder)  | _CC motor incremental encoder_  | [0V, 5V]  
| [ITF-
O_stepper_b1](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-O_stepper_b1)  | _Stepper motor B1 signal_  | [-5V, 5V]  
| [ITF-
P_stepper_a1](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-P_stepper_a1)  | _Stepper motor A1 signal_  | [-5V, 5V]  
| [ITF-
Q_stepper_a2](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-Q_stepper_a2)  | _Stepper motor A2 signal_  | [-5V, 5V]  
| [ITF-
R_reserved](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-R_reserved)  | _reserved track_  |  
| [ITF-S_3_3v](https://github.com/Bivi/medicotechnical/blob/master/interfaces
/ITF-S_3_3v)  | _3.3V alimentation_  | [3.3V, 3.3V]  
  
![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  effectivement,
dans "potentiel",  ce qui est important c'est la tension (une tension de
référence, par ex.) par contre dans "alimentation", c'est plus la puissance :
on va devoir débiter un courant sous cette tension. D'ailleurs à terme on
devra spécifier les courants max consommés par chaque module pour dimensionner
correctement les modules d'alimentation.

### **Hyacinthe Lacenne** - Apr 24, 2016 at 4:01 PM

Excellent!  
  
Un petit point, que je penses tu as réglé à coup de reverse quote, c'est
l'utilisation du underscore dans Markdown comme marqueur de style =)

### **Hyacinthe Lacenne** - Jul 10, 2016 at 8:54 AM

Bon, histoire de continuer sur les modules, le module 'TGC-Enveloppe-Ampli-
ADC' est né! Goblin de son petit nom (histoire de rester dans la thématique
des modules). Sa doc (et les premiers tests) se trouvent sur
[https://github.com/hyacinthe124/echomods/tree/master/goblin](https://github.com/hyacinthe124/echomods/tree/master/goblin%20)  
  
Encore qques points à vérifier, mais le nouveau né semble avoir toutes ses
pins, dans l'ordre, et fonctionelles, donc intégrables sur la carte mère
plutot directement =)  
  
Reste à tester avec une meilleure alim, et également tester les limites de
l'ADC (avec un Raspberry Pi Zero, un BBB, ... tout ce qui a du SPI en fait!



#  1 echtOpian nous rejoint pour qqs jours de dev ;) Archived

Hyacinthe Lacenne posted this Jan 22, 2016 at 12:54 AM · 1 person applauded

rigolo ;) je forwarde et je lui réponds  
  
Bonjour,  
  
Je viens de découvrir votre projet via Hacker News et je suis très  
enthousiaste à l'idée de venir passer quelques jours pour travailler  
sur echOpen avec vous!  
  
Je suis développeur Python, ayant complété ma maîtrise en sciences  
(plus précisément, en Biophotonique -- j'ai réalisé des algorithmes de  
traitement d'images en Python et C à l'aide d'OpenCV et d'autres  
librairies de traitement de signal). Je suis originaire de Montréal,  
en visite présentement à Paris pour encore 10 jours environ. Ce n'est  
pas beaucoup de temps, mais j'aimerais quand même voir si on pourrait  
travailler sur certains des challenges softwares ensemble..!  
  
Je vois sur votre site une invitation à passer vous voir à  
l'Hôtel-Dieu -- à quels moments vos locaux sont-ils ouverts (jour,  
soir)? Puis-je passer demain (vendredi 22 janvier)?  
  
Merci à l'avance et au plaisir!  
  
Greg Sadetsky  
+33 7 55 99 61 98

### **hyacinthe,** - Jan 22, 2016 at 6:19 AM

Btw, c'est hackernews qui a relayé l'information murgen (4300 visites et 6600
pageviews en moins de 24h :))

### **hyacinthe,** - Jan 22, 2016 at 8:58 AM

Btw aussi jcrois que niveau github ça a ramené pas mal de monde (on a 25
stargazers et 8 watchers sur hardware now)



#  Congrès IEEE Septembre 2016

Hyacinthe posted this Mar 29, 2016 at 10:49 AM · 1 person applauded

Bonjour à tous,  
  
au mois de Septembre 2016 aura lieu le congrès d'acoustique IEEE à Tours.
C'est  un des plus grand congrès internationaux d'acoustique. Il pourrait être
intéressant de faire une présentation à ce congrès pour communiquer et
potentiellement trouver des contributeurs.  
  
Pour cela il faut envoyer un résumé pour une communication orale ou poster
d'ici le 1 Avril (soit Vendredi). Vous trouverez un premier jet du résumé sur
le drive :  
<https://docs.google.com/document/d/15imsUDxaRaKlkY5SKQPMc9pjbVXLxiJ20UQWpYq3RPM/edit>  
N'hésitez pas à faire des commentaires.

### **Hyacinthe Lacenne** - Mar 29, 2016 at 10:56 AM

Super idée - though a tad late .. J'ai commencé à corriger des typos =)  
  
Si tu es chaud pour un poster,  tu trouveras attaché le poster qu'avait fait
Caskey pour inspiration. Dis moi, jte donne un coup de main pour boucler ca
viteuf.  
  
PS: possible aussi de faire un comparatif, display physique, notre image,
l'image d'un scanner pro ?  
  
(see <https://github.com/echopen/murgen-dev-kit/blob/master/Session_6.md> ? )  

[

![](./../../zz_assets/images/previews/3034651-kwan_bmes_2015_v1.png)

](bc3-raw/files/3034651-kwan_bmes_2015_v1.pdf)

[ Kwan_BMES_2015_v1.pdf  734 KB • Download
](bc3-raw/files/3034651-kwan_bmes_2015_v1.pdf)

### **Hyacinthe,** - Mar 31, 2016 at 2:39 PM

On met qui pour les auteurs?  
  
Il y aura moi, Hyacinthe, Hyacinthe, Hyacinthe, Hyacinthe.  
On rajoute Hyacinthe, Hyacinthe Loyaux et Gérard?

### **Hyacinthe KHOYRATEE,** - Mar 31, 2016 at 2:57 PM

C'est une bonne idée, effectivement ce serait bien de leur demander je penses!



#  Electronic lab'

Hyacinthe KHOYRATEE posted this Jun 20, 2016 at 2:06 PM · 5 people applauded

Salut à tous,  
  
J’espère que tout le monde va bien, je reprends une proposition que j'ai fais
il y a de cela un moment. L'idée est si vous le voulez, de pouvoir imprimer
vos circuits dans les locaux de l’hôtel dieu. Plusieurs sites expliquent la
procédure à suivre.  
  
Plusieurs façon d'imprimer ses circuits:  
<https://www.sonelec-musique.com/electronique_bases_realisation_ci.html>  
  
Gravure chimique (le moins cher à mon sens bien que certain on trouvé le moyen
de créer des graveurs mécaniques low cost à partir d'imprimante 3D et c'est la
que je me rends compte que ma parenthèse est trop grande):  
<http://www.68hc08.net/articles.item.42/gravure-pcb-solution-1.html>[  
](http://www.68hc08.net/articles.item.42/gravure-pcb-
solution-1.html)<http://wiki.jelectronique.com/doku.php?id=realisation_de_circuits_imprimes>  
  
Si jamais vous décidez que ça vaut le coup, il faut pour ça :  
* Une insoleuse (entre 200 et 1500e chez radiospare) ou alors regarder la solution d'un gars sur le site de sonelec ou il utilise une machine pour les ongles à 18e  
* Des plaques epoxy (futur support de vos Circuits Imprimé, CI à 15e en moyenne)  
* Des produits chimiques:  
          - Un révélateur (sachet déjà pret ou alors solution à base de soude, entre 1 à 5e)  
          - Perchlorure de fer (20 à 30e)  
* Du papier calque pour imprimer ses typons  
* Un logiciel de CAO, perso j'utilise Altium Designer mais il est cher, sinon j'ai un ami qui m'a montré celui la : <https://easyeda.com/> que je trouve vraiment bien!  
* Tout le matos de base de protection (lunette, blouse, gants etc)  
* Matos de méca : perceuse  
  
Voila, j'ai encore jamais essayé mais bon ça n'a pas l'air non plus d'être le
plus compliqué, si vous tentez dîtes le moi je suis curieux!

### **Hyacinthe Lacenne** - Jun 20, 2016 at 2:08 PM

Ça me semble bien top et pertinent pour avancer sur la voie électronique :)

### **Hyacinthe VINCENT,** - Jun 21, 2016 at 8:15 AM

Quelques autres pistes:  
**Avec une imp laser:**

  * Il semblerait que l'on puisse remplacer la phase typon, insolation, révélateur en faisant un transfert à chaud de l'encre des pistes imprimées sur papier à l'imprimante laser puis en éliminant le papier à l'eau. Il y a des tonnes d'exemples (ex <https://www.youtube.com/watch?v=imQTCW1yWkg>).
  * On pourrait même hacker une imprimante laser (y en aurait pas une dans la salle de réunion) pour qu'elle imprime directement sur le PCB (<https://www.youtube.com/watch?v=VY-7hQ6ocx8>)

**Avec une imp 3D  
**  

  * La gravure comme propose  ![Hyacinthe KHOYRATEE, Electronique at echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe 
  * Le dépot du masque directement sur le PCB (<http://www.instructables.com/id/Make-Flexible-Circuit-Boards-Using-A-3D-Printer/>)

  

Et aussi peut-être en profiter pour se développer une compétence en CMS
(composants soudés en surface) moins chers et bien plus compacts. Alors il
faudra, en plus une plancha à 30€.

### **Hyacinthe KHOYRATEE,** - Jun 21, 2016 at 8:56 AM

Très intéressant, l'utilisation d'imprimante, à essayer! Si ça m'est
accessible je tente le coup!  
  
Pour compléter ce que dit  ![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  à propos des
CMS, réfléchir sur le sujet me parait aussi important car les CMS ne
permettent pas seulement de gagner en place (plus besoin de percer sa carte et
le montage est possible en double face assez facilement) mais aussi de gagner
en performances  (distorsion en HF, CEM, bruit, etc). Il existe des façons
assez simple de braser le CMS grâce à un four à refusion :  
<http://wiki.jelectronique.com/doku.php?id=souder_des_cms>

### **Hyacinthe Lacenne** - Jun 21, 2016 at 9:07 AM

Yop, bien vrai ça! Petits soucis de distorsions qu'on voit apparaitre bien
facilement, sur des betes montages juste à base de résistances (non non non je
ne pense pas à des R2R au delà de 1MHz =) )

### **Hyacinthe Lacenne** - Jun 25, 2016 at 5:36 PM

Pour l'imprimante laser, je viens de lire ca.. ca peut etre pas con!  
  
<https://hackaday.io/project/12133-automatic-audio-source-switching/log/40600
-proto-build>



#  mois de la contribution wikipedia Archived

Hyacinthe Lacenne posted this Feb 19, 2016 at 10:11 PM · 1 person applauded

hello à tous  
  
le mois de mars est le mois de la contribution chez wikipedia  
  
voici la
[page](https://fr.wikipedia.org/wiki/Discussion_Wikip%C3%A9dia:Mois_de_la_contribution)
dédiée, il est recherché des wikipédiens pour monter un atelier. on se fait ça
?  
  
un wikithon autour de l'open source santé ? on proposerait ça à qqs asso du
libre et qqs makerspaces, l'occasion de nous impliquer plus dans cet eco-
système



#  Fréquence d'échantillonnage

Hyacinthe posted this May 03, 2016 at 3:58 PM

Suite à la réunion d'hier et de la discussion sur les fréquences
d'échantillonnages minimales envisageable, j'ai une petite simulation pour
comparer sur une même mesure (simulée) ce qu'on pourrait obtenir à 1, 2, 5 et
10 MHz de fréquence d'échantillonnage.  
Les résultats sont présentés dans ce document :  
<https://docs.google.com/document/d/104kDzqOb0_KzRr_Bt8KVuewdHG0HHP8LoOVddI_69Kk/edit>  
Ici on ne considère que l'enveloppe du signal pas le signal complet (sinon on
serait vraiment en sous-échantillonnage). Et on considère un système parfait :
pas de bruits et pleine échelle de l'ADC.  
  
Conclusions rapides :  
\- 1 MHz clairement insuffisant  
\- 10 MHz largement bon  
  
Pour moi le mieux est 5 MHz.

### **Hyacinthe Lacenne** - May 03, 2016 at 4:38 PM

Excellent modèle, intéressant! Pour clarifier, est ce que le signal (en vert)
correspond bien à l'enveloppe? A ce signal s'ajoute les déformations liées
transducteur et celle également du détecteur d'enveloppe?  
  
Pour compléter, purement en termes de physique, en termes de vitesse on est
bien à du c/2 -&gt; pour résoudre 1mm spatialement, l'onde doit parcourir 2mm
(1 AR).  
\- A cette fréquence, on a donc 1us (sampling a 1MHz) = 0.75mm d'image.  
\- A l'autre extrémité de l'échelle, on peut résoudre à la profondeur de la
focale à la louche .25mm, ce qui donne en termes de sampling du 3MHz.  
Tu me corriges si faux?  
  
Donc, peut on postuler que, dans le cadre de la détection d'enveloppe
analogique :  
\- 1MHz est trop juste (tout juste à 1.333 pts / mm, ce qui est trop
borderline mais dans les specs aujourd'hui)  
\- à 2MHz tu es à 2.66 pts / mm ce qui n'est pas top mais te permet de voir
les grosses structures, à une resolution dans les specs  
\- a 5MHz, le signal est pas mal (6.7px/mm)  
\- a 10MHz, 3 fois la fréquence de la porteuse, il y a un bon fit, et a cette
fréquence, le besoin d'une détection d'enveloppe analogique commence a
s'estomper.  
  
Bref, différentes fréquences, différents usages.  
  
Avec ce script, est il possible de quantifier l'erreur de mesure sur le signal
en termes d'erreur / signal sur la longueur de la ligne ?  
  
Ceci ne prend bien sur en compte que l'aspect enveloppe : à ces fréquences on
ne parle bien sur pas de traitement du signal =)  
  
J'essaye assez vite de faire un petit comparatif sur les images acquises à
5MHz, histoire de comparer les images à 1, 2 et 5 Msps =)

### **Hyacinthe Lacenne** - May 03, 2016 at 7:43 PM

En image : <https://github.com/hyacinthe124/murgen-dev-
kit/blob/master/worklog/Session_8.md>  
  
A 1Msps on a très peu de finesse, et 2.5Msps est clairement plus proche de
5Msps que de 1Msps =)

### **Hyacinthe,** - May 04, 2016 at 9:27 AM

Je ne présente que l'enveloppe dans le document, basé sur la réponse
impulsionnelle du transducteur. Le détecteur d'enveloppe est supposé parfait
(c'est une simulation très basique donc tout est supposé parfait).  
  
Le fait que l'onde fasse un aller et retour n'a rien à voir avec la fréquence
d'échantillonnage, c'est son enveloppe (ici) qui joue uniquement. Tu confond
taille de pixel et fréquence d'échantillonnage. La taille d'un pixel peu être
donné par la fréquence d'échantillonnage ou non. La fréquence
d'échantillonnage donne la précision temporelle afin de voir tous (et plus
important entièrement) les echos. La taille d'un pixel donne la précision de
taille qui tient en compte de l'aller retour et qui peut recouvrir plusieurs
échantillons (il faut alors intégrer les points).  
  
Il est très facile avec mon script de mesure l'erreur, c'est codé pour pouvoir
comparer les situations.  
  
Quand à tes images, je ne sais pas ce que tu as fait dessus, mais tout ce que
je vois c'est un effet de moyennage.

### **Hyacinthe Lacenne** - May 04, 2016 at 9:48 AM

Désolé de ne pas avoir été clair =)  
  
On est bien alignés que ce qui joue ici c'est l'enveloppe du signal, pas le
signal. D'autre part, dans mon message 1 pixel = 1 point acquis, l'image ne
venant qu'après (surtout si on induit les déformations de l'image liées à la
scan conversion). Effectivement dans ce qui était évoqué, les deux sont bien
liés. Au niveau temporel, on est quand même OK que les echos venant de deux
interfaces separées de d seront dans le temps séparés de 2*d/v?  
  
Pour les images, l'image à 5Msps (la moins floue) a été décimé d'un facteur 2
puis 5 pour simuler la perte d'information due au sous echantillonage, puis
ces images mises à l'échelle pour avoir la meme taille d'image. On devrait
avoir un output plus pixélisé, mais l'output en JPG "floute" ces différences.
Pour être rigoureux, faudrait faire ce test avec une image acquise à bien plus
haute vitesse, et voir l'effet du sous-echantillonage sur l'image finale.  
  
Désolé, pas vu de lien pour le code, ca m'aurait évité de poser une question
con au sujet de la réponse du tranducteur - et des dimensions de la tache
focale du piezo =)

### **Hyacinthe,** - May 04, 2016 at 10:06 AM

Je n'ai pas mis le lien de mon code effectivement.  
  
En ce qui concerne le temps d'arrivé d'échos venant de deux interfaces, on est
d'accord c'est bien 2d/v.  
  
En ce qui concerne tes images, j'ai trouvé ça comme code pour le changement de
fréquence d'échantillonnage j'ai l'impression (je ne pipe rien au python) :  
  

    
    
    # Creation d'une image non scan-converted
     for i in range(size[0]): # les lignes
     for j in range(size[1]):
      pix[i,j]=128
      value = 0
     for k in range(DECIMATION):
      value = value + SortedTable[i][j*DECIMATION+k]*(1.9*(j*DECIMATION+k)**(0.6)/(Depth**(0.6)))
      value = int(value/DECIMATION)
      ImagePoints[i][j] = (int)(value/64)
      pix[i,j] = (ImagePoints[i][j],ImagePoints[i][j],ImagePoints[i][j])

  

Si j'interprète bien la boucle sur k, tu dis que la valeur d'un pixel est
égale à la moyenne des points sur le nombre décimation, c'est ça? D'où l'effet
de moyennage que je vois sur l'image?

### **Hyacinthe Lacenne** - May 04, 2016 at 10:18 AM

L'effet de moyenne est surtout (je pense) du au redimensionnement de l'image :
à 1Msps, l'image sans redimensionnement (normalization) fait cette taille :
<https://github.com/hyacinthe124/murgen-dev-
kit/blob/master/worklog/Images/Session_8/source_files/2c10128b362d2e1652c1b97111ba0ae2
.data-DEC5-SC-4T.png>  
  
Effectivement, c'est la bonne boucle dans le bon script. Jpeux rajouter un
comparatif de l'image a 1Msps avec un point choisi au pif parmis les DEC
points, ca sera plus rigoureux =) A vue de nez, ca introduira une image plus
"piquée", mais le redimensionnement ultérieur va de toutes facons "lisser" ces
pics.  
  
A voir donc avec cet effet de randomization des points de l'image, bien vu!

### **Hyacinthe,** - May 04, 2016 at 10:35 AM

Par contre tu n'as pas répondu à ma question, la boucle sur k :  
  
  

    
    
    for k in range(DECIMATION):
      value = value + SortedTable[i][j*DECIMATION+k]*(1.9*(j*DECIMATION+k)**(0.6)/(Depth**(0.6)))
      value = int(value/DECIMATION)

  
  
ça fait la moyenne sur les n points?

### **Hyacinthe Lacenne** - May 04, 2016 at 10:39 AM

Effectivement, il faisait la moyenne =) D'où l'idée de refaire le comparatif
en choppant 1 point choisi au pif parmi les DEC disponible, pour être plus
rigoureux.

### **Hyacinthe VINCENT,** - May 04, 2016 at 11:02 AM

Et pour simuler le "peak&amp;hold" on pourrait aussi retenir le max des points
;-)

### **Hyacinthe,** - May 04, 2016 at 12:00 PM

Oui donc en faisant un moyennage tu n'as pas fait une décimation mais changé
la taille du pixel. Pour faire une décimation il faut effectivement ne garder
qu'un des points.

### **Hyacinthe Lacenne** - May 04, 2016 at 6:06 PM

Comparatif done at : <https://github.com/hyacinthe124/murgen-dev-
kit/blob/master/worklog/Session_8.md> et les sources (en quick and dirty :
<https://github.com/hyacinthe124/murgen-dev-
kit/tree/master/worklog/Images/Session_8/source_files> ) en particulier le
makeTest.sh Hope that helps!  
  
(edit : Session_8bis -&gt; Session_8 updated)

### **Hyacinthe VINCENT,** - May 09, 2016 at 8:23 AM

Pas mal, on voit bien qu'on a  moins d'érosion des détails avec le max qu'avec
la moyenne. On voit aussi que le random pourrait avoir du sens car il s'agit
d'une image animée et l'oeil ferait le reste du travail d'identification en
traitant l'empilage de plusieurs frames successives. Par contre le random ne
serait pas si facile à réaliser en analogique en amont de l'ADC.  
Par ailleurs, si on arrive à atteindre 10-15 fps, il y a aussi un coup à jouer
en faisant un traitement glissant sur 2-3 frames successives.



#  Ressources: matériaux et acoustique

Hyacinthe Lacenne posted this Apr 05, 2016 at 4:39 PM · 1 person applauded

Un petit thread sur les questions de matériaux:  
\- <http://www.signal-processing.com/us_data.html> -&gt;  Oil SAE 20 semble
pas mal - ou l'huile de mais  
\- <http://www.signal-processing.com/us_data_p.html> &gt; Ethyl vinyl acetate
pour l'impédance acoustique  
Ce dernier a l'air d'être le matériau de semelles des tongs... a voir ;)  
  
ps: du fantome à base d'huile de ricin : <http://www.orion-
france.com/radiodiagnostic/pdf/orion_fantome_fil_1860.pdf>

### **Hyacinthe Lacenne** - Apr 27, 2016 at 9:21 PM

![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe
![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  rigolo ;)  
  
<http://www.developpez.com/actu/98164/Un-ingenieur-propose-un-clone-d-Arduino-
de-la-taille-d-une-pile-AA-le-dispositif-tourne-avec-un-controleur-ATmega328P-
et-32-Ko-de-memoire-flash/>

### **Hyacinthe Lacenne** - May 17, 2016 at 9:14 AM

Pas le bon thread, matériaux c'est pour les matériaux ;)

### **Hyacinthe Lacenne** - May 17, 2016 at 1:38 PM

ok je me barre de là ;)

### **Hyacinthe Lacenne** - Jun 07, 2016 at 2:53 PM

Parce que c'est du matériau -- mais aussi du gel, je voulais partager ce lien
assez intéressant (sur la démarche comme sur les résultats) :  
  
"This paper describes design of a low cost, ultrasound gel from local products
applying aspects of Human Centered Design methodology. A multidisciplinary
team worked with clinicians who use ultrasound where commercial gel is cost
prohibitive and scarce. The team followed the format outlined in the Ideo Took
Kit. Research began by defining the challenge "how to create locally available
alternative ultrasound gel for a low-resourced environment? The "End-Users,"
were identified as clinicians who use ultrasound in Democratic Republic of the
Congo and Ethiopia. An expert group was identified and queried for possible
alternatives to commercial gel."  
  
#BOP #Jugaad #JusteCool  
  
Source:
<http://journals.plos.org/plosone/article/asset?id=10.1371%2Fjournal.pone.0134332.PDF>

### **Hyacinthe VINCENT,** - Jun 07, 2016 at 3:02 PM

Et en plus c'est comestible, ça doit être pour ça qu'ils rajoutent du sel,
sinon c'est pas bon :-)

### **Hyacinthe Lacenne** - Jun 07, 2016 at 6:07 PM

En plus facile de par chez nous, y'a aussi cette recette, trouvée online:  
  
1\. Mix 2 teaspoons of guar gum with 1-2 teaspoons of salt. (The amount of
salt isn't vitally important since it is just added to keep the guar gum from
clumping. Using slightly less than a teaspoon of salt per 2 cups makes a gel
with which is isotonic, which would be ideal for use near eyes or other mucus
membranes or on open wounds).  
  
2\. Boil two cups of water.  
  
3\. Slowly sprinkle the guar gum/salt mixture into the boiling water while
stirring vigorously with a fork or whisk.  
  
4\. Boil for about 1-2 minutes until thick and well mixed.  
  
5\. Cool before using. Save lives.  
  
La vidéo : <https://www.youtube.com/watch?v=FnjCqgvwj9I>

### **Hyacinthe Lacenne** - Jun 07, 2016 at 10:12 PM

mais c trop bien ;)

### **Hyacinthe Lacenne** - Jun 08, 2016 at 9:11 AM

Dans la même lignée: <http://www.ncbi.nlm.nih.gov/pubmed/24238590>  
  
In this study, a gel made from cornstarch and water was an acceptable coupling
medium and provided equally adequate images as compared with commercial
ultrasound gel. This inexpensive gel made from ubiquitous materials can be an
acceptable alternative to commercial gel in low-resource settings.

### **Hyacinthe Lacenne** - Jun 08, 2016 at 3:47 PM

Hum ca serait bien que ce plastique marche :)  
<https://www.rpelectronics.com/af-2504-polymorph-low-temperature-
thermoplastic-beads-100g.html>

### **Hyacinthe VINCENT,** - Jun 09, 2016 at 9:43 AM

Oui, ça j'en ai à la maison ;-) on essaiera. Encore qq idées à tester:

  * le plastique en grain qui fond dans un bol (j'ai)
  * l'ABS (j'ai)
  * la résine EPOXY (j'ai)
  * La pâte Fimo (j'ai)
  * La pâte [Sugru](https://sugru.com/about/) (j'ai)

### **Hyacinthe Lacenne** - Jun 09, 2016 at 9:50 AM

Excellent !!

### **hyacinthe,** - Jun 13, 2016 at 5:49 PM

![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  --  lien pour
le matos sur hackaday: <https://hackaday.io/project/11478-open-source-
ultrasound-phantoms>

### **Hyacinthe VINCENT,** - Jun 17, 2016 at 12:18 PM

En retournant faire un tour sur
<http://www.ondacorp.com/tecref_acoustictable.shtml> je suis tombé sur un des
seuls matériaux solides qui a le même indice que l'eau : le pin !  
Avouez que ce serait drôle de faire une sonde en bois :-)

### **Hyacinthe Lacenne** - Jun 20, 2016 at 2:16 PM

J'ai emprunté la tete de sonde 10PV retapée ce samedi pour essayer de
travailler dessus - en particulier sur le liquide dans la tete de sonde.  
  
D'après <http://www.signal-processing.com/us_data.html> \-- le meilleur
candidat serait "Oil SAE 20", aka de l'huile de moteur =) donc facilement
trouvable. Vous tiens au jus des avancées!

### **Hyacinthe VINCENT,** - Jun 21, 2016 at 8:29 AM

Mais bien visqueuse et crade ...  
Huile de lin ?  
Si une huile fine (huile de vaseline, l'huile de parafine, glycérine)...
fonctionnait ce serait plus clean à manipuler (et biocompatible).

### **Hyacinthe Lacenne** - Jun 21, 2016 at 8:43 AM

True!  
  
Huile de lin alors !



#  Commande de composants

Hyacinthe KHOYRATEE posted this Jan 20, 2016 at 5:00 PM

Bonsoir à tous,  
  
Un ingénieur électronique m'a recommandé ce site ; <https://octopart.com/>  
  
Il permet de retrouver des composants et d'en faire un comparatif de prix
selon le fournisseur.  
  
Enjoy ;)



#  Modularisation Echopen

Hyacinthe posted this Apr 06, 2016 at 3:08 PM

Salut, voici un premier jet d'un template de fiche module :  
  
<https://docs.google.com/document/d/1EeRx9UNmEvYHRDvSmZFVRK1LbnUJji-
7wTBdwWL5yZw/edit>  
  
A modifier, commenter sans retenu.

### **Hyacinthe Lacenne** - Apr 06, 2016 at 4:40 PM

Complet, top!

### **Emilie Mayer,** - Apr 08, 2016 at 9:11 AM

Je regarde ca en fin daprem!

### **Hyacinthe** - Apr 09, 2016 at 7:27 AM

Hello,  
  
Hier,  ![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  et  ![Michel
Bala, Electronique analogique  at
echopen](./../../zz_assets/images/avatars/2008321.png) Michel , sur la base du
premier brouillon de la fiche module, ont réalisé un premier module celui du
détecteur d'enveloppe (3 composants sur un bout de plaque).  
  
L'idée étant de poser une première proposition à vous présenter lundi soir
lors de la réunion hebdomadaire pour que tous puissiez faire vos retours,
remarques et suggestions et qu'on l'améliore par itérations et prendre en
compte les avancées et travaux des uns et des autres.  
  
La documentation, est disponible
[ici](https://docs.google.com/document/d/1ZrQnQYbzWZsSQswlGicaGloDg0jS_OSDsJJOcuHyHIk).
Là encore il s'agit d'un premier test en vue d'obtenir les retours de la
communauté et d'identifier les améliorations possibles.  
  
Voici une photo du module en question, la photo méritera d'être améliorer avec
une réf métrique et une vue plus explicite.  
  
Tous vos retours sont les bienvenus.  
  

[

![](bc3-raw/files/3504719-fullsizerender.jpg)

](bc3-raw/files/3504719-fullsizerender.jpg)

[ FullSizeRender.jpg  1.05 MB • Download
](bc3-raw/files/3504719-fullsizerender.jpg)

### **Hyacinthe Lacenne** - Apr 09, 2016 at 12:20 PM

Top!  
Je comprends que les IO (inputs/outputs) se font sur la plaque physiquement,
ou est ce à travers des pins?  
Si c'est à travers des pins, peut on s'aligner dans un premier temps sur une
configuration de pistes du style proposé earlier cette semaine ([tof remise
sur le wiki ici ](http://echopen.org/index.php?title=Worklog_-
_the_module_approach#A_rough_draft)) ?  
La standardisation dès le design permettra l'interoperabilité des modules =)

### **Hyacinthe VINCENT,** - Apr 10, 2016 at 9:38 AM

Ça commence a prendre forme :-)  
QQ petites remarques :

  * On doit pouvoir remettre la carte dans le bon sens avec les pistes en dessous : On plante le peigne de pins par dessus (plastique au dessus). On soude "finement" par dessous (bon exercice ;-) ). On utilise une rangée de connecteurs femelles de 5.6 de haut (au lieu de ceux 8.4) comme ça on gagne un peu en hauteur et les pins restent compatibles avec les bread board (juste un peu court). Il reste aussi des pins qui dépassent au dessus de la carte que l'on peut utiliser comme point de test ou couper ensuite (en retirant le plastique). A terme les modules seront surement réalisés en dble face à trous métallisés probablement soudable par le dessus.

[

![](bc3-raw/files/3514906-20160410_112533_hdr2.jpg)

](bc3-raw/files/3514906-20160410_112533_hdr2.jpg)

[ 20160410_112533_HDR2.jpg  805 KB • Download
](bc3-raw/files/3514906-20160410_112533_hdr2.jpg)

  * A priori une seule rangée de pins est nécessaire au lieu deux. En plus ça libère la largeur des modules.

### **Hyacinthe VINCENT,** - Apr 10, 2016 at 11:07 AM

Apropos de la proposition de  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  sur le Wiki :
"_une configuration de pistes du style proposé earlier cette semaine (_[_tof
remise sur le wiki ici _](http://echopen.org/index.php?title=Worklog_-
_the_module_approach#A_rough_draft)_)_".  
Je me suis permis de proposer qq modifs :

  * Ajout d'une colonne pour commencer à figer des id des signaux
  * Ajout de 3 pistes qui permettraient de piloter aussi les steppers. On y voir apparaitre une particularité : si on sait que deux technologies ne coexisteront jamais dans un même modèle de sonde, alors deux signaux différents peuvent se partager une même piste (cf. SIG-cc_motor_pwm ; SIG-stepper_b2).
  * SIG-pulser_on et SIG-pulser_off continuent de me gêner : une contrainte techno dans un des modules qui "remonte" sur le fond de panier. Si un jour qq'un refait un autre pulser sans cette contrainte, il sera obligé d'émuler les "faiblesses" du module historique. Mais, ça peut se justifier au nom du principe "KISS". Sinon ne pourrait-on pas ajouter une détection du front montant et du front descendant d'un SIG-pulse unique ?

### **Hyacinthe Lacenne** - Apr 10, 2016 at 12:13 PM

Top, et surtout... Félicitations pour ton premier Edit du wiki ;)  
Agreed sur le principe des usp - ca fait un fond de panier un peu plus
compliqué et orienté sur une base tech choisie.. Mais comme les pistes
stepper, nope? Autant tout garder pour le moment, quitte à reallouer la piste
après ?

### **Hyacinthe VINCENT,** - Apr 10, 2016 at 1:53 PM

Oui, très fier de ma contribution wiki ;-). Quoique rendu un peu perplexe par
la syntaxe wiki pour dessiner un tableau : c'est ni wysiwyg, ni wysiwym mais
plutôt wysiniq (what you see is n'importe quoi).

### **Emilie Mayer,** - Apr 11, 2016 at 4:44 PM

j'ai commenté le doc de  ![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  et liens vers
les précédents documents que j'avais fait :  
  
  

<https://docs.google.com/document/d/1RrCh8tkR_IoBdsZZnKcKZwsHm70WCpwMV6Ac_HJxho8/edit>

  

et le suivant:

  

<https://docs.google.com/document/d/11dJB4cTPcXkxdXE4P0HZj2o6fjAQtg2ZvGt33IAwT-s/edit>

### **Hyacinthe Lacenne** - Apr 12, 2016 at 12:42 PM

![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  comme convenu,
voici la doc des submodules de git. ca peut inspirer

### **Hyacinthe VINCENT,** - Apr 12, 2016 at 4:17 PM

Heu ? Où ça ?

### **Hyacinthe Lacenne** - Apr 12, 2016 at 4:35 PM

Oui ;) <https://git-scm.com/book/en/v2/Git-Tools-Submodules>

### **Hyacinthe Lacenne** - Apr 12, 2016 at 4:43 PM

Excellent !!

### **Hyacinthe VINCENT,** - Apr 13, 2016 at 8:56 AM

Vraiment intéressant !

### **Hyacinthe Lacenne** - Apr 13, 2016 at 11:55 AM

Par la meilleure sérendipité qui soit, j'ai déjeuné avec un CTO de Symfony qui
m'a parlé d'un problème similaire.  
  
Il recommende de jeter un coup d'oeil aux subtree splits sous git ( <https
://git-scm.com/book/en/v1/Git-Tools-Subtree-Merging> ) - c'est la solution
qu'ils ont adopté après 5 ans de tests -&gt; le DG lui même a pris 2 semaines
pour coder un robot qui en simplifie la manipulation.  
  
Meme si on a pas besoin de cet extreme, il semble que le subtree split soit
moins time-consuming en termes de maintenance que les submodules.  
  
Il est aussi curieux de venir dire bonjour, la mise à dispo d'outils dans des
assos l'intéresse fortement - et il a pas mal d'expériences dans ce cadre =)

### **Hyacinthe** - Apr 13, 2016 at 7:08 PM

Top. On prépare un apéro sur le sujet en mode multi-interventions ? À moitié
présentation et session de travail ?



#  IT echopen

Hyacinthe posted this May 17, 2016 at 9:45 AM

Discussion dédiée à l'IT du projet

### **Hyacinthe** - May 17, 2016 at 9:47 AM

Hello,  
  
Donc nous venons avec Hyacinthe de modifier les DNS de l'ancien server =&gt; vers
le nouveau server.  
  
Pour ceux qui ont des emails echopen et qui souhaitent les ajouter sur leur
adresse Gmail, la procédure est disponible
[ici](https://wiki.gandi.net/fr/mail/standard-settings/gmail).  
  
Pour vos MdP, je vous les communique comme vous le souhaitez (email / SMS).
Dites moi.  
  
@+

### **Hyacinthe** - May 17, 2016 at 2:33 PM

Visiblement les DNS ont bien migré et le wiki est désormais accessible sous :  
\- wiki.echopen.org  
\- echopen.org  
\- www.echopen.org

### **Hyacinthe Lacenne** - May 17, 2016 at 3:15 PM

Félicitations !  
Les adresses MX mail ont également été changées ?

### **Hyacinthe** - May 17, 2016 at 4:47 PM

A priori, j'imagine que oui :  
  

    
    
    @ 10800 IN MX 50 fb.mail.gandi.net.
    @ 10800 IN MX 10 spool.mail.gandi.net.

  
J'avais bien recréé les adresses emails demandé, et je vous avais envoyé vos
MdP. Je peux à nouveau vous envoyer un MdP si besoin. le mieux serait de
m'envoyer ce que vous souhaitez comme MdP par sms.  
  
@+  
  
ps : ceux qui ont besoin d'une adresse email, dites le moi, je peux les créer.

### **Hyacinthe Lacenne** - May 18, 2016 at 12:34 PM

Excellent!  
  
Serait il possible d'y rajouter également l'ID de suivi G Analytics, qui a
loggué la vie du wiki depuis le début, à savoir UA-43565921-10 ?  
  
Cheers!

### **Hyacinthe Lacenne** - May 18, 2016 at 9:21 PM

sure ca devrait être possible. De mémoire, il faut ajouter un script sur la
home, c cela ?

### **Hyacinthe Lacenne** - May 19, 2016 at 12:45 AM

Un bout sur Localsettings plutôt :) (il y a aussi la possibilité d'ajouter une
extension, mais ca rajoute de la complexité)  
  
-&gt; Des détails sur <http://stackoverflow.com/questions/25907743/how-to-add-external-script-to-head-section-for-all-mediawiki-pages>  
  
Et le code :  
  
&lt;script&gt;  
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){  
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new
Date();a=s.createElement(o),  
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)  
  })(window,document,'script','<https://www.google-
analytics.com/analytics.js','ga');>  
  
  ga('create', 'UA-43565921-10', 'auto');  
  ga('send', 'pageview');  
  
&lt;/script&gt;

### **Hyacinthe Lacenne** - May 19, 2016 at 2:20 PM

ok je regarde cela

### **Hyacinthe Lacenne** - May 19, 2016 at 2:44 PM

\+ double quote pour les exe c fait ;)

### **Hyacinthe Lacenne** - May 19, 2016 at 5:29 PM

Well done, thanks =)

### **Hyacinthe Lacenne** - May 21, 2016 at 1:38 PM

Dans la "catégorie relou" ... :)  
  
Mon ancien password n'était pas assez solide pour le nouvea wiki, qui m'a
demandé d'en changer, mais ne me permets plus de me logguer. Si je lui demande
un mail de reset, le mail n'arrive pas.  
  
Any solution?

### **Hyacinthe Lacenne** - May 23, 2016 at 12:46 PM

D'autre part @hyacinthe, en fait c'est pas dans le head qu'il faut mettre le code,
mais dans le &lt;body&gt; (relou I know ^^)

### **Hyacinthe Lacenne** - May 23, 2016 at 3:26 PM

ah bah j'ai suivi ton lien ;)  
  
en effet, ce n'est pas une bonne pratique de mettre cela dans le head, et c ce
que fait les instructions js du LocalSettings.  
  
à la console, javais un message d'erreur ReferenceError: GoogleAnalytics is
not defined et en effet j'en ai  trouvé la trace dans MediaWiki:Common.js,
il y a avait une extension genre {{mediawiki:googleanalytics}}. c toi ? on
doit toujours avoir 0 erreurs à la console ;). anyway me suis permis de le
supprimer  
  
j'ai mis le code dans MediaWiki:Common.js protégé par un async loader

### **Hyacinthe Lacenne** - May 23, 2016 at 4:47 PM

Sweet, ca marche!

### **Hyacinthe Lacenne** - May 30, 2016 at 10:23 AM

Bug identified: les mails de remise à zéro de mots de passe pour le wiki ne
marchent pas, ils n'arrivent jamais.  
  
Ca vous le fait aussi?

### **Hyacinthe Lacenne** - Jun 01, 2016 at 4:02 PM

ca marche maintenant de mon côté -  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe   tu confirmes ?

### **Hyacinthe Lacenne** - Jun 02, 2016 at 8:02 AM

Bizarre, tjrs rien recu :/  
  
Je suppose que l'adresse mail est tjrs
[hyacinthe@echopen.org](mailto:hyacinthe@echopen.org) dans la DB, peut etre qu'en la
changeant en [hyacinthe124@gmail.com](mailto:hyacinthe124@gmail.com) la notif arrivera?

### **Hyacinthe Lacenne** - Jun 02, 2016 at 9:34 AM

Je n'arrive pas à récupérer les mdps pour les users Hyacinthe et Murgen.  
  
Tu avais créé Newbee pour l'occasion I presume? Dans ce cas, ca pourrait peut
etre toucher les users créés avant la migration, peut etre?

### **Hyacinthe Lacenne** - Jun 02, 2016 at 9:37 AM

Sinon en quick and dirty t'as  
<https://www.mediawiki.org/wiki/Manual:Resetting_passwords#Use_the_changePassword.php_maintenance_script>
=) Et je change de password sitot le dummy password recu =)

### **hyacinthe,** - Jun 06, 2016 at 5:58 AM

Wiki down :/

### **Hyacinthe Lacenne** - Jun 06, 2016 at 8:09 AM

ok mysql a  crashé, pour quel raison ? serveur relancé

### **hyacinthe,** - Jun 06, 2016 at 4:24 PM

Les logs n'ont rien livré ?

### **Hyacinthe Lacenne** - Jul 01, 2016 at 7:32 AM

Un spammer qui est passé à travers les mailles du filet :  
  
-&gt; [http://echopen.org/index.php?title=Main_Page&amp;diff=6476&amp;oldid=6427](http://echopen.org/index.php?title=Main_Page&diff=6476&oldid=6427)

### **Hyacinthe Lacenne** - Jul 04, 2016 at 12:22 PM

Page d'accueil atteinte, 4 IPs différentes spammaient:
<http://echopen.org/index.php/Special:RecentChanges>  
  
Page restaurée.. pour combien de temps? -&gt; Voir pour un filtre NOSPAMMER

### **Hyacinthe Lacenne** - Jul 07, 2016 at 5:18 PM

![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe   :
si tu as déjà implémenté, tu peux prendre la main sur le sujet ?  
  
@++

### **Hyacinthe Lacenne** - Jul 07, 2016 at 5:25 PM

Pas accès au serveur.  
  
Le truc est tout bête, cf :
<https://www.mediawiki.org/wiki/Manual:Preventing_access#Restrict_anonymous_editing>
\-- qques lignes dans LocalSettings.php

### **Hyacinthe Lacenne** - Jul 08, 2016 at 7:51 AM

done



#  un petit coucou Archived

Hyacinthe Lacenne posted this Feb 08, 2016 at 5:29 PM

hello, j'ai eu un coup de fil de Hyacinthe qui vous passe tous un coucou et qui
passera de temps à autre le lundi soir  
  
![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe   ce
serait pas mal de l'ajouter à ce basecamp ?  
  
@++



#  Nouveau formateur

hyacinthe posted this Feb 08, 2016 at 8:08 AM · 1 person applauded

Encore qqun d'interessee!  
Une doc veut echopen pour faire un test/demo d'echopen - sweet!  
Par contre du doppler avec notre sonde.. Ça restera à développer ;) ou sinon
en utilisant un très bon adc?

### **Hyacinthe Lacenne** - Feb 08, 2016 at 8:10 AM

yes je vais lui faire une réponse du type, on a pas encore développé et lui
proposer que l'on se rencontre chez echopen et qu'on regarde ce qu'on peut
faire ensemble, notamment du côté de hyacinthe !

### **Hyacinthe** - Feb 08, 2016 at 8:18 AM

![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  pourrais tu mettre
ce type de sujets dans le il de discussion ondoarding ? Cela nous évitera que
les discussions se multiplient et qu'on finisse par perdre toutes les
informations ?

### **Hyacinthe,** - Feb 08, 2016 at 9:43 AM

Le doppler peut se faire si on ne fait pas de détection d'enveloppe. Le
traitement de base est de faire une fft glissante sur le signal. Il y a
surement plus évolué comme traitement.

### **Hyacinthe Lacenne** - Feb 08, 2016 at 9:56 AM

ok ;) nice  
  
il s'agit de Marie-Thérèse Barrellier, elle passe nous voir le vendredi 18.
![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  on lui fera un
update, et elle précise que sur la partie veineuse, le doppler est moins
critique que sur l'artériel. Or, une des pathologies le plus fréquemment
suspectée aux urg. est la phlébite, donc pathologie veineuse ;)

### **hyacinthe,** - Feb 08, 2016 at 10:27 AM

Jsuis d'accord sur la fft glissante @Hyacinthe , faut juste un truc approprié
pour voir un shift de fréquence de 0.03% dans le meilleur des cas (si vitesse
sang = 25Cm/s - et on a pas ça dans toutes les veines): faut résoudre 1kHz de
son pic à 3.5MHz en théorie ?  
Donc faut idéalement un bon adc pour le voir, à moins que des maths nous
sauvent par un petit trick des familles ?

### **Hyacinthe,** - Feb 08, 2016 at 10:53 AM

Effectivement, avec une fft glissante, la résolution fréquentielle est
pourrie. Une solution serait de faire un fenêtrage glissant sur le signal et
si besoin rajouter du zero padding pour avoir la résolution suffisante. Par
contre cette solution est chronophage à mort, car elle demande beaucoup de fft
sur de grands vecteurs... Il faut voir les solutions existantes dans les
échographes acutels.

### **Emilie Mayer,** - Feb 08, 2016 at 7:21 PM

jeudi 18 ou vendredi 19?

### **Hyacinthe Lacenne** - Feb 08, 2016 at 10:56 PM

![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  oups elle
passera le vendredi 18 mars  
  
@++



#  Restructuration du WIKI/ Analyse fonctionnelle

Emilie Mayer posted this Jan 16, 2016 at 12:56 PM

Nous proposons:  
  

  * 3 fonctions principales: **Sensing, processing, displaying ** <https://docs.google.com/drawings/d/1Xi6ZHxV0G2W_YmuFY_VORmxdJpKpj23IjRDAVagxA1s/edit?usp=sharing>

Ces 3 fonctions vous conviennent-elles ?  
  

  * Shéma APTE analyse fonctionnelle externe de l'usage: <https://docs.google.com/drawings/d/1NY-pk6dhdEY4e0gRkpg5XFVs4ZXp9x_lY69UsTLycu4/edit?usp=sharing>

  
Commentaires bienvenus....

### **Hyacinthe Lacenne** - Jan 16, 2016 at 3:46 PM

hello Emilie, pour le schéma APTE, j'ajouterai la fonction "formation"  
  
et peut-être assurer que le système soit un cercle vertueux en ajoutant la
fonction "feedback"  
  
@++

### **Hyacinthe** - Jan 17, 2016 at 9:15 AM

Parfait. Et +1 sur la remarque de Hyacinthe. Pourrait on imaginer ajouter la
dimension formation dans le FC4 (aspects communautaires) car les formations
autant que les retours me semblent avoir une pertinence s'ils sont implémentés
dans une dynamique communautaire. Communautés d'utilisateurs, formations et
échanges peer-to-peer, retour d'expériences, etc. Qui aidera sans nul doute la
diffusion de l'outils et du concept auprès des utilisateurs.

### **Hyacinthe Lacenne** - Jun 19, 2016 at 8:07 PM

![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  : tjrs d'actu
la restructuration? Fais signe si besoin d'un coup de main =)

### **Emilie Mayer,** - Jun 20, 2016 at 12:10 PM

Il s'agit de mettre en oeuvre ce qu'on avait fait avec muriel... on peut en
discuter

### **Hyacinthe Lacenne** - Jun 20, 2016 at 12:16 PM

On avait parlé de revenir sur l'ancien skin, faudra donc évoquer ca aussi en
plus de la réactulisation de cette activité, qu'en penses tu?  
et sinon of course à dispo pour donner des coups de mains sur le wiki selon
tes besoins!



#  rencontre électronique

Hyacinthe Lacenne posted this Jan 20, 2016 at 8:40 PM · 1 person applauded

hello,  
  
rencontre ce jour avec Jean-Christophe Billard. #pro.  
Sa boîte produit des devices connectés santé. Le produit phare est 1 ECG : ce
qu'ils font est remarquable, notamment en terme de miniaturisation
électronique  
  
il est intéressé par echopen dont il a entendu parlé non par Bertrand Duplat
mais par un autre de ses contacts  
  
il propose de nous accompagner sur  
  
\- la miniaturisation du device  
\- l'électronique FPGA, via 12c ingé, dont il estime qu'il est "génial" sic  
\- la mise au format kit, dont il pense que c non trivial  
  
parce que  
  
\- souhaite se positionner sur l'échographie car le use-case de l'ECG est
surtout les épreuves diagnostics de stress cardiaque qui en pratique  sont
souvent couplées d'échographie, dite "de stress"  
\- souhaite se positionner sur l'open source -&gt; recherche d'output comm.  
  
ce sera une contribution dont il reste à définir les termes, il y aura un
résiduel presta selon la quantité de travail  
  
btw, à terme il voudrait être incuber dans un environnement hospitalier,
l'Hôtel Dieu pouvant être d'intérêt ;)  
  
Au total :  
 je vous propose de monter en fin de semaine pro une réu #immersion  
pour lui exposer les avancements des différents pipes électroniques  
\- cartes actuels  
\- le presta US  
\- brief du travail de Philippe  
  
et on discuterait alors des termes opérationnels de sa contribution  
  
cette réu concerne les évolutions électroniques d'après février.

### **Hyacinthe** - Jan 21, 2016 at 6:59 AM

Top, @all si on pouvait profiter de ce temps pour caler l'ensemble des autres
éléments d'après février cela serait bien.  
  
Je propose donc une réunion en deux temps. Avec comme livrable :  
La définition du developpement technologique d'après février et de lister
l'ensemble des besoins associés

### **Hyacinthe Lacenne** - Feb 21, 2016 at 3:15 PM

Re!  ![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  ,  ![Hyacinthe
LICCIONI, FPGA at echopen](./../../zz_assets/images/avatars/1249124.png)
Hyacinthe  ,  ![Hyacinthe KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe   - pour ce qui
est de la discussion de vendredi sur la partie HV, deux solutions à proposer:  
\- Jatin Sharma et sa version sonar marin :
<https://www.duo.uio.no/handle/10852/47813> . Il passe de 12V à 180V, circuit
basé sur un [MAX1771](https://www.maximintegrated.com/en/products/power
/switching-regulators/MAX1771.html), et les gerbers et schematics sont dans sa
thèse de master. Ca vaut peut etre le coup de faire un board proprette comme
ca pour echopen, un HV supply séparé (pour appuyer la modularisation du design
;) ).  
\- Murgen: utilisation d'un [R05-100B](http://www.mouser.fr/ProductDetail
/RECOM-Power/R05-100B/?qs=3sBZtWOgbifm1JY3UuaavA%3D%3D) - plus simple (5V
-&gt; 120V).  Le cablage revient à 3 condos à voir donc.  
Ce n'est plus un circuit home-made, mais ca peut peut etre débloquer cette
histoire de bruit? A voir en tout cas =)

### **Hyacinthe VINCENT,** - Feb 22, 2016 at 8:58 AM

> un HV supply séparé (pour appuyer la modularisation du design ;) )

  
Je plussoie complètement ! On definit un format de "carte mère" qui ne
contient que des barettes de connecteurs. On subdivise celle-ci en carrés (2x3
carrés par exemple) et on essaye de faire des modules de 1, 2, 3 carrés en
surfaces. Un peu comme [**Modules "Click
Board™"**](http://www.lextronic.fr/C68-modules-click-board.html) mais en plus
simple. On design les modules individuellement, on maquette l'intégration sur
bread-board et on produit, à la fin, le PCB de la carte mère qui ne fait que
de l'interconnexion entre les connecteurs. On pourra avoir plusieurs cartes
mères en mezzanine. On pourra aussi blinder un seul module ou toute une carte.

### **Hyacinthe Lacenne** - Feb 22, 2016 at 9:04 AM

Et tu peux intégrer des choses comme un raspberry sur la carte mère, avec
cette version du compute module :  
<https://www.raspberrypi.org/blog/raspberry-pi-compute-module-new-product/> ;)

### **Hyacinthe VINCENT,** - Feb 22, 2016 at 9:21 AM

Moi je pensais les modules à plat mais en épis ... why not ? C'est plus
compact, c'est sur, mais peut-être moins universel, et compatible avec tous
les breakout qu'on trouve (comme l'espruino, le driver de pas-à-pas, les
régulateurs ...) aujourd'hui on trouve presque tout sous ce format avec des
picos à souder en option.  
Y a des gens qui étaient partis dans cette direction :
<https://www.gumstix.com/>.

### **Hyacinthe Lacenne** - Feb 22, 2016 at 9:45 PM

Ensuite, j'aime bien aussi le mode pins (breadboard compatible) - ca permet de
modulariser encore plus facilement !!  
Par exemple, une carte type murgen pourrait s'interfacer assez facilement avec
une xula2, hein  ![Hyacinthe KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe   =)



#  What's new

Hyacinthe posted this Jan 13, 2016 at 4:43 PM · 4 people applauded

Hey hey tout le monde.  
  
On vient de tester le circuit analogique (pulse à environ -60V + T/R switch)
et on arrive maintenant à voir un echo venant d'une partie du corps humain (en
occurrence ma main) :  

[

![](bc3-raw/files/789676-tek0002.JPG)

](bc3-raw/files/789676-tek0002.JPG)

[ TEK0002.JPG  165 KB • Download
](bc3-raw/files/789676-tek0002.JPG)

  
Ca demande encore du travail, mais c'est déjà une bonne avancée :)

### **Hyacinthe Lacenne** - Jan 13, 2016 at 4:45 PM

Top top top !

### **hyacinthe,** - Jan 13, 2016 at 4:47 PM

Sweet !!!!  
Moyenne sur X signaux ou sur une acquisition unique?

### **Hyacinthe** - Jan 13, 2016 at 4:50 PM

Bravo ;) Impatient de voir ça...

### **Hyacinthe,** - Jan 13, 2016 at 4:51 PM

On ne fait pas de moyenne ici

### **hyacinthe,** - Jan 13, 2016 at 4:53 PM

Ça gère !! Écho sur l'autre côté de ta main? Ou rebond sur ta main dans l'eau
?

### **Hyacinthe,** - Jan 13, 2016 at 4:56 PM

La main est dans l'eau, il faudrait zoomer pour en savoir un peu plus. Quid de
la peau ou d'un os qui donne un echo? Je pencherai plus pour un os

### **hyacinthe,** - Jan 13, 2016 at 5:17 PM

En zoomant c'est vrai qu'il y a plusieurs échos qui semblent apparaître!  
Ça vaudrait le coup de chopper abextla pitaya Xx échantillons sans la main
pour avoir la baseline, moyennee, et qques échantillons avec la main, pour en
retirer la baseline et voir ce qu'introduit ta main en termes d'échos? A-mode
rocks ;)



#  Traitement signal et image

Hyacinthe Lacenne posted this Jun 02, 2016 at 2:15 PM · 1 person applauded

la team Traitement d'Image est UP  
  
il s'agit de  ![Soobash, Feature extractor at
echopen](./../../zz_assets/images/avatars/4399577.png) Soobash  ![Zahra
Barwane, Image Cleaner at
echopen](./../../zz_assets/images/avatars/4179741.png) Zahra  (étudiante ISEP)  
  
ils travailleront sur l'interface cloud9  
  
les premiers steps identifiés par soobash sont :  
  
\- débruitage sur image en coordonnées polaires, i.e. avant scan conversion
pour que le denoising soit le plus efficace possible : sur images échos +
images de synthèse  
  
\- mesure des KPIs et stress test des soumissions d'algo  
  
\- utilisation de fantomes en situation réelle  
  
\- passage à GPU  
  
great ;) !

### **Hyacinthe Lacenne** - Jun 07, 2016 at 4:40 PM

demain réu hebdo de la team "traitement d'images"/denoising  
  
au programme -  
  
**définition du workflow  sur Cloud9**  
  
\- formalisation des espaces utilisateurs : règle de gestion users,
permissions, contrôle de source  
  
\- validation des soumissions  
  
**algo / denoising**   
  
\- règle de création d'images  
  
\- test des premiers algo sur images scan-convertées

### **Hyacinthe Lacenne** - Jun 14, 2016 at 1:58 PM

soobash produit ses premiers filtres de denoising  
  
le process de soumission est [ici](https://github.com/echopen/kit-
soft/tree/master/Cloud9Tools/scanconversion)  
  
une entrée wiki pour l'image processing est créée

### **Hyacinthe Lacenne** - Jun 14, 2016 at 7:43 PM

Nickel! Suite à nos échanges sur le format de l'image (dont les specs sont
r[ésumées ici](https://github.com/hyacinthe124/murgen-dev-
kit/blob/master/software/examples_csv/ReadMe.md) \-- on les valide une bonne
fois pour toute pour le stockage des données, good pour toi  ![lacenne
hyacinthe, echopen](./../../zz_assets/images/avatars/782178.png) lacenne   ?),
des images sont [sorties au bon format CSV et prêtes à être exploitées sur ce
repo](https://github.com/hyacinthe124/murgen-dev-
kit/tree/master/software/examples_csv).  
A noter, le filereader.py devra etre ajusté, et le hyacinthes.py as well,
puisque ces données sont caractéristiques de chaque CSV.

### **Hyacinthe Lacenne** - Jun 16, 2016 at 9:29 AM

oui, on est ok c validé. je fais l'update asap. dans les nouveaux jeux de
données, tu as ajouté les meta-data ?  
  
btw, c koi le process précis pour les pull requests, parce que ca me paraît un
peu long

### **Hyacinthe Lacenne** - Jun 16, 2016 at 9:33 AM

bwt, peux-tu updater, par une bannière d'info indiqant notre choix, la page
wiki du challenge format :
<http://echopen.org/index.php/Challenge:_Data_format>  
  
@+

### **Hyacinthe VINCENT,** - Jun 16, 2016 at 9:47 AM

Je débarque un peu tard, mais si j'ai bien compris, c'est du CSV avec les
meta-données à la fin ? Pas très classique, sachant que les meta-données
pourraient conditionner la lecture des données (nombre de lignes, cadrage des
valeurs, unités, dimensionnement de tableau...) , cela oblige à lire le
fichier en deux passes : une pour trouver les meta à la fin et une autre pour
lire, pré-traiter et stocker les  données.

### **Hyacinthe Lacenne** - Jun 16, 2016 at 10:53 AM

@hyacinthe : indeed, dans le dossier examples_csv, tu as les data au nouveau
format, et bzippées. ( <https://github.com/hyacinthe124/murgen-dev-
kit/tree/master/software/examples_csv> ) -- avec un preview des raw data en
PNG, classés par timestamp.  
  
@bivi: oui et non, en une passe de fichier, lecture ligne à ligne, tu peux
structurer ton jeu de données quand tu construis ton reader. Dans tous les
cas, tu dois lire ttes les données, avant de pouvoir tout processer. C'est
vrai que les méta en tete du fichier sont plus classiques (exemple du DICOM)
mais l'un dans l'autre on n'est pas sur des fichiers monstrueux, et quand on
voudra finaliser ca dans un format de distribution on pourra tout encapsuler
en DICOM classique.  
  
@hyacinthe: page challenge et banniere modifiées

### **Hyacinthe VINCENT,** - Jun 16, 2016 at 11:14 AM

Bon, prenons le sujet dans l'autre sens ;-) : quel est l'intérêt d'avoir les
données en premier ?

### **Hyacinthe Lacenne** - Jun 16, 2016 at 3:35 PM

ok  ![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe
: j'ai updaté aussi cette page

### **Soobash,** - Jun 16, 2016 at 7:09 PM

Salut  
Je reviens de lyon. Ba voir la levture du. data demain.

### **Hyacinthe VINCENT,** - Jun 27, 2016 at 2:56 PM

**DICOM server for medical imaging** : [Orthanc](http://www.orthanc-server.com/index.php)**  
**

### **Hyacinthe Lacenne** - Jun 27, 2016 at 3:01 PM

Indeed: on avait eu un premier contact (non seulement à travers l'article de
Medor) mais aussi plus direct, avec une idée sur le format des données :
<http://www.echopen.org/index.php/Challenge:_Data_format#Need_to_make_it_compatible_with_DICOM>
(c'est le fondateur d'orthanc qui écrivait ca =) ).

### **Hyacinthe VINCENT,** - Jun 27, 2016 at 3:06 PM

Ils viennent de sortir une nvlle version :
<https://twitter.com/sjodogne/status/747412280682287104>

### **Hyacinthe Lacenne** - Jul 01, 2016 at 9:41 AM

Hello, la team trouve son rythme de croisière hebdo -&gt; le mercredi fin d'am  
  
Benjamin Schannes, doctorant en stat/machine learning, X et amateur de
débruitage nous a rejoint

### **Hyacinthe Lacenne** - Jul 01, 2016 at 9:44 AM

Sweet! Y'a un canal de communication sur le sujet?

### **Hyacinthe Lacenne** - Jul 07, 2016 at 5:00 PM

réu hebdo :  
  
la méthode de contribution est calée

  

les métriques d’appréciation des performance du débruitage trouvée  
<https://drive.google.com/open?id=0B0V8htWBLPWBbml5WEZDVXRRd2s>

  

zahra travaille pour la semaine pro. à un script de validation des soumissions
: input vs. output selon ses métriques

  

soobash a fait un premier algo de débruitage : plus adapté à du débruitage sur
screen shot plutôt qu’en temps réel. Ceci étant le code agit localement sur
des fenêtres de pixels, et pourraient passer sous GPU

  

@me README

### **Hyacinthe Lacenne** - Jul 07, 2016 at 6:00 PM

Si vous voulez vous faire la main sur un signal normalisé acquis a tres haute
vitesse, d'un fantome simple, n'hésitez pas à vous faire la main, c'est sur
<https://github.com/hyacinthe124/murgen-dev-
kit/blob/master/worklog/Zach/2016-07-06.md> =)  
  
Attention, il s'agit des données brutes, donc vous pouvez aussi simuler le
detecteur d'enveloppe avec un Hilbert.  
  
Have fun!

### **Hyacinthe Lacenne** - Jul 21, 2016 at 11:28 AM

réu hebdo hier  
  
\- synthèse de revue de la littérature  
\- relecture du code de zhara pour script de validation, analyse des
soumissions  
\- présentation par benjamin shannes des principales métriques de signal-bruit  
\- script de testing de toutes les métriques pour la semaine prochaine par
![Soobash, Feature extractor at
echopen](./../../zz_assets/images/avatars/4399577.png) Soobash   et  ![Zahra
Barwane, Image Cleaner at
echopen](./../../zz_assets/images/avatars/4179741.png) Zahra  
  
de l'avis de benjamin et  ![Soobash, Feature extractor at
echopen](./../../zz_assets/images/avatars/4399577.png) Soobash   : on devrait
garder des métriques classiques et en déduire métrique qui nous sera propre ,
sur la base de quoi  ![Soobash, Feature extractor at
echopen](./../../zz_assets/images/avatars/4399577.png) Soobash  propose une
publication

### **Hyacinthe Lacenne** - Aug 03, 2016 at 5:06 PM

réu hebdo  
  
\- update des packages installés sur README.md  
\- avancement sur calcul des métriques  
\- récupération de l'ouvrage "Despeckle Filtering for Ultrasound Imaging and
Video"

### **Hyacinthe Lacenne** - Aug 13, 2016 at 2:30 PM

Séance hebdo du 10.08.16

  

\- l’équipage est en vacances et échange d’ordre général avec Benjamin

\-  ![Soobash, Feature extractor at
echopen](./../../zz_assets/images/avatars/4399577.png) Soobash  livre les
scripts de calcul des métriques ces tous prochains jours

\- nous sommes rejoint dans la team par Loic, aka hackolite, spécialiste de
python

  

Loic va travailler à l’implémentation des contributions sur la plate-forme
collaborative, dont voici le workflow

  

1) setup de l’espace de travail conformément au
[README](https://github.com/echopen/kit-soft/tree/master/ImageProcessing)

2) dump du dossier input

3) mis au point de l'algo

4) la fonction main() analyse la soumission en rapportant l’input à l’output
selon les métriques définies (cf. séance du 03.08.16),

5) update du leaderboard sur la plate-forme online de récupération de data

  

Loic va travailler au point 4 et 5, avec  ![Zahra Barwane, Image Cleaner at
echopen](./../../zz_assets/images/avatars/4179741.png) Zahra

  

  

Btw, pour les deux prochaine semaines, trêve estivale !

### **Hyacinthe Lacenne** - Aug 18, 2016 at 3:21 PM

hello,  
  
Loic a soumis un pull request en cours de reviewing : il s'agit de la routine
qui permet de valider une soumission, de comparer input et output.  
  
**Next steps**  
  
\- validation des scripts définissant les qaulity metrics d'un processing  
\- connection avec le leaderboard  
\- lancement appel à contribution

### **Hyacinthe Lacenne** - Sep 08, 2016 at 10:15 AM

réunion du 08.09.2106  
  
sortie des premiers scripts et métriques. pour les spécialistes, il s'agit
calcul  de mse, rmse, ssim  
  
en cours pour la semaine prochaine  
  
\- loic commence à updater la boucle de soumission en ajoutant le calcul des
précédentes métriques dans son workflow  
\- soobash finit les scripts relatifs aux calculs de 6 métriques
complémentaires  
\- benjamin fait une review de "Despeckle filtering for ultrasound imaging and
video, Vol. I: Algorithms and software" , notamment pour explorer les
techniques statistiques à l'usage en débruitage

### **Hyacinthe Lacenne** - Oct 05, 2016 at 9:07 PM

réunion du 05.10.16 : review de l'archi de contribution  
  
\- soobash continue de scripter les métriques, mais on en a l'essentiel  
  
\- loic a packagé le script de récupération des algo et d'extraction des
métriques selon les scripts de soobash  
  
\- l'arcghitecture pour le contributeur évolue dans le sens suivant  
  
\- &gt; l'espace ide collaboratif (cloud9) permet d'exposer et de jouer avec
les codes des contributeurs et leurs libs  
-&gt; une interface web/python notebook : avec un "how to" pour package un algo python et qui permet de le soumettre. Le contributeur fait le choix de son environnement de dev et garde ainsi toutes ses routines  
-&gt; nous processons le package, extrayons les métriques et updatons le leaderboard  
  
Au total, on est prêt dans 2 ou 3 semaines.  
  
le bottle neck est la mise en route de l'acquisition dans l'acquarium,
idéalement avec fantômes (rdv à ce sujet dans 2 semaines avec medicalem pour
livraison d'un fantôme carotidien).  
  
Dès que c bon, on prépare et lance un challenge autour du denoising : appel à
compétences et mise en compétition P6, MIT ?

### **Hyacinthe Lacenne** - Oct 10, 2016 at 3:38 PM

hello,  
  
Nous comptons 1 nouveau membre  dans le groupe Image Processing

  

Nourredine Ellouz est chercheur en traitement du signal, tout jeune retraité,
qui a dirigé un laboratoire d'une centaine de chercheurs en Tunisie et qui se
proposent de piper de nouvelles ressources, notamment ses étudiants, pour
notre groupe.  
  
De plus, il n'a pas fait d'elec depuis un moment mais se pique d'en refaire  
  
Et le plus fou, c'est que, lorsqu'on lui a parlé de l'ENS, on a évoqué Gérard
et il se trouve qu'ils se connaissent !!! ils ont travailmé ensemble dans les
années 90'.  
#P'tiMonde

  

Btw, à la prochaine séance, Djalel sera des nôtres car il souhaite se
familiariser avec notre approche, songeant à des approches "réseaux de
neurones" pour le débruitage, l'idée étant de maintenir une articulation entre
le groupe Image Processing et le groupe IA

### **Hyacinthe Lacenne** - Oct 13, 2016 at 7:17 AM

réu 12.10.16  
  
Nourredine Ellouze, ancien dir. de recherche en traitement du signal, avec une
focale sur le denoising + ingénieur électrique + plein de choses, rejoint
notre groupe ;)

  

Les next steps évoqués sont en parallèle :

  

1) Plate-forme web

achever la plate-forme d'upload/extraction des métriques des algorithmes de
débruitage + branchement de la sonde dans l'acquarium

  

2) Challenge

monter un challenge à partir de datasets, soit existant &amp; accessibles via
un récent challenge de Kaggle, soit à partir des data d'echOpen

  

3) Algo

\- quel spécificité du bruit échographique ? savoir reproduire
artificiellement le bruit pour les injecter dans les images -&gt; priorité de
la semaine qui vient

\- les reverse engeneerer par réseaux de neurones. A ce titre, Djalel,
animateur du groupe IA d'echOpen était présent, car important de maintenir une
articulation entre le groupe Image processing et le groupe IA et a donné
des pistes de travail : débruitage, compression du signal  
  
au plan pratique, les membres du groupe choisissent de se retrouver tous les
jeudis à compter du 27.10.16. Mais semaine pro, la réu a bien lieu un
mercredi, soit le 19.10.16  
  
oilà !

### **Hyacinthe Lacenne** - Oct 20, 2016 at 7:11 AM

réu 19.10.16  
  
1) discussion du challenge online qui sera lancé dès que tout est prêt  
  
2) interface web, django app, de récupération, d'analyse des soumissions et de
leaderboard achevée thanks @loic;)  
@todo :  analyse non d'une image mais d'une boucle d'images + système de login  
  
3) scripts de métriques des soumissions terminés thanks  ![Soobash, Feature
extractor at echopen](./../../zz_assets/images/avatars/4399577.png) Soobash ;)  
@todo constituer les métriques qui nous sont propres  
  
4) demeure la question de l'analyse de la typologie de bruit en vue de pouvoir
l'injecter à des "images saines" à des fins d'apprentissage.  
C @benjamin qui s'y colle pour la semaine pro thanks;)  
  
oilà !

### **Hyacinthe Lacenne** - Oct 27, 2016 at 11:49 PM

réu 27.10.16  
  
1) proposition par  ![Soobash, Feature extractor at
echopen](./../../zz_assets/images/avatars/4399577.png) Soobash  d'un score
pour le ranking du leaderboard + discussion sur l'adaptation des métriques de
frames d'images  
  
2) évolution de l'interface leaderboard par @hackolite @todo : adaptation de
l'algo pour calculer les métriques sur une séquence image, plutôt qu'une image
tel que c'est le cas aujourd'hui  
  
3) présentation par @benjamin d'une méthode d'injection sur images de bruit
spécifique à l'écho. @todo : implémentation d'un premier réseau de neurones
pour débruiter des images;)  
  
nota bene : les réu se tiennent maintenant tous les jeudis !  
  
oilà;)

### **Hyacinthe Lacenne** - Nov 10, 2016 at 7:41 PM

CR Meeting 10.11.16 ca se passe à présent
[ICI](https://docs.google.com/document/d/1kn_oJnskOg4OONO4MK5Ft724OLPkn4NYzj-
qJHVMMXo/edit#heading=h.os8lqi1nhxyh) !  
  
annonce d'1 nouvel arrivant dans la team Signal Processing : Mohamed Mahdi,
polytechnicien de tunis, en ce moment à l’école des Mines, spécialité
Robotique &amp; Traitement du Signal



#  Visuels Echopen Archived

Hyacinthe posted this Mar 17, 2016 at 10:43 AM · 1 person applauded

Bonjour à tous,  
  
Nous venons de recevoir les visuels de Barbara ;)  
  
Les voici ci-dessous. **Merci de ne pas encore les diffuser sur les réseaux
sociaux**, nous allons le faire dès le début de la semaine prochaine,
progressivement, pour mobiliser la communauté pour le 24 mars ;)  
  
A bientôt,  
  
O.  
  

[

![](bc3-raw/files/2647132-echopen-1.png)

](bc3-raw/files/2647132-echopen-1.png)

[ echopen-1.png  107 KB • Download
](bc3-raw/files/2647132-echopen-1.png)

[

![](bc3-raw/files/2647134-echopen-2.png)

](bc3-raw/files/2647134-echopen-2.png)

[ echopen-2.png  77.2 KB • Download
](bc3-raw/files/2647134-echopen-2.png)

[

![](bc3-raw/files/2647136-echopen-3.png)

](bc3-raw/files/2647136-echopen-3.png)

[ echopen-3.png  74.2 KB • Download
](bc3-raw/files/2647136-echopen-3.png)

[

![](bc3-raw/files/2647137-echopen-4.png)

](bc3-raw/files/2647137-echopen-4.png)

[ echopen-4.png  49.3 KB • Download
](bc3-raw/files/2647137-echopen-4.png)

[

![](bc3-raw/files/2647140-echopen-5.png)

](bc3-raw/files/2647140-echopen-5.png)

[ echopen-5.png  45.2 KB • Download
](bc3-raw/files/2647140-echopen-5.png)

### **Hyacinthe Lacenne** - Mar 17, 2016 at 1:23 PM

Ça claque !!!

### **Hyacinthe VINCENT,** - Mar 17, 2016 at 2:10 PM

Sympa, pas trop sérieux. Et au fait si on faisait une petite faute en
remplaçant ecosystem par echOsystem ;-).

### **Emilie Mayer,** - Mar 19, 2016 at 3:08 AM

Cool! J'aurais cependant quelques remarques (surtout sur la première), s'il
n'est pas trop tard:  
1-L'accent n'est pas assez mis sur les urgences, je trouve ça dommage car
c'est un point clé, pourquoi pas : "less overcroad emergency rooms"? qu'en
pensez vous?  
2- Le "Less need for precise and expressive ultrasound technologies" (erreur :
expensive plutot non? ) Est ce vraiment le message que l'on veut faire passer?
Pour moi ce serait plutôt : économies de temps et d'argent. Et plutot que
quelque chose de negatif : "less need" on pourrait mettre du positif "improved
use of" , c'est à dire amélioration de l'utilisation vers les personnes qui en
ont vraiment besoin.  
3- L'histoire de la télémédecine : a -t-on raison de mettre l'accent dessus,
on en a pas vraiment parlé si?  L'idée n'est pas forcément de remplacer le
médecin encore mais plus qu'il se déplace avec l'echostéthoscope? et le "half
day training est plutôt un two-day training non?  
4- Il n'y a pas la notion de kit, et de délocalisation du projet, avec la
possibilité de multi labos ou labo multi sites.  
5-Enfin ici on parle de diagnostique alors qu'on a toujours parlé "d'aide au
diagnostique", pas grave?  
  
En tout cas c'est très cool! Mais je pense qu'il faut faire très attention au
message qu'on envoie et faire valider par Hyacinthe pour être sur qu'il n'y a pas
d’ambiguïtés là où on ne le voudrait pas.

### **Hyacinthe** - Mar 20, 2016 at 10:13 AM

Merci  ![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  pour tes
remarques. je les ai fait passer. J'ettends leur retour pour savoir s'il est
encore temps.  
  
Concernant ton point 3. Pour les pro de santé (hors médecins) il s'agit d'une
demi-journée de formation, puisque c'est une formation au geste et non à la
lecture, d'où la télémédecine qui permet ensuite d'envoyer les images aux
médecins qui pourront alors donner leurs avis. C'est d'ailleurs le modèle
principale de l'utilisation des échographes portables dans les pays émérgents.  
  
En ce qui concerne la notion de kit, comme elle n'est as encore très claire,
nous pourrons voir cela dans un second temps.  
  
Enfin, en effet, c'est plutôt une aide au diag. Je leur envoi l'information.  
  
Merci.  
  
A demain,

### **Hyacinthe Lacenne** - Mar 21, 2016 at 8:31 AM

Yop,  
  
Je plussoie Emilie, la télémedecine n'est pas du tout dans le top use en pays
émergents: cf la méta-analyse des usages:  
<http://onlinelibrary.wiley.com/doi/10.1111/tmi.12657/pdf> \- a clarifier
donc.  
  
D'autre part, +1 pour le kit. Ce week end, on a eu les premieres images avec
un kit utilisable 100% à la maison, pas besoin de labo pour tirer de superbes
images =) Et a dispo pour argumenter ça.  
  
Bon début de semaine!  
  
Hyacinthe

### **Hyacinthe** - Mar 21, 2016 at 9:13 AM

Merci  ![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png)
Hyacinthe  pour ton retour.  
  
Concernant le télé-médecine, deux raisons nous pousse à la mettre en avant.
Sachant qu’elle se définie (selon les ARS) comme **une forme de pratique
médicale à distance utilisant les technologies de l’information et de la
communication.** Elle met en rapport, […] plusieurs professionnels de santé,
parmi lesquels figure nécessairement un professionnel médical et, le cas
échéant, d’autres professionnels apportant leurs soins au patient.



  1. La sonde étant connectée à un smartphone (lui même connecté à internet), à la différence des dispositifs évoqué dans la méta-analyse des usages centrée sur « the use of hand-carried and hand-held ultrasound devices in low- and middle-income countries », elle permet la transmission des images depuis un infirmier dans une maison de santé reculée, par exemple, vers un médecin pour un avis sur la prise en charge. C’est d’ailleurs l’une des preuves de concept de l’étude menée par Qualcomm et Trice Imaging (<http://technomag.ma/?p=11775>). C’est aussi l’un des points essentiels évoqué par Hyacinthe B. Notamment dans le cas des urgences ou le samu fait son echo sur le lieu d'un accident et envoi l'image aux médecins restés à l'hopital pour une prise en charge plus rapide à l'arrivée de l'ambulance, etc. 
  2. N’oublions pas ensuite, que nous sommes sur des visuels dont l’ambition est de communiquer, de convaincre et de mobiliser de nouveaux contributeurs, ce qui nous amène a prendre les cas d’usages les plus facilement compréhensibles, d’où ces choix.

  

Enfin, concernant le kit, je leur ai fait la demande et j’attends leur retour,
ils regardent ça aujorud'hui. J'espère qu'ils pourront ajuster rapidement pour
que nous soyons prêts jeudi. Si besoin,  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  je te mets en
contact s'ils ont des quesitons sur le kit.  
  
A dispo,  
  
Bonne journée.



#  Onboarding JC Billard - électronique

Hyacinthe Lacenne posted this Jan 22, 2016 at 10:02 AM

Oyé,  
  
JC propose un rdv ce lundi en début d'am  
  
l'idée est de présenter à lui et aux ingé de bitmakers  
  
\- un point d'étape et autres éléments de contexte  
\- les choix électroniques et leurs motivations pour les end-points de février
et de Juin  
  
l'idée serait qu'on sorte avec un embryon de structuration de l'accompagnement
d'ici à juin sur 3 sujets :  
  
\- FPGA  
\- miniaturisation  
\- dev d'1 kit  
  
@++



#  comm. Archived

Hyacinthe Lacenne posted this Jan 18, 2016 at 9:15 AM

j'ai participé à un hackathon ce we, et dans la salle des participants ont
interpellé les organisateurs à propos d'echopen, ce qui est rigolo ;)  
  
btw, j'ai croisé Hubert Guillaud de la Fing qui suit ce que l'on fait avec
intérêt. En revanche, il nous fait remarquer que depuis le wiki, on ne voit
pas les évolutions et du coup, on aurait parfois l'impression que le projet
n'avance pas  
  
-&gt; odj ce soir : ajouter un plug-in qui fait état des modifs du site ?  
-&gt; updater la home à la main et plus régulièrement (à chaque modification qui s'y prête)  
  
@++

### **hyacinthe,** - Jan 18, 2016 at 10:04 AM

Type flux rss pour les maj ?  
Sinon, pour la comm au quotidien, rien ne vaut un blog.. Mais il faut du temps
pour l'animer :)

### **Hyacinthe Lacenne** - Jan 18, 2016 at 10:20 AM

ok flux RSS serait en effet bien



#  echopenIA

Hyacinthe Lacenne posted this Apr 11, 2016 at 3:58 PM

un thread sur les aspects IA d'echopen

### **Hyacinthe Lacenne** - Apr 11, 2016 at 3:58 PM

Djalel Benbouzid, docteur en ML orienté plutôt res. de neurones,  est Ok pour
nous accompagner et organiser un working group sur le sujet.  
  
je viens de récupérer via l'hosto des datasets echo issus du challenge
[CLUST](http://clust.ethz.ch/)

### **hyacinthe,** - Apr 11, 2016 at 4:11 PM

Ça serait marrant de faire de la détection de billes de tapioca :

### **Hyacinthe Lacenne** - Apr 11, 2016 at 4:26 PM

Oui oui on peut ;) et avec un phantom (avec des tapiocas) c est top !

### **Emilie Mayer,** - Apr 11, 2016 at 4:46 PM

Il est sur le baseccamp?

### **Hyacinthe Lacenne** - Apr 11, 2016 at 4:49 PM

Y'a de quoi faire, on a une 30aine d'images prêtes à être exploitées :)

### **Emilie Mayer,** - Apr 11, 2016 at 5:33 PM

Je veux dire : Djalel est-il sur le basecamp?

### **Hyacinthe Lacenne** - Apr 11, 2016 at 6:07 PM

![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  je vais lui
demander demain  
  
![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  le
truc cqu'il faut bcp bcp de data pour entraîner les réseuax de neurones mais
on en parle ;)

### **hyacinthe,** - Apr 11, 2016 at 10:49 PM

Hum style une 30aîné d'images c'est pas assez... ;)

### **Hyacinthe Lacenne** - Jun 09, 2016 at 4:26 PM

hello, je sors d'une visite avec Antoine Tesnières, resp.
d'[ilumens](http://www.ilumens.fr), une sorte service médicale totalement
simulée avec tous le matos : echo, endoscopie, salle de réa, mater,... #dément  
  
on a un gros point de concours : la data échographique simulée. On se propose
d' installer un working group commun. L'idée étant pour eux de générer
aléatoirement des cas échographiques et pour nous de commencer l'apprentissage
des data  
  
autre sujet : ils ont des fantômes virtuels et réels et Antoine va essayer de
nous en trouver auprès de ses partenaires. Btw, sur ce sujet, je suis en
contact avec cirsinc, simulab, etc pour un prêt ou don. On devrait d'ailleurs
avoir une réponse rapide de simulab, vous tiens au courant

### **hyacinthe,** - Jun 11, 2016 at 11:30 PM

Au niveau de l'ia, en segmentation y'a des trucs funs récents:
<https://github.com/jocicmarko/ultrasound-nerve-segmentation>  
  
Plus sérieusement,  si une équipe sérieuse se monte, autant pour echopen
monter une team piur ce challenge kaggle et montrer de quoi on est capables ;)  
<https://www.kaggle.com/c/ultrasound-nerve-segmentation>

### **Hyacinthe Lacenne** - Jun 14, 2016 at 3:09 PM

ca aurait du sens, mais le temps que l'équipe se monte il sera le mois d'août
;)  
  
enfin à voir

### **Hyacinthe Lacenne** - Jun 14, 2016 at 3:18 PM

Damn!  
At least ca peut etre intéressant de regarder  
\- La gueule des data (2Go une fois compressées)  
\- Les solutions développées par d'autres  
\- Les outils utilisés  
\- La biblio qu'ils auront réalisé  
\- Trouver des gens intéressés par la thématique, qui pourraient rejoindre le
projet :)

### **Hyacinthe Lacenne** - Jun 14, 2016 at 3:19 PM

absolument

### **Hyacinthe Lacenne** - Jun 20, 2016 at 3:14 PM

je sais que l'info est quelque part, mais je ne la trouve pas. Quelles sont
donc les specs pour un fantôme ?  
  
De préférence, les specs pour un fantôme de formes géomtriques + un fantôme
médical, car il est possible qu'Antoine ait plus intérêt/latitude à se
procurer un fantôme médical  
  
@+

### **Hyacinthe Lacenne** - Jun 20, 2016 at 3:22 PM

Pas de specs à proprement parler dans notre cas, surtout un type de fantôme.
Pour nous, il s'agirait dans un premier temps d'avoir un fantôme à 15-20cm de
profondeur max, qui ressemblent à ça de l'extérieur :  
<http://www.meditron.ch/ultrasound-imaging/images/cirs/040gse_2.jpg>  
  
Qui donne des images comme ça: <http://www.supertechx-
ray.com/pics/Ultrasound/CIRS/CIRS-040GSE-Ultrasound.jpg>  
  
Ça peut être des fantomes de test, d'étalonnage, ou de calibration ça dépend
des fabricants, ou des specs fines. Mais l'idée générale est la.

### **Hyacinthe Lacenne** - Jun 21, 2016 at 12:27 PM

En parlant de datasets d'images echo, je viens de tomber sur publi assez cool
"Ultrasound Image Dataset for Image Analysis Algorithms Evaluation" , plus une
spécialisée sur la thyroide "An open access thyroid ultrasound image
database". Peut etre pas mal pour se lancer dans les datasets =)

### **hyacinthe,** - Jun 24, 2016 at 3:34 PM

Tjrs IA, il y avait deux projets IA au CRI, dont un parlait des data kaggle :)  
Vu la rapidité avec laquelle ils se sont emparés des data, ça pourrait
clairement faire le sujet d'un Hackaton :)

### **Hyacinthe Lacenne** - Jun 30, 2016 at 11:55 AM

du hardware learning: <http://www.nextplatform.com/2016/06/29/universal-fpga-
gpu-platform-deep-learning/>

### **Hyacinthe Lacenne** - Jun 30, 2016 at 2:21 PM

C'est vraiment à la mode!  
Deep Learning in Medical Imaging: Overview and Future Promise of an Exciting
New Technique --
[http://ieeexplore.ieee.org/stamp/stamp.jsp?reload=true&amp;arnumber=7463094](http://ieeexplore.ieee.org/stamp/stamp.jsp?reload=true&arnumber=7463094)  
  
Ca parle aussi de Kaggle :  
\- detection and staging of diabetic retinopathy : <https://www.kaggle.com/c
/diabetic-retinopathy-detection> (100k$ de prizes)  
\- Second medical image analysis competition was completed using MRI to
measure cardiac volumes and derive ejection fractions :
<https://www.kaggle.com/c/second-annual-data-science-bowl> (200k)  
  
Toute petite mention de l'ultrasons : "For a large dataset of 2891 cardiac
ultrasound examinations, Ghesu et al. [20] combine deep learning and marginal
space learning for object detection and segmentation. The combination of
“efficient exploration of large parameter spaces” and a method to enforce
sparsity in the deep networks, increased computational efficiency, and led to
a 13.5% reduction in mean segmentation error compared to a reference method
published by the same group."  
  
@lacenne : je poste ici, en attendant qu'il y ai un canal dédié pour le
groupe de reflexion / groupe de lecture proposé par Djalel, tu fais signe pour
les prochaines avancees / réunions de ce groupe ?

### **Hyacinthe Lacenne** - Jul 01, 2016 at 9:53 AM

premier meet-up avec Djalel :  
  
prez de Elsa Angelini, spé traitment du signal ultra-sons à l'Imperial College  
  
au total :  
  
au plan technique : conseil de faire le ML sur raw data, conseil de
récupération de phase, très riche en info  
  
au  plan logistique : installation d'un groupe de lecture et de veille sur
Deppe Learning (DL) + Imagerie Médicale.  
  
Première réunion : 3ème semaine d'août  
  
RoadMap :  
\- réunion bi-mensuelle du groupe de lecture : plusieurs personnes
intéressées, dont un des orga d'un des gros meet-up de ML (proposition de les
articuler avec les nôtres sis pertinent), et Tristan Cazenave, prof de DLà
Dauphine (orienté game, go...)  
\- lorsque la vision murie  
   organisation d'un meet-up  
   définition du cadre d'une typologie et des modalités pratiques récupération
de données  
   mise en place d'une infra de calcul  
   processing des data

### **Hyacinthe Lacenne** - Jul 05, 2016 at 12:41 PM

Tjrs dans la meme veine, plutot cool:  
<http://www.bbc.com/news/technology-36713308>

### **Hyacinthe Lacenne** - Oct 05, 2016 at 9:13 PM

prochain meetup prévu pour le vedredi 21.10.16  
  
rdv ce lundi avec le responsable du datalake de l'AP, on a toutes les infos
pour soumettre la demande détaillée des data : images + data cliniques.  
Calendrier putatif : soumission novembre, étude décembre, réponse janvier,
data en prod février/mars  
  
en parallèle : travail à l'appel à projet de l'Axa Research Fund. A la clé une
bourse pour un post-doc de 130K. Djalel souhaite candidater, ce qui est top.
La base de travail serait précisément le dataset de l'AP  
  
enfin : rdv avec la team AWS, pour accéder à de la puissance calcul, pour un
total de 10.000€  
  
oilà



#  Maintenance Contenus Echopen

hyacinthe posted this Feb 02, 2016 at 10:06 AM · 1 person applauded

**Récupération des données echopen sur plates-formes tierces   
**  
Petit recap sur l'accessibilité des données sur les services tiers - et la
faisabilité d'en extraire les données pour les mettre sur une archive, un
dump, explorable offline.  
  
**Wiki **: Export possible : par exemple<https://www.mediawiki.org/wiki/Help:Export/fr>  
**Basecamp**: <https://basecamp.com/help/2/guides/account/exports> - explorable en html  
**Github**: assez evident de chopper une archive -- clone des différents repos  
**Slack**:  
\- Dumper Slack: <https://get.slack.help/hc/en-us/articles/201658943
-Exporting-your-team-s-Slack-history>  
\- Formater Slack en explorable html :<https://levels.io/slack-export-to-
html/>  
  
**Twitter:** exportation facile :<https://support.twitter.com/articles/20170160?lang=en#>, explorable en html  
**  
Drive: **export... facile, oui ;)(j'en oublie?)  
On peut aussi imaginer un script qui scrap l'ensemble des archives pour
reformater l'ensemble sous la forme d'un "portail" au format web - doublé
d'une archive fichiers qui reprennent l'ensemble des fichiers drive, wiki,
basecamp -- ca donnerait un dump echopen à une date t. On peut se baser sur le
fait que les dumps de services sont, aujourd'hui, déjà exploitables tels quels
au format HTML.  
Hyacinthe a commencé à mettre les dumps (dont slack) sur le drive dans "0.1
MAINTENANCE" - j'y ajoute dump wiki, basecamp, et twitter pour ceux qui ont
envie d'explorer ca.  
Ping  ![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  @hyacinthe

### **Hyacinthe** - Feb 03, 2016 at 8:20 AM

![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  merci. Je pense
qu'on a tout en sauvegarde de contenu...  
  
Il reste peut-être le gitbook...  ![Hyacinthe Lacenne,
echopen](./../../zz_assets/images/avatars/782178.png) lacenne  ?  
  
Ensuite, je pense qu'il va falloir penser à une sauvegarde automatique des
éléments pour nous simplifier la vie et être certain que tout est bien safe ;)  
  
![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  si tu as des
idées de comment cela peut-être envisagé ? Je suis preneur.

### **hyacinthe,** - Feb 03, 2016 at 8:21 AM

Backupé - et rendu accessible dans un framework uniformise, ce serait cool!

### **Hyacinthe VINCENT,** - Feb 03, 2016 at 9:44 AM

Oui, je pense que dans l'ordre d'importance on a :

  1. S'assurer qu'on peut tout récupérer en local
  2. S'assurer qu'on peut tout relire/exploiter en local
  3. Migrer éventuellement vers des formats uniformes
  4. Avoir un outil de diffusion/navigation

  
On pourrait aussi avoir une approche inverse (un peu plus extremiste et
centralisée) :

  1. On définit un dépot unique (stockage et versionnement)
  2. On définit des formats uniformes et pérennes
  3. On produit/ajoute tout directement dans le dépot, à coups de commit et de lots cohérents.
  4. On utilise des outils de publication pour diffuser les différentes facettes du projet (administratif, comptable, technique, documentation, communication...)



#  GitHub

Hyacinthe Lacenne posted this Aug 17, 2016 at 8:07 AM

un thread temporaire pour restructurer, normaliser et nettoyer le repo GitHub

### **Hyacinthe Lacenne** - Aug 17, 2016 at 8:13 AM

voici qqs remarques  
  
2 repo me paraissent inutiles :  
  
image-builder  
EchoDocument  
  
le repo Hardware renvoie en premier sur Murgen et le lien est mort  
  
Il s'agirait d'harmoniser/merger -&gt;
[Prototype_software](https://github.com/echopen/Prototype_software),
[electronic](https://github.com/echopen/electronic), et la partie de kit-soft
qui est relative au hardware.  
  
des idées ?

### **Hyacinthe,** - Aug 17, 2016 at 8:19 AM

kit-soft est en grande partie voir totalement obselète. Je pensais également
faire une refonte des repos après avoir fini la doc. A méditer

### **Hyacinthe Lacenne** - Aug 17, 2016 at 8:27 AM

ok on peut d'ores et déjà supprimer EchoDocument sauf si objection
particulière  
  
par ailleurs, ce serait pas mal qu'on ait qqs règles de conventions de
nommage, je me lance  
  
\- langue utilisée : anglais  
\- le terme doit être explicite  
\- pas de majuscule sauf pour les gitbook de doc  
\- espace séparé par un “tiret du 6", selon la règle par défaut de création
des repo github  
  
A priori, on devrait disposer  
\- des repos Soft déclinés -&gt; app, image processing ...  
\- des repos Hard déclinés -&gt; mécanique, électronique...  
\- un repo de  ressources documentaires ? -&gt; 1 dossier twitter + 1 dossier
articles  
  
on discutera en bureau de la doc dont je vous proposerai qu'elle prenne la
forme de GitBook, selon la ventilation nom-de-repo/nom-de-repo-doc  
  
@compléter de vos doctes avis



#  Traduction wiki

Hyacinthe Lacenne posted this Feb 04, 2016 at 10:48 AM · 1 person applauded

deux traducteurs wiki fr-&gt;en se sont manifestés. ils vont commencer ce jour
. Il s'agit de Catherine Philips et Nicolas Etaix  
  
je leur ai proposé pour commencer  
  
_la page de home_

<http://echopen.org/>

  

_la page de FAQ_

  

<http://echopen.org/index.php?title=FAQ>

  

_le groupe de pages correspond à l'onglet Enjeux sur la home (avec trad des
ongles)_

<http://echopen.org/>  
  
@hyacinthe : tu devrais recevoir des demandes d'inscription  
  
@++

### **hyacinthe,** - Feb 04, 2016 at 11:05 AM

Sweet! Hyacinthe, le nom de Nicolas doit te rappeler qqchose :)  
Si y'a un problème quelquonque avec les droits de ces deux là pendant une
session hyacintheoffline , on est tous administrateurs donc on peut tous leur donner
les droits à priori.  
  
Et faut surtout leur demander de confirmer leur e-mail :)



#  events

Hyacinthe Lacenne posted this Oct 05, 2016 at 9:24 PM

Un thread pour les events

### **Hyacinthe Lacenne** - Oct 05, 2016 at 9:31 PM

echOpen est invité à participer à [Africa4Tech](https://africa4tech.org/) pour
un workshop dédié à la co-construction de l'app Android  
  
L'event aura lieu à Marrakech, le 02.11.16 et le 04.11.16 et est labellisé
Cop22  
  
Il y aura des devs front + back, avec me suis-je laissé entendre, des devs
high level, notamment des games developers  
  
l'idée est de faire, en amont d'HETIC, la partie intégration android + dev
algo sous GPU, et ce afin de se prémunir de la situation où l'on ne trouverait
pas le temps, pour décembre, d'intégrer la fournée de design d'HETIC

### **hyacinthe,** - Oct 07, 2016 at 10:51 AM

Un event où il serait clé qu'echopen participe, de par sa structure, et pour
se positionner :  
  
  
Le Domaine d’Activité Stratégique (DAS) « **Imagerie diagnostique et
interventionnelle** » du pôle de compétitivité **Medicen Paris Region**
organise en partenariat avec l’infrastructure nationale **France Life Imaging
(FLI)**, le **mardi 15 novembre 2016 **à l’Institut du Cerveau et de la Moelle
Epinière (Hôpital Pitié Salpêtrière, Paris),un colloque sur le thème : « **Les
ultrasons en France : innovations pour l’imagerie médicale et la thérapie en
2016 »**.  
  

Faisant suite au colloque organisé par FLI en novembre 2014, l’objectif de ce
colloque est de dresser un panorama des innovations académiques/cliniques et
industrielles des ultrasons pour l’imagerie diagnostique et interventionnelle.
Pour cela, un programme de communications invitées, complétées par des
sessions de pitchs réservés aux industriels d’une part, et aux
académiques/cliniques d’autre part, se succéderont pour présenter les
innovations du domaine des ultrasons. Medicen Paris Region lancera
prochainement un Appel à Manifestation d’Intérêt national auprès des autres
pôles de compétitivité nationaux, afin d’identifier les organismes
(académiques et industriels) ayant la volonté de venir présenter leurs
innovations lors de ces sessions de pitch

  
Les autres temps forts du colloque seront deux tables rondes : la première
traitera de la structuration d’une filière française des ultrasons, et la
deuxième abordera le passage de l’invention académique/clinique au marché.  
  

  
  
  

  
Ce colloque pourra être l’occasion d’annoncer la structuration de la filière
française des ultrasons médicaux.  
  

  
  
  

  
Le colloque sera animé par le journaliste scientifique Fabrice Papillon.  
  

  
  
  

  
Pour consulter le programme prévisionnel, répondre à l'Appel Manifestation
d'Intérêt ou encore vous inscrire **avant le vendredi 28 octobre, veuillez
consulter le lien suivant :**[**https://my.medicen.org/manifestations/27956/  
**](https://my.medicen.org/manifestations/27956/)

### **Hyacinthe Lacenne** - Nov 03, 2016 at 8:42 AM

Je viens d'être relancé pour le colloque du 15, si ca tente du monde ..  
<http://www.medicen.org/evenements/colloque-les-ultrasons-en-france-
innovations-pour-limagerie-medicale-et-la-therapie-en-2016/>



#  echopen wikipedia

Hyacinthe Lacenne posted this Jan 14, 2016 at 10:02 AM

hello tous, juste un clin d'oeil. je forwarde un mail échangé dans le cadre de
la mailing list "librehealthcare" qui rassemble les libristes de la santé.
J'ai rien dit ;)  
  
\---------- Forwarded message ---------  
From: Sébastien Jodogne
&lt;[s.jodogne@chu.ulg.ac.be](mailto:s.jodogne@chu.ulg.ac.be)&gt;  
Date: jeu. 14 janv. 2016 à 09:47  
Subject: [LibreHealthcare] Wikipédia  
To:
&lt;[librehealthcare@medecinelibre.net](mailto:librehealthcare@medecinelibre.net)&gt;

  
  
Chers tous,  
  
Je viens de découvrir l'existence sur Wikipédia en français d'une page qui
énumère les logiciels libres pour le secteur médical :  
<https://fr.wikipedia.org/wiki/Logiciel_libre_m%C3%A9dical>  
  
Ce serait bien que nous l'enrichissions (par exemple en y ajoutant echoOpen).  
  
Sébastien-

### **hyacinthe,** - Jan 14, 2016 at 10:05 AM

Sweet! Pour rappel, echopen est présent sur la page méta, de matériel médical
libre: <https://fr.m.wikipedia.org/wiki/Mat%C3%A9riel_libre>  
;)

### **Hyacinthe** - Jan 14, 2016 at 11:05 AM

Top. Du coup, pour éviter de se faire évincer si des liens trop proches sont
fait entre les éditeurs de la page et l'équipe d'echopen, si les membres de
libre healthcare peuvent poser les première hyacinthes, ce serait sans doute une
bonne manière pour nous ensuite de compléter.

### **Hyacinthe Lacenne** - Jan 14, 2016 at 11:19 AM

C leur proposition et donc à eux de jouer ;)

### **Hyacinthe** - Jan 14, 2016 at 11:22 AM

Ok. Mais ce ne vaudrait pas le coup de leur donner une réponse avec qq liens,
pour trouver les éléments principaux ? Je ne sais pas si cela peut porter
préjudice ou au contraire les aider... Je ne les connais pas suffisamment.  
  
A toi de voir ;)

### **Hyacinthe Lacenne** - Jan 14, 2016 at 11:23 AM

Je leur ai fait un mail pour leur dire que pour + d info, on est là;)

### **Hyacinthe Lacenne** - Jan 14, 2016 at 7:50 PM

voilà on y est  ;) <https://fr.wikipedia.org/wiki/Logiciel_libre_m%C3%A9dical>

### **Hyacinthe** - Jan 14, 2016 at 7:50 PM

Cool ;)



#  Ressources echOpen Diverses

Hyacinthe posted this Mar 30, 2016 at 4:04 PM

Hello à tous,  
  
Un fil de discussion pour échanger sur les ressources echopen. En effet, nous
produisons pas mal de choses en plus du hard &amp; du soft comme des photos,
etc. Du coup, comment pourrions nous imaginer une solution pour partager ces
éléments tous ensemble ?  
  
Sachant que nous devons penser les licences liées à ces productions. Nous
avons par exemple les dessins de Barbara en CC BY NC ND,  ![Hyacinthe VINCENT,
Libre faiseur at echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe
qui nous a donné ses photos sous les mêmes conditions de CC BY NC ND et mes
photos aussi, mais nous n'avons pas encore mentionné ces licences sur ces
images.  
  
Par ailleurs, nous allons recevoir les photos de Karine (commandées par Fabre)
qui seront sous : _ ©Karine S. Bouvatier pour la Fondation Hyacinthe Fabre
_sachant que l'association pourra les utiliser comme elle le souhaite pour ses
activités. _  
_  
Alors quelles seraient vos idées pour que nous puissions partager tout ça en
**prenant bien en compte ces différentes licences**.  
  
Merci pour vos retours.

### **Hyacinthe Lacenne** - May 23, 2016 at 12:29 PM

que pensez-vous d'installer ceci sur notre home ? pour faciliter l'intégration
à slack et router directement depuis notre page echopen.org  
  
<https://github.com/rauchg/slackin>

### **Hyacinthe VINCENT,** - May 24, 2016 at 11:15 AM

One Git repos to rule them all !!!

### **Hyacinthe Lacenne** - May 24, 2016 at 9:53 PM

![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  tu veux dire
que tout est sur git ? si oui, que fait-on des échanges de type slack ?

### **Hyacinthe Lacenne** - May 25, 2016 at 9:57 AM

slackin installé accessible à <http://echopen.org:3000/>  
  
![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  crée
un sous-domaine slack.echopen.org pour lading page + badge sur la home
d'échopen

### **Hyacinthe VINCENT,** - May 25, 2016 at 1:41 PM

"_Hyacinthe tu veux dire que tout est sur git ?_ ". Moi j'aurais tendance au
moins à stocker la connaissance dans un dépot (file système, Git...) et à la
publier sur un site Web généré automatiquement.  
Je n'aime pas bien mélanger création/stockage/publication  d'information dans
un même outil rudimentaire comme le wiki (ex: combien de temps pour migrer
d'un serveur à un autre ? ;-) ). Mais c'est un avis assez personnel et très
orienté développeur de SI.  
"Slack" ? Je ne savais pas qu'il y avait de la connaissance dedans... Si il
s'agit des échanges entre qq personnes, c'est pas très digeste comme info. Il
faut penser un minimum à nos lecteurs. Pour moi Slack n'a d'interêt que pour
les personnes qui ont participé à la conversation. Mais c'est vrai que je
l'utilise peu et je ne sais pas bien ce qu'il y a dedans. Et il est légitime
de vouloir archiver ces fils de discussion (de là à les publier ...).  
Par contre, quand on dépose un ensemble d'infos dans Git et que l'on fait un
commit, avec un commentaire, on s'engage sur un contenu
cohérent,daté,signé,sans défaut connu... et destiné à être lu (ou compilé) par
tous ceux qui ont accès au dépot.  
  
Pour revenir au sujet initial des photos, au fil des années (dizaines...) je
suis toujours revenu à un stockage en arborescence chronologique de fichiers
jpg (raw) avec qq tags directement dans les noms. C'est la seule structure qui
resiste à tout (backups, plateformes, outils, chgt de version, de format...)
et j'ai un petit outil qui en copie certaines vers un site de publication.
KISS !

### **Hyacinthe Lacenne** - May 25, 2016 at 7:42 PM

merci pour ces informations circonstanciés. côté slack, on peut y inclure des
échanges bcp plus informelles, il ne s'agit pas vraiment d'une base de
connaissance mais d'une modalité d'inclusion de notre communauté au sens très
lâche, du community management inclusif en somme. Pour ma part, je ne suis pas
pratiquant de slack mais  ![Hyacinthe,
echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  et  ![Hyacinthe
Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  sont
utilisateurs et je laisse la parole à leur point de vue plus précis

### **Hyacinthe** - May 25, 2016 at 7:49 PM

Slack est un bon moyen pour discuter lorsque les gens ne sont pas ensemble
dans la même pièce et pour éviter les boucles e-mails infinies.  
  
Mais c'est aussi un bon moyen pour accueillir les contributeurs et répondre à
leur questions. Beaucoup l'utilisent comme "service client". En revanche c'est
certain que ce n'est pas un lieu de production de connaissance à proprement
parlé mais plutôt un lieu d'échange. Si des connaissances apparaissent il est
important d'en faire la synthèse, mais cela représente un gros travail et
devrait plutôt être sur un Q&amp;A. Tous ces outils sont complémentaires les
uns des autres, et permettent à des profils très différents de se rencontrer
et d'échanger.  
  
Pour ma part, je pense que slack (ou assimilé) est à conserver et à dynamiser
pour être le pendant en ligne du lieu physique d'Echopen.  
  
Voilà pour un premier retour ;)

### **Hyacinthe Lacenne** - May 25, 2016 at 10:08 PM

Yop  
Pour faire court, si tout le monde ne s'en sert pas (comme toi hyacinthe), ça perd
de sa puissance. A voir, puisque basecamp à un aussi un systeme de chat.  
Ensuite, en échanges bilatéraux, y'a le mail.  
Enfin, le fait d'avoir de la connaissance dispersée, des outils épars implique
comme vous le dites de faire des synthèses... Donc autant éviter non?  
Perso, vu l'utilisation qu'on a de Slack, la question se poserait de le
garder: autant onboarder sur un outil plus actif.  
A noter, Slack est utilisé pour onboarder, et soit ce sont des botsqui font
l'accueil, soit des participants actifs. Vu qu'on a aucun des deux...On
pourrait safely laisser tomber Slack (I guess).  
My two cents ;)

### **Hyacinthe Lacenne** - May 26, 2016 at 8:14 AM

ok donc on met cela à l'odj de lundi et on tranche alors ;)



#  Génération De Documentation (automatique)

Hyacinthe VINCENT posted this Apr 06, 2016 at 8:40 AM · 1 person applauded

![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  :
ton outils d'extraction automatique de documentation à partir des sources me
semble être la bonne voie.  
J'avais glâné quelques ressources :  
  

  * [Static Site Generators](https://staticsitegenerators.net/) : une synthèse des outils
  * [GPP 2.23 — Generic Preprocessor](http://files.nothingisreal.com/software/gpp/gpp.html) : je savait même pas que ça existait. A creuser ;-)
  * [Building Publishing Workflows with Pandoc and Git](http://publishing.sfu.ca/2013/11/building-publishing-workflows-with-pandoc-and-git/)
  * [HF Antennas: Vertical or Horizontal?](http://hamwaves.com/vertical-horizontal/en/index.html#summary) : Un exemple de site statique (pas beau) &gt;&gt;&gt; **ouvrir le fichier "make"** : lien en haut à gauche.
  * [Writing, Markdown and Pandoc](http://brizzled.clapper.org/blog/2010/11/26/writing-markdown-and-pandoc/)
  * [Pandoc Extras](https://github.com/jgm/pandoc/wiki/Pandoc-Extras) : d'autres outils
  * [EspruinoDocs](https://github.com/espruino/EspruinoDocs#espruinodocs) : sous /bin, je générateur de doc.**  
  
  
  
  
  
**

### **Hyacinthe** - Apr 06, 2016 at 9:07 AM

Merci  ![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  je vous invite
avec  ![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png)
Hyacinthe  comme vous avez commencé à avancer ce sujet à proposer un draft de
solution à la réunion de  
Lundi prochain. Ça vous va ?

### **Hyacinthe VINCENT,** - Apr 06, 2016 at 10:38 AM

Ca dépendra de l'avancement. C'est en train de murir tranquillement. Mais je
pourrais dire deux mots de la voie qu'on est en train d'explorer.

### **Hyacinthe Lacenne** - Apr 06, 2016 at 10:43 AM

+1 :)  
Pour voir en pratique, cf dernières modifications sur le wiki.

### **Hyacinthe VINCENT,** - Apr 06, 2016 at 11:50 AM

C'est plutôt bien je trouve.

### **hyacinthe,** - Apr 06, 2016 at 2:53 PM

Wep ça marche pas mal.  
Shell+pandoc+bot wiki en python :)

### **Hyacinthe VINCENT,** - Apr 06, 2016 at 4:17 PM

Le Shell aura un peu de mal à tourner sous Windows, mais comme tu vas nous
scripter tout ça en Python on sera bien multiplateforme ;-).

### **Hyacinthe VINCENT,** - Apr 07, 2016 at 8:21 AM

Dans ce cadre et aussi en rapport avec
<https://3.basecamp.com/3152267/buckets/155345/messages/100695652>. Je pense
qu'il est temps de commencer à mettre en place un système de référencement
cohérent des entités manipulées et que l'on retrouvera un peu partout (doc,
dépot, sources, noms de fichier, de répertoires, URL...).  
  
Je propose, surtout histoire de lancer débat, quelque chose comme :

  * **Composants (CMP-...) **:
    * CMP-alimentation
    * CMP-HV_alim (se forkant par exempe, en CMP-HV_alim_cascaded ou CMP-HV_alim_boost, CMP-HV_alim_hv7360...)
    * CMP-tranducer_ENS_v2
    * ... et n'importe quoi commençant par CMP-...
  * **Signaux d'interface (SIG-... ou ITF-...)** :
    * SIG-gnd
    * SIG-5v
    * SIG-pulse_HV
    * SIG-amplified_signal
  * **Fonctions (FCT_...)** :
    * FCT-sensing
    * FCT-...
  * _Et tout ce qu'on veut ..._

  
Bon, vous avez compris le principe. C'est ce système de référencement qui sera
garant de l'intégrité du projet et nous permettra d'en automatiser au maximum
la gestion. C'est, par exemple ce qu'on retrouvera en métadonnées des éléments
de documentation. Mais pourquoi pas, aussi, directement dans les commentaires
des sources.  
Ce référentiel sera le degré 0 de l'echOsystem.  
Avec ça, plus d'ambiguité entre FCT-clipping et CMP-clipper.  
  
On peut référencer à peu près tout : exemple un Captech (CAP-tech_2016-04-05)
ce qui permettra de le siter dans, par exemple, l'argumentation d'une
technologie décrite dans la doc d'un composant et donc naviguer du composant
au notes du Captech.

### **Hyacinthe** - Apr 12, 2016 at 6:20 AM

![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe  et
![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  par rapport à
ce qui a été dit hier, pensez-vous qu'il serait intéressant de créer un repo
GitHub pour tester le modèle discuté de documentation ?  
  

  1. Créer un repo sur le Github "medico-technique" 
  2. Ajouter un readme avec l'essentiel des règles (que nous pourrons modifier au fur et à mesure) incluant : 
    1. How to contribute 
    2. File name (nomenclature) 
    3. Principles / flow and merge conditions 
    4. Glossaire (inclu ou non dans le readme) - fait par  ![Emilie Mayer, Community & knowledge  at echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  
  3. Ajouter le premier module (réalisé par Michel) avec doc &amp; source files puis avancer avec  ![Hyacinthe, Danseur du ventre at echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  sur les autres modules petit à petit et voir comment ajuster ? On pourrait ainsi faire un bilan à chaque ajout et ajuster l'ensemble en conséquence. 

  
L'idée serait de pouvoir avoir en un seul endroit tous nos derniers éléments
qui convergent et qui ainsi nous permettrons de tester les hypothèses
d'organisation de la documentation.  
  
Ce sera aussi une bonne occasion de tester les issues, notamment avec la
question posé hier par  ![Jean François C, Signal processor  at
echopen](./../../zz_assets/images/avatars/3458716.png) Jean  sur l'ADC et d'en
discuter directement sur github.  
  
Dès qu'on ajoute un contenu on peut ensuite supprimer les google doc
correspondants.  
  
Vos avis et remarques ?

### **Hyacinthe VINCENT,** - Apr 12, 2016 at 7:35 AM

Ok d'ac, laissez moi juste un peu de temps pour essayer de créer une base la
plus cohérente possible. Ou alors je fork chez moi et fait un pull request
ensuite.  
  
_"Ce sera aussi une bonne occasion de tester les issues, notamment avec la
question posé hier par Jean  sur l'ADC et d'en discuter directement sur
github."_ :  
Peut-être pas la peine dans un premier temps de tous basculer sur GitHub.
D'abord voir si on peut faire un bon dépot pour y mettre ce qui est stable. Et
en retirer de la doc à jour.  
  
On peut aussi en faire un "brouillon" pour essayer d'y faire tenir tout
l'existant afin de voir si la structure est "bullet proof" et ensuite on en
refait un tout propre avec uniquement la nouvelle génération modulaire.

### **Hyacinthe Lacenne** - Apr 12, 2016 at 7:38 AM

Top.  
  
J'ai créé le repo, @hyacinthe tu en es admin également, comme ca tu pourras aussi
aider à gérer les pull-requests pertinentes ;)  
  
Tu peux forker!

### **Hyacinthe** - Apr 12, 2016 at 9:38 AM

ok. top. Do it, fail it fix it ;)  ![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  on te laisse le
temps de voir et dès qu'on a ton feu vert, on tenter d'ajouter le module de
michel pour test.  
  
On pourra en effet tout à fait le refaire ensuite après avoir tester.  
  
Merci.

### **Hyacinthe Lacenne** - Apr 12, 2016 at 12:27 PM

( dans l'esprit : <http://www.koszek.com/blog/2016/04/11/dont-document-
automate/> )

### **Hyacinthe Lacenne** - Aug 19, 2016 at 11:22 AM

ce n'est pas de la doc automatique mais il s'agit de la structuration sous le
format GitBook que j'évoquais la semaine prochaine et que je ré-évoquerais en
réu qd tout le mode sera là  
  
on a [4 GitBooks](https://www.gitbook.com/@lacenne/dashboard?q=echopen) en
chantiers  
  
\- espace echOpen  
\- start-kit : instance echOpen  
\- l'application android  
\- l'image processing  
  
l'avantage  
  
\- structuration de la doc via un plan &gt;&gt; wiki  
\- édition collaborative  
\- synchronisation bi-directionnelle GitBook &lt;-&gt; GitHub  &amp; donc
congruent à la génération de doc

### **Hyacinthe Lacenne** - Aug 19, 2016 at 11:26 AM

J'ajouterais que la génération de doc peut aussi générer un gitbook, easy.  
Pour harmoniser les structures de gitbook, il peut être intéressant d'avoir
une table des matières générale commune à ces gitbook, pour avoir de la
cohérence entre les travaux.

### **Hyacinthe Lacenne** - Aug 19, 2016 at 11:40 AM

yep pour l'autodoc  
  
btw, je suis déjà dessus sur les communs de doc : non seulement sur le plan
mais aussi les licences, les formats de biblio &amp; such. Un sujet à traiter
es l'update de l'information. Suggestion : toutes les informations dont on
sait qu'elles sont sujettes à évoluer doivent avoir un sigle distinctif, ce
qui permet de les retrouver par search et d'ajuster ~un peu comme les @todo
dans les IDE  
  
j'ajouterai aussi qu'on peut les assembler et les vendre ;)

### **Hyacinthe Lacenne** - Aug 19, 2016 at 12:01 PM

du coup il faut qu'on fasse un point sur  
  
\- l'harmonisation du soft et du modèle de doc de  ![Hyacinthe VINCENT, Libre
faiseur at echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  
\- la génération de gitbook à partir de l a doc  
  
-&gt; mini-workshop sur la doc vendredi prochain ? en mode reprise de saison pour les apéros

### **Hyacinthe Lacenne** - Oct 17, 2016 at 9:20 PM

A y est, le PDF généré dépasse les [250
pages](https://www.gitbook.com/book/hyacinthe124/echomods/) sur le kit, quand on le
DL en PDF =)



#  Schéma important pour le WIKI qui demande retour avant vendredi matin

Emilie Mayer posted this Jan 11, 2016 at 7:07 PM · 1 person applauded

Voici le schéma "bête à corne" de la méthode "apte" qui récapitule la base du
projet Echopen et explicite le pourquoi. Pourriez vous y jeter un coup d'oeil
et le commenter avant vendredi matin?  
  
Merci !  
<https://docs.google.com/drawings/d/1nnm6XBpvT74xdEnMIAr6KTZ2bwj428GBi_LyP0ob40o/edit?usp=sharing>  
  
  
De plus, n'hésitez pas à aller jeter un coup d'oeil à "Déclinaison du besoin
médical en exigences techniques, dans la to do list, car j'ai mis quelques
liens concernant les normes.

### **Hyacinthe LICCIONI,** - Jan 11, 2016 at 10:05 PM

J'ai pas les accès... Normal?

### **Emilie Mayer,** - Jan 12, 2016 at 9:22 AM

J'ai changé le lien, ça devrait marcher maintenant

### **Hyacinthe** - Jan 12, 2016 at 9:34 AM

Sinon, voilà le schéma...

[

![](bc3-raw/files/751401-capture-d-ecran-2016-01-12-a-10-32-27.png)

](bc3-raw/files/751401-capture-d-ecran-2016-01-12-a-10-32-27.png)

[ Capture d’écran 2016-01-12 à 10.32.27.png  506 KB • Download
](bc3-raw/files/751401-capture-d-ecran-2016-01-12-a-10-32-27.png)



#  un peu de veille

Hyacinthe Lacenne posted this Jan 16, 2016 at 12:17 PM · 1 person applauded

des sites qui vont intéresseront  
  
le github du hardware : encore très confus mais intéressant  
<https://www.makake.co>  
  
de quoi se connecter ;)  
<https://www.fablabs.io/projects>

### **Hyacinthe Lacenne** - May 24, 2016 at 7:45 AM

un site que vous connaissez sans doute  
  
<https://getchip.com/pages/chip>  
  
la prez et la doc sont claires - ce serait pas mal qu'on se refasse 12c4 une
session sur les pros &amp; cons d'un wiki à présent

### **hyacinthe,** - May 24, 2016 at 1:19 PM

Yup. Et qu'on definisse ce qu'on mets, et où, en fonction au passage de notre
bande passante/de notre capacité (ou disponibilité) à utiliser les outils. un
wiki de travail n'est pas un site de promo, ou un gît de contribution :)  
Et de voir si on peut jouer avec un générateur de site statique (pas absurde)
a la pages.github.io Itoo ?



#  rencontre electronique

Hyacinthe Lacenne posted this Jan 18, 2016 at 10:28 AM · 1 person applauded

bertrand (duplat) vient ce mercredi fin de mat avec un ingé/électronicien
paraît-il de très high level -&gt; Jean-Christophe Billard, qui travaille dans
les device santé et est intéressé par echOpen ;)

### **hyacinthe,** - Jan 18, 2016 at 11:22 AM

Du très bon! Un gadz qui a fait un ecg malin, du hardware de a à z,de
l'innovation, et un business model pour bitmakers qui est intéressant!

### **Hyacinthe VINCENT,** - Jan 18, 2016 at 12:45 PM

Un autre gadz ... on est foutus !!!

### **hyacinthe,** - Jan 18, 2016 at 2:13 PM

Ils sont partout !!

### **hyacinthe,** - Jan 20, 2016 at 8:26 PM

On peut le contacter sans souci?  
La rencontre s'est bien passée ?



#  queuing the docs

Hyacinthe Lacenne posted this Feb 10, 2016 at 11:41 AM · 1 person applauded

hello à tous,  
  
Voici un message d'un doc ;) Comme pour Marie-Thérèse Barrellier, je vais lui
proposer de passer nous voir - à défaut d'avoir un outil utilisable, il
faudrait qu'on commence à les impliquer -&gt; IA Djalel + hyacinthe &amp; why not
Moocification de la formation de hyacinthe  
  
Bonjour,  
Médecin urgentiste SAMU-SMUR-Urgences, formé à l’écho (DIU d’Echographie
Appliquée à l’Urgence), j’utilise la technique au quotidien:  
abdo, voies urinaires, coeur, gros vaisseaux, musculo-squelletique, un peu de
poumons et de DTC;  
sans prétendre nullement au titre « d’expert ».  
En quoi puis-je vous être utile?  
Amicalement,  
Alexandre Maisonneuve  
[alexmaisonneuve@msn.com](mailto:alexmaisonneuve@msn.com)

### **hyacinthe,** - Feb 10, 2016 at 11:51 AM

On peut peut être ls impliquer sur des points qu'on devrait creuser avec
l'optique "user" (en vrac):

  * Le cahier des charges de l'outil 
  * Un appui à l'expression et l'analyse des besoins 
  * Une cartographie plus poussée des usages

What say?

### **Hyacinthe Lacenne** - Feb 10, 2016 at 3:06 PM

sure - je mets cela dans le pipe ;) de toutes façons il faudra que l'on monte
incessamment un CapMed

### **Hyacinthe Lacenne** - Mar 02, 2016 at 11:30 AM

voici un mail que nous venons de recevoir ;)  
  
Bonjour

  
Je suis cadre supérieur de santé sur les HUPC issu de la filière rééducation,
kinésithérapie.

  
Je suis également responsable d’une organisation professionnelle de
kinésithérapeutes et nous serions intéressés que vous présentiez l’echOpen au
congrès de kinésithérapie que nous organisons début juin.

  
Nous pensons également que l’échographie pourrait apporter une aide pertinente
aux professionnels dans leur rééducation.  
  
Je connais bien l’Hôtel Dieu pour y avoir exercé pendant 5 ans et je sollicite
de vous y rencontrer, ou ailleurs, afin d’évoquer ces différents sujets.  
  
Bien cordialement  
Didier LANTZ  
06 61 44 09 41  
  
*HUPC dans le mail qui veut dire (Hôpitaux Universitaires Paris-Centre, Cochin, Broca, Hôtel-Dieu)

### **Hyacinthe Lacenne** - Mar 03, 2016 at 2:11 PM

hello,  
  
J'ai rencontré ce jour Didier Lantz. Gentilhomme cordial et attentif ;) il a
officié à Cochin puis à l'Hôtel Dieu, ce qui me rappelle ;)  
  
Les usages qui intéresseraient les kiné sont pas nécessairement là où mes
habitudes m'auraient porté :  
  
\- état de la vessie : pb important en rééducation neuro, vérifier si la
vessie est +/- pleine, important dans les contextes de sondage)  
\- au plan pulmonaire : s'assurer de la qualité des manoeuvres respiratoires  
\- et bien entendu, l'ostéo-articulaire  
  
Il nous propose d'intervenir au congrès du syndicat dont il est président, le
2 ou le 3 juin. Ca se passe à Aix-les-bains.  
  
Je lui proposé de participer au prochain CapMed. Il est Ok pour venir avec ses
collègues praticiens dont un qui utilise l'échographie à usage d'exploration
kinésithérapique  
  
Il nous propose de recruter des béta-testeurs  
  
Il nous propose le moment venu de diffuser l'info echOpen auprès des 35000
contacts de sa profession  
  
oilà



#  workshops communautaires

Hyacinthe Lacenne posted this Mar 21, 2016 at 11:00 AM

fil de discussion autour des captech, capdev et autres hackathons

### **Hyacinthe Lacenne** - Mar 21, 2016 at 11:05 AM

ce vendredi 18.03.16, rencontre avec Hyacinthe et le CRI - thème :
makathon/mécathon  
  
\- ok pour un hackathon méca  
\- thématiquer  
\- public du CRI : de l'étudiant en master aux doctorants (+ difficle à
mobliser mais étant donnée la nature du projet, ca devrait le faire) :
formation techno-scientifique (dev, electro, gamers), designers...  
\- thématique : 3 enjeux identifiés -&gt; conception mécanique, design de
l'objet, publication d'un guide montage  
\- date proposée : soit avant le 21 avril soit à compter de la mi-mai : car
déménagement de l'Open Lab à Cochin. Etant donnés les contraintes de prépa, on
est convenu de mi-mai  
  
btw, le matériel de l'Open Lab nous est ouvert et ce, notamment pour la
fabrication de la boîte pour le 24 mars

### **Hyacinthe VINCENT,** - Mar 21, 2016 at 12:31 PM

Et je suis resté un peu ensuite pour faire un tour du Fablab :

  * Qq outils de découpe de bois.
  * Impression 3D : filaire et résine polymérisée aux UV.
  * Découpeuse laser.
  * Bonne compétence de réalisation de circuits électroniques en CMS "à la plancha", ça n'a pas l'air si difficile, le résultat était nickel et ils sont prets à nous accompagner. Les circuits sont commandés en chine et livrés dans la semaine (40€ les 40 de 30x30 en double face, 5€ pce en 4 couches).
  * Accessible aussi le WE.

### **Hyacinthe** - Mar 31, 2016 at 11:05 AM

Pour le Captech de mardi prochain :  
Le document de base de référence est disponible
[ici](https://docs.google.com/document/d/1vNT7Ir01gAAjsohgqN5a_Y9ZoAEBHPQmQlIxxvTKVGc/edit#).
Pour ce qui est des points fonctions &amp; such, on voit cela demain matin
avec  ![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  et  ![Muriel,
Contributeur méthodologie at
echopen](./../../zz_assets/images/avatars/1269173.png) Muriel . On finalise
aujourd'hui avec  ![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  le schéma de la
sonde.  
  
Vos remarques sont les bienvenues ;)

### **Hyacinthe Lacenne** - Mar 31, 2016 at 8:23 PM

Merci!  
J'ai avancé sur le doc.

### **Hyacinthe** - Apr 02, 2016 at 11:05 AM

Bonjour à tous,  
  
En prévision du CAPTech de mardi prochain, voici les premiers éléments de
présentation

  * Le [Schéma](https://docs.google.com/presentation/d/1X4QVfOYeUJSIhjSg8QRVOj-x31x2ZA7QWVpnQNl3qtY/edit#slide=id.p4) de la sonde (revu par  ![Hyacinthe VINCENT, Libre faiseur at echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe ) que je mettrai en forme lundi après-midi sur la base du travail déjà réalisé par  ![Hyacinthe, Danseur du ventre at echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  puis avec  ![Emilie Mayer, Community & knowledge  at echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  et  ![Muriel, Contributeur méthodologie at echopen](./../../zz_assets/images/avatars/1269173.png) Muriel  et parti du [tableau](https://docs.google.com/spreadsheets/d/17jtXg-r6_nDEFxN0xtRFjEYXCeVaxZG9clrJDgage0o/edit) général. 
  * Nous parlerons aussi des aspects de documentation pour le quel  ![Emilie Mayer, Community & knowledge  at echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  et  ![Muriel, Contributeur méthodologie at echopen](./../../zz_assets/images/avatars/1269173.png) Muriel  on commencé une [document](https://docs.google.com/document/d/11dJB4cTPcXkxdXE4P0HZj2o6fjAQtg2ZvGt33IAwT-s/edit#) que je vous invite à regarder et vos remarques sont les bienvenues. Notez que dans ce travail de documentation il est important que la lecture soit simple et qu'il y aura, à terme, des normes à respecter.  

  
Bonne journée à tous.

### **Hyacinthe Lacenne** - Apr 12, 2016 at 2:12 PM

![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe  voici le gdoc
d'  ![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe
pour la prépa du hackaton méca ;)  
  
<https://docs.google.com/document/d/1T0rcg9NmNtdjPB8jdhmQ5RWkwCaVaP7IqTzbHIdKJgM/edit#heading=h.51pvtcdf4smh>



#  Notes et cr d'apéros

hyacinthe posted this Feb 15, 2016 at 8:05 AM · 2 people applauded

Pour ce Cr, erci à Ozanne et Emilie :)  
N'hésitez pas à éditer les notes de l'apero licenses libres sur :  
  
<http://echopen.org/index.php?title=Ap%C3%A9ro_Licences_Ouvertes_avec_Benjamin_Jean>

### **Hyacinthe Lacenne** - Feb 21, 2016 at 5:08 PM

Dans la floppée, ça peut être bien pour communiquer (au sens large, pour les
bailleurs, partenaires, membres, ...) sur les progrès d'echOpen et là où on en
est today. Y'a un draft qui traine sur le drive ici [[Rapport
d'Etape](https://docs.google.com/document/d/1R9Ri3CTBX9NzoTmAcjsDLzI7vcvIfR1WK8pGgXPXAbY/edit?usp=sharing)]
- n'hésitez pas à apporter vos idées, souvenirs, et brains dump divers dans ce
fichier =)



#  Séance Photo Pour Fabre Archived

Hyacinthe posted this Jan 26, 2016 at 5:18 PM · 1 person applauded

Hello à tous,  
  
Je viens de discuter avec une photographe qui est passé nous voir de la part
de la Fondation Fabre. Elle aimerait faire quelques images de ce que nous
faisons et quelques portraits de nous ;)  
  
Ce sera l'occasion pour nous d'avoir des images pour étayer ce que nous
faisons et pour Fabre de pouvoir parler du projet dans leurs différents
rapports.  
  
Il y aurait deux passages :

  1. Pour des images des activités + portraits 
  2. Pour des images des test avec notre proto

  
On attends son retour et nos dates pour caler ça.



#  Licences echOpen

Hyacinthe posted this Feb 04, 2016 at 2:27 PM · 1 person applauded

Les licences echopen, licences qui couvrent l'ensemble des travaux réalisés
par la communauté sont :  
\- Une licence Hardware (libre) disponible sur le
[wiki](http://echopen.org/index.php?title=Licence_echopen)  
\- Une licence Software (bsd / open) disponible sur le
[github](https://github.com/echopen/echopen/blob/master/LICENSE)  
  
Nous avons clarifié la situation des licences ce matin dans les différents
repo sur le github en ajoutant en plus les liens en tête de chaque ReadMe.  
  
Je vous invite à discuter des licences sur ce fil de discussion pour le cas ou
vous auriez des questions.



#  Newsletter Nouvelle Année Archived

Emilie Mayer posted this Jan 13, 2016 at 7:14 PM · 1 person applauded

Bonsoir!  
  
En vue de préparer la newsletter de rentrée, n'hésitez pas à m'envoyer
quelques lignes résumant l'essentiel des avancées de votre pole depuis
CapTech! Idéalement, d'ici ce week-end.  
  
  
Je pense en particulier aux:  
*transducteur  
*méca 3D  
*CapDev  
*Avancées Hyacinthe-Hyacinthe-Hyacinthe   
  
Merci!

### **Hyacinthe** - Jan 14, 2016 at 11:03 AM

Merci Emilie, pour préciser:

  * Transducteur =&gt; il faut faire un email a Hyacinthe et voir avec Hyacinthe qui dois y passer cet après-midi
  * Méca 3D =&gt; Voir avec Hyacinthe 
  * CapDev =&gt; Hyacinthe
  * Partie analogique =&gt; Hyacinthe, Hyacinthe et Hyacinthe

  
@+

### **Hyacinthe LICCIONI,** - Jan 14, 2016 at 2:04 PM

Il nous fallait réaliser le programme qui contrôle l'ensemble du système, à
savoir:

  * Commander l'émission de l'impulsion
  * Commander le TGC dont le rôle est d'amplifier le signal
  * Asservir le moteur en vitesse de rotation
  * Calculer les positions du moteur
  * Acquérir les données
  * Transférer les données

On a toute la partie contrôle du système. Il reste à réaliser l'asservissement
du moteur ainsi que les calculs de ses positions, tester l'acquisition des
données et le transfert USB, et tout sera fait pour la partie programme.

### **Hyacinthe Lacenne** - Jan 14, 2016 at 4:30 PM

![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  c dans ta boîte
;)



#  Onboarding Communautaire

Hyacinthe posted this Jan 25, 2016 at 4:34 PM · 1 person applauded

discussion dédiée à l'accueil des nouveaux membres de la communauté

### **Hyacinthe Lacenne** - Jan 25, 2016 at 5:18 PM

je préconiserais aussi François Dupayrat et Loic !

### **Hyacinthe** - Jan 25, 2016 at 6:40 PM

Done...

### **Hyacinthe** - Feb 10, 2016 at 8:40 AM

welcome  ![Michel Bala, Electronique analogique  at
echopen](./../../zz_assets/images/avatars/2008321.png) Michel  qui nous
rejoint dans le cadre de son projet pour l'agrégation et qui va travailler
avec nous sur la partie éléctronique analogique.  
  
![Hyacinthe KHOYRATEE, Electronique at
echopen](./../../zz_assets/images/avatars/1249123.png) Hyacinthe  et  ![Hyacinthe,
Danseur du ventre at echopen](./../../zz_assets/images/avatars/1248689.png)
Hyacinthe  je vous laisse lui donner les éléments importants.

### **Michel Bala,** - Feb 10, 2016 at 8:54 AM

Bonjour à tous.  
  
Je remplacerai Hyacinthe sur la partie électronique Analogique.  
Après les épreuves écrites, c'est à dire à partir de la deuxième semaine de
Mars, je serai disponible pour apporter ma contribution jusqu'à fin Mai.  
Un de mes objectifs est de produire une exploitation pédagogique du système.

### **hyacinthe,** - Feb 10, 2016 at 10:34 AM

Bienvenue :)  
Par curiosité, qu'appelles tu une exploitation pédagogique ? L'équivalent du
kit?

### **hyacinthe,** - Feb 10, 2016 at 12:04 PM

@all: n'oubliez pas que vous pouvez avoir une adresse e-mail en
pré[nom@echopen.org](mailto:nom@echopen.org) ;)

### **Emilie Mayer,** - Feb 12, 2016 at 6:05 PM

Pour ce qui est pédagogique, n'hésite pas à me pinguer, je suis déjà un peu
dessus.

### **Hyacinthe** - Apr 29, 2016 at 12:07 PM

Hello,  
  
Virginie est venue cette semaine et nous l'avons rencontré avec  ![Hyacinthe
Lacenne, echopen](./../../zz_assets/images/avatars/2157822.png) Hyacinthe . Voici
ce qu'elle propose de regarder se son côté:  
  
\- fantômes : matériaux, procédés, besoins des cliniciens pour l'apprentissage

\- dialogue entre médecins et ingénieurs, pour cerner les vrais besoin, le
ressenti, voir le quand le comment et le pourquoi de l'utilisation  
  
Elle souhaite rejoindre le projet à partir de la fin juin et l'an prochain et
devrait nous rejoindre dans les réunions du lundi.  
  
Pour mémoire, elle est en thèse en medical imaging &amp; oncology à l'IGR.

### **Hyacinthe Lacenne** - Apr 29, 2016 at 1:43 PM

J'en profite pour rajouter un autre contributeur "SWAT medic, CBRNE officer,
been hacking all my life", vivant aux US de mémoire, qui est ultra partant
pour nous aider sur la question des fantomes:  
  
"Really long day.  Thanks tons for getting this set up.  Also, thanks for
doing better in English than I did in French (I tried.  I'm the only one in my
family that isn't fluent...)  
OK, I'm going to hit the store and start getting gelatin.  The trick is going
to be finding the right combination of gelatin and bacterial growth inhibitor.
Along the way we'll find techniques for various inclusions (Penrose drains for
veins, grapes for "tumors", etc).  I need to find an ultrasound system down
here that I can test on.  I'll go back and talk to the hospital.  What I need
from the community (you folks!) is feature requests, bug reports, etc.  How
deep of a phantom do you need?"  
  
Il a été mis en relation avec Virginie, on a aussi lancé un début de
bibliographie - pour ceux que la question des fantomes intéresse!

### **Hyacinthe** - Jun 02, 2016 at 7:24 AM

Bonjour à tous,  
  
Nous accueillons  ![Joris JEAN-BAPTISTE, Elec analog & digit + Soft  at
echopen](./../../zz_assets/images/avatars/4392629.png) Joris  qui nous rejoint
pour deux mois au sein du projet qui va travailler sur :

  * ADC
  * Micro-contrôleur
  * &amp; such

  
Il est basé à nos côté chez echopen ;)

### **Joris JEAN-BAPTISTE,** - Jun 02, 2016 at 7:25 AM

Bonjour à tous je suis ravi de vous rejoindre sur ce projet !

### **Hyacinthe Lacenne** - Jun 02, 2016 at 7:55 AM

hello Joris,  
  
Welcome on board !  
  
Hyacinthe

### **Hyacinthe Lacenne** - Jun 02, 2016 at 7:57 AM

Salut Joris,  
  
Bienvenue =)  
  
Hyacinthe

### **Hyacinthe** - Jun 13, 2016 at 8:31 AM

Nous accueillons  ![saa sa, Javascript server web at
echopen](./../../zz_assets/images/avatars/4574039.png) saa  et  ![Feng WANG,
Mecatronique at echopen](./../../zz_assets/images/avatars/4574256.png) Feng
pour respectivement 3 semaines pour travailler sur le server web signal  la
suite de Matthieu et 2 mois pour avancer sur les modules et une partie
Mecatronique ;) welcome !!

### **Hyacinthe Lacenne** - Jun 14, 2016 at 3:07 PM

hello à tous, ce serait pas mal qu'il poste un welcome message sur la page
facebook ;) ?



#  crowdsourcing rép. journaleux

Hyacinthe Lacenne posted this Feb 05, 2016 at 11:24 AM

Quentin Noirfalisse, journaliste de [medor ](https://medor.coop/fr/)(les yeux
ouverts), qui nous a connu par Nicolas Pettiaux (université lilbre de
bruxelles, qui était présent au captech ), nous a adressé une série de
questions, en vue d'un billet sur leur site  
  
voici un doc pour recceuillir vos contributions.  ![Hyacinthe,
echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  a formulé les
premières réponses.  
  
<https://drive.google.com/drive/folders/0B0V8htWBLPWBZW5sN25WNUwzX0k>  
  
il faudrait converger pour lundi  
  
@++

### **Hyacinthe VINCENT,** - Feb 08, 2016 at 9:22 AM

Je n'y ai pas accès :-(

### **Hyacinthe Lacenne** - Feb 08, 2016 at 9:31 AM

![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe   je viens de te
renvoyer le lien  
![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  tu
confirmes qu'on a tous accès au drive d'échopen qd on ouvre un document ?

### **Hyacinthe** - Feb 08, 2016 at 9:40 AM

Voilà, tous les accès sont clarifiés. Il y a 3 dossiers de base / ce sont les
dossiers racines : 1. Communauté / 2. Prototypage / 3. Medical.

### **Hyacinthe Lacenne** - Feb 08, 2016 at 11:19 AM

top ;)

### **Hyacinthe** - Feb 08, 2016 at 11:21 AM

btw, concernant le sujet de cette discussion =&gt; Pour moi c'est ok. J'ai
posé les éléments, vous avez revu certains détails et j'ai ajouté les
commentaires.  
  
Je pense qu'on va pouvoir envoyer, non ? D'autres ajouts ?

### **hyacinthe,** - Feb 08, 2016 at 11:25 AM

Bien mais plutôt rempli au départ -ca vaudrait le coup de compléter la partie
sur.les.changements pour le médecin nope?

### **hyacinthe,** - Feb 08, 2016 at 5:56 PM

Cool!  
Ça a pu partir ?

### **Hyacinthe Lacenne** - Feb 08, 2016 at 10:58 PM

sure c parti ;)

### **Hyacinthe** - Feb 09, 2016 at 8:22 AM

J'archive la discussion du coup ;)

### **Hyacinthe Lacenne** - Apr 12, 2016 at 7:09 PM

Fil désarchivé pour une autre demande d'article. Le journal des anciens de
l'ESPCI propose de sortir quelques mots sur la soirée de release du 24 mars
(chouette pour toucher du monde pertinent). Deadline chaude, c'est demain
soir.  
Ils m'ont demandé, mais rien n'empeche de coécrire le bouzin.  
N'hésitez pas !  
Commentaires:
<https://docs.google.com/document/d/11uGdGUb4h3xAyBeTBzWYqizbbci5hhatmiWBB15tFGg/edit?usp=sharing>

### **Hyacinthe Lacenne** - Apr 25, 2016 at 8:03 AM

nice ;)



#  Administration serveur dédié

Hyacinthe VINCENT posted this Feb 18, 2016 at 9:21 AM · 1 person applauded

Avec  ![hyacinthe, hardware thinker at
echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  on se disait lundi
soir qu'il serait peut-être bien d'équiper le serveur Gandi d'une surcouche
d'administration qui permettrait une gestion via le Web plus facile à aborder
pour ceux qui, comme moi,  ne sont pas des dieux du ssh.  ![hyacinthe, hardware
thinker at echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  parlait
de cPanel (qu'il connait bien) et moi de Webmin (que j'utilise
quotidiennement). Après un petit tour sur
<http://alternativeto.net/software/webmin/> il s'avère que le trio gagnant
serait :

  1. Webmin (128) - Open source : <http://www.webmin.com/>
  2. Ajenti (87) - Open source : <http://ajenti.org/>
  3. cPanel (63) - Commercial : <http://www.cpanel.com/>

  
Qu'en pensez-vous ? Pourrait-on en parler à la personne qui a réinstallé le
serveur ?

### **Hyacinthe Lacenne** - Feb 18, 2016 at 12:57 PM

sure ;) manifestement il rencontre des difficultés avec la dernière version de
mediawiki26. Après quoi, on le mettra sur la tâche ou s'il n'a pas le temps,
je ferai l'install ;)



#  CAPMed - Définition du besoin médical

Hyacinthe posted this May 10, 2016 at 10:27 AM · 2 people applauded

Hello à tous,  
  
Suite à une rencontre ce matin avec Maxime, un urgentiste de l'Hopital
LARIBOISIÈRE envoyé par Hyacinthe Bourrier, il est motivé pour nous accompagner
sur l'organisation du CAPMed.  
  
**DATE** :  Une journée, courant Juin =&gt; En attente de 3 dates de leur côté =&gt; sans doute le samedi 18 juin de 10.00 à 18.00  
**SUJET** : Définition du besoin médical (ergo, usage, design, qualité d'image, etc.)   
**LIVRABLE** : Un document de définition du besoin médical dont l'ambition sera d'être une base aux futurs développements techniques, un outil de plaidoyer pour l'echostéthoscopie et un outil de sensibilisation des professionnels de santé.   
**CIBLES** : Médecins (généralistes, spécialistes, professeurs, etc.), techniciens &amp; ingénieurs, développeurs, spécialistes normes et processus qualité, designer, etc.   
**DEROULE** : 

  1. Présentation et retours d'expériences des urgentistes de LARIBOISIÈRE (2 ans avec un Vscan + formations à l'échographie clinique) + 2 ou 3 cas cliniques 
  2. Brainstorm et itération avec la communauté =&gt; Quel besoin médical 
  3. Déjeuner 
  4. Convergence et expression du besoin médical 
  5. Synthèse
  6. Ouverture sur les enjeux de formation 

  
![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie , je sais que le
sujet t'intéresse, serais tu dispo pour nous aider dans l'organisation ?  
![Muriel, Contributeur méthodologie at
echopen](./../../zz_assets/images/avatars/1269173.png) Muriel , Comment nous
conseilles tu de structurer la définition de ce besoin ?  
  
@All, vos retours et votre présence seront/sera bienvenue.

### **Emilie Mayer,** - May 10, 2016 at 9:40 PM

![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  Tout
dépend des dates qu'ils te donnent, sur le principe, très motivée !

### **Emilie Mayer,** - May 10, 2016 at 9:41 PM

Concernant les enjeux de formation, plus qu'une ouverture non?

### **Hyacinthe Lacenne** - May 11, 2016 at 7:49 AM

en effet, on est mûr pour réfléchir au portage de la formation en ligne -&gt;
je pense notamment aux aspects d'apprentissage des bases radio-anatomiques;  
  
en matière d'écho, il y a une sorte de MOOC en hyacinthee évolution qui peut
être une bonne base d'inspiration : <https://123sonography.com/>

### **Hyacinthe** - May 11, 2016 at 9:38 AM

Hello,  
  
Merci  ![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  pour ton
retour. Je pense qu'il est surtout important de voir, qui dans les médecins de
la communauté sont prêts à accompagner l'enjeu de formation, car il est
évident que nous n'aurons pas suffisamment de temps pour aller au delà d'une
simple définition du scope et de la mobilisation des médecins présents sur cet
enjeu.  
  
Dès que je reçois leurs propositions de dates, je vous les communique.  
  
Il va aussi falloir que nous définissions la liste des éléments sur lesquels
nous souhaitons que les médecins se prononcent dans cette définition du besoin
médical.  
  
@+

### **Hyacinthe** - May 11, 2016 at 2:00 PM

Séance de travail rapide cet après-midi avec  ![Muriel, Contributeur
méthodologie at echopen](./../../zz_assets/images/avatars/1269173.png) Muriel
pour tenter de poser les bases d'un cadre de définition du besoin médical.  
  
Le document est disponible sur le drive et
[ici](https://docs.google.com/document/d/1GFbr_EVgpueh3udHefIvB8nSU5UNe2lCPHE3wb8Vs0M/edit#).  
  
![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/782178.png)
lacenne ,  ![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  et tous les
autres, je vous invite à y jeter un oeil et à ajouter vos commentaires,
remarques &amp; such pour ensuite l'envoyer aux urgentistes de Lariboisière en
vue du CAPMed.  
L'objectif de ce document est d'être un cadre de travail pour la définition
des besoins d'usages afin d'en déduire les exigences et les spéc. techniques
nécessaires pour le développement de la sonde et enfin, de prioriser les
applications médicales.  
  
@+

### **Emilie Mayer,** - May 11, 2016 at 5:09 PM

J'ai lu rapidement et c'est top ! Il y a une chose importante à rajouter :
Quantifier et qualifier les usages,  et doit on en privilégier certains plutôt
que d'autres ?

### **Emilie Mayer,** - May 11, 2016 at 5:10 PM

\+ point spécial télémédecine?

### **Hyacinthe** - May 11, 2016 at 5:18 PM

Merci  ![Emilie Mayer, Community & knowledge  at
echopen](./../../zz_assets/images/avatars/1269172.png) Emilie  pour ton
retour. Pour ce qui est de la qualification et quantification des usages,
c'est ce que propose la dernière partie du document. N'hésites pas à clarifier
si cela n'est pas suffisamment clair.  
  
L'aspect télémédecine devrait apparaitre dans les cas d'usages qu'on déduira
avec les médecins, ce qui nous permettra d'ailleurs de le valider. On est
resté pour le moment à un niveau framework générique, sans rentrer dans trop
de détails. La prochaine étape sera de réaliser la matrice et de la remplir
petit à petit et surtout lors du CAPMed.  
  
A bientôt,

### **Hyacinthe** - May 13, 2016 at 2:50 PM

Bonjour à tous,  
  
Une nouvelle version du document est désormais disponible avec comme ajouts :

  * Caractéristiques génériques pressenties d'un échostéthoscope - réalisé avec Hyacinthe B. lors d'une réunion de travail ce-jour
  * La liste des applications médicales imaginées - réalisé l'an dernier avec Hyacinthe M. et Hyacinthe B. 
  * Les résultats attendus du CAPMed en terme de livrables

  
Le document est disponible en suivant ce
[lien](https://docs.google.com/document/d/1GFbr_EVgpueh3udHefIvB8nSU5UNe2lCPHE3wb8Vs0M/edit#).  
  
Vos commentaires sont les bienvenus, n'hésitez pas à les ajouter directement
sur le document.  
  
Bonne fin de journée,

### **Hyacinthe** - May 13, 2016 at 3:09 PM

[LOGISTIQUE] - Les dates proposées par les urgentistes de Larib sont :  
  

  * Lundi 13 juin
  * Mardi 14 juin - DIFFICILE EN RAISON DE APInnov (event innovation APHP)
  * Mercredi 15 juin - DIFFICILE CAR FORMATION A LARIB
  * Jeudi 16 juin
  * Samedi 18 juin - DATE PRESSENTIES en raison des dispo des médecins et autres. 

  
Merci de vos retours.  
  
A vite,

### **Hyacinthe Lacenne** - May 13, 2016 at 11:59 PM

pour moi le 18 est OK. Etienne Englais de KB est ok ?  ![Hyacinthe,
echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe   comment
s'appelle l'echo-pneumologue avec lequel on s'était entretenu il y a un an ?
ca peut être intéressant de l'avoir avec nous.  
  
dès que la date est Ok, je rameute de l'interne et du chef de clinique ;)

### **Emilie Mayer,** - May 17, 2016 at 10:27 AM

Ce serait le soir ou la journée si en semaine?

### **Hyacinthe** - May 17, 2016 at 10:32 AM

On part sur la journée pour avoir le temps d'aborder les sujets. Ceci dit pour
le moment c'est le samedi 18 qui semble l'emporter en raison de la
disponibilité des médecins.

### **Hyacinthe** - May 17, 2016 at 4:39 PM

[UPDATE]  
  

  * La date du CAPMed semble pour le moment s'orienter pour le samedi 18 juin (09.30 à 18.00)  =&gt; Nous confirmerons cette date vendredi 20 mai. 
  * Le programme de la journée est disponible en suivant ce [lien](https://docs.google.com/document/d/1JHH5XlSX8Pn3-7OVNNQre2fW4wdfBY4XOvuLpiosrEM/edit#)
  * Le document de référence / Framework de la définition du besoin médical est disponible [ici](https://docs.google.com/document/d/1GFbr_EVgpueh3udHefIvB8nSU5UNe2lCPHE3wb8Vs0M/edit?userstoinvite=lanfiphone@gmail.com&ts=5735ee94#heading=h.k1t11sr6buf5). 

  
Vos retours sont les bienvenus ;)

### **Hyacinthe** - May 20, 2016 at 12:54 PM

[UPDATE]  
Le CAPMed est confirmé le samedi 18 juin de 09.30 à 18.00  
  

  * Le programme est en cours de finalisation et sera envoyé début de semaine prochaine. 
  * On va prochainement créer les invitations en ligne pour diffuser + l'envoie d'un emailing à toute la communauté. 

  
En complément des professionnels de santé, il nous faut des tech ;) afin de
pouvoir accompagner la transcription du besoin médical en exigences
techniques.  
  
Bonne fin de journée à tous,

### **Emilie Mayer,** - May 20, 2016 at 6:19 PM

Je serai là !

### **Hyacinthe Lacenne** - May 29, 2016 at 6:46 PM

Vla qques uns des fichiers échangés sur le groupe FB =)  
On profitera du channel
[UseCases](https://echopen.slack.com/messages/usecases/) sur slack ?  

[

![](./../../zz_assets/images/previews/5636730-32f6353f5f012be42194e2288025effce83d81177acb2707b6c4afe8bded5f28.png)

](bc3-raw/files/5636730-32f6353f5f012be42194e2288025effce83d81177acb2707b6c4afe8bded5f28.pdf)

[ 32f6353f5f012be42194e2288025effce83d81177acb2707b6c4afe8bded5f28.pdf  146 KB
• Download
](bc3-raw/files/5636730-32f6353f5f012be42194e2288025effce83d81177acb2707b6c4afe8bded5f28.pdf)

[

![](./../../zz_assets/images/previews/5636737-echoscopy-atlas-vscan.png)

](bc3-raw/files/5636737
-echoscopy-atlas-vscan.pdf)

[ echoscopy-atlas-vscan.pdf  2.22 MB • Download
](bc3-raw/files/5636737
-echoscopy-atlas-vscan.pdf)

[

![](./../../zz_assets/images/previews/5636738-horizon-scanning-
report0036-ultrasound.png)

](bc3-raw/files/5636738
-horizon-scanning-report0036-ultrasound.pdf)

[ Horizon scanning report0036 Ultrasound.pdf  343 KB • Download
](bc3-raw/files/5636738
-horizon-scanning-report0036-ultrasound.pdf)

[

![](./../../zz_assets/images/previews/5636739-rfe_ecmu1_2016.png)

](bc3-raw/files/5636739-rfe_ecmu1_2016.pdf)

[ rfe_ecmu1_2016.pdf  322 KB • Download
](bc3-raw/files/5636739-rfe_ecmu1_2016.pdf)

### **Hyacinthe Lacenne** - May 31, 2016 at 8:26 AM

![Hyacinthe, echopen](./../../zz_assets/images/avatars/791737.png) Hyacinthe  g
fait qqs remarques sur le doc. Pour la partie usage médical, je proposerai
qu'on ouvre le gdoc aux contributions remote. Je ferai l'animation sur les
groupes facebook de médecins, notamment eppocrate. Si ok, on peut ouvrir le
jour même, ou en amont ?

### **Hyacinthe Lacenne** - Jun 06, 2016 at 8:47 PM

Un petit truc marrant de la part du [mec qui bosse au
SWAT](https://hackaday.io/DET5Labs), et qui réfléchit aux fantomes (btw on a
possiblement un second contributeur étranger, [voir en bas dans les
commentaires](https://hackaday.io/project/11478-open-source-ultrasound-
phantoms#discussions) =) ):  
  
_I had a difficult case the other day and was thinking about you. We had a ton
of trouble trying to locate a fragment in someone's leg the other day.  
 Have you thought about putting a comprehensive motion sensor (accelerometer,
gyroscope, magnetometer) in your ultrasound probe to create pseudo-three
dimensional images? This would allow me to better see the length of my forceps
within a wound in relation to the fragment I was trying to recover.  
 I know this is a completely different direction for your work, but it is a
tremendous increase in functionality. I wouldn't use it as a primary mode (I'm
very used to using ultrasound in two dimensions), but as a back up, it would
have really helped the other day. _



#  Câblage capteur optique

Hyacinthe VINCENT posted this Jan 26, 2016 at 9:48 PM · 1 person applauded

![Hyacinthe, Danseur du ventre at
echopen](./../../zz_assets/images/avatars/1248689.png) Hyacinthe  dit : "_dis
moi, ton capteur et la diode sont alimentés en 3.3V ou en 5V?_"  
  
Tout est alimenté en 5V (par l'USB). On vise un courant de 20 mA dans la
diode.  
Par contre la résistance de 40 Ko n'est pas présente sur le breadboard car on
utilise celle présente en interne de l'Espruino car on configure l'entrée
utilisée A8 en mode "input_pulldown" donc avec résistance de 40 Ko de mise à
la masse.  
Donc, au final on présente du 5V sur l'entrée du µC, il a l'air de supporter
mais c'est vrai que je devrais essayer de mettre du 3.3V sur la pin 4.  

[

![](bc3-raw/files/1092201-20160126_222450.jpg)

](bc3-raw/files/1092201-20160126_222450.jpg)

[ 20160126_222450.jpg  2.19 MB • Download
](bc3-raw/files/1092201-20160126_222450.jpg)

### **Hyacinthe,** - Jan 26, 2016 at 10:32 PM

Et la diode laser, c'est du 5V également?

### **Hyacinthe VINCENT,** - Jan 27, 2016 at 8:30 AM

Dans les specs c'est 4.5V et là j'utilise du 5V. Par contre j'évite de
l'alimenter en continu (juste des pulses), j'ai l'impression que sinon elle
chauffe et baisse en luminosité (ou se défocalise ???).



#  Outils echOpen

Hyacinthe posted this Feb 08, 2016 at 4:50 PM

Nouveau fil de discussion dédié aux outils communautaires ;)  
  
Pour commencer, nous avons évoqué le besoin d'avoir un sign/up/in publique sur
le slack et visiblement, nous ne sommes pas les premiers à en avoir besoin...  
  
Après avoir passé une bonne partie du we dans la documentation de slack et un
petit tour par les slack de projets Open Source, j'ai trouvé la solution qui
me semble répondre à nos besoins ;)  
  
La voici : <https://github.com/rauchg/slackin> //
[Infos](http://rauchg.com/slackin/)  
  
Mais cela demande un peu d'installation... Il faut mettre un petit module sur
le server pour pouvoir faire tourner cette appli...  
  
Dites moi ce que vous en pensez et qui serais prêts à aider dans son
installation ?  
  
Merci

### **Hyacinthe Lacenne** - Feb 08, 2016 at 5:37 PM

top - ca pourra être bien pour router des echtopians depuis le site vers le
slack  
  
@++

### **Emilie Mayer,** - Feb 09, 2016 at 10:56 AM

Je profite de ce fil de discussion pour relancer la discussion sur le
stack/FAQ, suite à la réunion de samedi:  
  

  * Quand le met-on en ligne? 
  * Est-il en anglais?



#  Design

Hyacinthe Lacenne posted this Nov 01, 2016 at 10:42 AM

un thread dédié au design : indus/app

### **Hyacinthe Lacenne** - Nov 01, 2016 at 10:50 AM

un [design camp](https://echopen.github.io/UXCamp20161025.html) était organisé
le 25.10.11 à des fins d'UX. L'output est un templating psd prêt à être
intégré  
  
gros sujet complexe car l'opérateur  
  
\- doit avoir l'attention sur le patient et l'écran doit pouvoir être controlé
intuitivement  
  
\- doit utiliser le device d'une seule main, car l'autre tient la sonde et est
souvent pleine de gel, ce qui prévient tout usage de type click  
  
On a eu des design high level, qui ont craqué le sujet. Thomas Robillard, web
designer de l'epitech en stage chez echOpen a produit les psd. Ces derniers
sont ouverts à la co-contribution sur InVision.  
  
Les templates sont stabilisés pour jeudi, date du workshop d'intégration
android, qui aura lieu à [Africa4Tech](http://africa4tech.org/) sur 2 jours  
  
oilà;)



#  Philippe Levesque

Hyacinthe posted this Apr 07, 2016 at 10:15 AM · 1 person applauded

Je viens de repenser que Philippe Levesque attendait qu'on fournisse des
résultats avant de se prononcer pour nous ouvrir sa carte électronique de
sonde. Maintenant qu'on a fait notre première démo il peut être temps de le
recontacter non?

### **Hyacinthe Lacenne** - Apr 07, 2016 at 10:17 AM

Already done =)



#  partenaires

Hyacinthe Lacenne posted this Apr 06, 2016 at 8:01 AM

Ceci est un thread pour les partenaires

### **Hyacinthe Lacenne** - Apr 06, 2016 at 8:16 AM

Muriel SHAN SEI FAN, resp. [Groupe thématique Logiciel Libre](http
://systematic-paris-region.org/fr/logiciel-libre), de la [thématique de
R&amp;D et d'innovation "Systèmes d'information"](http://systematic-paris-
region.org/fr/actualites/systemes-d-information-pour-la-transformation-
numerique), au pôle de compétitivité  SYSTEMATIC souhaite nous inclure dans le
groupe logiciel libre  
  
Leur objectif est de mener les projets vers l'industrialisation :
accompagnement du financement les projets, inclusion dans 1 éco-sytème avec
les acteurs...  
  
on nous propose une audition en mai ou en juin  
  
right on time ? prématuré ? votre avis ;)  
  

[

![](./../../zz_assets/images/previews/3355976-guidedesmembresdugtll.png)

](bc3-raw/files/3355976-guidedesmembresdugtll.pdf)

[ GuideDesMembresDuGTLL.pdf  232 KB • Download
](bc3-raw/files/3355976-guidedesmembresdugtll.pdf)

### **Hyacinthe Lacenne** - May 03, 2016 at 4:50 PM

une instance echOpen en algérie ?  
  
voici un mail de nassim Chadli :  
  
  
Bonsoir,  
Je suis Chadli Nassim, étudiant en 5eme année de médecine à Annaba (Algérie);
je suis aussi le National Assistant of Medical Education de l'IFMSA Algerie et
le Local Officier of Research Exchange du Souk Annaba (Association des
étudiants en médecine); J'ai toujours été passionné par les nouvelles
technologies, et cela fait pas mal de temps que je suis les progrès de
l'Echopen. J'ai eu aussi quelques formations sur la programmation (Notamment
en Python) et des notions en Data science (Hadoop). Aujourd'hui je m'adresse à
vous pour voir s'il y aurai possibilité d'avoir un prototype de l'echopen en
vu de la création d'un lab à notre faculté où le projet intéresse beaucoup
d'autres camarades et membres de notre association. Je serais à Paris pour une
semaine, ça serait superbe aussi si je pourrais vous rendre visite ! En
attendant votre réponse, je vous envoi mes ondes les plus positives !!  
  
  
rencontre proposée ;)

### **Emilie Mayer,** - May 04, 2016 at 9:41 AM

Concernant le "systematic", ça peut être intéressant....

### **Hyacinthe Lacenne** - May 04, 2016 at 8:26 PM

Nessim est passé ce jour avec ses collègues. Ils sont une petite bande de
jeunes étudiants en médecine, d'ingé en elec et sont chauds pour monter une
instance echOpen en Algérie, précisément à Annaba. On leur shipera les modules
dès que dispo.  
  
Btw, ils reviendront courant de l'année et on va organiser pour les jeunes
futurs médecins du groupe une séance de formation à l'écho avec le Hyacinthe

### **Hyacinthe Lacenne** - May 05, 2016 at 8:42 AM

Sweet ! On peut aussi les envoyer le code source des modules pour qu'ils
puissent s'essayer à les faire?  
En attendant, pourquoi ne pas les inviter sur le Slack ?

### **Hyacinthe Lacenne** - May 09, 2016 at 7:39 AM

@hyacinthe sure : yes mais on a pas bcp d'activités sur le slack, ca peut être
déceptif. en revanche  dans la mesure où ils vont mettre les mains dans le
cambouis, on peut les inviter au basecamp ?

### **Hyacinthe Lacenne** - May 11, 2016 at 7:45 AM

je prends cela comme un oui ;) ?

### **Hyacinthe Lacenne** - Aug 09, 2016 at 9:07 AM

Hello

  

call ce jour avec Isabelle Wachsmuth, Project manager Health Innovation &amp;
System (HIS) à l_’_OMS

  

**Contexte**  

\- a un point d'intérêt pour la gestion/diffusion de la connaissance dans les
éco-systèmes complexes

  

\- son travail consiste à instiller une culture d’innovation dans les systèmes
de santé : avec un accent sur low cost



-&gt; chapitres nationaux et inter-nationaux  

  

-&gt; veille d’information et diffusion les bonnes pratiques 



**Propositions**  

1) Publication

  * d’un memo sur nos parcours et méthodes
    * description des cycles d‘innovation réalisables 
    * dans le nouveau journal de l’innovation de l'OMS 

      -&gt; diffusion world wide 

      -&gt; selon Isabelle, ça nous donne un point d’ancrage pour  

          - les acteurs publics locaux qui peuvent diffuser la techno : équipement + formation 

          - les essais cliniques 

          - les acteurs qui peuvent financer 

  

2) Mise en relation avec l'EPFL  
  
rdv avec Isabelle pris en novembre à Lausanne pour mise en relation avec ses
contacts à l’EPFL, et à l’occasion de notre venue à Hackarium



#  prod. echopen versionnée

Hyacinthe Lacenne posted this Feb 15, 2016 at 9:09 AM · 1 person applauded

hello à tous,  
  
dans la suite des intuitions de  ![Hyacinthe VINCENT, Libre faiseur at
echopen](./../../zz_assets/images/avatars/1275581.png) Hyacinthe   sur le
versionning de toute la prod.,
vo[ICI](https://github.com/LibreHealthcare/LibreHealthcare)  
l'example de librehealthcare  
  
@++

### **Hyacinthe VINCENT,** - Feb 15, 2016 at 9:51 AM

Oui, c'est bien l'idée.  
Juste un peu surpris par les fichiers "*.org" en plus des "*.md" mais Github à
l'air de savoir les afficher ce qui est intéressant. Je ne connaissais pas ce
format (wiki like).  
Un petit coup de Google -&gt; <http://orgmode.org/fr/index.html> : ça à l'air
intéressant !  
C'est bien beau de découper toute la doc en pages/fiches liées par des tags
et dans une syntaxe textuelle simple mais à un moment il faut générer un site
web (ou un pdf, ou des slides, ...) avec des menus, des hyper liens, un
template... "_Org mode"_ à l'air de se charger de ça (et de beaucoup d'autres
choses aussi). Petit pb, ça a l'air d'être un package d'Emacs.  
A voir si on trouverait un outil équivalent de génération de site web statique
à partir de fichiers sources textuels mais moins exotique.

  * Voir des choses autour de "_Pandoc_" qui, lui, sait convertir chaque page individuellement.
  * Voir aussi <http://jekyllrb.com/> (là c'est du ruby).
  * On préfère du python ... il suffit de demander : <http://hyde.github.io/> (<http://philipm.at/2011/jekyll_vs_hyde.html>).

### **Hyacinthe VINCENT,** - Feb 15, 2016 at 1:37 PM

Il ne faudra par perdre de vue que, si la doc est disséminée partout parmi les
fichiers sources, l'outil de doc devra être capable de collecter les pages
dans une arborescence quelconque et différente de la structure du site web à
produire.



#  un contributeur coréen ;)

Hyacinthe Lacenne posted this Feb 02, 2016 at 8:49 AM · 1 person applauded

nous avons reçu une demande de support pour l'app android de la part de  
Honey Durga Tiwari, pour être complet :  
  
Ph.D. from Department of Electronic, Information and Communication
Engineering, Konkuk University,  Assistant Professor in Department of Computer
Science, Kwangwoon University, Seoul, S. Korea.  
  
il veut displayer un flow de data sur l'app. -&gt; j'ai demandé + d'infos pour
l'accompagner  
  
une fois cela précisé, on échangera sur d'éventuelles interactions
électroniques  
  
-&gt; @hyacinthe : à l'odj de la prochaine réu, demander si certains souhaitent être destinataires des mails de la boîte [contact@echopen.org](mailto:contact@echopen.org) de façon à suivre ce type d'échanges   
  
@++

### **Hyacinthe** - Feb 02, 2016 at 9:56 AM

top.  
  
Pour l'adresse email contact, n'aurions nous pas intérêt à la connecter sur
une sorte de mailing list dans laquelle nous pourrions lancer certains
messages de basecamp en public link ?  
  
Ce qui offre à tous ceux qui souhaitent répondre de se rendre sur le public
link d'une discussion du Basecamp sans avoir besoin de connexion...  
  
Bref, on voit ça à ce moment là.

### **hyacinthe,** - Feb 02, 2016 at 10:03 AM

On pouvait forwarder automatiquement les    sur basecamp2, je ne sais pas  ça
marche sur basecamp3.  
Hyacinthe, tu sais si ya une adresse ?

### **hyacinthe,** - Feb 02, 2016 at 10:38 AM

Sinon, @hyacinthe, ça vaut pas le coup pour des gens en delocalise, de créer un
emulateur qui stream des vraies donnés en boucle ? Histoire qu'ils puissent
essayer sur une pseudo boucle loupée ?

### **Hyacinthe Lacenne** - Feb 02, 2016 at 11:27 AM

déjà proposé - voici le dernier échange en attendant d'organiser l'accès à ce
type d'échange  
  
@+  
  
"Firstly, I wish to thank you for the quick and prompt reply.I will follow
the steps mentioned in your mail to post the feedback on GitHub.

  

I will also follow the DOC for OenCv integration in the project. As for the
streaming data i mean the continuous data coming from a 16 element sensor
probe which will correspondingly changing the display continuously.

I wonder if we will be able to keep the frame refresh rate high enough  given
the high volume of data coming from sensor. I think that although we can do
"scan conversion" with static data, the computation will limit the maximum
refresh rate.However, I also think that first we may worry about accuracy of
the display rather than speed at this moment.Hence, at the moment I require
the help regarding the use of TCP connection for bringing in the sensor data
at high speed to the handheld device and then using it with echOpen.At this
moment i do not have the probe but my associates are working on designing such
a probe.Hence, I am trying to run the echOpen  on a handheld device and bring
the sensor data using TCP where the TCP server may be sitting on some local
network where the sensor data is being refreshed continuously.

Since we already have the TCP and UDP implementations such setup will be a
test example for using TCP /UDP connection with echOpen.I shall be highly
obliged if you could help me to set up and run such a simulation.

I am extremely sorry for the inconvenience and thank you for the help and Once
again thank you for you quick reply.Thank you,With regards,Yours
sincerely,Honey Durga Tiwari

"  
  
  
Hi again Honey Durga Tiwari,  
  
If I understand well, you have some simulated data running on a local TCP
server and you want to bring them in the app. If this is the case, you have
indeed to follow the doc and then I think we'll have to interact together in
order to fine tune the configuration settings that you'll find int the
Hyacinthes class. Moreover our hyacinthes are set in 1 element probe context,
so we should adapt them. We are at disposal to work on that.  
  
If you don't have any simulated data, we could work and ship to you a TCP
server with fake data continuously running on it.  
  
By the way, we will release in one month the full ultrasound probe prototype -
hardware+android app - perhaps we could share our knowledge about that. If so,
we could organize a transpacific hangout. What do you think  ?

…

  

Best regards,

nowami

### **hyacinthe,** - Feb 02, 2016 at 7:50 PM

Sweet !

### **Hyacinthe Lacenne** - Feb 03, 2016 at 8:48 AM

la suite ;)

  
  

Le mer. 3 févr. 2016 à 05:41, Honey Durga Tiwari
&lt;[hdurgatiwari@gmail.com](mailto:hdurgatiwari@gmail.com)&gt; a écrit :

> Respected Sir,  
>  
> Please accept my sincere thanks for sparring your most valuable time in
answering my questions.  
>  
> At the moment I do not have the server with sensor data. My original plan
was to make a local server using some interface with MATLAB where I will model
a simple sensor. Then connect my handheld device to get the sensor data from
server using any wireless interface. Then use this sensor data for conversion
to image and display it using some android application.  
>  
> In the later stage my colleagues will develop a commercial probe which will
send the data using TCP to any application which will do image conversion and
display.  
>  
> I completely understand that the explanation above is vague in every sense
but it is just an overly simplified version of the plan.  
>  
> From my end I will do whatever humanly possible to contribute for the
development of echOpen. It will be an honor for me if I could be of any
assistance.  
>  
> My only request to you is for the help in setting the android studio
environment and running the simulation with whatever input data available to
us at the moment. As I continue to use and understand the system I will keep
discussing and providing you the simulation results.  
>  
> Although I am little bit bound by the funds available to me, in terms of
education or work there is absolutely no bounds for sharing any kind of
information. Hence please let me know the way you think I can work with you.  
>  
> Once again I wish to thank you for all the help extended to me and I
sincerely apologize for any inconvenience caused to you due to me.  
>  
> Thanking you,  
>  
> With regards,  
>  
> Yours sincerely,  
>  
> Honey Durga Tiwari

  
et la réponse  
  
Dear Honey Durga Tiwari,

  
  

Thank you for your response ;)

  
  

I think the best way for us to help you on the TCP side would be to send us
fake data of your TCP server and set correctly the hyacinthes.

  
  

What I propose  you is to have some skype meeting in order for me to show you
what are the main configuration setting that need to be set

in the Hyacinthes class. It will be the opportunity to present you the state
of the art of our work and we will measure the interactions we can have.

  
  

So it is my turn to thank you warmly for the help you want to give to our
team.

  

Do you have any availability these days ?

  

Best regards,

nowami

### **hyacinthe,** - Feb 03, 2016 at 9:20 AM

Gaffe à la license donc, ils font un truc commercial, et tant que y'a pas de
license sur le repo, ils peuvent capturer le code et le mettre sous leur
licence ;)

### **Emilie Mayer,** - Feb 03, 2016 at 9:37 AM

Yes je me demande ce qu'ils font comme sonde exactement...   ![hyacinthe, hardware
thinker at echopen](./../../zz_assets/images/avatars/782574.png) hyacinthe  je ne
comprend pas ta phrase pas de licence sur le repo?

### **hyacinthe,** - Feb 04, 2016 at 5:33 AM

Le repository ne contenait pas de licence, le contenu n'était donc pas
couvert, appropriable possiblement par qqun qui ne voudrait pas mettre le code
sous license ouverte ;)

### **Hyacinthe Lacenne** - Feb 04, 2016 at 10:53 AM

hello,  
  
je ne comprends pas bien car le code de l'app est sous licence depuis qu'on a
eu les éléments de jonathan.  
![Hyacinthe LICCIONI, FPGA at
echopen](./../../zz_assets/images/avatars/1249124.png) Hyacinthe   et  ![Hyacinthe,
Danseur du ventre at echopen](./../../zz_assets/images/avatars/1248689.png)
Hyacinthe  confirment que leur kit-soft est bien sous licence  
  
btw, selon jonathan, il s'agissait de mettre sous contrôle de licence la
racine des repo  
  
@hyacinthe: qu'as tu précisément en tête ?  
  
@+

### **hyacinthe,** - Feb 04, 2016 at 10:59 AM

My bad, la partie license du readme est vide, la mention de la license étant
en tête de fichier :)  
Mes xcuses les plus plates :  
p  
  
Edit: a moins que la mention de le readme ait été ajoutée today ;)

### **hyacinthe,** - Feb 04, 2016 at 12:26 PM

Pour clarifier comment faire, y'a la page gnu.org/licenses/gpl-
faq.html#LicenceCopyOnly qui est bien faite -  
Donc rajouter la mention dans le readme semble lever toute ambiguïté :)

### **Hyacinthe Lacenne** - Feb 04, 2016 at 12:26 PM

en fait, hyacinthe a jouté les mentions dans les readme ce jour et du coup je
les ai ajoutées dans les différents readme du soft  
  
mais à ma connaissance, il y a des des gros proj comme hadoop :
<https://github.com/apache/hadoop>  
  
anyway, je ne connaissais pas ces usages donc updaté  
  
;)



#  Sondes d'occasion

Hyacinthe Lacenne posted this Feb 21, 2016 at 5:31 PM · 1 person applauded

Yop,  
  
ATL a sorti a une époque des sondes trifréquences (5, 7 et 10) et ...
mécaniques.  
Et, oh bonté divine,  ils la vendent à 82$ (plus 40 de livraison, et 20 de
frais de douane).  
  
Ca vaudrait pas le coup de la prendre? Pour :  
\- voir comment elle est concue au global  
\- récupérer 3 transducteurs  
\- voir la mécanique  
  
Let me know!  
  
Topette

### **Hyacinthe Lacenne** - Feb 22, 2016 at 1:00 PM

je plussoie ;)

### **Hyacinthe Lacenne** - Apr 16, 2016 at 5:45 PM

hi hi,  
  
Gabriel Perraud, du hakerspace Nicelab, vient de récupérer une sonde endo-
cavitaire et souhaite la désosser pour comprendre le dispo. Et il nous demande
si ce serait une bonne façon de nous aider. Si vous avez en tête des points
qu'on pourrait leur proposer de faire, et mettre en perspective une
dissémination, je transmets !  
  
btw, on pourrait faire un remote apéro avec le nicelab  
  
@++

### **Hyacinthe Lacenne** - Apr 16, 2016 at 5:49 PM

Sure! Y'a du dessossage deja sur le wiki, categorie retroengineering, sur 3
sondes (et une pas posée apparament pour des questions de PI), il peut s'en
inspirer.  
  
Par contre ca peut etre interessant de savoir des maintenant si il a bien une
sonde méca, et pas un array (il peut communiquer le modele?) =)  
  
Idée : pourquoi pas l'inviter sur le basecamp et le mettre sur un thread dédié
à ce démontage?

### **hyacinthe,** - Apr 18, 2016 at 7:34 PM

Si ça peut aider, j'ai trouvé un mec qui a désossé la même trifrequence que
nous (mec trouve sur geektimes).. Ping @bhyacinthe @hyacinthe  
  

[

![](bc3-raw/files/3845549-screenshot_2016-04-18-21-31-43.png)

](bc3-raw/files/3845549-screenshot_2016-04-18-21-31-43.png)

[ Screenshot_2016-04-18-21-31-43.png  486 KB • Download
](bc3-raw/files/3845549-screenshot_2016-04-18-21-31-43.png)

### **Hyacinthe Lacenne** - Apr 24, 2016 at 4:04 PM

Quoi de neuf pour ce hacker de sonde?

### **Hyacinthe Lacenne** - Apr 25, 2016 at 7:05 AM

il me dit qu'il est en partiel jusqu'à fin mai et qu'il commence le désossage
cet été ;)

### **Hyacinthe Lacenne** - Jun 18, 2016 at 2:37 PM

![Hyacinthe Lacenne, echopen](./../../zz_assets/images/avatars/782178.png)
lacenne   Faut lui dire  qu'on a fait remarcher la notre sur :
<https://github.com/hyacinthe124/echomods/tree/master/retro10PV>

### **Hyacinthe Lacenne** - Jun 30, 2016 at 9:47 AM

Deux sondes d'occasions assez sympa pour démontage et analyse (mécanique /
materiaux / piezos):  
<http://www.ebay.com/itm/Philips-ATL-Access-A-3Mhz-Ultrasound-Scanhead-
Transducer-Probe-/262496926313?hash=item3d1e093a69:g:psAAAOSwcL5XMe0n> (50$)  
<http://www.ebay.com/itm/Hitachi-Ultrasound-Probe-EZU-
PM3-/400943782280?hash=item5d5a1c9988:g:cdAAAOSwyQtVga8m> (30$)

