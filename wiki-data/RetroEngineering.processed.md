

# IR1510AK

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# James Mehi

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# ATL A6-3

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# James I. Mehi

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Thomas Nefos

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Susumu Enjoji

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Category:TechTeam

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Nefos Thomas P

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Donald J. Nisler

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Yushichi Kikuchi

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Jonathan Ophir

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# EchOpen on GitHub

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# GitHub

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Kiyoshi Hara

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Roger Michael Costello

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>





# IR1510AK

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# James Mehi

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# ATL A6-3

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# James I. Mehi

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Thomas Nefos

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Susumu Enjoji

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Category:TechTeam

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Nefos Thomas P

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Donald J. Nisler

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Yushichi Kikuchi

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Jonathan Ophir

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# EchOpen on GitHub

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# GitHub

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Kiyoshi Hara

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Roger Michael Costello

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Stewart Gavin Bartlett

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Social Impact

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Xiaohui Hao

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Dymax Corporation

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Thomas G. Cooper

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Howard F. Fidel

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Nicholas Christopher Chaggares

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# A6-3

Démontage d'une sonde abdominale, multi-éléments annulaires.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schema.png "fig:Photographie de la sonde S-VRW77AK."){width="500"}
La sonde se décompose essentiellement en 2 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Enveloppe : regroupe l'élément piézoéletrique, la motorisation et
    l'électronique

Beaucoup plus compacte que les deux autres sondes démontées par echOpen,
elle se différencie particulièrement par la nature de sa motorisation,
qui n'est pas générée par un mouvement de rotation mais par un mouvement
de translation, au moyen d'un verin.

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](connecteur_A6-3.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier comprenant 2x130 petits picots,
regroupés de part et d'autre d'un picot central. Ce connecteur est
particulièrement grand, puisque sa taille est supérieure à celle de la
sonde elle même, et les raisons de telles dimensions seraient de nature
historiques.

### Partie interne

Démontage de l'enveloppe
------------------------

Pics :

<File:ATL.jpg> <File:ALT2.jpg> <File:Structure> intérieure.jpg

<Category:TechTeam> <Category:RetroEngineering>



# Github

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Robert McConaghy

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# F. Stuart Foster

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Réunion - 28 Mars 2015

Le but serait de re-créer une sonde à partir de matériaux existants:

-   Transducteurs déjà assemblés de chez Alibaba
-   Moteurs

Approches aujourd'hui
---------------------

### Exemples concrets de sondes à analyser

-   On a une sonde [IR1510AK](IR1510AK "wikilink") trouvée sur ebay
    @70USD (sonde en cours de démontage, détails sur
    [IR1510AK](IR1510AK "wikilink")).
-   Une autre KRETZ TECHNICK [S-VRW77AK](S-VRW77AK "wikilink") (IPX7)
    ULTRASOUND PROBE TRANSDUCER
    -   <http://www.accessdata.fda.gov/cdrh_docs/pdf/K940942.pdf> pour
        la fiche
    -   <http://www.icacommission.org/Proceedings/ICA1998Seattle/pdfs/vol_2/1069_1.pdf>
        pour les usages
-   Une ATL / Philips [A6-3](A6-3 "wikilink") (The ATL A6-3 has a wide
    aperature and has a frequency range of 3 to 6 MHz. - Annular array
    probe // Wide aperature // Mechanical sector )
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>

### MAteriel à récupérer

-   Sondes en général : les sondes à retroengineerer sont les suivantes:
    -   sondes mécaniques sectorielles
    -   sondes mécaniques mono-élément
    -   sondes à balayage
    -   "wobbler probes"
-   Celles à ne pas récupérer sont:
    -   sondes à matrice
    -   sondes multiélément
    -   sondes linéaires/sondes linéaires courbes
    -   sondes à balayage électronique

### Approche raspberry pi

-   Existant : démonstration d'un sonar
-   

Sourcing Potentiel
------------------

### Electronique

### Neuf mais ...

### Occasion

-   leboncoin : meilleur prix, 400€ used
    -   <http://www.leboncoin.fr/materiel_medical/747007800.htm>
    -   <http://www.leboncoin.fr/materiel_medical/781199518.htm?ca=12_s>
-   tous les sites de sourcing de matériel d'occasion..
    -   <http://bestengineer.chez.com/ultrasound.html>
    -   <http://www.dotmed.com/listing/vet.-ultrasound/kontron/sigma-1ac-&-2-probes/1194647>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/instruments-w-5-mhz-ds-type-:-wobbler-ultrasound-transducer-probe/1557682>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/5-mhz-b-/1557669>
    -   <http://www.umed-ultrasound.com/StockSondes_KONTRON.htm>
-   Autres
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=sonde+ultrasons>
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=echographe>
    -   <http://medical.fr/fr/1105-sonde>?&orderby=price&orderway=asc
    -   <http://www.dotmed.com/listings/search/equipment.html?key=wobbler&type=equipment>
    -   <http://www.ebay.com/sch/i.html?_odkw=sector+ultrasound&_sop=3&_from=R40&_osacat=0&_ssc=1&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xwobbler+ultrasound&_nkw=wobbler+ultrasound&_sacat=0>
-   A suivre
    -   <http://www.ebay.com/itm/Aloka-ASU-32CWD-5-Mechanical-Doppler-Probe-/331496509627>?
    -   <http://www.ebay.com/itm/GE-2-5-48S-P-N-45-231613G1-Sector-Ultrasound-Transducer-Probe-/111626681515?pt=LH_DefaultDomain_0&hash=item19fd77fcab>
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>
        -- ATL / Philips A6-3

Manuels
-------

-   <http://www.frankshospitalworkshop.com/equipment/documents/ultrasonographs/user_manuals/Kontron_Sigma_1_-_Usermanual.pdf>

<Category:TechTeam> <Category:RetroEngineering>



# Richard A. Terwilliger

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# John W. Sliwa

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# S-VRW77AK

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Talk:Sonoline SX

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Approche Hacking de l'existant

Le but serait de re-créer une sonde à partir de matériaux existants:

-   Transducteurs déjà assemblés de chez Alibaba
-   Moteurs

Approches aujourd'hui
---------------------

### Exemples concrets de sondes à analyser

-   On a une sonde [IR1510AK](IR1510AK "wikilink") trouvée sur ebay
    @70USD (sonde en cours de démontage, détails sur
    [IR1510AK](IR1510AK "wikilink")).
-   Une autre KRETZ TECHNICK [S-VRW77AK](S-VRW77AK "wikilink") (IPX7)
    ULTRASOUND PROBE TRANSDUCER
    -   <http://www.accessdata.fda.gov/cdrh_docs/pdf/K940942.pdf> pour
        la fiche
    -   <http://www.icacommission.org/Proceedings/ICA1998Seattle/pdfs/vol_2/1069_1.pdf>
        pour les usages
-   Une ATL / Philips [A6-3](A6-3 "wikilink") (The ATL A6-3 has a wide
    aperature and has a frequency range of 3 to 6 MHz. - Annular array
    probe // Wide aperature // Mechanical sector )
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>

### MAteriel à récupérer

-   Sondes en général : les sondes à retroengineerer sont les suivantes:
    -   sondes mécaniques sectorielles
    -   sondes mécaniques mono-élément
    -   sondes à balayage
    -   "wobbler probes"
-   Celles à ne pas récupérer sont:
    -   sondes à matrice
    -   sondes multiélément
    -   sondes linéaires/sondes linéaires courbes
    -   sondes à balayage électronique

### Approche raspberry pi

-   Existant : démonstration d'un sonar
-   

Sourcing Potentiel
------------------

### Electronique

### Neuf mais ...

### Occasion

-   leboncoin : meilleur prix, 400€ used
    -   <http://www.leboncoin.fr/materiel_medical/747007800.htm>
    -   <http://www.leboncoin.fr/materiel_medical/781199518.htm?ca=12_s>
-   tous les sites de sourcing de matériel d'occasion..
    -   <http://bestengineer.chez.com/ultrasound.html>
    -   <http://www.dotmed.com/listing/vet.-ultrasound/kontron/sigma-1ac-&-2-probes/1194647>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/instruments-w-5-mhz-ds-type-:-wobbler-ultrasound-transducer-probe/1557682>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/5-mhz-b-/1557669>
    -   <http://www.umed-ultrasound.com/StockSondes_KONTRON.htm>
-   Autres
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=sonde+ultrasons>
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=echographe>
    -   <http://medical.fr/fr/1105-sonde>?&orderby=price&orderway=asc
    -   <http://www.dotmed.com/listings/search/equipment.html?key=wobbler&type=equipment>
    -   <http://www.ebay.com/sch/i.html?_odkw=sector+ultrasound&_sop=3&_from=R40&_osacat=0&_ssc=1&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xwobbler+ultrasound&_nkw=wobbler+ultrasound&_sacat=0>
-   A suivre
    -   <http://www.ebay.com/itm/Aloka-ASU-32CWD-5-Mechanical-Doppler-Probe-/331496509627>?
    -   <http://www.ebay.com/itm/GE-2-5-48S-P-N-45-231613G1-Sector-Ultrasound-Transducer-Probe-/111626681515?pt=LH_DefaultDomain_0&hash=item19fd77fcab>
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>
        -- ATL / Philips A6-3

Manuels
-------

-   <http://www.frankshospitalworkshop.com/equipment/documents/ultrasonographs/user_manuals/Kontron_Sigma_1_-_Usermanual.pdf>

<Category:TechTeam> <Category:RetroEngineering>



# Stuart Foster

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Talk:Sonoline 3000

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Sevig Ayter

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# David L. Greenwood

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>




# Stewart Gavin Bartlett

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Social Impact

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Xiaohui Hao

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Dymax Corporation

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Thomas G. Cooper

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Howard F. Fidel

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Nicholas Christopher Chaggares

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# A6-3

Démontage d'une sonde abdominale, multi-éléments annulaires.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schema.png "fig:Photographie de la sonde S-VRW77AK."){width="500"}
La sonde se décompose essentiellement en 2 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Enveloppe : regroupe l'élément piézoéletrique, la motorisation et
    l'électronique

Beaucoup plus compacte que les deux autres sondes démontées par echOpen,
elle se différencie particulièrement par la nature de sa motorisation,
qui n'est pas générée par un mouvement de rotation mais par un mouvement
de translation, au moyen d'un verin.

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](connecteur_A6-3.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier comprenant 2x130 petits picots,
regroupés de part et d'autre d'un picot central. Ce connecteur est
particulièrement grand, puisque sa taille est supérieure à celle de la
sonde elle même, et les raisons de telles dimensions seraient de nature
historiques.

### Partie interne

Démontage de l'enveloppe
------------------------

Pics :

<File:ATL.jpg> <File:ALT2.jpg> <File:Structure> intérieure.jpg

<Category:TechTeam> <Category:RetroEngineering>



# Github

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Robert McConaghy

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# F. Stuart Foster

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>





# IR1510AK

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# James Mehi

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# ATL A6-3

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# James I. Mehi

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Thomas Nefos

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Susumu Enjoji

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Category:TechTeam

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Nefos Thomas P

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Donald J. Nisler

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Yushichi Kikuchi

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Jonathan Ophir

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# EchOpen on GitHub

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# GitHub

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Kiyoshi Hara

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Roger Michael Costello

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Introduction to Mechanical probes

Introduction to Mechanical probes
---------------------------------

### Page 1

![](000.png "000.png"){width="400"}

### Page 2

![](001.png "001.png"){width="400"}

<Category:Historique> <Category:Sonde> <Category:Balayage>
<Category:TechTeam>



# Stewart Gavin Bartlett

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Prototype

<div style="float:right;">
\_\_TOC\_\_

</div>
WORK IN PROGRESS
================

Le prototypage a commencé en février 2015 et les différents chantiers
ont été lancés conjointement.

L'objectif est de produire une première sonde fonctionnelle d'ici la fin
de l'année 2015 pour présenter ce prototype le 17 février 2016,
bicentenaire de l'invention du stéthoscope par Laennec.

Development [Planning](Planning "wikilink")
===========================================

The sensor developed by Echopen is a culmination requiring several steps
and different prototypes in order to control each component . Each of
these prototypes is studied in stages, kinds of micro challenges to
mobilize the community wishing to participate in their development:

-   [Protaud](Protaud "wikilink") (V0.0)
-   [Michaud](Michaud "wikilink") (V0.1)
-   [Neaud](Neaud "wikilink") (V1.0)

An overview of the project is also available so you can discover,
explore plug and participate at our work
[planning](planning "wikilink").

![](computer248.png "fig:computer248.png"){width="20"} Hardware
===============================================================

Une sonde, comme nous la concevons, est l'assemblage d'un transducteur
(piézo + backing), d'un beamformer et des l'électronique nécéssaire à
l'emission d'un signal envoyé vers l'application qui pourra ainsi la
transformer en image échographique, lisible par un professionnel de
santé.

Cahier des charges
------------------

-   [Cahier des charges V0.0](Cahier_des_charges_V0.0 "wikilink")
-   [Cahier des charges V0.1](Cahier_des_charges_V0.1 "wikilink")
-   [Cahier des charges V1.0](Cahier_des_charges_V1.0 "wikilink")

**Une première synthèse d'outil serait le Kit
[Protaud](Protaud "wikilink"), compatible avec la V0.**

Le transducteur
---------------

Le développement du transducteur est conduit actuellement tous les jeudi
au laboratoire Satie de l'ENS Cachan dont le [Carnet de bord -
Laboratoire SATIE](Carnet_de_bord_-_Laboratoire_SATIE "wikilink") donne
les principaux éléments.

L'électronique
--------------

La partie [électronique](électronique "wikilink") a commencé pendant
l'été 2015

### Microcontroleur

### Code microcontroleur

### Motor controlling

#### Basic charactics

The motor that we use are a motor of small dimensions includes an
encoder able to determine the rotation and speed. Boasting a high
quality construction and a very competitive price, it has a reduction
ratio of 1:57.     The encoder and the motor power supply are accessible
via a 10 cm cable terminated by a female connector 6 points. This
connector is directly provided to receive an optional control module
provided at the bottom of the page.

Characteristics:

-   Power supply: 6 Vdc
-   Power consumption: &lt;= 240 mA
-   Torque: 617 g-cm
-   Speed: 126 rpm
-   No load speed: 152 rpm

![ 600 px](motor.JPG  " 600 px")

-   Signals on the connector:
-   COLOR FUNCTION
    -   Black -&gt; Motor +
    -   Red -&gt; Motor-
    -   Brown -&gt; VCC
    -   green -&gt; GND
    -   Blue -&gt; SA
    -   Violet-&gt; SB

More information can be found in the site LEXTRONIC
[1](http://www.lextronic.fr/P5448-moteur-reducteur-avec-encodeur.html)

#### Test of the motor

The connection of the arduino and the motor can be found in the site
DIGILENT
[2](http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,401,503&Prod=PMOD-HB5)

![ 600 px](motor connection.jpg  " 600 px")

As we haven't the Motor shield, we build a simple motor control circuit
thanks to this blog
[3](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors/overview)

![ 400 px](circuit-arduino.jpg  " 400 px")

Now we can build the circuit around the motor:

![](connection motor-encoder-arduino.png "connection motor-encoder-arduino.png")

Other composants that we need are:

1, Resistor 10 kOhms x 2;

2, Transistor PN2222 x 1;

3, 1N4001 diode x 1;

4, 270 Ω Resistor (red, purple, brown stripes) x 1;

5, Half-size Breadboard x 1;

6, Jumper wire pack;

7, Un potentiometer

#### Reading Rotary Encoders

There are manyopen sources in the Arduino Playground
[4](http://playground.arduino.cc/Main/RotaryEncoders) Below is an image
showing the waveforms of the A & B channels of an encoder.

![600 px](encoder function.jpg  "600 px")

the motor and the encoder turns as 1:57,

After connecting the motor and arduino together with a potentiometer. We
can test the output of SA and SB by the code below:

<code>

`/* Read  Encoder`\
` * Connect Encoder to Pins encoder0PinA, encoder0PinB, and +5V, GND.`\
` */  `\
`double motorVelocity = 0;`\
`int val; `\
\
`// direction of motor is decided by changing the motor+ and motor-`\
\
`int pinIntensityMotor = 6;`\
\
`int pinPotentiometre = A5;`\
\
`int encoder0PinA = A1; `\
\
`int encoder0PinB = A3;`\
\
`int encoder0Pos = 0;`\
\
`int encoder0PinALast = LOW;`\
\
`int n = LOW; `\
\
`int speed=100;`\
\
`void setup() { `\
`  `\
`  pinMode(pinIntensityMotor, OUTPUT);`\
`  pinMode (encoder0PinA,INPUT);`\
`  pinMode (encoder0PinB,INPUT);`\
`  Serial.begin (9600);`\
`} `

</code>

<code>

`/* utilise the potentiometer to change the speed of the motor and read the encoder`\
\
`void loop() { `\
\
`   val = analogRead(pinPotentiometre);    // read the value from the sensor`\
`motorVelocity = (double)((val/1023.0)*255.0);`

</code> <code>

`if (motorVelocity < 100){`\
`  motorVelocity=0;`\
`}`

</code> <code>

`analogWrite(pinIntensityMotor, motorVelocity);`\
` `\
`  n = digitalRead(encoder0PinA);`

</code>

<code> if ((encoder0PinALast == LOW) && (n == HIGH)) {

`    if (digitalRead(encoder0PinB) == LOW) {`\
`      encoder0Pos--;`\
`    } else {`\
`      encoder0Pos++;`\
`    }`

</code> <code>

`  Serial.print (encoder0Pos);`\
`  Serial.print ("\n");`\
`  } `\
`  encoder0PinALast = n;`\
\
`} `

</code>

Open the monotoring window in ARDUINO IDE to observe the plus in the
encoder： ![ 800 px](test of encoder.jpg  "fig: 800 px")

### Construire l'Alimentation

#### Scheme 1 : Build 'High Voltage Power Supply' (HVPS)

L'Ardunio DUE travaille à 3.3V, mais le transducteur piézoélectrique
fonctionne habituellement à 100-300V, il semble donc obligé de
construire un système d'alimentation à haute tension afin de générer de
haute inpulse pour faire fonctionner le transducteur.

Pour obtenir de haute tension réglable, nous allons transformer le
courant continu réglable de les LVPS en courant alternatif réglable à
une fréquence d'environ, au moyen d'un oscillateur LC. Puis, un
transformateur de step-up sera utilisé pour obtenir AC haute tension,
qui peut être transformé en courant continu avec une demi-onde de
tension redresseur doubleur. Voici le schéma de principe:

![ 600 px](schema-HVPS.jpg  " 600 px")

Voici un schéma électronique et la simulation sur NI Multisim

![ 600 px](schema-1.jpg  " 600 px")

Le résultat de la simulation:

![ 600 px](Test result-3.3v,N0.35.jpg  " 600 px")

<http://forums.futura-sciences.com/electronique/704890-arduino-amplification-voltage-100v.html>

In order to amplify the signal, we need a square waveform 5 V high. The
digital outputs of the arduino are only 3.3 V high, so had to built a
little circuit to do that. The arduino has a 5 V direct courant output,
so with a transistor it is possible to have the desire signal with this
:

![400 px|center](crenelleur_scéma.png "400 px|center")

![400 px|center](crenelleur_bb.png "400 px|center")

There are two 1000 Ohm resistors and a PN2222 transistor. With a
blinking code we access to a 150 kHz signal with a 5 V amplitude this
lead to a 70 V direct currant signal. This frequency of 150 kHz is the
maximal frequency we can access with the classical digitalWrite function
of the arduino. Is it possible to increase this frequency by using more
low level function such as :

`REG_PIOB_SODR = 0x1 << 27;`\
`REG_PIOB_CODR = 0x1 << 27;`

this two lines replace the digitalWrite function. With this script, it
possible to access to a 10 MHz signal!

So with this new function, we have tried to increase the frequency of
the square waveform input signal, but the amplitude of the direct output
current does not increase more than the one we obtained at 150 kHz.

#### Scheme 2 :Build a boost converter

After discussions with John Norman, Director of NTS Ultrasonics Pty
Ltd[5](http://www.ntsu.net.au/), he proposed us a 30-60VDC/DC boost
calculator[6](https://learn.adafruit.com/diy-boost-calc/overview).

![](boost calculator.jpg "boost calculator.jpg")

by turning on and turning of Q2, the output can be controlled by the PWM
pin of a microcontroller.

To build this circuit, all the materials needed are :

# Diode 1N5817 X1;
2.  MosFET 1RFD 110 X1;
3.  DC supply baterry 9V x1;
4.  capacitor 47uF x1, 33uFx1, 0.1 uFx1;
5.  Inductance 2200uHx1;

See [Theory of the Boost Converter](Boost_Converter "wikilink")

After test on Multisim, we I find that the parametres of the composants
are very important. Actually, we have to calculator the current first by
the calculator cited in this site. In our case, we want to get an DC
between 0 to 200V, so the maximum output is 200V. A potentiometer is
used to change the output. The circuit are as follows:

![ 1000 px](HVPS-5V-200V.png " 1000 px")

#### The drive circuit

We use the HVPS to provide high DC voltage, and the drive circuit is
then designed as follows: The drive circuit: ![ 1000
px](The drive circuit.png "fig: 1000 px")

### Test of the electronic circuit

At the beginning, we have test the boost converter with a DC lab power
supply 0-30 V. So we have first put a 30 V VCC signal, without
transducer we obtain this kind of signal with a 2.5 us pulse from input
(yellow):

![400 px|center](pulser_signal.jpg "400 px|center")

where, in blue we have a negative pulse (-7.8 V) and after a rebound
with a positive tension (+0.8 V). After we have put a transducer in
water, by plugging the transducer on the circuit the signal is now of
this type:

![400 px|center](pulser_transducer.jpg "400 px|center")

where the negative pulse is -2.6 V high and the rebound is +1.16 V high.
With this set-up, the transducer emit a signal which is reflected by the
border of the container where the transducer is putted:

![400 px|center](echo.jpg "400 px|center")

which is 212 mV peak to peak high.

By using our HVPS, we now have a 55V VCC, but this signal is noisy. The
sending an receiving signal to the transducer is also noisy:

![](noisy_signal.jpg "noisy_signal.jpg"){width="400"}

The negative pulse is now -2.2 V high with the transducer. The echo is
89.6 mV amplitude peak to peak.

La mécanique
------------

### Motor

### Pièces mécaniques

### Collecteur

Retro-ingénierie de sondes
--------------------------

Cf la page [Approche Hacking de
l'existant](Approche_Hacking_de_l'existant "wikilink")

![](smartphone8.png "fig:smartphone8.png"){width="20"} Software
===============================================================

Les premières bases du développement de l'application sont disponibles
sur le compte-rendu du [Design & Code
Camp](Design_&_Code_Camp "wikilink") du 16 mai 2015. Et la page dédiée
au développement du [software echopen](software_echopen "wikilink")

### Inspirations

[vula](http://www.vulamobile.com/) : une application mobile pour
réaliser des examens des yeux | [Pour plus
d'informations](http://bopobs.com/2015/04/16/vula-mobile-faciliter-soins-ophtalmologiques-en-afrique/)

How to protect the receiving part ? See [Clipping
test](Clipping_test "wikilink")

The Emile test
==============

Presentation
------------

BOM
---

Schematics
----------

Setup
-----

Measurements
------------

Display
-------

See [Red Pitaya WebApp](Red_Pitaya_WebApp "wikilink")

Des ressources clé
==================

<File:Experimental> System Prototype of a Portable US Device.pdf
<File:HARDWARE> AND SOFTWARE IMPROVEMENT OF LOW COST US MACHINE.pdf
<File:Hardware-Software> Partitioning of US probes.pdf <File:Low-Cost>
Digital Ultrasound Beamformer Design using Field Programmable Gate
Arrays.pdf <File:Low-Power> Receive-Electronics for 3D Ultrasound.pdf
<File:Design> of an Open-Architecture Ultrasound Acquisition System for
Real-Time Processing and Control.pdf <File:Design> of Low-Cost Portable
Ultrasound systems.pdf

Biblio
======

<Category:TechTeam> <Category:HardIntroduction>



# Social Impact

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Xiaohui Hao

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Talk:Les statuts de l'association

The aim of the technical stake is to solve the question: how can we
build an open-source portable echograph with a community?

Hardware
--------

Before starting, we recommend you get a read of [ Introduction to the
echopen hardware](:Category:HardIntro "wikilink") to get to know the
technical aspects and engineering behind the artifact.

Kits and products
-----------------

Given the nature of the product, a tool to be used by health
professional, echopen is facing the issue of

Engineering
===========

Obviously, there are a couple of questions that are lurking around, such
as:

-   How to build an [Open-source
    Hardware](Open-source_Hardware "wikilink") - what guidelines to be
    used?
    -   We had first guidelines on our [ first big
        challenge](Challenge:_the_echOpen_shield#Questions "wikilink")
    -   How to document on a wiki: it's easy to push code on github,
        much less with physical objects =)

Pending work
------------

-   Progress being done at the [ENS](ENS "wikilink") with [
    Constant](User:Constant_Bourdeloux "wikilink") : [Carnet de bord -
    Laboratoire SATIE](Carnet_de_bord_-_Laboratoire_SATIE "wikilink")
    for the transducer [EchOpen
    Transducer‎](EchOpen_Transducer‎ "wikilink")
-   Some hacking of previous probes such as the [ATL
    A6-3](ATL_A6-3 "wikilink"), the [S-VRW77AK](S-VRW77AK "wikilink"),
    or [IR1510AK](IR1510AK "wikilink") are on [Approche Hacking de
    l'existant](Approche_Hacking_de_l'existant "wikilink"): we do love
    [Kretztechnik](:Category:Kretztechnik "wikilink") for the beauty,
    simplicity and robustness of their design !
-   Building the echOpen tranducer

Done
----

-   Hardware
    -   17/10/2015: Structuring our knowledge on hardware : a must read
        page is
    -   02/10/2015: We built our first kit : Category:Emile
    -   01/07/2015 En apprendre plus sur le
        [Balayage](Balayage "wikilink") en général, une [Introduction to
        Mechanical
        probes](Introduction_to_Mechanical_probes "wikilink"), et voir
        la [Old Devices list](Old_Devices_list "wikilink"), et apprendre
        ce qui s'est fait dans les
        [Premières\_années](Premières_années "wikilink")
        de l'échographie.
-   Intellectual property
    -   04/04/2015 : listing interesting patents at
        [:Category:Patents](:Category:Patents "wikilink") and inventors
        [:Category:CoolHand](:Category:CoolHand "wikilink").
-   Signal processing:
    -   14/10/2015: Having fun with [ FFT Filtering and signal
        processing](Compressing_with_FFT "wikilink").

Bibliography
------------

<Category:TechTeam> <Category:Sonde> <Category:HardIntroduction>
<Category:HardIntroduction>



# Dymax Corporation

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Thomas G. Cooper

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Howard F. Fidel

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Nicholas Christopher Chaggares

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# A6-3

Démontage d'une sonde abdominale, multi-éléments annulaires.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schema.png "fig:Photographie de la sonde S-VRW77AK."){width="500"}
La sonde se décompose essentiellement en 2 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Enveloppe : regroupe l'élément piézoéletrique, la motorisation et
    l'électronique

Beaucoup plus compacte que les deux autres sondes démontées par echOpen,
elle se différencie particulièrement par la nature de sa motorisation,
qui n'est pas générée par un mouvement de rotation mais par un mouvement
de translation, au moyen d'un verin.

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](connecteur_A6-3.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier comprenant 2x130 petits picots,
regroupés de part et d'autre d'un picot central. Ce connecteur est
particulièrement grand, puisque sa taille est supérieure à celle de la
sonde elle même, et les raisons de telles dimensions seraient de nature
historiques.

### Partie interne

Démontage de l'enveloppe
------------------------

Pics :

<File:ATL.jpg> <File:ALT2.jpg> <File:Structure> intérieure.jpg

<Category:TechTeam> <Category:RetroEngineering>



# Github

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Robert McConaghy

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# F. Stuart Foster

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Sonic Window

The aim of the technical stake is to solve the question: how can we
build an open-source portable echograph with a community?

Hardware
--------

Before starting, we recommend you get a read of [ Introduction to the
echopen hardware](:Category:HardIntro "wikilink") to get to know the
technical aspects and engineering behind the artifact.

Kits and products
-----------------

Given the nature of the product, a tool to be used by health
professional, echopen is facing the issue of

Engineering
===========

Obviously, there are a couple of questions that are lurking around, such
as:

-   How to build an [Open-source
    Hardware](Open-source_Hardware "wikilink") - what guidelines to be
    used?
    -   We had first guidelines on our [ first big
        challenge](Challenge:_the_echOpen_shield#Questions "wikilink")
    -   How to document on a wiki: it's easy to push code on github,
        much less with physical objects =)

Pending work
------------

-   Progress being done at the [ENS](ENS "wikilink") with [
    Constant](User:Constant_Bourdeloux "wikilink") : [Carnet de bord -
    Laboratoire SATIE](Carnet_de_bord_-_Laboratoire_SATIE "wikilink")
    for the transducer [EchOpen
    Transducer‎](EchOpen_Transducer‎ "wikilink")
-   Some hacking of previous probes such as the [ATL
    A6-3](ATL_A6-3 "wikilink"), the [S-VRW77AK](S-VRW77AK "wikilink"),
    or [IR1510AK](IR1510AK "wikilink") are on [Approche Hacking de
    l'existant](Approche_Hacking_de_l'existant "wikilink"): we do love
    [Kretztechnik](:Category:Kretztechnik "wikilink") for the beauty,
    simplicity and robustness of their design !
-   Building the echOpen tranducer

Done
----

-   Hardware
    -   17/10/2015: Structuring our knowledge on hardware : a must read
        page is
    -   02/10/2015: We built our first kit : Category:Emile
    -   01/07/2015 En apprendre plus sur le
        [Balayage](Balayage "wikilink") en général, une [Introduction to
        Mechanical
        probes](Introduction_to_Mechanical_probes "wikilink"), et voir
        la [Old Devices list](Old_Devices_list "wikilink"), et apprendre
        ce qui s'est fait dans les
        [Premières\_années](Premières_années "wikilink")
        de l'échographie.
-   Intellectual property
    -   04/04/2015 : listing interesting patents at
        [:Category:Patents](:Category:Patents "wikilink") and inventors
        [:Category:CoolHand](:Category:CoolHand "wikilink").
-   Signal processing:
    -   14/10/2015: Having fun with [ FFT Filtering and signal
        processing](Compressing_with_FFT "wikilink").

Bibliography
------------

<Category:TechTeam> <Category:Sonde> <Category:HardIntroduction>
<Category:HardIntroduction>



# EchOpen Transducer

Transducteur acoustique d'echOpen
=================================

Qu'est-ce qu'un transducteur piézoélectrique ?
----------------------------------------------

![Schéma d'une capsule
piézoélectrique](SchemaPiezo.gif "fig:Schéma d'une capsule piézoélectrique")
Un transducteur est un dispositif permettant de convertir une grandeur
physique en une autre. Par exemple, un haut-parleur transforme un signal
électrique en ondes acoustiques.\
Une sonde échographique requiert justement un transducteur
électro-acoustique. Nous n'allons pas utiliser un haut-parleur mais un
transducteur piézoélectrique. Le fonctionnement de ce dernier est
simple. Sous une contrainte mécanique, la capsule piézoélectrique se
polarise, induisant une tension entre ses bornes (effet piézoélectrique
direct). Inversement, sous l'effet d'un champ électrique la capsule
piézoélectrique se déforme (effet piézoélectrique indirect).

Cahier des charges
------------------

Le transducteur doit respecter plusieurs contraintes techniques.

-   Focalisation à 10 cm.
-   Fréquence centrale de 3,5, 5,5 et 7,5 MHz

Evidemment, un transducteur a une fréquence centrale fixée ce qui
nécessite de concevoir trois transducteurs différents.

Solution technique retenue
--------------------------

Pour l'instant nous ne fabriquons pas nos propres capsules
piézoélectriques. Nous avons acheté des capsules piézoélectriques
concaves (focalisation à 10 cm) en Pz27 chez Ferroperm. Elles ont un
diamètre de 1,5 cm.\
\
Nous venons de terminer la conception du backing pour le transducteur.
Le backing est un élément essentiel du transducteur. Il permet d'éviter
une résonnance néfaste des ondes acoustiques dans le cristal
piézoélectrique. Sans cet élément il est impossible d'obtenir des images
échographiques. Avec ce backing nous avons maintenant un transducteur
fonctionnel.\
\
La conception de cet élément nécessite du temps puisqu'il faut faire de
nombreux essais expérimentaux pour obtenir un résultat concluant.
Finalement, nous avons bien un backing caractérisé par son impédance
acoustique de 4,5 MRayl, homogène. Notre backing est un mélange de
poudre de verre, de poudre de tungstène et de colle époxy. Voici le
tableau récapitulatif de nos essais : [:File:Tableau de suivi des essais
de
backing.pdf](:File:Tableau_de_suivi_des_essais_de_backing.pdf "wikilink").\
\
Afin d'améliorer la qualité de notre sonde, nous souhaitons ajouter une
lame adaptatrice d'impédance acoustique en sortie du transducteur (sur
la face concave). C'est un défi technologique à relever puisque cette
lame a une épaisseur de 0,1 mm et doit épouser une surface concave.

Backing
-------

### Composition

La composition pour un backing à 4,5 MRayl homogène est la suivante.

-   Colle époxy (type SADER) : 3,0 g.
    -   Durcisseur : 1,5 g.
    -   Résine : 1,5 g.
-   Poudre de tungstène (grain 12 µm) : 3,4 g.
-   Poudre de verre (grain 12 µm) : 1,0 g.

Il faut respecter les proportions de chaque composants. Les masses ne
sont données qu'à titre indicatif.

### Processus de fabrication

Six étapes sont indispensables pour concevoir un backing fonctionnel.

-   Ajouter les composants sus-cités dans un contenant ouvert
    (type bécher).
-   Mélanger et homogénéiser.
-   Dégazer le mélange sous vide.
-   Couler le mélange dans un moule.
-   Dégazer le mélange sous vide.
-   Laisser polymériser (à température ambiante ou à l'étuve).

Piézoélectrique et backing
--------------------------

L'assemblage de la capsule piézoélectrique et du backing se fait en dix
étapes.

-   Coller un fil électrique sur la face convexe de la capsule.
-   Ajouter les composants nécessaires au backing dans un contenant
    ouvert (type bécher).
-   Mélanger et homogénéiser.
-   Dégazer le mélange sous vide.
-   Placer la capsule piézoélectrique dans un moule adapté, face concave
    au fond en laissant ressortir le fil électrique.
-   Couler le mélange du backing dans le moule, sur la
    capsule piézoélectrique.
-   Dégazer le mélange sous vide.
-   Laisser polymériser (à température ambiante ou à l'étuve).
-   Démouler.
-   Coller un deuxième fil électrique sur la face concave de la capsule.

\

<Category:Sonde> <Category:Balayage> <Category:Transducer>
<Category:TechTeam>



# Réunion - 28 Mars 2015

Le but serait de re-créer une sonde à partir de matériaux existants:

-   Transducteurs déjà assemblés de chez Alibaba
-   Moteurs

Approches aujourd'hui
---------------------

### Exemples concrets de sondes à analyser

-   On a une sonde [IR1510AK](IR1510AK "wikilink") trouvée sur ebay
    @70USD (sonde en cours de démontage, détails sur
    [IR1510AK](IR1510AK "wikilink")).
-   Une autre KRETZ TECHNICK [S-VRW77AK](S-VRW77AK "wikilink") (IPX7)
    ULTRASOUND PROBE TRANSDUCER
    -   <http://www.accessdata.fda.gov/cdrh_docs/pdf/K940942.pdf> pour
        la fiche
    -   <http://www.icacommission.org/Proceedings/ICA1998Seattle/pdfs/vol_2/1069_1.pdf>
        pour les usages
-   Une ATL / Philips [A6-3](A6-3 "wikilink") (The ATL A6-3 has a wide
    aperature and has a frequency range of 3 to 6 MHz. - Annular array
    probe // Wide aperature // Mechanical sector )
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>

### MAteriel à récupérer

-   Sondes en général : les sondes à retroengineerer sont les suivantes:
    -   sondes mécaniques sectorielles
    -   sondes mécaniques mono-élément
    -   sondes à balayage
    -   "wobbler probes"
-   Celles à ne pas récupérer sont:
    -   sondes à matrice
    -   sondes multiélément
    -   sondes linéaires/sondes linéaires courbes
    -   sondes à balayage électronique

### Approche raspberry pi

-   Existant : démonstration d'un sonar
-   

Sourcing Potentiel
------------------

### Electronique

### Neuf mais ...

### Occasion

-   leboncoin : meilleur prix, 400€ used
    -   <http://www.leboncoin.fr/materiel_medical/747007800.htm>
    -   <http://www.leboncoin.fr/materiel_medical/781199518.htm?ca=12_s>
-   tous les sites de sourcing de matériel d'occasion..
    -   <http://bestengineer.chez.com/ultrasound.html>
    -   <http://www.dotmed.com/listing/vet.-ultrasound/kontron/sigma-1ac-&-2-probes/1194647>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/instruments-w-5-mhz-ds-type-:-wobbler-ultrasound-transducer-probe/1557682>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/5-mhz-b-/1557669>
    -   <http://www.umed-ultrasound.com/StockSondes_KONTRON.htm>
-   Autres
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=sonde+ultrasons>
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=echographe>
    -   <http://medical.fr/fr/1105-sonde>?&orderby=price&orderway=asc
    -   <http://www.dotmed.com/listings/search/equipment.html?key=wobbler&type=equipment>
    -   <http://www.ebay.com/sch/i.html?_odkw=sector+ultrasound&_sop=3&_from=R40&_osacat=0&_ssc=1&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xwobbler+ultrasound&_nkw=wobbler+ultrasound&_sacat=0>
-   A suivre
    -   <http://www.ebay.com/itm/Aloka-ASU-32CWD-5-Mechanical-Doppler-Probe-/331496509627>?
    -   <http://www.ebay.com/itm/GE-2-5-48S-P-N-45-231613G1-Sector-Ultrasound-Transducer-Probe-/111626681515?pt=LH_DefaultDomain_0&hash=item19fd77fcab>
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>
        -- ATL / Philips A6-3

Manuels
-------

-   <http://www.frankshospitalworkshop.com/equipment/documents/ultrasonographs/user_manuals/Kontron_Sigma_1_-_Usermanual.pdf>

<Category:TechTeam> <Category:RetroEngineering>



# Richard A. Terwilliger

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# John W. Sliwa

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Carnet de bord - Laboratoire SATIE

Carnet de bord - Laboratoire SATIE
==================================

Ce carnet de bord recense les actions menées au laboratoire SATIE (ENS
Cachan). Nous essayons de fabriquer un prototype de sonde échographique
rotative mécanique.\
[Site du laboratoire SATIE](http://www.satie.ens-cachan.fr/)\
\* Équipe

-   -   Vincent L., conception, transducteurs.
    -   Gérard C., électronique.
    -   Patrice V., mécanique.

Année 2015
----------

### Jeudi 5 Février

Présence de Vincent, Patrice et Gérard.\

#### Caractéristiques techniques du transducteur

Piézoélectrique concave pour focaliser l'onde acoustique.\
Distance focale imposée par le constructeur.\
\
![Méthode de focalisation des ondes
ultrasonores](piezo-concave.png "fig:Méthode de focalisation des ondes ultrasonores"){width="600"}\
\
Fréquences utiles des piézoélectriques: 3.5MHz, 5MHz et 7.5MHz.\
Impulsions : \~1µs.\

##### Propriétés acoustiques

Impédance acoustique du backing : Zb = \[4;5\] MRayl (choisir plutôt 4
MRayl).\
Impédance acoustique du piézoélectrique : Zp = 33 MRayl.\
Impédance acoustique du milieu extérieur (\~eau) : Ze = 1.5 MRayl.\
Impédance acoustique de la couche adaptatrice d'impédance : Za =
(Zp\*(Ze\^2))\^(1/3) donc Za = 4.2 MRayl.\
\

##### Propriétés géométriques

Diamètre du piézoélectrique : \[10;20\] mm (choisir plutôt 20 mm).\
Épaisseur du piézoélectrique : \~ 2mm.\
Longueur du backing : \[20;30\] mm.

#### Circuit électronique

Schéma de principe :\
![Schéma de principe d'une sonde échographique à un transducteur
mono-élément](receiver-transmitter2.png "fig:Schéma de principe d'une sonde échographique à un transducteur mono-élément"){width="600"}\

##### Caractéristiques techniques

On décompose la partie électronique en 4.

-   Amplificateur à base de MOS (passer de 10V à 100V, tension
    d'alimentation du piézoélectrique).
-   Switch (pont de diode) pour l'émission/réception avec protection du
    circuit en cas de surtension (cf circuit TX810).
-   Amplificateur à la réception puisque le signal d'écho est de l'ordre
    du volt voir du millivolt. (idée d'utiliser un système d’écrêtage).
-   Module de transfert des données, via un port usb par exemple ou des
    ondes wifi. Nécessité d'une interface style Raspberry.

#### Objectifs

-   Un maximum d'atténuation dans le backing.
    -   Nécessite un milieu fortement inhomogène.
    -   Matériaux nécessaires.
        -   Araldite
            20-20 (http://uk.farnell.com/araldite/araldite-2020-0-5kg/adhesive-araldite-2020-0-5kg/dp/1759533)
        -   Billes de verre pleines et creuses.
        -   Poudres de Tungstène et/ou Fer et/ou Cuivre.

#### Expériences

Pas d'expériences réalisées lors de cette première séance.\
Patrice va fabriquer un moule en téflon pour réaliser des prototypes de
backing.\
Ensuite on étudiera expérimentalement le backing pour l'optimiser.

#### Problèmes rencontrés

Théorie concernant le mélange à réaliser pour avoir un backing optimal.\
Besoin d'un point de départ pour réaliser des expériences de backing
(tranches fines pour étudier la propagation et l'atténuation des ondes
acoustiques dans ce milieu).

#### Bibliographie et ressources annexes

Quelques articles, rapports et thèses intéressants:\
\* [ Thesis Insoo Kim 2009](Thesis_Insoo_Kim_2009 "wikilink")

-   [ Effect of backing layer composition on ultrasonic
    probe\_bandwith](Effect_of_backing_layer_composition_on_ultrasonic_probe_bandwith "wikilink")
-   [ High frequency properties of passive materials for ultrasonic
    transducers](High_frequency_properties_of_passive_materials_for_ultrasonic_transducers "wikilink")

\
Sites web :

-   [Wayne Kerr - Precision Impedance Analyzers 6500B
    Series](http://www.waynekerrtest.com/global/html/products/impedanceanalysis/6500B.htm)

\

### Jeudi 12 Février

Présence de Vincent.\

#### Problème du backing résolu

On sait comment faire le backing grâce à ce document :
[High\_frequency\_properties\_of\_passive\_materials\_for\_ultrasonic\_transducers](High_frequency_properties_of_passive_materials_for_ultrasonic_transducers "wikilink")\
On se restreint à 5-7% de tungstène (en fraction volumique) dans le
mélange époxy-tungstène. On trouve cette valeur en regardant le graphe
de l'impédance acoustique en fonction de la fraction volumique de
tungstène. On sait que l'impédance acoustique du backing doit être entre
4 et 5 MRayl. On en déduit la fraction volumique de tungstène.\
Il reste à faire les expériences pour trouver le rapport optimal, on ne
regardera que la tranche 5-7% en fraction volumique de tungstène.\
Pour ces valeurs l'atténuation du backing varie entre 0,73 dB/mm/MHz et
0,90 dB/mm/MHz.\
Si nous choisissons un backing de longueur 1 cm, l'atténuation après
aller-retour de l'onde émise est comprise entre 147 dB et 180 dB, ce qui
est amplement suffisant.\
\
![Graphes liant fraction volumique de tungstène dans le backing,
impédance acoustique du backing et atténuation dans le
backing.](backing-modelization.png "fig:Graphes liant fraction volumique de tungstène dans le backing, impédance acoustique du backing et atténuation dans le backing."){width="600"}\
\

#### Choix de la poudre de tungstène

Nous devons choisir une poudre de tungstène adaptée à la longueur
d'onde. Au vu des fréquences auxquelles nous travaillons (3,5 5 et 7,5
MHz) et de la vitesse du son dans le tungstène (5180 m/s pour les ondes
longitudinales, 2870 m/s pour les ondes transversales), la longueur
d'onde varie entre 2,1 mm et 0,69 mm.\
Il faut choisir une poudre de tungstène de longueur caractéristique de
l'ordre de la dizaine de micromètre pour obtenir l'atténuation
nécessaire.\

#### Liste de produits

La poudre de tungstène coûte cher, de l'ordre de la centaine d'euros les
500g.\
Voici une liste de quelques produits trouvés sur Internet :\
\*
<http://www.sigmaaldrich.com/catalog/product/aldrich/510106?lang=fr&region=FR>

-   <http://www.goodfellow.com/catalogue/GFCat4.php?ewd_token=i4epRoTqmdmEfSaSjNsIoCslj7ClT8&n=kJvdFtf8wiW04VWARSHZRhrqrgSTJE&ewd_urlNo=GFCatSeab1&CatLook=TUNGSTENE%20%28W%29%20POUDRE>
-   <http://www.merckmillipore.com/FR/fr/product/,MDA_CHEM-112406%3Bpgid%3D8iFMKfaYPCFSRpEowZVgbI720000l0yoKiep%3Bsid%3DyZ4Kw6t_IqMKw_-jOWkaS0UqcBjInP_dIR8qkMh91e9kDyMREVxviVlj2CVzXIbmvc8k2ngJCqPzaxyzu7WBLdSaqz-OyiT6Z0nxt44r5zekZxvzN1wfwlJ_VZZLPfJveRS9D9lUnTziQs41O4IWssWz#anchor_orderingcomp>

### Jeudi 19 Février

Présence de Vincent, Gérard et Patrice\

#### Obtention du moule pour le backing

Patrice a réalisé un moule en téflon en 2 parties amovibles serrées par
des vis. La forme utile est un cylindre.\
Diamètre : d = 2,0 cm.\
Hauteur du cylindre : h = 1,0 cm.\
Soit un volume de π =\~ 3.14159 cm\^3.\
Nécessaire pour réaliser les premiers moulages de backing. Il faudra en
faire un autre pour faire le transducteur en entier (backing+piezo+lame
adaptatrice)\
![Moule et
tungstène](moule-et-tungstene.png "fig:Moule et tungstène"){width="600"}\

#### Matériel à notre disposition pour le backing

Ce jour, nous avons utilisés:\
\* Araldite 2020 (2 composants à mélanger, une résine et un durcissant)
:
[:File:araldite20-20-datasheet.pdf](:File:araldite20-20-datasheet.pdf "wikilink")

-   -   Masse volumique : rho = 1,33 g/cm\^3
-   Poudre de tungstène :
    [1](https://www.sigmaaldrich.com/catalog/product/aldrich/267511?lang=fr&region=FR)
    -   Masse volumique : rho = 19,3 g/cm\^3
    -   Diamètre des grains : 12µm
    -   Pureté : 99,99%

#### Dosage des composants pour le backing

En prenant en compte l'impédance acoustique du piézoélectrique, nous
avons déduit les proportions de composants nécessaires pour le backing
pour plusieurs possibilités.\
Il faudra tester chacune de ses possibilités si on veut optimiser le
backing.\
[:File:dosage-composants-backing.pdf](:File:dosage-composants-backing.pdf "wikilink")\

#### Expérience : premier essai de backing

\
![Paillasse laboratoire
SATIE](paillasse-ens.png "fig:Paillasse laboratoire SATIE"){width="600"}\
=====Matériel===== Choix d'un ratio tungstène/époxy de 3,5%.\
Quantités nécessaires (on en fait toujours un peu plus puisqu'on en perd
en faisant les manipulations) :

-   5,07 g d'araldite 2020.
    -   3,9 g de résine.
    -   1,17 g de durcissant.
-   2,668 g de poudre de tungstène.

\
\
![Araldite](araldite.png "fig:Araldite"){width="600"}\
![Poudre de
tungstène](poudre-de-tungstene.png "fig:Poudre de tungstène"){width="600"}\
Matériel nécessaire :\
\* Balance de précision (\~10\^-4 g).

-   Pompe à vide (supprime les bulles d'air).
-   Étuve (\~ 100 °C pour polymérisation rapide).
-   Bécher (ici on a utilisé un petit verre).
-   Spatules.
-   Coupelle (ici on a utilisé un morceau d'aluminium).
-   Alcool non dénaturé (pour nettoyer le matériel)

\
![Balance de
précision](balance-de-precision.png "fig:Balance de précision"){width="600"}

##### Protocole suivi (non concluant)

Ajouter 3,9 g de résine dans un bécher.\
Ajouter 1,17 g de durcissant.\
Mélanger doucement jusqu'à obtenir une phase liquide homogène.
Attention, il faut introduire le moins d'air possible dans le mélange.\
Ajouter petit à petit 2,6668 g de poudre de tungstène dans le mélange,
tout en agitant pendant environ 5 minutes. Attention, il faut introduire
le moins d'air possible dans le mélange.\
Mettre le bécher sous vide et observer un dégazage. Attention, il y a
des risques de débordement si beaucoup d'air a été incorporé dans la
solution.\
Placer le bécher 10 minutes à l'étuve.\
![Balance et
tungstène](balance-tungstene-araldite.png "fig:Balance et tungstène"){width="600"}\
![Mélange de l'époxy et du
tungstène](melange-epocy-tungstene.png "fig:Mélange de l'époxy et du tungstène"){width="600"}

##### Observations

Nous avons décelés plusieurs problèmes.\
\* Sédimentation très rapide du tungstène dans la solution d'araldite
2020. En moins d'une minute, la majorité de la poudre de tungstène se
retrouve au fond du bécher, ce qui nuit bien évidemment à la qualité du
backing (inutilisable en l'état).\
\* Polymérisation très rapide à l'étuve. Bien que lente à température
ambiante (en 30 minutes la viscosité du mélange époxy n'a pas changé),
la polymérisation du mélange est très rapide. En effet, après 10 minutes
à l'étuve (120°C), le mélange était entièrement polymérisé (impossible
de le retirer du bécher).\
\* Note concernant l'utilisation sous vide Après avoir terminé l'étape
sous vide, il faut remettre la pression atmosphérique doucement sous
peine de renversement du bécher et projections (donc perte définitive)
du mélange. ![Polymérisation trop rapide à l'étuve
(120°C)](polymerisation-trop-rapide.png "fig:Polymérisation trop rapide à l'étuve (120°C)"){width="600"}\

##### Solutions envisagées

Utiliser une plaque chauffante tout en agitant manuellement le mélange
permet de régler à la fois le problème de sédimentation ainsi que le
problème de polymérisation trop rapide.

### Jeudi 5 Mars

Présence de Vincent.\

#### Troisième essai de backing

##### Matériaux

Mêmes quantités que la fois précédente :

-   5,07 g d'araldite 2020.
    -   3,9 g de résine.
    -   1,17 g de durcissant.
-   2,668 g de poudre de tungstène.

##### Protocole

Utilisation d'une plaque chauffante.\
Permet de polymériser la résine plus rapidement (12 heures à température
ambiante) tout en mélangeant correctement et de manière homogène la
poudre de tungstène (on souhaite éviter le phénomène de sédimentation).\
Effectivement, la fois dernière l'étuve à 120°C avait fait polymériser
le mélange trop rapidement, le rendant inutilisable.\
\
Chauffage :

-   10 minutes à 50°C.
-   10 minutes à 65°C.
-   10 minutes à 80°C.
-   2 minutes à 95°C.

\
![Plaque
chauffante](plaque-chauffante.png "fig:Plaque chauffante"){width="600"}\
![Thermomètre et plaque
chauffante](thermometre-et-plaque-chauffante.png "fig:Thermomètre et plaque chauffante"){width="600"}

##### Résultats

C'est un échec. La polymérisation de l'araldite 2020 est un phénomène de
réaction en chaîne. Si la température est trop élevée (\~90°C ici), la
résine polymérise avant qu'on ne la verse dans le moule.\
Il faut donc chauffer à une moindre température.

#### Quatrième essai de backing

##### Matériaux

Mêmes quantités que la fois précédente :

-   5,07 g d'araldite 2020.
    -   3,9 g de résine.
    -   1,17 g de durcissant.
-   2,668 g de poudre de tungstène.

##### Protocole

Utilisation d'une plaque chauffante.\
Permet de polymériser la résine plus rapidement (12 heures à température
ambiante) tout en mélangeant correctement et de manière homogène la
poudre de tungstène (on souhaite éviter le phénomène de sédimentation).\
Chauffage :

-   12 minutes à 30°C.
-   15 minutes à 45°C.
-   5 minutes à 30°C.

\
Le mélange étant assez visqueux (pas de risque de sédimentation
normalement), on le verse dans le moule en téflon.\
On place le moule remplit dans une étude à 80°C pendant 30 minutes.\
![Plaque chauffante Rotamag
C11](rotamag.png "fig:Plaque chauffante Rotamag C11"){width="600"}\
![Mélange d'araldite et de poudre de
tungstène](araldite-dans-moule.png "fig:Mélange d'araldite et de poudre de tungstène"){width="600"}

##### Résultats

C'est l'essai le plus concluant jusqu'à maintenant et le premier coulage
dans le moule réussit. On doit attendre la polymérisation complète avant
de démouler le backing.\
La prochaine étape sera la découpe en tranches fines du backing pour
tester ses propriétés acoustiques. On espère qu'elles répondront à nos
attentes concernant l'atténuation des ondes acoustiques considérées
(3.5MHz).\
Ce moyen permet aussi de tester l'homogénéité du backing pour détecter
notamment le problème de sédimentation (propriétés acoustiques des
tranches différentes dans ce cas là).

### Jeudi 19 Mars

Présence de Vincent et de Gérard.\

#### Démoulage du backing numéro 4

##### Résultats

Le problème de sédimentation est toujours présent. Toute la poudre de
tungstène est au fond du moule malgré le nouveau protocole que nous
avons utilisé (chauffage avant moulage pour durcir préalablement
l'araldite 2020).\
![Sédimentation du tungstène dans le
backing](backing-n4-sedimentation2.png "fig:Sédimentation du tungstène dans le backing"){width="600"}\
Nous allons devoir utiliser une autre résine, plus visqueuse, pour
éviter ce problème de sédimentation.\
\
Le moulage est bien réalisé, la résine est très dure (comme du verre à
première vue).\
![Backing (essai n°4) vue de
dessus](backing-n4-front.png "fig:Backing (essai n°4) vue de dessus"){width="600"}\
![Backing (essai n°4) vue de
dessous](backing-n4-back.png "fig:Backing (essai n°4) vue de dessous"){width="600"}\
Un autre problème est évident, c'est la présence de bulles d'air dans le
backing. Il faudra utiliser une pompe à vide pour extraire préalablement
l'air avant de faire la polymérisation finale.

#### Cinquième essai de backing

##### Matériaux

On utilise une nouvelle colle (colle époxy de supermarché) : *SADER
colle époxy progressive bicomposante - prise deux heures*.

-   4.9898 g d'époxy.
    -   2.50771 g de résine.
    -   2,48209 g de durcissant.
-   2,668 g de poudre de tungstène.

##### Protocole

D'abord, on mélange la résine et le durcissant pour obtenir une phase
homogène (formation de petites bulles d'air).\
On ajoute la poudre de tungstène et on mélange pour avoir une phase
homogène.\
Ensuite on passe le tout sous vide pendant 15 minutes.\
Le mélange étant assez visqueux (pas de risque de sédimentation
normalement), on le verse dans le moule en téflon.\
On place le moule remplit dans une étude à 80°C pendant plus d'une heure
(polymérisation complète).

##### Images

![Matériel pour faire le
vide](matos-pour-vide.png "fig:Matériel pour faire le vide"){width="600"}\
![Faire le vide](faire-le-vide.png "fig:Faire le vide"){width="600"}\
![Pompe à
vide](pompe-a-vide-gerard.png "fig:Pompe à vide"){width="600"}\
![Bulles d'air (backing sous
vide)](bulles-air.png "fig:Bulles d'air (backing sous vide)"){width="600"}

#### Nouvelles idées

On voudrait utiliser des billes de verre plutôt que de la poudre de
tungstène. On aurait moins de problèmes de sédimentation.\
On a besoin des propriétés acoustiques et mécaniques des résines que
nous utilisons. Nous avons un document (base de donnée) regroupant
différentes caractéristiques pour plusieurs résines et colles :
[:File:cue\_materials\_database\_ver1.2\_aug\_2005.pdf](:File:cue_materials_database_ver1.2_aug_2005.pdf "wikilink")\
En particulier, pour l'araldite 2020 :\
![Propriétés acoustiques et mécaniques de l'araldite
20-20](proprietes-acoustiques-mecaniques-araldite-20-20.png "fig:Propriétés acoustiques et mécaniques de l'araldite 20-20"){width="600"}

### Jeudi 9 Avril

Présence de Vincent et de Heldmuth L. Présentation du laboratoire à
Heldmuth.\

#### Caractéristiques acoustiques du backing (numéro 5)

##### Théorie

L'idée est de déterminer les caractéristiques acoustiques (vitesse des
ondes, atténuation, impédance acoustique) du backing que nous avons
créé. Le backing numéro 5 semble convenir : pas de sédimentation mais
beaucoup de bulles d'air malgré un dégazage poussé la fois dernière.\
On le découpe en fines tranches (5 au total ici) de moins de 2 mm
d'épaisseur pour vérifier l'homogénéité du backing et détecter les
problèmes éventuels de sédimentation.\
On envoi un pulse (burst de sinus) acoustique et on mesure le temps
nécessaire à l'onde acoustique pour faire un aller. On mesure également
la masse de chaque échantillon et son volume pour déterminer sa masse
volumique.\
On en déduit l'impédance acoustique de l'échantillon en utilisant la
vitesse de propagation de l'onde sonore et la masse volumique de
l'échantillon.

###### Matériel nécessaire

-   Oscilloscope
-   GBF
-   Transducteurs acoustiques (un en émission, l'autre en réception)
-   Gel échographique
-   Balance de précision
-   Pied à coulisse
-   Serre-joint

##### Manipulation

On considère que le backing est réalisé.\
D'abord, on découpe le backing en fines tranches (de l'ordre du mm). Des
tranches trop épaisses empêchent le signal test de traverser
l'échantillon. En revanche le son passe trop rapidement dans des
tranches très fines ce qui ne permet pas une mesure précise du signal
mesuré (il y a superposition entre signal émis et signal mesuré).\
![Backing (n°5) découpé en 5
tranches](backing-5-tranches.png "fig:Backing (n°5) découpé en 5 tranches"){width="600"}\
Ensuite, on ajuste les transducteurs (émission et réception) de chaque
côté de la tranche à étudier. Il ne faut pas oublier d'ajouter du gel
échographique entre les éléments.\
![Gel pour
échographie](gel-echographie.png "fig:Gel pour échographie"){width="600"}\
![Détermination des caractéristiques acoustiques d'un échantillon de
backing](manip-test-backing.png "fig:Détermination des caractéristiques acoustiques d'un échantillon de backing"){width="600"}\
![Détermination des caractéristiques acoustiques d'un échantillon de
backing](transducteur-test-backing.png "fig:Détermination des caractéristiques acoustiques d'un échantillon de backing"){width="600"}\
On relie le transducteur d'émission au GBF et à l'oscilloscope. On relie
le transducteur de réception à l'oscilloscope. Attention, les signaux
détectés ont une amplitude bien plus faible (\~mV) que les signaux émis
(\~10V), il faut ajuster les calibres.\
On peut s'aider de la fonction moyenne de l'oscilloscope pour moyenner
sur plusieurs périodes temporelles. L'ajout de filtres permet également
de limiter le bruit.\
\
Si tout ce passe bien, on observe un temps Δt de décalage entre le
signal émis et le signal reçu. Ce temps est la durée de trajet du son à
travers le matériau pour un aller simple.\
Connaissant l'épaisseur de l'échantillon, on en déduit la vitesse du son
dans ce matériau.\
On trouve l'impédance acoustique de la tranche en utilisant la formule Z
= ρ\*v où ρ est la masse volumique de l'échantillon et v la vitesse des
ondes sonores dans l'élément.

###### Résultats expérimentaux

On a fait l'expérience pour deux tranches d'un même backing (le numéro
5). On trouve des impédances acoustiques égales à 2,92 MRayl et 3,28
Mrayl.\
Notons que les mesures sont peu précises (le son est très atténué et le
signal reçu est faible) et que les résultats sont donc approximatifs.

###### Interprétation

Théoriquement on devrait trouver des impédances acoustiques autour de 4
MRayl selon nos calculs. Nous expliquons cette différence par
l'introduction non négligeable de bulles d'air dans l'échantillon.\
En effet, le matériau est très poreux et les bulles sont visibles à
l’œil nu (on pourrait par ailleurs regarder la surface au microscope).
On avait pourtant fait un dégazage avant de mouler le backing.\
L'avantage de l'air est qu'il induit naturellement une inhomogénéité
forte dans le milieu. Cette propriété est intéressante pour
l'atténuation que nous recherchons (on cherche a atténuer complètement
les ondes sonores passant dans le backing).\
Il nous reste à étudier la reproductibilité d'un tel processus : comment
obtenir toujours les mêmes bulles d'air, quelles sont les conditions de
pression qu'il faut imposer lors du dégazage, de quelle manière
introduire l'air etc ... Sans cela il nous est impossible de contrôler
précisément l'impédance acoustique de notre backing.\
\
Une autre solution est d'utiliser à nouveau la résine Araldite 20-20 qui
est très liquide et contient peu de bulles après dégazage (on a déjà
fait un backing avec mais il y a avait un problème de sédimentation non
résolu). On va essayer une fois prochaine de mélanger des billes de
verre creuses à de l'araldite 20-20. Les billes seront en suspension
dans la résine et le problème de sédimentation pourra être évité.

###### Photographies

![Scie circulaire pour découper le
backing](scie-circulaire.png "fig:Scie circulaire pour découper le backing"){width="600"}\
![Oscillateur et GBF (générateur basse
fréquence)](oscillo(mauvais)-et-gbf.png "fig:Oscillateur et GBF (générateur basse fréquence)"){width="600"}

### Jeudi 16 Avril

Présence de Vincent et de Gérard.\
Cette séance nous avons testé la poudre de verre pour remplacer la
poudre de tungstène. Nous voulons éviter le phénomène de sédimentation
et réduire les coûts de production.\
Nous avons essayé une méthode de polymérisation rapide à 120 °C (moule
chaud et étuve réglée à 120° C) pour éviter le phénomène de
sédimentation.

#### Dosage des composants pour le backing

En prenant en compte l'impédance acoustique du piézoélectrique, nous
avons déduit les proportions de composants nécessaires pour le backing
pour plusieurs possibilités. Les valeurs sont évidemment différentes
puisqu'on utilise ici du verre et pas du tungstène.\
![Impédance acoustique en fonction de la fraction volumique de verre
dans l'araldite
20-20](fraction-araldite-verre.png "fig:Impédance acoustique en fonction de la fraction volumique de verre dans l'araldite 20-20"){width="600"}\
[:File:dosage-composants-backing-verre-araldite-20-20.pdf](:File:dosage-composants-backing-verre-araldite-20-20.pdf "wikilink")\

#### Sixième essai de backing

##### Matériaux

On utilise de l'araldite 20-20 et des billes de verre pleines de
diamètre 130 µm.

-   3,76 g d'époxy.
    -   2.63 g de résine.
    -   1,13 g de durcissant.
-   0,79 g de poudre de verre.

##### Protocole

D'abord, on mélange la résine et le durcissant pour obtenir une phase
homogène (formation de petites bulles d'air).\
On ajoute la poudre de tungstène et on mélange pour avoir une phase
homogène.\
Ensuite on passe le tout sous vide pendant 10 minutes.\
Le mélange n'étant pas assez visqueux (on voit la sédimentation), on a
essayé de le durcir en le chauffant sur une plaque chauffante. Continuer
de mélanger tout en chauffant à 80 °C.\
Mettre le tout à l'étuve.

##### Résultats

C'est un échec. Le produit a polymérisé avant qu'on ait réussi à le
couler dans le moule.\
Le phénomène de polymérisation est exothermique. En chauffant le mélange
on accélère le processus et une réaction en chaîne se produit. Apporter
de la chaleur génère de la chaleur.\
La polymérisation se fait de manière violente en moins de 10 secondes.
Ceci ne laisse pas le temps de couler le mélange, ni de le dégazer.
C'est une méthode non concluante.

#### Septième essai de backing

Après ce dernier échec nous abandonnons l'araldite 20-20 qui est trop
liquide, pas assez visqueuse et engendre un phénomène de sédimentation.\
Nous nous tournons vers une résine époxy industrielle de supermarché,
déjà utilisée (backing n° 5) et assez concluante : SADER colle époxy
progressive bicomposante - prise deux heures.\
![Colle époxy
SADER](colle-epoxy-progressive-SADER.jpg "fig:Colle époxy SADER"){width="600"}\
Son utilisation est très facile (50% de résine, 50% de durcissant) et
elle est très visqueuse.\
Voici le tableau de valeurs que nous utilisons :\
[:File:dosage-composants-backing-verre-SADER-epoxy.pdf](:File:dosage-composants-backing-verre-SADER-epoxy.pdf "wikilink")\
Nous allons également utiliser une pompe à vide plus puissante puisque
le défaut du backing n°5 était une présence trop importante et non
maîtrisée de bulles d'air malgré un dégazage. Ici, nous avons fait
plusieurs dégazages successifs, avant et après avoir coulé la résine
dans le moule.\
![Montage pour le dégazage du backing
7](degazage-backing-7-3.png "fig:Montage pour le dégazage du backing 7"){width="600"}\
![Montage pour le dégazage du backing
7](degazage-backing-7-2.png "fig:Montage pour le dégazage du backing 7"){width="600"}

##### Matériaux

On utilise de la colle époxy SADER et des billes de verre pleines de
diamètre 130 µm.

-   3,8 g d'époxy.
    -   1,91 g de résine.
    -   1,89 g de durcissant.
-   0,79 g de poudre de verre.

##### Protocole

D'abord, on mélange la résine et le durcissant pour obtenir une phase
homogène (formation de bulles d'air).\
Ensuite on passe le tout sous vide pendant 20 minutes (utiliser une
pompe puissante). Il ne faut pas hésiter à le faire par à-coups. En
effet, la colle est très visqueuse et risque de déborder. Une fois que
la mousse est haute et menace de déborder, casser le vide (ceci a pour
effet de supprimer la mousse) puis recommencer.\
![Dégazage du backing
7](degazage-backing-7.png "fig:Dégazage du backing 7"){width="600"}\
![Dégazage du backing
7](video-degazage-backing-16-avril.mp4 "fig:Dégazage du backing 7"){width="600"}\
Verser le mélange dans le moule.\
Dégazer pendant 10 minutes. Même technique, dégazer par à-coups si
besoin.\
Mettre le tout à l'étuve à 80 °C jusqu'à polymérisation complète.

##### Résultats

Le mélange semble correct. On ne voit pas de sédimentation. Il faut
étudier les propriétés acoustiques.

#### Autres idées

Pour lutter contre le phénomène de sédimentation on pourrait utiliser
des matériaux avec une masse volumique plus faible que le tungstène ou
le verre. Dans les métaux, le magnésium a une masse volumique de 1,7
g/cm3. On pourra peut-être l'utiliser pour de prochains essais.

### Jeudi 23 Avril

Présence de Vincent.\

#### Manipulations

On a utilisé le même protocole que pour le [backing n° 5 du jeudi 9
avril 2015](#Jeudi_9_Avril "wikilink").\
On dispose de 5 tranches du [backing n° 7](#Jeudi_16_Avril "wikilink")
composé de billes de verre et de résine époxy SADER.\
![Tranches du backing n° 7 - SADER et
verre](backing-7-verre-sder.png "fig:Tranches du backing n° 7 - SADER et verre"){width="600"}\
![Tranche de backing n°
7](backing-7.png "fig:Tranche de backing n° 7"){width="600"}

#### Résultats

On numérote les tranches de 0 (haut) à 4 (bas).\
Notons que les tranches 0 et 4 sont assez grossières et les faces non
parallèles entre elles, ce qui induit des erreurs de mesures. Tous
calculs faits, on trouve les impédances acoustiques suivantes pour
chaque tranche :

-   0 : non déterminé (mauvaise qualité).
-   1 : 2,84 MRayl.
-   2 : 3,05 MRayl.
-   3 : 2,97 MRayl.
-   4 : \~ 3,39 MRayl (valeur approximative car faces non parallèles
    donc mesures faussées).

\

#### Observations

Ce backing est de bonne qualité. On ne discerne pas de bulles d'air à
l’œil nu. Il est très résistant et homogène. Le verre est réparti
correctement (on a un léger gradient de sédimentation quand on fait les
mesures d'impédance acoustique qui se traduit par une augmentation de
l'impédance quand on descend au fond du backing).\
L'utilisation du verre (poudre de 130 µm) semble concluante. Le verre
est bon marché ce qui réduit les coûts de production du transducteur.
C'est une matière première simple a obtenir même s'il est nécessaire
d'avoir une machine pour broyer le verre (on veut des particules de
l'ordre de la centaine de micromètre et même plus petit, si possible de
l'ordre de la dizaine de micromètre).\
Il reste à obtenir l'impédance voulue à savoir 4 MRayl. On va devoir
ajouter plus de poudre de verre pour corriger ce défaut. Une fois les
proportions volumiques de verre et de résine connues, on aura la
composition exacte et précise de notre backing. Il ne reste plus qu'à
couler le backing, le piézoélectrique et les lames adaptatrices
d'impédance ensembles.

#### Photographies

![Manipulation pour tester les backings (ici test du backing n°
7)](manip-test-backing-7.png "fig:Manipulation pour tester les backings (ici test du backing n° 7)"){width="600"}
![Transducteur 20 MHz utilisé pour tester les
backings](transducteur-20Mhz.png "fig:Transducteur 20 MHz utilisé pour tester les backings"){width="600"}
![Oscilloscope Lecroy utilisé pour tester les
backings](oscillo-lecroy-2.png "fig:Oscilloscope Lecroy utilisé pour tester les backings"){width="600"}
![Oscilloscope Lecroy utilisé pour tester les
backings](oscillo-lecroy.png "fig:Oscilloscope Lecroy utilisé pour tester les backings"){width="600"}

### Jeudi 7 Mai

Présence de Vincent.\

#### Huitième essai de backing

##### Matériaux

-   5,01 g d'époxy SADER.
    -   2,55 g de résine.
    -   2,56 g de durcissant.
-   2,66 g de poudre de tungstène.

##### Protocole

On mélange le tout (l'époxy SADER est très visqueuse et on ne subit plus
le phénomène de sédimentation). Néanmoins, on a le problème de l'air qui
reste piégé dans l'échantillon. Il faut dégazer sous vide.\
Dégazer par à-coup dans le récipient pendant 20 minutes en évitant les
débordements (faire une dizaine de cycles).\
Verser le mélange dans le moule et dégazer le tout par à-coup pendant 20
minutes en évitant les débordements (une dizaine de cycles).\
Mettre le moule dans l'étuve à 80 °C pendant 1h30.\
![Backing n° 8 dans le moule sous
cloche](degazage-backing-8.png "fig:Backing n° 8 dans le moule sous cloche"){width="600"}\
![Dégazage du backing
8](video-degazage-backing-7-mai.mp4 "fig:Dégazage du backing 8"){width="600"}\
![Dégazage du backing
8](backing-8-sous-cloche.png "fig:Dégazage du backing 8"){width="600"}\

### Jeudi 21 Mai

Présence de Vincent.\

#### Manipulations

On a utilisé le même protocole que pour le [backing n° 5 du jeudi 9
avril 2015](#Jeudi_9_Avril "wikilink"). On a utilisé un oscilloscope
plus performant (LeCroy WaveRunner HRO 66Zi - 600 Mhz 12-bit).\
![Matériel utilisé pour l'étude du backing n°
8](matos-backing-8.png "fig:Matériel utilisé pour l'étude du backing n° 8"){width="600"}\
On dispose de 5 tranches du [backing n° 8](#Jeudi_7_Mai "wikilink")
composé de poudre de tungstène et de résine époxy SADER.\
![](backing-8-1.png "fig:backing-8-1.png"){width="400"}
![](backing-8-2.png "fig:backing-8-2.png"){width="400"}
![](backing-8-3.png "fig:backing-8-3.png"){width="400"}
![](backing-8-4.png "fig:backing-8-4.png"){width="400"}\

#### Résultats

On numérote les tranches de 1 (haut) à 5 (bas).\
Notons que les tranches 1 et 5 sont assez grossières ce qui induit des
erreurs de mesures. Tous calculs faits, on trouve les impédances
acoustiques suivantes pour chaque tranche :

-   1 : 2,99 MRayl.
-   2 : 3,39 MRayl.
-   3 : 3,52 MRayl.
-   4 : 3,56 MRayl.
-   5 : 3,85 MRayl.

\
Les résultats sont détaillés dans le document suivant : [:File:Etude
acoustique du backing numéro
8.pdf](:File:Etude_acoustique_du_backing_numéro_8.pdf "wikilink").\
![Impédance acoustique du backing n°8 en fonction de la profondeur
moyenne](impédance-acoustique-backing-8.png "fig:Impédance acoustique du backing n°8 en fonction de la profondeur moyenne"){width="600"}\
![Masse volumique du backing n°8 en fonction de la profondeur
moyenne](masse-volumique-backing-8.png "fig:Masse volumique du backing n°8 en fonction de la profondeur moyenne"){width="600"}\
![Vitesse du son dans le backing n°8 en fonction de la profondeur
moyenne](vitesse-son-backing-8.png "fig:Vitesse du son dans le backing n°8 en fonction de la profondeur moyenne"){width="600"}\
==== Observations ==== Ce backing est de qualité correcte mais un léger
gradient en concentration de poudre de tungstène persiste. On ne
discerne pas de bulles d'air à l’œil nu, sauf sur la première tranche
(bulles en surface). Il est très résistant et homogène. Le tungstène est
réparti correctement malgré un gradient vertical dû à la sédimentation.
Ce phénomène n'est pas forcément perturbateur pour nous vu que le
gradient est faible.\
Il reste à obtenir l'impédance voulue à savoir 4 MRayl. On va devoir
ajouter plus de poudre de tungstène pour corriger ce défaut.

#### Photographies

![Générateur de fonctions
Agilent](gbf.png "fig:Générateur de fonctions Agilent"){width="600"}
![Manipulation pour le backing
n°8](manip-backing-8.png "fig:Manipulation pour le backing n°8"){width="600"}
![Courbes obtenues sur l'oscilloscope au cours de la manipulation pour
le backing n°
8](results-backing-8-1.png "fig:Courbes obtenues sur l'oscilloscope au cours de la manipulation pour le backing n° 8"){width="600"}
![Courbes obtenues sur l'oscilloscope au cours de la manipulation pour
le backing n°
8](results-backing-8-2.png "fig:Courbes obtenues sur l'oscilloscope au cours de la manipulation pour le backing n° 8"){width="600"}

### Jeudi 28 Mai

Présence de Vincent, Patrice et Gérard.\
Pas d'expériences réalisées ce jour-là.\

#### Caractéristiques des éléments piézoélectriques

On a reçu 5 capsules piézoélectriques concaves.

-   Matériau : Pz27.
-   Focale : 100mm.
-   Diamètre : 15mm.
-   Prix : 32 euros unité.

#### Protocole d'assemblage du transducteur

On doit assembler 3 éléments pour fabriquer le transducteur complet : le
backing, la capsule piézoélectrique et la couche adaptatrice
d'impédance.\
Le backing et la couche adaptatrice d'impédance sont composés de la même
matière (recherches menées lors des précédentes séances). On doit aussi
souder deux fils électriques (cuivre étamé) sur chaque électrode de la
capsule piézoélectrique, un sur chaque côté.\
Patrice est en mesure de réaliser deux nouveaux moules. Un pour le
backing (20mm de profondeur) et un deuxième (0,25mm de profondeur) pour
la couche adaptatrice d'impédance.\
On va couler le backing et plaquer le piézo directement sur le backing
pour une meilleur efficacité.\
Par contre la couche adaptatrice doit être usinée à part. On la coule
dans le moule en téflon puis on laisse l'époxy polymériser et refroidir.
La couche étant très fine (0,25mm d'épaisseur), on la chauffe et on la
déforme à l'aide d'un moule en métal épousant la forme de la capsule
piézo (bon rayon de courbure), puis on laisse refroidir et durcir.
Enfin, on colle la couche sur le piézo en utilisant très peu de colle.\
On obtient notre transducteur acoustique.\

### Jeudi 4 Juin

Présence de Vincent et de Gérard.\

#### Neuvième essai de backing

On a reçu de la poudre de dioxyde de silicium SiO2 (\~verre) commandée
chez Sigma-Aldrich.\
Taille des grains :\
\* 99% entre 0,5 et 10 µm

-   80% entre 1 et 5 µm

\
Cet ordre de grandeur est largement correct puisque ce sont les bonnes
dimensions que l'on recherche vu l'ordre de grandeur des longueurs
d'ondes utilisées.\
![Dioxyde de silicium -
Sigma-Aldrich](dioxyde-de-silice-1.png "fig:Dioxyde de silicium - Sigma-Aldrich"){width="600"}\
![Dioxyde de silicium -
Sigma-Aldrich](dioxyde-de-silice-2.png "fig:Dioxyde de silicium - Sigma-Aldrich"){width="600"}\

##### Matériaux

Matériaux utilisés :\
\* 3,25513 g d'époxy SADER.

-   -   1,60046 g de résine.
    -   1,65467 g de durcissant.
-   0,78502 g de poudre de tungstène.

\
Proportions utilisées : 10% de dioxyde de silicium et 90% de colle
époxy.\

##### Protocole

On mélange le tout (l'époxy SADER est très visqueuse et on ne subit plus
le phénomène de sédimentation). Néanmoins, on a le problème de l'air qui
reste piégé dans l'échantillon. Il faut dégazer sous vide.\
Dégazer par à-coup dans le récipient pendant 20 minutes en évitant les
débordements (faire une dizaine de cycles).\
Verser le mélange dans le moule et dégazer le tout par à-coup pendant 20
minutes en évitant les débordements (une dizaine de cycles).\
Mettre le moule dans l'étuve à 80 °C pendant 1h30.\
![Matériaux à mélanger pour le backing
9](materiau-backing-9.png "fig:Matériaux à mélanger pour le backing 9"){width="600"}\
![Mélange pour le backing
9](melange-backing-9-1.png "fig:Mélange pour le backing 9"){width="600"}\
![Mélange pour le backing
9](melange-backing-9-2.png "fig:Mélange pour le backing 9"){width="600"}

### Mercredi 1 Juillet

Présence de Vincent.\

#### Manipulations

On a utilisé le même protocole que pour le [backing n° 5 du jeudi 9
avril 2015](#Jeudi_9_Avril "wikilink").\
On dispose de 4 tranches du [backing n° 9](#Jeudi_4_Juin "wikilink")
composé de poudre de dioxyde de silicium et de résine époxy SADER.\

#### Résultats

On numérote les tranches de 1 (bas) à 4 (haut).\
Tous calculs faits, on trouve les impédances acoustiques suivantes pour
chaque tranche :

-   1 : 2,4065 MRayl.
-   2 : 2,4572 MRayl.
-   3 : 2,3937 MRayl.
-   4 : 2,8309 MRayl.

#### Observations

Ce backing est de bonne qualité générale mais les impédances acoustiques
ne sont pas respectées, il faut y remédier. On ne discerne pas de bulles
d'air à l’œil nu, sauf sur la première tranche (bulles en surface). Il
est très résistant et homogène. Le dioxyde de silicium est réparti
correctement.\
Il reste à obtenir l'impédance voulue à savoir 4 MRayl. On va devoir
ajouter plus de poudre de dioxyde de silicium pour corriger ce défaut.

### Mercredi 8 Juillet

Présence de Vincent et de Gérard.\

#### Dixième essai de backing

Pour ce backing on décide de mettre plus de poudre de dioxyde de
silicium que dans le précédent backing numéro 9.\

##### Matériaux

Matériaux utilisés :\
\* 3,15028 g d'époxy SADER.

-   -   1,5554 g de résine.
    -   1,59488 g de durcissant.
-   1,29369 g de poudre de tungstène.

##### Protocole

On mélange le tout (l'époxy SADER est très visqueuse et on ne subit plus
le phénomène de sédimentation). Néanmoins, on a le problème de l'air qui
reste piégé dans l'échantillon. Il faut dégazer sous vide.\
Dégazer par à-coup dans le récipient pendant 20 minutes en évitant les
débordements (faire une dizaine de cycles).\
Verser le mélange dans le moule et dégazer le tout par à-coup pendant 20
minutes en évitant les débordements (une dizaine de cycles).\
Mettre le moule dans l'étuve à 80 °C pendant 1h30.\

### Mercredi 22 Juillet

Présence de Vincent.\

#### Manipulations

On a utilisé le même protocole que pour le [backing n° 5 du jeudi 9
avril 2015](#Jeudi_9_Avril "wikilink").\
On dispose de 4 tranches du [backing n°
10](#Mercredi_8_Juillet "wikilink") composé de poudre de dioxyde de
silicium et de résine époxy SADER.\

#### Résultats

On numérote les tranches de 1 (fond) à 4 (haut).\
Tous calculs faits, on trouve les impédances acoustiques suivantes pour
chaque tranche :

-   1 : 3,18 MRayl.
-   2 : 3,18 MRayl.
-   3 : 3,77 MRayl.
-   4 : 3,75 MRayl.

#### Observations

Ce backing est de bonne qualité générale mais les impédances acoustiques
ne sont pas respectées, il faut y remédier. On ne discerne pas de bulles
d'air à l’œil nu. Il est très résistant et homogène. Le dioxyde de
silicium est réparti correctement.\
Il reste à obtenir l'impédance voulue à savoir 4 MRayl. On va devoir
ajouter plus de poudre de dioxyde de silicium pour corriger ce défaut.\
On va également ajouter de la poudre de tungstène.

### Jeudi 10 Septembre

Présence de Vincent et de Gérard.\

#### Onzième essai de backing

On réalise un nouvel essai de backing en suivant le protocole habituel.
Cette fois on charge le backing en verre et on ajoute de la poudre de
tungstène.

##### Matériaux

Matériaux utilisés :\
\* 3,08072 g d'époxy SADER.

-   -   1,56147 g de résine.
    -   1,51925 g de durcissant.
-   1,26306 g de SiO2.
-   0,98754 g de poudre de tungstène.

##### Protocole

On mélange le tout (l'époxy SADER est très visqueuse et on ne subit plus
le phénomène de sédimentation). Néanmoins, on a le problème de l'air qui
reste piégé dans l'échantillon. Il faut dégazer sous vide.\
Dégazer par à-coup dans le récipient pendant 20 minutes (6 cycles
environ) en évitant les débordements.\
Verser le mélange dans le moule et dégazer le tout par à-coup pendant 20
minutes en évitant les débordements (une dizaine de cycles).\
Mettre le moule dans l'étuve à 80 °C pendant 1h30.

##### Test d'un transducteur

On a testé un transducteur industriel. ![Test d'un
transducteur](test-transducteur-500euros.jpg "fig:Test d'un transducteur"){width="600"}

### Jeudi 17 Septembre

Présence de Vincent.\

#### Manipulations

On a utilisé le même protocole que pour le [backing n° 5 du jeudi 9
avril 2015](#Jeudi_9_Avril "wikilink").\
On dispose de 3 tranches du [backing n°
11](#Jeudi_10_Septembre "wikilink") composé de poudre de dioxyde de
silicium, de poudre de tungstène et de résine époxy SADER.\
![Test acoustique du backing
11](paillasse-test-backing-11.jpg "fig:Test acoustique du backing 11"){width="600"}\
![Test acoustique du backing
11](test-backing-11.jpg "fig:Test acoustique du backing 11"){width="600"}\

#### Résultats

On numérote les tranches de 1 (haut) à 3 (bas).\
Tous calculs faits, on trouve les impédances acoustiques suivantes pour
chaque tranche :

-   1 : 3,46 MRayl.
-   2 : 3,47 MRayl.
-   3 : 3,51 MRayl.

#### Observations

Ce backing est de bonne qualité générale mais les impédances acoustiques
ne sont pas encore respectées, il faut y remédier. On ne discerne pas de
bulles d'air à l’œil nu, sauf sur la première tranche (bulles en
surface). Il est très résistant et homogène. Le dioxyde de silicium est
réparti correctement. On observe quelques amas de poudre de tungstène.\
Il reste à obtenir l'impédance voulue à savoir 4 MRayl. On va devoir
ajouter plus de poudre de tungstène pour corriger ce défaut.\
On réalise donc un nouveau backing.

#### Douzième essai de backing

On réalise un nouvel essai de backing en suivant le protocole habituel.
Cette fois on utilise du verre et beaucoup de tungstène.

##### Matériaux

Matériaux utilisés :\
\* 2,968 g d'époxy SADER.

-   -   1,4872 g de résine.
    -   1,48075 g de durcissant.
-   1,03598 g de SiO2.
-   6,05836 g de poudre de tungstène.

\
![Préparation du backing
12](preparation-backing-12.jpg "fig:Préparation du backing 12"){width="600"}\

##### Protocole

On mélange le tout (l'époxy SADER est très visqueuse et on ne subit plus
le phénomène de sédimentation). Néanmoins, on a le problème de l'air qui
reste piégé dans l'échantillon. Il faut dégazer sous vide.\
Dégazer par à-coup dans le récipient pendant 20 minutes (6 cycles
environ) en évitant les débordements.\
Verser le mélange dans le moule et dégazer le tout par à-coup pendant 20
minutes en évitant les débordements (une dizaine de cycles).\
Mettre le moule dans l'étuve à 80 °C pendant 1h30.

#### Cycles de dégazage du backing n° 12

![Dégazage du backing
12](degazage-backing-12.jpg "fig:Dégazage du backing 12"){width="600"}
![Dégazage du backing
12](mousse-backing-12.jpg "fig:Dégazage du backing 12"){width="600"}
![Système de dégazage du backing
12](systeme-degazage-backing-12.jpg "fig:Système de dégazage du backing 12"){width="600"}

[:File:degazage-backing-12-cycle-1.mp4](:File:degazage-backing-12-cycle-1.mp4 "wikilink")\
[:File:degazage-backing-12-cycle-2.mp4](:File:degazage-backing-12-cycle-2.mp4 "wikilink")\
[:File:degazage-backing-12-cycle-3.mp4](:File:degazage-backing-12-cycle-3.mp4 "wikilink")\
[:File:degazage-backing-12-cycle-4.mp4](:File:degazage-backing-12-cycle-4.mp4 "wikilink")\
[:File:degazage-backing-12-cycle-5.mp4](:File:degazage-backing-12-cycle-5.mp4 "wikilink")\
\
[:File:degazage-backing-12-moule.mp4](:File:degazage-backing-12-moule.mp4 "wikilink")

### Jeudi 15 Octobre

Présence de Vincent et de Gérard.\

#### Manipulations

On a utilisé le même protocole que pour le [backing n° 5 du jeudi 9
avril 2015](#Jeudi_9_Avril "wikilink").\
On dispose de 2 tranches du [backing n°
12](#Jeudi_17_Septembre "wikilink") composé de poudre de dioxyde de
silicium, de poudre de tungstène et de résine époxy SADER.\
![Test acoustique du backing
12](caracterisation-backing-12.jpg "fig:Test acoustique du backing 12"){width="600"}\

#### Résultats

On numérote les tranches de 1 (bas) à 2 (haut).\
Tous calculs faits, on trouve les impédances acoustiques suivantes pour
chaque tranche :

-   1 : 5,62 MRayl.
-   2 : 5,57 MRayl.

#### Observations

Ce backing est de bonne qualité générale et les impédances acoustiques
sont élevées du fait de la forte concentration en tungstène. Néanmoins,
elles ne sont pas encore respectées puisqu'on cherche à avoir un backing
à 4,5 Mrayl. On ne discerne pas de bulles d'air à l’œil nu. Il est très
résistant et homogène. Le dioxyde de silicium est réparti correctement.\
On réalise donc un nouveau backing contenant moins de tungstène.

#### Treizième essai de backing

On réalise un nouvel essai de backing en suivant le protocole habituel.
Cette fois on utilise du verre et du tungstène (moins de tungstène que
pour le backing précédent).

##### Matériaux

Matériaux utilisés :\
\* 3,0682 g d'époxy SADER.

-   -   1,55647 g de résine.
    -   1,51173 g de durcissant.
-   0,99483 g de SiO2.
-   3,40021 g de poudre de tungstène.

##### Protocole

On mélange le tout (l'époxy SADER est très visqueuse et on ne subit plus
le phénomène de sédimentation). Néanmoins, on a le problème de l'air qui
reste piégé dans l'échantillon. Il faut dégazer sous vide.\
Dégazer par à-coup dans le récipient pendant 20 minutes (6 cycles
environ) en évitant les débordements.\
Verser le mélange dans le moule et dégazer le tout par à-coup pendant 20
minutes en évitant les débordements (une dizaine de cycles).\
Mettre le moule dans l'étuve à 80 °C pendant 1h30.

#### Première tentative d'assemblage de transducteur

On a essayé de fabriquer un premier transducteur (backing + capsule
piézoélectrique).\
On a rencontré un problème lors de la soudure des fils sur la capsule
piézoélectrique. En effet, la soudure ne tient pas (surface spéciale).\
On doit donc utiliser une colle conductrice spéciale pour fixer des fils
sur la capsule piézoélectrique.\
![Tentative de soudure de fils sur la capsule
piézoélectrique](tentative-soudure-piezo.jpg "fig:Tentative de soudure de fils sur la capsule piézoélectrique"){width="600"}\

### Jeudi 22 Octobre

Présence de Vincent.\
Ce jour nous avons caractérisé les propriétés acoustiques du backing 13.
Ce dernier correspondant à nos attentes (impédance acoustique de 4,5
MRayl, homogène), nous avons réalisé un premier assemblage de capsule
piézoélectrique avec backing (numéro 14), backing constitué des mêmes
proportions que le backing numéro 13. Nous avons fabriqué deux fois plus
de backing numéro 14. Cela nous permettra de caractériser l'impédance
acoustique du backing 14 (utilisé pour l'assemblage) en utilisant la
méthode habituelle.

#### Manipulations - Test acoustique du backing n° 13

On a utilisé le même protocole que pour le [backing n° 5 du jeudi 9
avril 2015](#Jeudi_9_Avril "wikilink").\
On dispose de 2 tranches du [backing n°
13](#Jeudi_15_Octobre "wikilink") composé de poudre de dioxyde de
silicium, de poudre de tungstène et de résine époxy SADER.

#### Résultats

On numérote les tranches de 1 (bas) à 2 (haut).\
Tous calculs faits, on trouve les impédances acoustiques suivantes pour
chaque tranche :

-   1 : 4,52 MRayl.
-   2 : 4,57 MRayl.

#### Observations

Ce backing est de très bonne qualité. L'impédance acoustique est de
l'ordre de 4,5 MRayl, ce que nous souhaitons. Le backing est homogène
sans sédimentation.\
Il convient parfaitement. Nous pouvons commencer à fabriquer des
transducteurs.\
\
Pour un compte-rendu sur les différents essais de backing, vous pouvez
consulter ce document : [:File:Tableau de suivi des essais de
backing.pdf](:File:Tableau_de_suivi_des_essais_de_backing.pdf "wikilink")

#### Protocole de caractérisation acoustique du backing

##### Découper le backing en lamelles

La scie circulaire étant en panne, on coupe le backing à l'aide d'une
scie standard.\
![Découpage du backing
13](etablis-backing-13.jpg "fig:Découpage du backing 13"){width="600"}\
![Découpage du backing
13](etablis-backing-13-2.jpg "fig:Découpage du backing 13"){width="600"}\

##### Poncer les lamelles

Il faut poncer les lamelles pour qu'elles soit bien plates de chaque
côté.\
![Ponçage du backing
13](etablis-backing-13-3.jpg "fig:Ponçage du backing 13"){width="600"}\
![Ponçage du backing
13](etablis-backing-13-4.jpg "fig:Ponçage du backing 13"){width="600"}\

##### Observer les caractéristiques acoustiques

A l'aide d'un oscilloscope, d'un GBF et de transducteurs acoustiques, on
peut mesurer la vitesse v de propagation des ondes sonores dans les
tranches de backing.\
On mesure l'épaisseur des tranches à l'aide d'un pied à coulisse
(généralement les tranches font entre 1 et 2 mm). On connait également
le diamètre du backing (2 cm). On a donc accès au volume de la tranche.\
On mesure la masse des tranches à l'aide d'une balance de haute
précision.\
La masse et le volume de la tranche nous donne accès à la masse
volumique ρ de la tranche.\
On en déduit l'impédance acoustique Z de la tranche à l'aide de la
formule suivante : Z = ρ\*v.

![Test acoustique du backing
13](caracterisation-backing-13.jpg "fig:Test acoustique du backing 13"){width="600"}\
![Test acoustique du backing
13](caracterisation-backing-13-2.jpg "fig:Test acoustique du backing 13"){width="600"}
![Test acoustique du backing 13 (jaune : signal émis, rouge : signal
reçu)](caracterisation-backing-13-3.jpg "fig:Test acoustique du backing 13 (jaune : signal émis, rouge : signal reçu)"){width="600"}\
![Test acoustique du backing 13 (jaune : signal émis, rouge : signal
reçu)](caracterisation-backing-13-4.jpg "fig:Test acoustique du backing 13 (jaune : signal émis, rouge : signal reçu)"){width="600"}\
![Test acoustique du backing 13 (jaune : signal émis, rouge : signal
reçu)](caracterisation-backing-13-5.jpg "fig:Test acoustique du backing 13 (jaune : signal émis, rouge : signal reçu)"){width="600"}

\

#### Assemblage capsule piézoélectrique et backing numéro 14

Maintenant que le backing correspond à nos besoins (impédance acoustique
de 4,5 MRayl), nous allons assembler un élément piézoélectrique et un
backing.\
Nous fabriquons un backing en utilisant les mêmes proportions que le
backing n° 13 mais en doublant les doses. En effet, la moitié sera
utilisée pour l'assemblage avec le piézoélectrique tandis que l'autre
moitié sera utilisée pour faire des tests acoustiques.\
Il ne faut pas hésiter à bien dégazer (plusieurs cycles, casser le vide
quand il y a débordement et recommencer une dizaine de fois).\
![Backing n° 14 après
dégazage](transducteur-backing-13-11.jpg "fig:Backing n° 14 après dégazage"){width="600"}\

##### Ajouter un fil sur la face convexe de l'élément piézoélectrique

Cette étape nécessite l'utilisation de colle conductrice. En effet, il
n'est pas possible de souder directement un fil sur le piézoélectrique.
La soudure ne tient pas.\
![Élément piézoélectrique avec un fil
collé](transducteur-backing-13.jpg "fig:Élément piézoélectrique avec un fil collé"){width="600"}\

##### Placer le piézoélectrique dans un moule adapté

Le diamètre intérieur du moule doit parfaitement correspondre avec celui
de la capsule piézoélectrique pour éviter que cette dernière ne bouge
pendant le coulage.

\
![Moule utilisé pour le coulage du backing sur l'élément
piézoélectrique](transducteur-backing-13-2.jpg "fig:Moule utilisé pour le coulage du backing sur l'élément piézoélectrique"){width="600"}\
![Moule
démonté](transducteur-backing-13-3.jpg "fig:Moule démonté"){width="600"}\
![Moule démonté (vue de
dessus)](transducteur-backing-13-7.jpg "fig:Moule démonté (vue de dessus)"){width="600"}\
![Capsule piézoélectrique dans la chambre intérieure du
moule](transducteur-backing-13-4.jpg "fig:Capsule piézoélectrique dans la chambre intérieure du moule"){width="600"}\
![Capsule piézoélectrique dans la chambre intérieure du
moule](transducteur-backing-13-5.jpg "fig:Capsule piézoélectrique dans la chambre intérieure du moule"){width="600"}\
![Capsule piézoélectrique dans la chambre intérieure du moule (vue de
dessus)](transducteur-backing-13-6.jpg "fig:Capsule piézoélectrique dans la chambre intérieure du moule (vue de dessus)"){width="600"}\
![Moule monté avec capsule piézoélectrique dans la chambre intérieure du
moule (vue de
dessus)](transducteur-backing-13-8.jpg "fig:Moule monté avec capsule piézoélectrique dans la chambre intérieure du moule (vue de dessus)"){width="600"}\

##### Utiliser du scotch pour maintenir le fil en place

On graisse l'intérieur du moule et on protège le fil électrique en
utilisant une fine couche de scotch.

\
![Scotch sur le fil relié à la capsule piézoélectrique (vue de
dessus)](transducteur-backing-13-10.jpg "fig:Scotch sur le fil relié à la capsule piézoélectrique (vue de dessus)"){width="600"}\

##### Ajouter un peu de backing au fond du moule, contre le piézoélectrique

Cette petite couche de backing doit être parfaitement dégazée et
homogène. On prend soin de dégazer plusieurs fois pour minimiser les
bulles d'air.

##### Ajouter le backing nécessaire et dégazer

On ajoute la quantité de backing nécessaire (ici on fait un backing de
1,5 cm de hauteur). On dégaze bien plusieurs fois en évitant les
débordements (casser le vide régulièrement, faire une dizaine de
cycles).

##### Laisser polymériser à température ambiante

Il n'est pas utile de mettre le moule à l'étuve. Le backing n°13 a
polymérisé à température ambiante et il est de très bonne qualité.\
![Backing n° 14 prêt à être coulé dans le moule contenant le
piézoélectrique](transducteur-backing-13-9.jpg "fig:Backing n° 14 prêt à être coulé dans le moule contenant le piézoélectrique"){width="600"}\

#### Prochaines étapes

Nous allons caractériser les propriétés acoustiques du backing n° 14
(utilisé avec le piézoélectrique). Nous devons retrouver les mêmes
propriétés que le backing n°13 puisque nous avons utilisé les mêmes
proportions.\
Ensuite, nous allons tester notre premier transducteu, même si ce
dernier ne contient pas de couche adaptatrice d'impédance du côté
convexe.\
La prochaine étape importante est donc la fabrication d'une couche
adaptatrice d'impédance. Nous allons utiliser le même matériau que pour
le backing.

### Jeudi 5 Novembre

Présence de Vincent, Gérard et Patrice.\
Ce jour nous avons caractérisé les propriétés acoustiques du backing 14.
Ce dernier a été utilisé dans la conception du premier transducteur.
Nous avons également regardé l'impédance électrique du transducteur
numéro 1.

#### Test acoustique du backing n° 14

On a utilisé le même protocole que pour le [backing n° 5 du jeudi 9
avril 2015](#Jeudi_9_Avril "wikilink").\
On dispose de 2 tranches du [backing n°
14](#Jeudi_22_Octobre "wikilink") composé de poudre de dioxyde de
silicium, de poudre de tungstène et de résine époxy SADER.

#### Résultats

On numérote les tranches de 1 (bas) à 2 (haut, mauvaise planéité).\
Tous calculs faits, on trouve les impédances acoustiques suivantes pour
chaque tranche :

-   1 : 4,509 MRayl.
-   2 : 5,08 MRayl (résultat faussé puisque la tranche numéro 2 n'était
    pas totalement plate).

#### Observations

Ce backing est de très bonne qualité. L'impédance acoustique est de
l'ordre de 4,5 MRayl, ce que nous souhaitons. Le backing est homogène
sans sédimentation.\
Il convient parfaitement. Le transducteur numéro 1 est donc bien backé.\
\
![Test acoustique du backing
14](test-acoustique-backing-14.jpg "fig:Test acoustique du backing 14"){width="600"}

#### Transducteur n° 1

Ce transducteur est composé d'une capsule piézoélectrique et d'un
backing. Nous cherchons une solution pour fabriquer une couche
adaptatrice d'impédance de même composition que le backing, très fine
(lame quart d'onde) et épousant la forme concave de la capsule
piézoélectrique. Nous utilisons des capsules piézoélectriques de
diamètre 1,5 cm et de distance de focalisation de 10 cm.\
Nous utilisons une colle conductrice pour assembler les fils sur les
deux faces du piézoélectrique.\
Nous avons également caractérisé l'impédance électrique du transducteur
n° 1. Il semble en état de fonctionnement.\
\
![Etude de l'impédance électrique du transducteur
1](impedance-electrique-transducteur-1.jpg "fig:Etude de l'impédance électrique du transducteur 1"){width="600"}\
![Etude de l'mpédance électrique du transducteur
1](impedance-electrique-transducteur-1-2.jpg "fig:Etude de l'mpédance électrique du transducteur 1"){width="600"}\
![Etude de l'impédance électrique du transducteur
1](impedance-electrique-transducteur-1-3.jpg "fig:Etude de l'impédance électrique du transducteur 1"){width="600"}\
![Etude de l'impédance électrique du transducteur
1](impedance-electrique-transducteur-1-4.jpg "fig:Etude de l'impédance électrique du transducteur 1"){width="600"}

Bibliographie
-------------

Nous recensons ici les ouvrages, articles et autres documents utilisés
dans notre recherche.\
[Ondes élastiques dans les solides (Royer,
Dieulesaint)](Ondes_élastiques_dans_les_solides_(Royer,_Dieulesaint) "wikilink")\
![](These_-_FULLY_INTEGRATED_CMOS_ULTRASOUND_TRANSCEIVER_CHIP--FOR_HIGH-FREQUENCY_HIGH-RESOLUTION_ULTRASONIC_IMAGING_SYSTEMS.pdf "fig:These_-_FULLY_INTEGRATED_CMOS_ULTRASOUND_TRANSCEIVER_CHIP--FOR_HIGH-FREQUENCY_HIGH-RESOLUTION_ULTRASONIC_IMAGING_SYSTEMS.pdf")\
![](TX810_-_Switcher.pdf "fig:TX810_-_Switcher.pdf")\
![](Cypress_USB_Microcontroller.pdf "fig:Cypress_USB_Microcontroller.pdf")\
![](Ultrasonic.pdf "fig:Ultrasonic.pdf")\
[Thesis Insoo Kim 2009](Thesis_Insoo_Kim_2009 "wikilink")\
[Effect of backing layer composition on ultrasonic probe
bandwith](Effect_of_backing_layer_composition_on_ultrasonic_probe_bandwith "wikilink")\
[High frequency properties of passive materials for ultrasonic
transducers](High_frequency_properties_of_passive_materials_for_ultrasonic_transducers "wikilink")\
[Transducteurs mono-élément pour l'imagerie ultrasonore haute
résolution](Transducteurs_mono-élément_pour_l'imagerie_ultrasonore_haute_résolution "wikilink")\
[Transducer Models](Transducer_Models "wikilink")\
[Effects of backing, bonding, and electrode
layers](Effects_of_backing,_bonding,_and_electrode_layers "wikilink")\
[:File:araldite20-20-datasheet.pdf](:File:araldite20-20-datasheet.pdf "wikilink")\
[:File:dosage-composants-backing.pdf](:File:dosage-composants-backing.pdf "wikilink")\
[:File:cue\_materials\_database\_ver1.2\_aug\_2005.pdf](:File:cue_materials_database_ver1.2_aug_2005.pdf "wikilink")\
[:File:dosage-composants-backing-verre-araldite-20-20.pdf](:File:dosage-composants-backing-verre-araldite-20-20.pdf "wikilink")\
[:File:Tableau de suivi des essais de
backing.pdf](:File:Tableau_de_suivi_des_essais_de_backing.pdf "wikilink")\
[:File:Tableau de suivi des essais de
backing.docx](:File:Tableau_de_suivi_des_essais_de_backing.docx "wikilink")\
[:File:Ferroperm-Catalogue.pdf](:File:Ferroperm-Catalogue.pdf "wikilink")

<Category:Sonde> <Category:Balayage> <Category:TechTeam>
<Category:Transducer>



# S-VRW77AK

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Talk:Sonoline SX

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Approche Hacking de l'existant

Le but serait de re-créer une sonde à partir de matériaux existants:

-   Transducteurs déjà assemblés de chez Alibaba
-   Moteurs

Approches aujourd'hui
---------------------

### Exemples concrets de sondes à analyser

-   On a une sonde [IR1510AK](IR1510AK "wikilink") trouvée sur ebay
    @70USD (sonde en cours de démontage, détails sur
    [IR1510AK](IR1510AK "wikilink")).
-   Une autre KRETZ TECHNICK [S-VRW77AK](S-VRW77AK "wikilink") (IPX7)
    ULTRASOUND PROBE TRANSDUCER
    -   <http://www.accessdata.fda.gov/cdrh_docs/pdf/K940942.pdf> pour
        la fiche
    -   <http://www.icacommission.org/Proceedings/ICA1998Seattle/pdfs/vol_2/1069_1.pdf>
        pour les usages
-   Une ATL / Philips [A6-3](A6-3 "wikilink") (The ATL A6-3 has a wide
    aperature and has a frequency range of 3 to 6 MHz. - Annular array
    probe // Wide aperature // Mechanical sector )
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>

### MAteriel à récupérer

-   Sondes en général : les sondes à retroengineerer sont les suivantes:
    -   sondes mécaniques sectorielles
    -   sondes mécaniques mono-élément
    -   sondes à balayage
    -   "wobbler probes"
-   Celles à ne pas récupérer sont:
    -   sondes à matrice
    -   sondes multiélément
    -   sondes linéaires/sondes linéaires courbes
    -   sondes à balayage électronique

### Approche raspberry pi

-   Existant : démonstration d'un sonar
-   

Sourcing Potentiel
------------------

### Electronique

### Neuf mais ...

### Occasion

-   leboncoin : meilleur prix, 400€ used
    -   <http://www.leboncoin.fr/materiel_medical/747007800.htm>
    -   <http://www.leboncoin.fr/materiel_medical/781199518.htm?ca=12_s>
-   tous les sites de sourcing de matériel d'occasion..
    -   <http://bestengineer.chez.com/ultrasound.html>
    -   <http://www.dotmed.com/listing/vet.-ultrasound/kontron/sigma-1ac-&-2-probes/1194647>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/instruments-w-5-mhz-ds-type-:-wobbler-ultrasound-transducer-probe/1557682>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/5-mhz-b-/1557669>
    -   <http://www.umed-ultrasound.com/StockSondes_KONTRON.htm>
-   Autres
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=sonde+ultrasons>
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=echographe>
    -   <http://medical.fr/fr/1105-sonde>?&orderby=price&orderway=asc
    -   <http://www.dotmed.com/listings/search/equipment.html?key=wobbler&type=equipment>
    -   <http://www.ebay.com/sch/i.html?_odkw=sector+ultrasound&_sop=3&_from=R40&_osacat=0&_ssc=1&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xwobbler+ultrasound&_nkw=wobbler+ultrasound&_sacat=0>
-   A suivre
    -   <http://www.ebay.com/itm/Aloka-ASU-32CWD-5-Mechanical-Doppler-Probe-/331496509627>?
    -   <http://www.ebay.com/itm/GE-2-5-48S-P-N-45-231613G1-Sector-Ultrasound-Transducer-Probe-/111626681515?pt=LH_DefaultDomain_0&hash=item19fd77fcab>
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>
        -- ATL / Philips A6-3

Manuels
-------

-   <http://www.frankshospitalworkshop.com/equipment/documents/ultrasonographs/user_manuals/Kontron_Sigma_1_-_Usermanual.pdf>

<Category:TechTeam> <Category:RetroEngineering>



# Stuart Foster

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Talk:Sonoline 3000

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Sevig Ayter

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# David L. Greenwood

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Enjeux techniques

The aim of the technical stake is to solve the question: how can we
build an open-source portable echograph with a community?

Hardware
--------

Before starting, we recommend you get a read of [ Introduction to the
echopen hardware](:Category:HardIntro "wikilink") to get to know the
technical aspects and engineering behind the artifact.

Kits and products
-----------------

Given the nature of the product, a tool to be used by health
professional, echopen is facing the issue of

Engineering
===========

Obviously, there are a couple of questions that are lurking around, such
as:

-   How to build an [Open-source
    Hardware](Open-source_Hardware "wikilink") - what guidelines to be
    used?
    -   We had first guidelines on our [ first big
        challenge](Challenge:_the_echOpen_shield#Questions "wikilink")
    -   How to document on a wiki: it's easy to push code on github,
        much less with physical objects =)

Pending work
------------

-   Progress being done at the [ENS](ENS "wikilink") with [
    Constant](User:Constant_Bourdeloux "wikilink") : [Carnet de bord -
    Laboratoire SATIE](Carnet_de_bord_-_Laboratoire_SATIE "wikilink")
    for the transducer [EchOpen
    Transducer‎](EchOpen_Transducer‎ "wikilink")
-   Some hacking of previous probes such as the [ATL
    A6-3](ATL_A6-3 "wikilink"), the [S-VRW77AK](S-VRW77AK "wikilink"),
    or [IR1510AK](IR1510AK "wikilink") are on [Approche Hacking de
    l'existant](Approche_Hacking_de_l'existant "wikilink"): we do love
    [Kretztechnik](:Category:Kretztechnik "wikilink") for the beauty,
    simplicity and robustness of their design !
-   Building the echOpen tranducer

Done
----

-   Hardware
    -   17/10/2015: Structuring our knowledge on hardware : a must read
        page is
    -   02/10/2015: We built our first kit : Category:Emile
    -   01/07/2015 En apprendre plus sur le
        [Balayage](Balayage "wikilink") en général, une [Introduction to
        Mechanical
        probes](Introduction_to_Mechanical_probes "wikilink"), et voir
        la [Old Devices list](Old_Devices_list "wikilink"), et apprendre
        ce qui s'est fait dans les
        [Premières\_années](Premières_années "wikilink")
        de l'échographie.
-   Intellectual property
    -   04/04/2015 : listing interesting patents at
        [:Category:Patents](:Category:Patents "wikilink") and inventors
        [:Category:CoolHand](:Category:CoolHand "wikilink").
-   Signal processing:
    -   14/10/2015: Having fun with [ FFT Filtering and signal
        processing](Compressing_with_FFT "wikilink").

Bibliography
------------

<Category:TechTeam> <Category:Sonde> <Category:HardIntroduction>
<Category:HardIntroduction>




# Réunion - 28 Mars 2015

Le but serait de re-créer une sonde à partir de matériaux existants:

-   Transducteurs déjà assemblés de chez Alibaba
-   Moteurs

Approches aujourd'hui
---------------------

### Exemples concrets de sondes à analyser

-   On a une sonde [IR1510AK](IR1510AK "wikilink") trouvée sur ebay
    @70USD (sonde en cours de démontage, détails sur
    [IR1510AK](IR1510AK "wikilink")).
-   Une autre KRETZ TECHNICK [S-VRW77AK](S-VRW77AK "wikilink") (IPX7)
    ULTRASOUND PROBE TRANSDUCER
    -   <http://www.accessdata.fda.gov/cdrh_docs/pdf/K940942.pdf> pour
        la fiche
    -   <http://www.icacommission.org/Proceedings/ICA1998Seattle/pdfs/vol_2/1069_1.pdf>
        pour les usages
-   Une ATL / Philips [A6-3](A6-3 "wikilink") (The ATL A6-3 has a wide
    aperature and has a frequency range of 3 to 6 MHz. - Annular array
    probe // Wide aperature // Mechanical sector )
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>

### MAteriel à récupérer

-   Sondes en général : les sondes à retroengineerer sont les suivantes:
    -   sondes mécaniques sectorielles
    -   sondes mécaniques mono-élément
    -   sondes à balayage
    -   "wobbler probes"
-   Celles à ne pas récupérer sont:
    -   sondes à matrice
    -   sondes multiélément
    -   sondes linéaires/sondes linéaires courbes
    -   sondes à balayage électronique

### Approche raspberry pi

-   Existant : démonstration d'un sonar
-   

Sourcing Potentiel
------------------

### Electronique

### Neuf mais ...

### Occasion

-   leboncoin : meilleur prix, 400€ used
    -   <http://www.leboncoin.fr/materiel_medical/747007800.htm>
    -   <http://www.leboncoin.fr/materiel_medical/781199518.htm?ca=12_s>
-   tous les sites de sourcing de matériel d'occasion..
    -   <http://bestengineer.chez.com/ultrasound.html>
    -   <http://www.dotmed.com/listing/vet.-ultrasound/kontron/sigma-1ac-&-2-probes/1194647>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/instruments-w-5-mhz-ds-type-:-wobbler-ultrasound-transducer-probe/1557682>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/5-mhz-b-/1557669>
    -   <http://www.umed-ultrasound.com/StockSondes_KONTRON.htm>
-   Autres
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=sonde+ultrasons>
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=echographe>
    -   <http://medical.fr/fr/1105-sonde>?&orderby=price&orderway=asc
    -   <http://www.dotmed.com/listings/search/equipment.html?key=wobbler&type=equipment>
    -   <http://www.ebay.com/sch/i.html?_odkw=sector+ultrasound&_sop=3&_from=R40&_osacat=0&_ssc=1&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xwobbler+ultrasound&_nkw=wobbler+ultrasound&_sacat=0>
-   A suivre
    -   <http://www.ebay.com/itm/Aloka-ASU-32CWD-5-Mechanical-Doppler-Probe-/331496509627>?
    -   <http://www.ebay.com/itm/GE-2-5-48S-P-N-45-231613G1-Sector-Ultrasound-Transducer-Probe-/111626681515?pt=LH_DefaultDomain_0&hash=item19fd77fcab>
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>
        -- ATL / Philips A6-3

Manuels
-------

-   <http://www.frankshospitalworkshop.com/equipment/documents/ultrasonographs/user_manuals/Kontron_Sigma_1_-_Usermanual.pdf>

<Category:TechTeam> <Category:RetroEngineering>



# Richard A. Terwilliger

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# John W. Sliwa

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# S-VRW77AK

Démontage d'une sonde vaginale Kretz.

Schéma global de la sonde
-------------------------

![Photographie de la sonde
S-VRW77AK.](schéma1.png "fig:Photographie de la sonde S-VRW77AK."){width="750"}
La sonde se décompose essentiellement en 4 parties :

-   Connectique : assure l'interface sonde-ordinateur selon un
    branchement spécifique
-   Électronique : reçoit, interprète et traite les signaux
    d'entrée/sortie
-   Tige : isole le piézo de l'électronique
-   Piézo : élément piézoélectrique jouant le rôle d'émetteur/récepteur
    d'ondes ultrasonores

Démontage partie connectique
----------------------------

![Boitier connecteur de la sonde et
prises](image1.png "fig:Boitier connecteur de la sonde et prises"){width="300"}
Le connecteur de la sonde est un boitier composé de deux étages ; le
premier étage contenant la prise A et le deuxième étage contenant la
prise B, directement reliée au câble.

### Prise A

<File:20150811_143242.jpg> <File:20150811_143303.jpg>
<File:20150811_143331.jpg>

### Prise B

<File:20150811_143350.jpg> <File:20150811_143422.jpg>
<File:20150811_143511.jpg> <File:20150811_143519.jpg>

Démontage partie électronique
-----------------------------

![Partie connectique ; l'enveloppe plastique a été
retirée.](electronique.png "fig:Partie connectique ; l'enveloppe plastique a été retirée."){width="750"}
Sous l'enveloppe plastique, la partie électronique se décompose
essentiellement en 4 parties :

-   Deux étages de circuits électroniques cachées sous une bande de
    cuivre faisant office de masse (à gauche)
-   Un moteur assurant la rotation suivant l'axe de la tige centrale,
    reliée aux transducteurs et équipé de codeurs de position à capteur
    optique
-   Un circuit imprimé contrôlant l'asservissement du moteur
-   Un moteur assurant la rotation suivant un axe transversal à la tige
    centrale, également reliée aux transducteurs

L'ensemble est maintenu par une armature métallique sur laquelle sont
fixés les différentes parties mentionnées ci-dessus ![Zoom sur les trois
composant principaux de la partie
électronique.](elec1.png "fig:Zoom sur les trois composant principaux de la partie électronique."){width="500"}
Une fois la bande de cuivre retirée, on découvre les deux étages de
circuits électronique (encadré rose) et l'on peut extraire le moteur
(encadré rouge). L'encadré vert met en évidence le troisième circuit
électronique, initialement vissé sur l'armature ; ce dernier assure la
liaison entre les signaux provenant de la partie connectique, et
relayées par les deux étages de circuits imprimés, et les moteurs (les
fils de connexion ont été sectionnés sur la photo ci-contre). Le
deuxième moteur est à peine visible sur la photo (à droite). Ce circuit,
n'est pas directement fixé sur l'armature métallique mais sur un
composant annexe, servant de support et lui même fixé sur l'armature
principale.

### Circuit électronique central

Le circuit électronique central (encadré vert sur la photo ci-dessus)
joue le rôle de "carrefour électronique" de la sonde, reliant ainsi les
signaux provenant de l'opérateur, les signaux provenant des moteurs et
les signaux issus des piézos. ![Circuit électronique
central.](cirele.png "fig:Circuit électronique central."){width="500"}

-   Les moteurs, axial et transversal, sont reliés au circuit
    électronique central par 2x7 fils (encadrés rouges et violet) : deux
    fils d'alimentation + cinq fils codeurs. Sur la photo ci-contre, les
    4 fils codeurs (en bleu) ont été sectionnées et les fils
    d'alimentation suivent la convention rouge/noir. Il manque un fil
    codeur pour chaque moteur.

<!-- -->

-   L'asservissement des moteurs et la communication avec les piézo
    (signaux d'entrée/sortie) sont assurés par une douzaine de fils
    (encadrés jaunes).

<Category:TechTeam> <Category:RetroEngineering>



# Talk:Sonoline SX

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Approche Hacking de l'existant

Le but serait de re-créer une sonde à partir de matériaux existants:

-   Transducteurs déjà assemblés de chez Alibaba
-   Moteurs

Approches aujourd'hui
---------------------

### Exemples concrets de sondes à analyser

-   On a une sonde [IR1510AK](IR1510AK "wikilink") trouvée sur ebay
    @70USD (sonde en cours de démontage, détails sur
    [IR1510AK](IR1510AK "wikilink")).
-   Une autre KRETZ TECHNICK [S-VRW77AK](S-VRW77AK "wikilink") (IPX7)
    ULTRASOUND PROBE TRANSDUCER
    -   <http://www.accessdata.fda.gov/cdrh_docs/pdf/K940942.pdf> pour
        la fiche
    -   <http://www.icacommission.org/Proceedings/ICA1998Seattle/pdfs/vol_2/1069_1.pdf>
        pour les usages
-   Une ATL / Philips [A6-3](A6-3 "wikilink") (The ATL A6-3 has a wide
    aperature and has a frequency range of 3 to 6 MHz. - Annular array
    probe // Wide aperature // Mechanical sector )
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>

### MAteriel à récupérer

-   Sondes en général : les sondes à retroengineerer sont les suivantes:
    -   sondes mécaniques sectorielles
    -   sondes mécaniques mono-élément
    -   sondes à balayage
    -   "wobbler probes"
-   Celles à ne pas récupérer sont:
    -   sondes à matrice
    -   sondes multiélément
    -   sondes linéaires/sondes linéaires courbes
    -   sondes à balayage électronique

### Approche raspberry pi

-   Existant : démonstration d'un sonar
-   

Sourcing Potentiel
------------------

### Electronique

### Neuf mais ...

### Occasion

-   leboncoin : meilleur prix, 400€ used
    -   <http://www.leboncoin.fr/materiel_medical/747007800.htm>
    -   <http://www.leboncoin.fr/materiel_medical/781199518.htm?ca=12_s>
-   tous les sites de sourcing de matériel d'occasion..
    -   <http://bestengineer.chez.com/ultrasound.html>
    -   <http://www.dotmed.com/listing/vet.-ultrasound/kontron/sigma-1ac-&-2-probes/1194647>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/instruments-w-5-mhz-ds-type-:-wobbler-ultrasound-transducer-probe/1557682>
    -   <http://www.dotmed.com/listing/ultrasound-transducer/kontron/5-mhz-b-/1557669>
    -   <http://www.umed-ultrasound.com/StockSondes_KONTRON.htm>
-   Autres
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=sonde+ultrasons>
    -   <http://www.leboncoin.fr/materiel_medical/?f=a&th=1&q=echographe>
    -   <http://medical.fr/fr/1105-sonde>?&orderby=price&orderway=asc
    -   <http://www.dotmed.com/listings/search/equipment.html?key=wobbler&type=equipment>
    -   <http://www.ebay.com/sch/i.html?_odkw=sector+ultrasound&_sop=3&_from=R40&_osacat=0&_ssc=1&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xwobbler+ultrasound&_nkw=wobbler+ultrasound&_sacat=0>
-   A suivre
    -   <http://www.ebay.com/itm/Aloka-ASU-32CWD-5-Mechanical-Doppler-Probe-/331496509627>?
    -   <http://www.ebay.com/itm/GE-2-5-48S-P-N-45-231613G1-Sector-Ultrasound-Transducer-Probe-/111626681515?pt=LH_DefaultDomain_0&hash=item19fd77fcab>
    -   <http://www.ebay.com/itm/ATL-Philips-A6-3-Wide-Aperature-Ultrasound-Probe-Transducer-for-UM9-HDI-/221763430549?pt=LH_DefaultDomain_0&hash=item33a2216895>
        -- ATL / Philips A6-3

Manuels
-------

-   <http://www.frankshospitalworkshop.com/equipment/documents/ultrasonographs/user_manuals/Kontron_Sigma_1_-_Usermanual.pdf>

<Category:TechTeam> <Category:RetroEngineering>



# Stuart Foster

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Talk:Sonoline 3000

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# Sevig Ayter

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>



# David L. Greenwood

C'est là où l'autopsie de la IR1510AK a commencé !

Step 1
------

<File:IR1510AK-> (1).JPG <File:IR1510AK-> (2).JPG <File:IR1510AK->
(3).JPG <File:IR1510AK-> (5).JPG <File:IR1510AK-> (6).JPG
<File:IR1510AK-> (7).JPG <File:IR1510AK-> (12).JPG <File:IR1510AK->
(14).JPG <File:IR1510AK-> (15).JPG <File:IR1510AK-> (16).JPG
<File:IR1510AK-> (17).JPG <File:IR1510AK-> (18).JPG <File:IR1510AK->
(19).JPG <File:IR1510AK-> (21).JPG <File:IR1510AK-> (24).JPG
<File:IR1510AK-> (25).JPG <File:IR1510AK-> (26).JPG <File:IR1510AK->
(27).JPG <File:IR1510AK-> (30).JPG <File:IR1510AK-> (32).JPG
<File:IR1510AK-> (33).JPG

Step II
-------

<File:IR1510AK> - Step II (12).JPG <File:IR1510AK> - Step II (1).JPG
<File:IR1510AK> - Step II (2).JPG <File:IR1510AK> - Step II (3).JPG
<File:IR1510AK> - Step II (4).JPG <File:IR1510AK> - Step II (6).JPG
<File:IR1510AK> - Step II (7).JPG <File:IR1510AK> - Step II (8).JPG
<File:IR1510AK> - Step II (9).JPG <File:IR1510AK> - Step II (11).JPG

Autopsie commentée
==================

Géométrie générale de la sonde
------------------------------

Une fois le capot de la sonde démonté, on remarque qu'elle est composée
de trois circuits imprimés :

![](luc1b.jpg "fig:luc1b.jpg") ![](luc2b.jpg "fig:luc2b.jpg")

le circuit 1 (en rouge) situé à la base de la sonde, et les circuits 2
(en vert) et 3 (en bleu) situés en haut de la sonde. Le circuit 1 est le
circuit principal les circuits 2 et 3 étant des déviations de celui-ci.
Ensuite en haut de la sonde se trouve une tige sur laquelle sont fixés
trois transducteurs :

![](IR1510AK_tete_de_sonde.jpg "IR1510AK_tete_de_sonde.jpg"){width="500"}

la sonde doit travailler à trois fréquences différentes étant donné
qu'on a trois tailles de transducteur. Si on retire maintenant la tige :

![](IR1510AK - Step II (1).JPG  "IR1510AK - Step II (1).JPG "){width="500"}

on voit trois paires de fils entraînées en rotation, chaque paire permet
de contrôler un transducteur. Le collecteur tournant (pièce permettant
d'avoir une connexion électrique entre une pièce fixe et une pièce
tournante) n'est donc pas dans la tige, mais dans le corps de la sonde.

Démontage et définition des blocs constituant la sonde
------------------------------------------------------

Dans cette section nous allons développer le démontage de chaque bloc et
définir leur rôle (si possible) dans le fonctionnement de la sonde. Les
blocs sont démontés de haut en bas, on ne suit donc pas les numéros des
circuits présentés précédemment.

### Le collecteur tournant

La première pièce accessible est la pièce dont sort les trois paires de
câbles contrôlant les transducteurs. Les circuits 2 et 3 sont attachés à
cette pièce :

![](IR1510AK_collecteur_tournant_1.JPG "IR1510AK_collecteur_tournant_1.JPG"){width="500"}

on voit sur cette image le côté de la sonde où est fixé le circuit 2.
Contrairement au circuit 3 qui est juste fixé par des vis sur cette
pièce, le circuit 2 est en plus collé. Si on y regarde d'un peu plus
près, on voit que cette pièce est entraînée en rotation par le moteur à
l'aide d'une pièce en plastique noir :

![](IR1510AK_liaison_moteur_collecteur.JPG "IR1510AK_liaison_moteur_collecteur.JPG"){width="500"}

et qu'au niveau des points de colle passent des câbles reliant
l’intérieur du système au circuit 2 :

![](IR1510AK_collecteur_profil.JPG "IR1510AK_collecteur_profil.JPG"){width="500"}

On a donc en entré trois câbles coaxiaux qui sont fixes par rapport au
bâti et en sortie 3 paires de fils en rotation, c'est donc bien un
collecteur tournant qui une fois démonté ressemble à ça :

![](IR1510AK_collecteur_tournant_2.JPG "IR1510AK_collecteur_tournant_2.JPG"){width="500"}

### Le circuit 3

Une fois démonté, le circuit 3 ressemble à ça :

![](IR1510AK_circuit3.JPG "IR1510AK_circuit3.JPG"){width="500"}

ce circuit me laisse perplexe car il y a un circuit RC qui n'est relié
qu'à un seul fil (droite de l'image)...

### Le circuit 1

On voit sur les photos suivantes le circuit 1 de face et de l'arrière
respectivement.

![](IR1510AK_circuit1_face2.jpg "fig:IR1510AK_circuit1_face2.jpg"){width="500"}
![](IE1510AK_circuit1_arriere.JPG "fig:IE1510AK_circuit1_arriere.JPG"){width="500"}

De face on voit le côté des soudures avec les trois fils coaxiaux qui
vont contrôler les transducteurs. Sur la photo de face, le cercle rouge
repère comment est fixé le circuit sur le bâti : une partie du bâti est
plié pour maintenir en place le circuit 1. A l'arrière les composants
sont cachés par un boitier à gauche et à droite il y a deux relais. Les
câbles que l'on voit sur la face arrière sont les câbles alimentant le
moteur (on remarque la logique de ne pas suivre un code couleur...).

### Le moteur

Maintenant que tous les circuits sont démontés de la sonde, on peut
retirer le moteur :

![](IR1510AK_moteur.JPG "IR1510AK_moteur.JPG"){width="500"}

Après quelques recherches, il semble que l'on ai affaire à un moteur pas
à pas bipolaire. A l'aide d'un multimètre, on note que les fils qui sont
reliés entre eux sont le marron avec le bleu et le jaune avec le rouge.

### Le bâti

Pour des raisons de sécurité, le bâti est relié à la masse en différents
points

### La connectique

La sonde est reliée à l'explorer par la connectique que l'on voit
ci-dessous

![](IR1510AK_connectique_face.JPG "fig:IR1510AK_connectique_face.JPG"){width="500"}
![](IR1510AK_connectique_arrière.jpg "fig:IR1510AK_connectique_arrière.jpg"){width="500"}

9 câbles et 3 câbles coaxiaux sont reliés à la connectique.

Issues
======

Issue 1 | Schéma électrique
---------------------------

Suite au démontage de la sonde, 4 questions se sont posées auxquelles
nous n'avons pas de réponses pour le moment.

# les connections du relais et entre les deux relais.
2.  l'inductance
3.  les broches du transistor ( fonction d'amplificateur ici ? )
4.  le fonction des 4 diode D1-ZD4-ZD3-D2 ( Un montage en pont ? mais
    c'est pas complet ...)

Voici un schéma du circuit, réalisé avec le logiciel PCBWeb Designer :

![ 700 px](Schema electronique-sonde IR.png  " 700 px")

Et quelques photos des cartes électroniques dont il est question :

![ 256px](IR1510AK3.jpg  "fig: 256px") ![
256px](IR1510AK1.jpg  "fig: 256px") ![
256px](IR1510AK4.jpg  "fig: 256px") ![
256px](IR1510AK2.jpg  "fig: 256px")

![ 650 px](IMG_sonde IR.JPG  " 650 px")

Le but étant de savoir s'il y a des mauvaises connexions dans ce circuit
et de connaître les fonctions de chacune des parties.

Nous avons posé les questions sur le *' forum
snootlab*'[1](http://forum.snootlab.com/viewtopic.php?f=32&t=1386) pour
en discuter avec les électroniciens.

<Category:TechTeam> <Category:RetroEngineering>

