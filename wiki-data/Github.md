1.  Github

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
