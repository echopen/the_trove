1.  Design & Code Camp

Le **16 mai 2015 de 10.00 à 19.00 à La Paillasse** - 226, rue
Saint-Denis 75002 Paris, France L'évènement est ouvert à tous.

Le programme
============

  --------------------------------------- -------------------------------------------------------------- ----------------------------------------------------------------------------------------------
  **Qu'allons-nous faire ?**              **De qui avons-nous besoin ?**                                 **Quels seront les livrables ?**

  -   Echanger et passer un bon moment    -   De vous tous pour offrir votre regard                      -   Les premières lignes de codes sur GitHub
  -   Imaginer l'application              -   De médecins pour nous dire comment on utilise une sonde    -   Un parcours utilisateurs identifié avec des schémas, des MockUps et les fonctionnalités.
  -   Coder les premières lignes          -   De développeurs pour poser les premières briques de code   -   Des histoires utilisateurs via des cas d'utilisations
  -   Designer l'experience utilisateur   -   De designers pour imaginer l'experience utilisateur        
                                          -   De graphistes pour rendre-compte de l'experience           
                                          -   D'érgonomes pour imaginer une app simple                   
                                          -   D'ingénieurs pour nous orienter                            
                                          -   Des gens logiques pour nous dire si c'est clair            
                                                                                                         
  --------------------------------------- -------------------------------------------------------------- ----------------------------------------------------------------------------------------------

On compte sur vous tous pour mobiliser, relayer le message, et venir
nombreux pour qu'ensemble, nous puissions obtenir un prototype
fonctionnel d'écho-stéthoscope pour le bicentenaire de l'invention du
stéthoscope.

### Le déroulé

-   10.00 - 10.30 Accueil des participants
-   10.30 - 11.00 Présentation de la journée, des ateliers et des
    livrables
-   11.00 Lancement
-   17.00 Mise en commun des résultats
-   18.00 Echanges
-   19.00 Fin du camp

Compte-rendu
============

Présentation
------------

10.00 - 10.30 : Présentation des enjeux et des grands principes
d'echopen

-   -   Intro de Mehdi: Contexte général
    -   Intro de Pierre Bourrier : enjeux de santé - double conception
        du projet intéressante: aspect technique + éducation

![ 256px](IMG_0784.jpg  " 256px")

-   10.30 - 10.45 : Tour de table : quels intérêts autour de la table ?
    -   Transitions sociales
    -   Démocratisation de la médecine
    -   Nouvelles problématiques ethiques
    -   Question des collectes de données
    -   Ingénieur et chercheur / Orienté communauté
    -   chaine de valeur
    -   Relations praticien patient -- comme avec le stethoscope
    -   Comment les praticiens vont se servir de l'objet?
    -   Transmission
    -   Vocabulaire sur la science ouverte =)
    -   Creer des ponts avec des étudiants
-   10.45 - 11.00 : Echanges sur les questions techniques
    -   Quelles sont les fonctionnalités dont on a vraiment besoin ?
    -   Qui sont les utilisateurs ?

Brainstorm commun
-----------------

### Utilisateurs et utilisations

Echange entre les participants pour identifier les utilisateurs et les
utilisations et définir quelques cas spécifiques d'usage

![ 256px](IMG_0785.jpg  " 256px")

  --------------------------- -----------------------------
  Profils d’utilisateurs      Zones d’utilisation

  -   Médecins généralistes   -   Milieu hospitalier
  -   Médecins spécialistes   -   Médecine de ville
  -   Urgentistes             -   Médecine de campagne
  -   Pompiers                -   Zones sous-médicalisées
  -   Samu                    -   Dispensaires
  -   Matrones                -   Pays en développement
  -   Infirmier-e-s           
                              
  --------------------------- -----------------------------

### La formation à l'utilisation de la sonde

pour les médecins, non radiologues, ne doit pas prendre plus de deux
jours.

-   Simplifier la sonde au maximum
-   Simplifier les fonctionnalité pour que le médecin n'ait pas à
    réfléchir aux réglages dont il a besoin
-   La courbe d'apprentissage d'utilisation doit être très rapide =&gt;
    J'ai besoin, j'allume et j'ai ma réponse
-   Le réglage de la profondeur doit être automatisé au maximum

### Cas typique d'utilisation

-   Les douleurs abdominales chez les enfants
-   En pédiatrie

ex. Un enfant arrive aux urgences, l'enfant semble avoir mal au ventre/
:   La question

    :   Est-ce une colique
    :   Une peritonite
    :   Autre

=&gt; Besoin d'un outils d'aide au diagnostic.

### Les sondes existantes

Découverte des échographes ultra-portables et des UI/UX

![ 256px](IMG_0788.jpg  "fig: 256px") ![
256px](IMG_0789.jpg  "fig: 256px")

### Principe de l'analyse et de la lecture de l'image

Plusieurs options peuvent être envisagées :

-   Une application mobile pour être utilisée sur mobile
-   Une série de Rasperry PI avec un écran.
-   Autre

Workshop en équipes
===================

Groupe A
--------

Contributeurs : Olivier M., Nicolas L., Yannick, Betty, Bertrand.

### Spécifications

Éléments
:   Condition : l'app doit tourner sur une interface tactile.
:   Les gestes doivent prolonger les questions du mécedins.
:   Pas de commande vocale (car certaines infos n'ont pas vocation à
    être partagées frontalement avec le patient dans la phase
    de diagnostic).
:   L'application doit être facile à manier avec le pouce.
:   C'est "l'anti-main" qui va gérer le smartphone.
:   Perspective : flasher le code-barre du patient.
:   Enjeu : archiver les endroits échographiés.

<!-- -->

Specifications :
:   Bouton 'SAVE' pour enregistrer les images.
:   Régler le gain avec les boutons sur le côté.
:   Infos à rentrer : nom / code barre / 'settings'.

### Ecrans

-   Écran 1 : flasher le code-barre du patient
    -   Nom / Prénom
    -   Date naissance
    -   Sexe

=&gt; Données importées depuis le logiciel de l'hopital.

-   Écran 2 : vérifier si les données sont correctes.
-   Écran 3 : que puis-je faire pour vous (vocal / voir)
-   Ecran 4 : 'vous serez double-checké" (par un pair)
    -   Sur les enjeux de validation P2P, voir par exemple.

=&gt; Olivier va nous connecter avec l'un des membres.

-   Ecran 5 : diagnostic (i.e. prendre une image)

&gt; Quel est l'examen que vous souhaitez faire ?
=================================================

&gt; On peut se baser sur une banque d'images (ex).

Groupe B
--------

Contributeurs : Medhi, Pierre, Christophe, Sylvia

Obserrvations préliminaires :
:   Les étapes du protocole
:   Questions préliminaires : selon un des médecins, les questions
    préliminaires sont indispensables en amont de l'examen par
    l'utilisation de l'outil. Il s'agit de faire interface entre un
    raisonnement et un outil.
:   Préréglages (par le biais de pictogrammes)
:   Rappel : L'Echostétoscopie est un complément à l'examen clinique. En
    aucun cas un examen approfondi à l'image de l'échographie.

<!-- -->

Expérience utilisateur
:   Il faut penser l'expérience utilisateur dans son ensemble, prendre
    en compte la disponibilité des mains du médecins.
:   Pour cela, nous imaginons un certain nombre de solutions :
:   Contrôles directement sur l'outil
:   Les paramètres préformatés permettre de reformater l'image au touch,
    sans revenir à linterface de réglage.

<!-- -->

Formation, expérience et acquisition
:   En terme de niveau d'apprentissage du médecin, besoin de réflexivité
    (être en mesure de différencier si le problème de lecture provient
    d'une incompétence du médecin ou d'un problème de réglage). La
    formation de 48h consiste en un accompagnement sur des études
    de cas.
:   L'écriture par le médecin via l'interface participe au processus
    même de réflexion

=&gt; Quelles sont les infos importantes pour arriver au préréglage,
quelles modalités d'affichage ?

Modalités d'affichage
:   Menu déroulant, pictogramme...
:   Avantage des pictogrammes :

    :   intuitif
    :   permet l'usage de l'application à l'échelle internationale (pas
        de traduction nécessaire)

:   Boutons d'optimisation.

<!-- -->

Outils complémentaires constituant des reperts normés, au delà de l’intuition du médecin
:   mesure (dimension)
:   mesure de volume
:   Procédure : enregistrer l’image et mesurer

<!-- -->

3 modes d’affichage
:   video en direct
:   affichage d’une image enregistrée
:   Mode simplifié et mode avancé (pouvant être préréglé par le médecin)

    :   Tir TM (voir le mouvement d'une structure dans le temps)
    :   modification de la ligne de tir (par itération) &gt; bouton
        complémentaire

<!-- -->

Qualité de l’image :
:   courbe de gris optimisé (égalisation du gain sur la profondeur)

<!-- -->

Transmission
:   Bouton de transmission, permettant deux niveau d'utilisation :
:   via wifi vers un ordinateur, un téléphone (screenshoots)
:   vers un cloud sécurisé (pour les hospitaux spécialisés) (implique
    des choix d'architecture)

<!-- -->

Différents types de profils
:   Flow selon le contexte d'utilisation

### Synthèse des fonctionnalités

Pendant l'aquisition d'une image, de combien de fonctionnalités supplémentaires a-t-on besoin ?
:   préréglage : Mode simplifié et mode avancé (pouvant être préréglé
    par le médecin)
:   1 bouton d'optimisation qui réactualise l'image (ou un tap)
:   gain total (réglage de la luminosité de l'écran, du blanc au noir,
    selon le contexte)
:   Zoom
:   Tir TM (discussion sur l'occupation de l'espace de l'écran : TM sans
    le voir)
:   Transmission (très peu de post-processing)

<!-- -->

Exemple de navigation dans l'interface :
:   homme/ femme
:   adulte : enfant
:   morphologie
:   examen et lancement des préréglages pour l'examen choisi

Les workshops en images
-----------------------

![ 256 px](11101102_10206844389937352_1225481050_n.jpg  "fig: 256 px")
![ 256 px](11117676_10206844389657345_900924702_n.jpg  "fig: 256 px") ![
256 px](11245329_10206844389577343_690770528_n.jpg  "fig: 256 px") ![
256 px](11272755_10206844389537342_554418889_n.jpg  "fig: 256 px") ![
256 px](11280487_10206844390017354_1614890489_n.jpg  "fig: 256 px") ![
256 px](11287236_10206844389617344_1764693605_n.jpg  "fig: 256 px") ![
256 px](11291821_10206844389977353_218216424_n.jpg  "fig: 256 px")

MockUps
=======

Drafts des Mockups
------------------

<File:echopen_1.jpg> <File:echopen_2.jpg> <File:echopen_3.jpg>
<File:echopen_4.jpg> <File:echopen_5.jpg> <File:echopen_6.jpg>
<File:echopen_7.jpg> <File:echopen_8.jpg> <File:echopen_9.jpg>
<File:echopen_10.jpg> <File:echopen_11.jpg>

Synthèse des dratfs de mockups
------------------------------

![ 256 px](Capture d’écran 2015-05-16 à 20.27.49.png  "fig: 256 px") ![
256 px](Capture d’écran 2015-05-16 à 20.27.38.png  "fig: 256 px") ![ 256
px](Capture d’écran 2015-05-16 à 20.27.20.png  "fig: 256 px") ![ 256
px](Capture d’écran 2015-05-16 à 20.27.09.png  "fig: 256 px")

MockUps finalisés
-----------------

### Série \#1

![ 256px](A.jpg  "fig: 256px")![ 256px](b.jpg  "fig: 256px")![
256px](C.jpg  "fig: 256px")![ 256px](D.jpg  "fig: 256px")

### Série \#2

![ 256px](echopen_MockUp_1.png  "fig: 256px") ![
256px](echopen_MockUp_1.2.png  "fig: 256px") ![
256px](echopen_MockUp_1_2.png  "fig: 256px")

<Category:Communication>
