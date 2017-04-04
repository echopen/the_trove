1.  Michaud

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
