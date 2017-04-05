1.  Bibliographie

Dans cette section, nous allons présenter la bibliographie que nous
avons effectué jusqu'à présent. Elle sera mise à jour au fur et à mesure
des articles pertinent que nous trouverons. Les articles seront
référencé suivant leur thématique principale (mécanique, électronique,
transducteur, traitement du signal, médicale). Un court résumé de ces
articles sera présenté, ainsi toute personne étant intéressé pourra
chercher cet article pour le lire (attention, certains articles sont
tirés de revues internationales, leur accès est payant!).

Pour les petits curieux assoiffés de connaissances, vous pouvez trouver
des articles en libre accès sur divers sujets (aussi bien en droit,
sciences sociales, physique, mathématique...) sur le site [Digital
common network](http://network.bepress.com).

Mécanique
=========

**J. M. Griffith and W. L. Henry, A sector scanner for real time
two-dimensional echocardiography, *Circulation*, 49, 6 (1974)**

Les auteurs ont fabriqué une sonde échographique sectorielle mécanique
avec un transducteur oscillant autour d'un axe. Transducteur de 12 mm de
diamètre, fonctionnant à 2,25 MHz. La cadence est de 30 images par
seconde, pour un scan de 30° avec 66 lignes de mesure. L'angle du
transducteur est déterminé par un "*rotary variable differential
transformer*".

**\#mechanical scanning, \#portable probe**

**H. H. Holm *et al.*, A new mechanical real time ultrasonic contact
scanner, *Ultrasound in medicine and biology*, 2 (1975)**

Les auteurs ont fabriqué une sonde échographique avec scanner mécanique.
Elle est composée de 4 transducteurs non-focalisés (ils n'expliquent pas
comment ils arrivent à obtenir une image avec cette méthode) fixés sur
une roue de 60 mm de diamètre. Les transducteurs font 20 mm de diamètre
et travaillent à 2 MHz. La cadence est de 16 images par seconde. L'image
est faite sur un angle de 50° composé de 69 lignes de mesure.

**\#mechanical scanning**

**R. Carotenuto, *et al.* Very Fast Scanning Probe for Ophthalmic
Echography Using an Ultrasound Motor, *IEEE Transactions on Ultrasonics,
Ferroelectrics, and Frequency Control*, 52, 11 (2004)**

Design d'une sonde échographique ophtalmique monoélément. Le
transducteur est entrainé en rotation par un moteur acoustique dont les
caractéristiques sont données dans (R. Carotenuto, A. Iula, N. Lamberti,
M. Pappalardo, “A new low voltage piezoelectric micromotor based on the
stator precessional motion,” IEEE Trans. Ultrason., Ferroelec., Freq.
Contr., vol. 45, n. 5, pp. 1427-1435, Sept. 1998.). Le transducteur et
le moteur sont synchronisés à l'aide d'un détecteur optique. Le
transducteur est centré sur 35 MHz, de diamètre 7 mm et de focal 12,1mm.
La sonde est controllée par ordinateur, le signal processing et le
système énergétique sont dans un module externe. Mesure sur 256 lignes,
pas angulaire de 0,175° (soit 44,625° de balyage), 15 images par
seconde.

**\#ultrasound motor, \#portable probe, \#mechanical scanning**

**Y. Saijo *et al.*, Development of an ultra-portable echo device
connected to USB port, *ultrasonics*, 42 (2004)**

Sonde (échocardiographe) portable branchée sur ordinateur (OS : windows)
par port USB2. La sonde est composée de deux transducteurs attachés de
chaque coté (180°) d'un rotor de 14 mm de diamètre. La sonde mesure
150x40x?\^mm$3$ pour 200 g. Fréquence de travail entre 2,5 et 7,5 MHz,
profondeur d'image de 150mm, 30 images par seconde. Le prix de la sonde
est estimé à environ 3000\$.

**\#USB, \#portbale probe, \#low-cost, \#mechanical scanner**

Electronique
============

**J. J. Hwang *et al.*, Portable ultrasound device for battlefield
trauma, *1998 IEEE Ultrasonics Symposium Proceedings*, 2 (1998)**

Sonde pour imager les tissus ou le flux sanguin, portable (&lt;2,3 kg)
marchant sur batterie ou secteur. Sonde multiélément convexe. La sonde
mesure 166,4x86,4x38,1 mm$^3$. Elle est composée de 4 circuits imprimés
dont la tâche de chacun est donnée dans le texte (p. 4).

**\#portable probe, \#electronic**

**P. Wells, Ulstrasonic imaging of the human body, *Reports on Progress
in Physics*, 62, 5 (1999)**

Un long document de revue sur les différents points des sondes
échographiques et de l'échographie en elle même. Intéressant pour la
culture générale sur l'échographie.

**\#review, \#acoustic, \#electronic, \#signal processing**

**W. D. Richard *et al.*, A low-cost B-mode usb ultrasound probe,
*ultrasonic imaging* 30 (2008)**

Sondes (trois sondes différentes) monoélément directement connectées à
l'ordinateur par port USB (2,5W). 256 lignes de mesure. Préamplificateur
de 20 dB. Détails techniques de l'électronique, très intéressant. TGC
(*Time Gain Compansation*) dans le soft, il n’est pas nécessaire du
point de vu électronique car ils ont déjà un amplificateur
logarithmique.

**\#portable probe, \#low-cost, \#electronic, \#USB**

**M. I. Fuller *et al.*, Experimental system prototype of a portable,
low-cost, C-scan ultrasound imaging device, *IEEE Transactions on
Biomedical Engineering*, 55, 2 (2008)**

Sonde échographique 2D (32\*32 transducteurs). Beamforming et traitement
du signal sont faits par un soft sur PC. Description du circuit
électronique. Test de différents beamforming (en réception).

**\#portable probe, \#3D, \#electronic, \#beamforming**

**G. K. Lewis and W. L. Olbricht, Development of a portable therapeutic
and high intensity ultrasound system for military, medical, and research
use, *The Review of scientific instruments*, 79, 11 (2008)**

Développement d'une sonde haute puissance pour traitement thérapeutique
low cost (150\$). A nécessité le développement d'un amplificateur faible
voltage, faible impédance (0,3 ohm). Batterie en module externe. Donnent
tous les détails de l'électronique.

**\#portable probe, \#high intensity, \#low-cost, \#electronic**

**W. D. Richard and D. M. Zar, Smart phone-compatibleUSB ultrasound
probe (2009)**

Sonde faible consommation d'énergie. Ils mettent leur soft dans le
domaine publique donc téléchargeable (gratuitement?).

**\#portable probe, \#low-cost, \#USB**

**J. M. Baran, Design of low-cost portable ultrasound systems,
*Proceedings of the 31st Annual International Conference of the IEEE
Engineering in Medicine and Biology Society*, (2009)**

Discussion sur les différents points techniques d'une sonde afin de
d'abaisser le prix d'une sonde à une valeur abordable. Deux entreprises
sont sur ce marché : GE Healthcare et Sonosite. Il discute donc sur les
différentes technologies (low cost) :

-des transducteurs

-de l'électronique (circuits émission et réception)

-des algorithmes de beamforming

-de la protection contre les court-circuits et pics de tension

**\#low-cost, \#review, \#electronic, \#beamforming, \#transducer**

**Z. Yu, Low-Power Receive-Electronics for a Miniature 3D Ultrasound
Probe (2012)**

Manuscrit de thèse sur la création d'une sonde portable 3D faible
puissance électrique.

**\#electronic**

Transducteur
============

[:File:2002 Design, Fabrication, and Evaluation of
High.pdf](:File:2002_Design,_Fabrication,_and_Evaluation_of_High.pdf "wikilink")

**J. M. Cannata *et al.*, Design of Efficient, Broadband Single-Element
(20–80 MHz) Ultrasonic Transducers for Medical Imaging Applications,
*IEEE Trans. Ultrason. Ferroelectr. Freq. Control*, 50, 11 (2003)**

**P. MARECHAL, [Transducteurs mono-élement pour l’imagerie ultrasonore
haute résolution : modélisation, réalisation et
caractérisation](:File:These_conception_transducteur.pdf "wikilink")
(2007)**

Manuscrit de thèse sur la conception d'un transducteur focalisé pour
implanter sur une sonde échographique.

**\#transducer**

[:File:2014 A review of piezoelectric polymers
as.pdf](:File:2014_A_review_of_piezoelectric_polymers_as.pdf "wikilink")

Traitement du signal
====================

**R. Souchon *et al.*, Ultrasonic elastography using sector scan imaging
and a radial compression, *Ultrasonics*, 40 (2002)**

Article issu d'un travail de thèse (Application de l’élastographie à
l’imagerie du cancer de la prostate et à sa thérapie par ultrasons
focalisés). Ils mesurent le module d'Young (élastographie) dans les
tissus et mettent en application des algorithmes de postraitement pour
améliorer l'image. Effectrivement les contraintes diminuent en $r^{-2}$
(normal, car en 3D les champs acoustiques varient de cette façon).

**\#elastrography, \#signal processing**

Médical
=======

**V. Steen *et al.*, Survey of Developments in Cardiac and
Cardiovascular (2000)**

Une revue sur l'évolution des techniques d'imagerie acoustique pour
l'échocardiographie.

**\#review, \#echocardiography**

**J. R. T. C. Roelandt, A personal ultrasound imager (ultrasound
stethoscope): A revolution in the physical cardiac diagnosis, *European
Heart Journal*, 23, 7 (2002)**

Sur l'utilisation d'échocardiographes (deux différents dont les
références sont donnés) portable (barrette de transducteurs + doppler,
sur batterie ou branchés).

**\#diagnosis, \#portable probe, \#medical**

**K. K. DeStigter *et al.*, Low-cost teleradiology for rural ultrasound,
*Proceedings - 2011 IEEE Global Humanitarian Technology Conference*,
(2011)**

Les auteurs font un test dans une région en voie de développement
n'ayant pas accès aux échographes. Pour pallier le problème, ils
utilisent une sonde portable connectée par satellite à des
professionnels pour transmettre les échographies afin de diagnostiquer
les problèmes prénataux.

**\#medical, \#diagnosis, \#portable probe**

**N. Cardim *et al.*, Usefulness of a new miniaturized echocardiographic
system in outpatient cardiology consultations as an extension of
physical examination, *Journal of the American Society of
Echocardiography*, 24, 2 (2011)**

Intérêt d'un stéthoscope ultrasonore combiné à un diagnostic classique
en quelques chiffres : allongement moyen d'une consultation préliminaire
de 3 minutes. Augmentation du nombre de diagnostics +75%. Diminution du
nombre de patients orientés vers le laboratoire -66% + gain inestimable
de temps pour les patients, médecins et laborantins.

**\#Portable probe, \#diagnosis, \#medical**

**L. M. Gilman and A. W. Kirkpatrick, Portable bedside ultrasound : the
visual stethoscope of the 21st century, *scandinavian journal of
trauma*, 20, 1 (2012)**

Article de revue sur le diagnostique indirecte de différents syndromes
du poumon à l'aide d'artéfacts sur les échographies.

**\#diagnosis, \#review, \#medical**

**D. Jones, Smartphone-compatible ultrasound probe, Journal of
Diagnostic Medical Sonography, 30, 4 (2014)**

Utilités, avantages d'avoir des échographes portables, intérêts des
sondes qui se branchent sur un smartphone. Présente quelques sondes
actuelles, les prix tournent environ entre 5000 et 10000£.

**\#portable probe, \#review, \#medical**

Files
-----

-   [:File:Fuller\_experimental\_low\_cost\_Cscan.pdf](:File:Fuller_experimental_low_cost_Cscan.pdf "wikilink")
-   [:File:Jone\_smartphones\_compatible\_ultasound\_probe.pdf](:File:Jone_smartphones_compatible_ultasound_probe.pdf "wikilink")
-   [:File:Memoire\_these\_Wilm.pdf](:File:Memoire_these_Wilm.pdf "wikilink")
-   [:File:Richard\_low\_cost\_probe.pdf](:File:Richard_low_cost_probe.pdf "wikilink")
-   [:File:Richard\_smartphone\_usb\_ultrasound\_probe.pdf](:File:Richard_smartphone_usb_ultrasound_probe.pdf "wikilink")
-   [:File:Baran\_Low\_Cost\_Portable\_Ultrasound.pdf](:File:Baran_Low_Cost_Portable_Ultrasound.pdf "wikilink")
-   [:File:Cannata\_Design\_of\_efficient\_broadband\_single\_element.pdf](:File:Cannata_Design_of_efficient_broadband_single_element.pdf "wikilink")
-   [:File:Carotenuto\_ophtalmic\_prob.pdf](:File:Carotenuto_ophtalmic_prob.pdf "wikilink")
