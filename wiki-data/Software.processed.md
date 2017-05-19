

# Old probes mechanisms

Challenge
---------

Hi there community!

Here's an interesting challenge for you guys : wouldn't it be
interesting to have a standard format for all files being created with
the echOpen kits - those being images, on the one hand, and raw signals
on the other hand?

The project already acquires some data on which one can work - being
images or data - it would then be awesome to capitalize on this and
allow those who want to do some signal processing to work on a couple of
files that can be given to data processing specialists.

The objective is to set a format that

-   allows consistency in time,
-   captures all relevant information about the data since the very
    first images,
-   allows the use of consistent tools to work on these data
-   allows a proper tagging for images.

The format could include for exemple, raw data (signal enveloppe or raw
data), and meta information/headers, such as:

# probe timestamping
2.  size of expected image
3.  ID of the transducer
4.  the sampling unit (mm between two pixels, ns between two points, ..)
5.  the kit version
6.  the embedded firmware version
7.  ID of the board/kit/release
8.  geometry parameters / parameters to be taken in by the scan
    conversion
9.  the settings of the app (username, config (ie which setting is used,
    what organ is being looked at, ...)

and so on..

Initial proposal
----------------

''Salut la communauté,

Petite question à ouvrir: est ce que ca ne vaudrait pas le coup de
standardiser le format des fichiers pour ce qui est des images d'une
part, les signaux bruts de l'autre? On commence à acquerir des données
sur lesquelles on peut déjà travailler, ce serait top de capitaliser là
dessus, et ca permettrait à ceux qui veulent faire du traitement de
l'image d'avoir une base sur laquelle travailler pour traiter les
ressources/fichiers qu'on peut mettre à disposition.

L'idée est d'avoir un format qui soit consistant dans le temps pour
qu'on puisse développer des outils qui n'aient pas besoin d'évoluer à
chaque fois, et d'avoir des données tagguées proprement, de manière à
voir les évolutions qu'on pourra avoir en fonction des kits et releases,
et d'avoir ces données propres.

Il y aurait d'un côté des headers, de l'autre les données en tant que
telles.

Dans le header, on pourrait avoir:

# la date/heure de l'image
2.  la taille de l'image qui sera attendue
3.  le serial du transducteur utilisé
4.  la fréquence du transducteur
5.  le pas entre deux points
6.  la version du kit
7.  la version du firmware embarqué
8.  le serial de la board/kit/release
9.  les parametres à passer dans le scan conversion if any (à lister)
10. les parametres de l'app (ex: organe en train d'etre imagé, user,
    timestamp côté app, ...)
11. ... j'en passe et des meilleures.

Ca permettrait d'avoir une continuité des données dans le temps, malgré
les évolutions qu'on pourrait avoir - un interêt certain. ''

<Category:Challenge> <Category:Data> <Category:Software>



# V0.0 Sprint log - Getting an image

Log
===

Disclaimer
----------

Quick and dirty

Tuesday 22nd
------------

After a WiFi problem, we shifted the Pitaya to the main room with the
oscillo to do the tests. We ...

-   went shopping, despite rain and fleet, and discovered
    [HackSpark](http://hackspark.fr);
-   built a housing for the probe: motor and collector were reused, from
    the elements of the [IR1510AK](IR1510AK "wikilink") probe;
-   reviewed the booster, according to an article
    ([Thadani](Thesis:_Thadani,_MIT,_1997 "wikilink") et al);
-   refactored an old probe piezzo ([S-VRW77AK](S-VRW77AK "wikilink"));
-   synced the RedPitaya acquisition to an external trigger
    (the arduino).

Wednesday 23rd
--------------

-   Problems with existing collectors -&gt; enhancement of existing
    mechanics, research of new sliprings
-   Red pitaya : connection issues with the livebox
-   RP : issues with the Channels - different inputs/outputs
-   Red pitaya: description of the webapp at [Red Pitaya
    WebApp](Red_Pitaya_WebApp "wikilink")
-   Test of the new transducers: beginnings of the circuit by NAL at 63V
    to test
-   Arduino Workshop @Langevinium
-   RP: getting new apps to work on the code

Thursday 24th
-------------

-   Creating Red and Yellow from the older probe to get a testing unit
-   Testing with the booster circuit : [First Pulses (Sept.
    2015)](First_Pulses_(Sept._2015) "wikilink")

Friday 25th
-----------

-   Testing the probes with the pulser circuit
-   Waterproofing Red and Yellow

Sunday 27th
-----------

-   Sweeping servomotor on the [BBB](BBB "wikilink") // [BBB Servomotor
    wiring](BBB_Servomotor_wiring "wikilink")
-   Some websites to get inspiration:
    -   <http://www.biosono.com/ElctLgd/ElctLgd.php?id=ED_TC>
        Transceiver
    -   <http://www.biosono.com/ElctLgd/ElctLgd.php?id=ED_UP> Pulser
    -   <http://echopen.org/index.php?title=File:Thesis_Insoo_Kim.pdf>

Monday 28th
-----------

-   Testing the good quality transducer -&gt; issues with the physical
    stability
-   Improvising an aquarium with a soup bowl
-   Playind with Red and Blue to get the [First Echoes (Sept.
    2015)](First_Echoes_(Sept._2015) "wikilink")
-   Documenting the RedPitaya issues [The case for Red
    Pitaya](The_case_for_Red_Pitaya "wikilink")
-   Code to wire the servo on the arduino ([Arduino Servomotor
    Wiring](Arduino_Servomotor_Wiring "wikilink")) and to
    synchronise pulses.

Tuesday 29th
------------

-   Going into the dark hole of Clipping circuits

Wednesday 30th
--------------

-   Meeting partners at Issy les Moulineaux
-   Trying ecretage / clipping filters -- at [Clipping
    Test](Clipping_Test "wikilink")
-   Using circuitlab to test some circuits (see above)

Thursday 1st
------------

-   Finalizing the Michaud structure
-   Trying other clipping filters - [Clipping
    test](Clipping_test "wikilink") or on CircuitLab
-   News from some additional transducer suppliers
-   Processing tool on the Pitaya webapp interface

Friday 2nd
----------

-   Apéro on the impact social
-   Meeting with N.L. for information centralisation
-   Mehdi off to BXL, ULB
-   Thinking about UDP communication (with its limitations)

Sunday 4th
----------

-   Closing the [UDP
    Tool](https://github.com/kelu124/rechOpen/tree/master/UDP%20Tool),
    pushing to github
    -   For code, see below

Remaining ToDo
==============

High priority
-------------

-   Synchro RP (JED 23.09)
-   Montage protection double diode (NAL, 22.09)
-   Circuit d'amplification (NAL, 22.09)
-   Chassis + axe de rotation (JED/CAG, 01.10)
-   Moteur Ard. RP (NAL, CAG, LJO, 25.09)
-   Interface 2D (CAG,LJO, 25.09)
-   Documentation (All, ongoing)
-   Test of new, "repaired" transducers -- Out of ampli from NAL.

Second level of priority
------------------------

-   List of equipment for V0 V0.1
-   Bills of materials (
-   Arduino training @Langevinium

Documentation
=============

-   Get a poster out of the prototype
-   Get a short article

Soft so far
===========

### Files

All is there : [repo
github](https://github.com/kelu124/rechOpen/tree/master/UDP%20Tool)

### How to use

-   UDP\_receive.py has to run before executing the server - it listens
    on the right UDP port and dumps the packets, decoded, into the
    corresponding log file in data/
    -   For example, 20151004-185450\_UDP-DATA.log stores a packet
        per line. Each 16k points line in the raw data was squared,
        clipped, averaged over 16 points samples, resulting in a 1024
        points echo line.
    -   Each 1024 points line was splitted over 256 points packets, plus
        the 7 first ints bearing additional information (right now, the
        critical data are the position of the packet in the line, in
        Col1, the line number, in Col5, and the position of the servo
        in Col4)
    -   So 1024 points are splitted over 4 packets of size (256+7)
        (sizeof(int), so the total is around 1098 bytes.
-   To obtain these lines, one must compile the src/CreateImage16s.c
    using the ./run.sh tool included in the SDK.
    -   After launching, it should print the status of data transfer
    -   One should see the progress in parallel displayed by
        UDP\_receive.py
-   LogParser.py takes a log file and creates the corresponding PNG file
    -   Beware, appropriate libraries should be included, like Image

### Disclaimer

After a couple of issues with the Red Pitaya web app, we have tried to
set up a UDP server on the Pitaya.

The first trials were done with **/srcTestServer.c** -- but we were
still quite buggy, especially in terms of memory management, which
proved quite tricky for a C n00b like me.

Moreover, I think that the UDP data rate, at least with the Pitaya, are
note quite compatible with the data rate in terms of raw images. The
time being, I rather focused on delivering an image.

### Some pics

<https://raw.githubusercontent.com/kelu124/rechOpen/master/UDP%20Tool/data/fantom.png>

-   [Links
    here](https://github.com/kelu124/rechOpen/blob/master/UDP%20Tool/data/fantom.png)

<!-- -->

-   [A big fat
    interface](https://github.com/kelu124/rechOpen/blob/master/UDP%20Tool/data/20151004-190413_UDP-DATA.log.png)
-   [A phantom
    ?](https://github.com/kelu124/rechOpen/blob/master/UDP%20Tool/data/20151004-185810_UDP-DATA.log.png)

Structure
---------

The setup consists in :

-   a server, ie CreateImage16s.c (which sends averages of 16s).
    -   I removed the triggerdelay from the RP to avoid loosing to much
        time waiting for a second pulse for the PMW -- I'm just taking
        what I need to know where the motor is.
    -   Using the SDK, an executable in /tmp/api\_test will appear on
        the RP. It can be safely executed from there.
    -   Over the 16k samples, it takes the sums of the squares
-   It packs at the moment 256 samples, on 4 bytes int, plus 7 int
    bearing information (motor, date, time elapsed, ...) on each packet.
-   UDP client, in Python.
    -   It unpacks the data coming through the UDP and processes the
        packet "header"
    -   It stores the packets in a .log file, which can be used to
        replay the capture
-   A LogParser, which interprets a log file, repacks the different
    parts of a same line, sorts the lines according to their positions
    as encoded on the single int left, an shoots a png that represents
    the capture

So far, I canceled working on the createref.py tool, to remove the
baseline from all the signals

HowTo // Protocole
------------------

-   Starting python UDP\_receiver.py
-   Launching the acquisition through CreateImage16s
-   Shutting down UDPReceiver
-   Unpacking the corresponding log using the Parser.py
-   Admiring the newly formed PNG image

TODO
----

-   Sending RawData (sampled at 125MHZ) through UDP.
-   Having the Pitaya broadcast its messages, instead of streaming them
    to the main computer (INANYADDR)
-   Having a pitaya emulator replay the log files in a local C
    UDP server.
-   Artificial TCG in the LogParser\*
-   Forgetting, it's getting late.

Bibliography
============

-   Un pour l'argent, deux pour le spectacle, et trois pour le caillou:
    <https://www.youtube.com/watch?v=9jK-NcRmVcw>
-   A bit of (ultra)sound:
    <http://8tracks.com/meowmers/it-s-in-the-way-you-love>

<Category:Software> <Category:Transducer> <Category:Transmitting>
<Category:Receiving> <Category:Emile>



# Trophée des ingénieurs de demain - édition 2015

Challenge
---------

Hi there community!

Here's an interesting challenge for you guys : wouldn't it be
interesting to have a standard format for all files being created with
the echOpen kits - those being images, on the one hand, and raw signals
on the other hand?

The project already acquires some data on which one can work - being
images or data - it would then be awesome to capitalize on this and
allow those who want to do some signal processing to work on a couple of
files that can be given to data processing specialists.

The objective is to set a format that

-   allows consistency in time,
-   captures all relevant information about the data since the very
    first images,
-   allows the use of consistent tools to work on these data
-   allows a proper tagging for images.

The format could include for exemple, raw data (signal enveloppe or raw
data), and meta information/headers, such as:

# probe timestamping
2.  size of expected image
3.  ID of the transducer
4.  the sampling unit (mm between two pixels, ns between two points, ..)
5.  the kit version
6.  the embedded firmware version
7.  ID of the board/kit/release
8.  geometry parameters / parameters to be taken in by the scan
    conversion
9.  the settings of the app (username, config (ie which setting is used,
    what organ is being looked at, ...)

and so on..

Initial proposal
----------------

''Salut la communauté,

Petite question à ouvrir: est ce que ca ne vaudrait pas le coup de
standardiser le format des fichiers pour ce qui est des images d'une
part, les signaux bruts de l'autre? On commence à acquerir des données
sur lesquelles on peut déjà travailler, ce serait top de capitaliser là
dessus, et ca permettrait à ceux qui veulent faire du traitement de
l'image d'avoir une base sur laquelle travailler pour traiter les
ressources/fichiers qu'on peut mettre à disposition.

L'idée est d'avoir un format qui soit consistant dans le temps pour
qu'on puisse développer des outils qui n'aient pas besoin d'évoluer à
chaque fois, et d'avoir des données tagguées proprement, de manière à
voir les évolutions qu'on pourra avoir en fonction des kits et releases,
et d'avoir ces données propres.

Il y aurait d'un côté des headers, de l'autre les données en tant que
telles.

Dans le header, on pourrait avoir:

# la date/heure de l'image
2.  la taille de l'image qui sera attendue
3.  le serial du transducteur utilisé
4.  la fréquence du transducteur
5.  le pas entre deux points
6.  la version du kit
7.  la version du firmware embarqué
8.  le serial de la board/kit/release
9.  les parametres à passer dans le scan conversion if any (à lister)
10. les parametres de l'app (ex: organe en train d'etre imagé, user,
    timestamp côté app, ...)
11. ... j'en passe et des meilleures.

Ca permettrait d'avoir une continuité des données dans le temps, malgré
les évolutions qu'on pourrait avoir - un interêt certain. ''

<Category:Challenge> <Category:Data> <Category:Software>



# Challenge: Data format

Challenge
---------

Hi there community!

Here's an interesting challenge for you guys : wouldn't it be
interesting to have a standard format for all files being created with
the echOpen kits - those being images, on the one hand, and raw signals
on the other hand?

The project already acquires some data on which one can work - being
images or data - it would then be awesome to capitalize on this and
allow those who want to do some signal processing to work on a couple of
files that can be given to data processing specialists.

The objective is to set a format that

-   allows consistency in time,
-   captures all relevant information about the data since the very
    first images,
-   allows the use of consistent tools to work on these data
-   allows a proper tagging for images.

The format could include for exemple, raw data (signal enveloppe or raw
data), and meta information/headers, such as:

# probe timestamping
2.  size of expected image
3.  ID of the transducer
4.  the sampling unit (mm between two pixels, ns between two points, ..)
5.  the kit version
6.  the embedded firmware version
7.  ID of the board/kit/release
8.  geometry parameters / parameters to be taken in by the scan
    conversion
9.  the settings of the app (username, config (ie which setting is used,
    what organ is being looked at, ...)

and so on..

Initial proposal
----------------

''Salut la communauté,

Petite question à ouvrir: est ce que ca ne vaudrait pas le coup de
standardiser le format des fichiers pour ce qui est des images d'une
part, les signaux bruts de l'autre? On commence à acquerir des données
sur lesquelles on peut déjà travailler, ce serait top de capitaliser là
dessus, et ca permettrait à ceux qui veulent faire du traitement de
l'image d'avoir une base sur laquelle travailler pour traiter les
ressources/fichiers qu'on peut mettre à disposition.

L'idée est d'avoir un format qui soit consistant dans le temps pour
qu'on puisse développer des outils qui n'aient pas besoin d'évoluer à
chaque fois, et d'avoir des données tagguées proprement, de manière à
voir les évolutions qu'on pourra avoir en fonction des kits et releases,
et d'avoir ces données propres.

Il y aurait d'un côté des headers, de l'autre les données en tant que
telles.

Dans le header, on pourrait avoir:

# la date/heure de l'image
2.  la taille de l'image qui sera attendue
3.  le serial du transducteur utilisé
4.  la fréquence du transducteur
5.  le pas entre deux points
6.  la version du kit
7.  la version du firmware embarqué
8.  le serial de la board/kit/release
9.  les parametres à passer dans le scan conversion if any (à lister)
10. les parametres de l'app (ex: organe en train d'etre imagé, user,
    timestamp côté app, ...)
11. ... j'en passe et des meilleures.

Ca permettrait d'avoir une continuité des données dans le temps, malgré
les évolutions qu'on pourrait avoir - un interêt certain. ''

<Category:Challenge> <Category:Data> <Category:Software>



# Become a member

Challenge
---------

Hi there community!

Here's an interesting challenge for you guys : wouldn't it be
interesting to have a standard format for all files being created with
the echOpen kits - those being images, on the one hand, and raw signals
on the other hand?

The project already acquires some data on which one can work - being
images or data - it would then be awesome to capitalize on this and
allow those who want to do some signal processing to work on a couple of
files that can be given to data processing specialists.

The objective is to set a format that

-   allows consistency in time,
-   captures all relevant information about the data since the very
    first images,
-   allows the use of consistent tools to work on these data
-   allows a proper tagging for images.

The format could include for exemple, raw data (signal enveloppe or raw
data), and meta information/headers, such as:

# probe timestamping
2.  size of expected image
3.  ID of the transducer
4.  the sampling unit (mm between two pixels, ns between two points, ..)
5.  the kit version
6.  the embedded firmware version
7.  ID of the board/kit/release
8.  geometry parameters / parameters to be taken in by the scan
    conversion
9.  the settings of the app (username, config (ie which setting is used,
    what organ is being looked at, ...)

and so on..

Initial proposal
----------------

''Salut la communauté,

Petite question à ouvrir: est ce que ca ne vaudrait pas le coup de
standardiser le format des fichiers pour ce qui est des images d'une
part, les signaux bruts de l'autre? On commence à acquerir des données
sur lesquelles on peut déjà travailler, ce serait top de capitaliser là
dessus, et ca permettrait à ceux qui veulent faire du traitement de
l'image d'avoir une base sur laquelle travailler pour traiter les
ressources/fichiers qu'on peut mettre à disposition.

L'idée est d'avoir un format qui soit consistant dans le temps pour
qu'on puisse développer des outils qui n'aient pas besoin d'évoluer à
chaque fois, et d'avoir des données tagguées proprement, de manière à
voir les évolutions qu'on pourra avoir en fonction des kits et releases,
et d'avoir ces données propres.

Il y aurait d'un côté des headers, de l'autre les données en tant que
telles.

Dans le header, on pourrait avoir:

# la date/heure de l'image
2.  la taille de l'image qui sera attendue
3.  le serial du transducteur utilisé
4.  la fréquence du transducteur
5.  le pas entre deux points
6.  la version du kit
7.  la version du firmware embarqué
8.  le serial de la board/kit/release
9.  les parametres à passer dans le scan conversion if any (à lister)
10. les parametres de l'app (ex: organe en train d'etre imagé, user,
    timestamp côté app, ...)
11. ... j'en passe et des meilleures.

Ca permettrait d'avoir une continuité des données dans le temps, malgré
les évolutions qu'on pourrait avoir - un interêt certain. ''

<Category:Challenge> <Category:Data> <Category:Software>



# Talk:Challenge filtrage signal

Challenge
---------

Hi there community!

Here's an interesting challenge for you guys : wouldn't it be
interesting to have a standard format for all files being created with
the echOpen kits - those being images, on the one hand, and raw signals
on the other hand?

The project already acquires some data on which one can work - being
images or data - it would then be awesome to capitalize on this and
allow those who want to do some signal processing to work on a couple of
files that can be given to data processing specialists.

The objective is to set a format that

-   allows consistency in time,
-   captures all relevant information about the data since the very
    first images,
-   allows the use of consistent tools to work on these data
-   allows a proper tagging for images.

The format could include for exemple, raw data (signal enveloppe or raw
data), and meta information/headers, such as:

# probe timestamping
2.  size of expected image
3.  ID of the transducer
4.  the sampling unit (mm between two pixels, ns between two points, ..)
5.  the kit version
6.  the embedded firmware version
7.  ID of the board/kit/release
8.  geometry parameters / parameters to be taken in by the scan
    conversion
9.  the settings of the app (username, config (ie which setting is used,
    what organ is being looked at, ...)

and so on..

Initial proposal
----------------

''Salut la communauté,

Petite question à ouvrir: est ce que ca ne vaudrait pas le coup de
standardiser le format des fichiers pour ce qui est des images d'une
part, les signaux bruts de l'autre? On commence à acquerir des données
sur lesquelles on peut déjà travailler, ce serait top de capitaliser là
dessus, et ca permettrait à ceux qui veulent faire du traitement de
l'image d'avoir une base sur laquelle travailler pour traiter les
ressources/fichiers qu'on peut mettre à disposition.

L'idée est d'avoir un format qui soit consistant dans le temps pour
qu'on puisse développer des outils qui n'aient pas besoin d'évoluer à
chaque fois, et d'avoir des données tagguées proprement, de manière à
voir les évolutions qu'on pourra avoir en fonction des kits et releases,
et d'avoir ces données propres.

Il y aurait d'un côté des headers, de l'autre les données en tant que
telles.

Dans le header, on pourrait avoir:

# la date/heure de l'image
2.  la taille de l'image qui sera attendue
3.  le serial du transducteur utilisé
4.  la fréquence du transducteur
5.  le pas entre deux points
6.  la version du kit
7.  la version du firmware embarqué
8.  le serial de la board/kit/release
9.  les parametres à passer dans le scan conversion if any (à lister)
10. les parametres de l'app (ex: organe en train d'etre imagé, user,
    timestamp côté app, ...)
11. ... j'en passe et des meilleures.

Ca permettrait d'avoir une continuité des données dans le temps, malgré
les évolutions qu'on pourrait avoir - un interêt certain. ''

<Category:Challenge> <Category:Data> <Category:Software>

