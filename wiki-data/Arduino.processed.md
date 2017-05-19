

# Michaud

<div style="float:right;">
\_\_TOC\_\_

</div>
Le [Michaud](Michaud "wikilink") pourrait être le premier prototype, le
livrable 0.1 de la communauté pour la communauté.

Il aurait plusieurs avantages:

-   Permettre d'avoir un kit prototype de sonde : une liste de
    composants que l'on peut acheter sur le marché, du code pour le
    faire tourner.
-   Impliquer la communauté Arduino, dont parisienne - mix hard et soft.
-   Documentation riche
-   Permettre de mettre du code "sonde" disponible directement sur
    GitHub
-   On garde la philosophie "open" du projet

Pourquoi faire ce livrable? Cela nous permet de commencer à diffuser un
prototype hardware, "assez facile" à sourcer et à monter (en tout cas,
c'est le cahier des charges en une ligne de cette version), qui intègre
déjà du code, et qui leverage les connaissances de la communauté arduino
=)

Contexte de la Michaud-Arduino
==============================

A priori, ce serait un Kit compatible avec le [Cahier des charges
V0.0](Cahier_des_charges_V0.0 "wikilink") mais également [Cahier des
charges V0.1](Cahier_des_charges_V0.1 "wikilink").

Schéma
------

![](schemamichaud.png "schemamichaud.png")

Microconcontroleur
------------------

L'Arduino DUE : ''The Arduino Due is a microcontroller board based on
the Atmel SAM3X8E ARM Cortex-M3 CPU (datasheet). It is the first Arduino
board based on a 32-bit ARM core microcontroller. It has 54 digital
input/output pins (of which 12 can be used as PWM outputs), 12 analog
inputs, 4 UARTs (hardware serial ports), a 84 MHz clock, an USB OTG
capable connection, 2 DAC (digital to analog), 2 TWI, a power jack, an
SPI header, a JTAG header, a reset button and an erase button. Puissant
car:

-   A 32-bit core, that allows operations on 4 bytes wide data within a
    single CPU clock. (for more information look int type page).
-   CPU Clock at 84Mhz.
-   96 KBytes of SRAM.
-   512 KBytes of Flash memory for code.
-   a DMA controller, that can relieve the CPU from doing memory
    intensive tasks.

'' Plus de détails sur <https://www.arduino.cc/en/Main/arduinoBoardDue>

Après discussion avec l'équipe, il semble qu'on puisse remonter une
sonde d'essai sur la base d'un [Arduino DUE](Arduino_DUE "wikilink").
Processeur basé sur du 84Mhz, devrait etre suffisant. Des inputs analog,
54 digital, 2 DAC, une connection USB déjà présente.

A voir si l'acquisition se fait correctement, principalement au niveau
de l'acquisition et de la fréquence d'échantillonage.

Transducteur
------------

-   Voir si il est possible de récupérer celui de la
    [IR1510AK](IR1510AK "wikilink"). Sinon, en commander après notre
    réunion à Tours. Ca vaut aussi le coup de contacter les personnes
    ayant passé une thèse dans le domaine, par exemple PM (fait partie
    de notre biblio).

Electronique
------------

Le reste du matériel serait dans l'électronique:

-   Dans un premier temps, pas besoin d'ampli en reception, si tests
    dans un aquarium. Cela permet de retirer le switch, et l'ampli, donc
    de plugger directement sur le shield.
-   Challenge : quid des shields arduino? Quelle utilisation dans le
    cadre de notre projet ?
-   Relais : des shields existent tout faits. D'autres ressources
    permettent de comprendre la logique :
    <https://cuillere2000.wordpress.com/2014/05/02/commander-un-relais-avec-un-micro-controleur-savoir-choisir-ses-composants/>

Mécanique
---------

### Moteur

-   Utiliser le moteur de la [S-VRW77AK](S-VRW77AK "wikilink"). On va
    vérifier si l'encodage optique fonctionne correctement.
-   Retrouver les référence d'un bon moteur ([moteur à codage de
    position optique](moteur_à_codage_de_position_optique "wikilink")
    (codeurs absolus multitours)). Entrée et sorties pilotables par
    l'arduino à travers un shield?

### Encodeur de position

-   <http://ams.com/eng>

### Collecteur

-   On peut réutiliser celui de la [IR1510AK](IR1510AK "wikilink")
    par exemple.
-   Identifier un [collecteur
    tournant](collecteur_tournant "wikilink") (mécanique) pour Arduino?
    -   <http://www.robotshop.com/eu/fr/collecteur-tournant-collerette-736.html>,
        collecteur à 300 rpm
    -   <http://www.moog.com/products/slip-rings/>
    -   <http://www.moflon.com/>

Pending Issues
--------------

### Documentation Arduino

OK, mis dans notre drive.

### Challenges

-   \[CLOSED - books, doc, expériementation\] Comment utiliser un
    arduino?
-   Où trouver le bon transducteur, pistes : imasonic, sofranel,
    sonaxis, olympus
-   Où trouver des collecteurs?
-   Où trouver des bons moteurs? [micromo](http://www.micromo.com)
-   Comment se servir des shields?
-   Comment utiliser le 100ksps d'échantillonnage du DUE
    -   <http://forum.arduino.cc/index.php?topic=113879.0>
    -   Si pas assez : see [The Case for BeagleBone
        Black](The_Case_for_BeagleBone_Black "wikilink").
    -   Or else, [The case for Red
        Pitaya](The_case_for_Red_Pitaya "wikilink").

--[Hyacinthe](User:Hyacinthe "wikilink")
([talk](User_talk:Hyacinthe "wikilink")) 13:58, 14 August 2015 (EDT)

### Quelques sites ressources

-   <http://forum.arduino.cc/index.php?topic=177489.0>
-   <http://forum.arduino.cc/index.php?topic=79285.0>
-   <http://www.instructables.com/answers/How-can-i-image-ultrasound-using-PIC-or-any-othe/>
-   <http://electronics.stackexchange.com/questions/50577/what-ultrasonic-sensoremitter-should-i-use-for-my-medical-ultrasound-project>
-   <http://electronics.stackexchange.com/questions/129582/what-is-the-current-consumed-by-ultrasonic-sensors-transducers-1-2mhz-to-gener?rq=1>
-   <http://www.piceramic.com/products/piezo-elements.html>

The Michaud-Pitaya
==================

Schematics
----------

Here's the rough idea of the MichaudPitaya
![](Michaud-Pitaya.png "fig:Michaud-Pitaya.png"){width="800"}

The reason of the change
------------------------

Ideas
-----

Simplifying all the questions we had with the Arduino.

### Soft

All the soft should be on the RedPitaya card..

### Motor

Could be setup using the GPIOs of the Pitaya

### Transducer

Several solutions:

-   Using the one we got?
-   Using the ones we got on the old equipment
-   Chinese ones?
-   The academic group ones?

### Electronics

If using the +-16V transducer, only two items remain:

-   A 5V to 16V [Boost Converter](Boost_Converter "wikilink")
-   A [Tx/Rx Switch](Tx/Rx_Switch "wikilink") at the transducer level

Resources
---------

All relevant updates were described on [Prototype](Prototype "wikilink")

<Category:Microcontroller> <Category:Prototype> <Category:V0>
<Category:Michaud> <Category:Arduino> <Category:RedPitaya>
<Category:HardIntroduction>



# Challenge: Signal Acquisition through Arduino

**Défi**
--------

echOpen doit acquérir un signal à une fréquence élevée.. trop pour lui?

**\#arduino \#acquisition \#can \#performance**

**Difficulté**
--------------

medium

**Skills**
----------

Electronique, Analog to Digital Conversion

**Mission**
-----------

### Acquisition électronique

Le problème est d'utiliser un arduino due pour émettre et recevoir un
signal à 84 MHz (fréquence du microcontroleur). Pour cela on dispose
d'un CAN 80 Msps 14 bits (ad9641bcpz-80) et d'un CNA 80 Msps 14 bits
(ad9117bcpzn).

L'objectif est donc qu'à chaque temps d'horloge (à 84 MHz) on puisse
envoyer via le CNA (ou recevoir via le CAN) un nombre en 14 bits (ou en
8 bits avec d'autres CAN et CNA). La question est alors comment coder
l'arduino pour être sur qu'à chaque temps d'horloge on envoie (ou
reçoit) le nombre voulu.

*Faut il utiliser d'une horloge externe pour tout synchroniser ? Y a
t'il un bus à privilégier pour cela : SPI, I2C, série ?*

### Physique du problème

-   Le signal arrive sur une porteuse à 5MHz, d'où un échantillonage à
    ces fréquences. On en veut l'enveloppe par la suite, que l'on veut
    récupérer à une résolution de l'ordre de 0.50µs (résolution, 1mm
    à 1500m/s). Peut etre que l'électronique amont peut gérer ça?
-   L'acquisition se fait par burst, tu choppes say 128 points, soit
    8.5µs, et entre deux acquisitions tu as en ordre de grandeur
    50µs d'attente.

### Elements PHH

En fait, c'est pas tant une question de processeur, que de bus
disponible. (200k échantillons par seconde, un arduino peut
effectivement le tenir). L'interface utilisé par l'ADC proposé utilise
un bus JESD204A. C'est un bus plutôt prévu pour être utilisé avec des
FPGA/ASIC dédiés. De ce que je vois, le JESD204A n'est même pas
compatible électriquement avec le LVDS (la norme ""habituelle"" pour des
signaux différentiels). Je pense qu'à moins d'avoir une carte affichant
explicitement le support du JESD204, ça ne passera pas. (que ce soit sur
le PRU ou le processeur principal ne change pas grand chose au résultat,
c'est probablement plus simple si c'est sur le processeur principal,
enfin question de goût). (Alexis si ça te dit quelque chose ce type
d'interfaces, et que t'as déjà vu ça quelque part)

Du coup, je vais poser la question autrement: vous avez vraiment besoin
de 84MHz/14bits ? Pour une précision de 0.5us, sans interpolation, 4MHz
devrait suffire, non ? (Avec interpolation, en fonction du type du
signal, ça me choquerait pas de pouvoir descendre à 800kHz)

En relisant un peu les posts au dessus, je pense comprendre que vous
voulez monter aussi haut pour générer la porteuse ? Si c'est le cas,
c'est effectivement pas le bon outil, et là il faut effectivement faire
travailler l'électronique

Sur <http://echopen.org/index.php?title=Michaud> le DAC est sur un i2c,
bus ""infiniment lent"" (devant 84MHz), et je pense comprendre que c'est
le "bi-polar pulser" qui génère la porteuse.

Aussi, les évenements font 0.5us, sur une porteuse de 0.2us de période ?
Ça parait empêcher d'être précis (ou le but est de faire plein de
mesures pour interpoler?), et ne pas nécessiter les 14 bits de mesures
(ou alors les 14bits sont là pour rattraper les différences de
"conductances ultra-soniques" entre personnes?)

(Désolé j'amène plus de questions que de réponses)

### Elements Jérôme

Le schéma électronique présenté est le schéma d'une sonde présentée dans
un article, on s'en sert de base, ce n'est pas notre schéma final. Le
bipolar pulser génère juste un pulse pour l'émission.

Premièrement le CNA peut effectivement être moins rapide, on peut même
s'en passer car on peut simplement envoyer un pulse de quelques ns voir
ms pour exciter un transducteur. On voulait un CNA rapide pour pouvoir
tester différents types d'excitations voir si on pouvait améliorer la
qualité de notre image.

Ensuite le CAN a été choisi à 80 MHz en 14 bits pour avoir un signal
vraiment bien échantillonné avec une bonne précision de mesure pour
ensuite le post-traité informatiquement. On peut ainsi analyser
l'influence des différents paramètres pour nous permettre d'avoir une
image de qualité suffisante en diminuant la puissance de l'électronique.

On n'est pas obligé de travailler à 80 MHz en 14 bits, on peut se
limiter à du 30-40 MHz en 8 bits. Voir si on peut obtenir analogiquement
l'enveloppe du signal, on peut encore diviser par 2 la fréquence. Mais
on aura pas beaucoup de marge de manœuvre.

Je ne m'y connais pas en sous échantillonnage. Mais on n'a aucune
connaissance a priori de la réponse (mis à part que la réponse est en
gros un peigne de Dirac (dont l'amplitude des Dirac et le temps entre
chaque Dirac est inconnu) convolué par le signal émis pas le
transducteur (connu)).

Par contre, pour pouvoir échantillonner à 0.5us, il faudrait pouvoir
intégrer l'enveloppe du signal analogique sur ces 0.5us. Existe-t-il de
tels composants électronique ?

Sinon, il faut noter qu'on ne vas pas mesurer avec le CAN en continue,
on va avoir des séquences de tirs, genre toutes les 650 us. Le temps de
mesure est environ de 200us (soit 16000 points de mesure). Donc,
n'est-il pas possible d'envoyer les donnés du CAN dans un genre de
mémoire tampon qui renverrai ces données à l'arduino avec une fréquence
de 1 MHz ?

Si certaines de mes explications vous paraissent un peu flou, n'hésitez
pas à me contacter pour que je reformule.

### Alternative

Thanks to @nowami, we have been exploring the BBB solution -&gt; see
[The Case for BeagleBone
Black](The_Case_for_BeagleBone_Black "wikilink").

**Reward**
----------

-   Free featuring au projet open
-   Résidence temporaire dans nos nouveaux locaux à l'hôtel dieu

'''Ressources '''
-----------------

La page du prototype pour comprendre la vue d'ensemble
[Michaud](Michaud "wikilink")

**Repos**
---------

Elements de réponse sur le Wiki

**Captains…**
-------------

`jerome@echopen.org`

**Experts...**
--------------

-   jerome@echopen.org
-   PHH

<Category:Challenge> <Category:Arduino> <Category:Microcontroller>
<Category:Electronics>

