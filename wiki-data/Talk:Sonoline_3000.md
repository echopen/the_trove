1.  Talk:Sonoline 3000

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

1.  les connections du relais et entre les deux relais.
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
