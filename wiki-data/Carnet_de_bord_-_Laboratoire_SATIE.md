1.  Carnet de bord - Laboratoire SATIE

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
