1.  Challenge: Signal Acquisition through Arduino

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
