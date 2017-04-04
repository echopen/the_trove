1.  Talk:Challenge filtrage signal

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

1.  probe timestamping
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

1.  la date/heure de l'image
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
