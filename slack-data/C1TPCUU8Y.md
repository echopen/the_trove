* _2016-07-21 10:16:36_> @U04DFTZ7D: <@U04DFTZ7D> has joined the channel
* _2016-07-21 10:16:37_> @U04DFTZ7D: <@U04DFTZ7D> set the channel purpose: As the community is constantly documenting its work. Ad edicated channel would be a great space to discuss documentation methods and processes.
* _2016-07-21 10:17:22_> @U1N5Q9334: <@U1N5Q9334> has joined the channel
* _2016-07-21 10:17:22_> @U0GMX7QUB: <@U0GMX7QUB> has joined the channel
* _2016-07-21 10:17:22_> @U0FN1B8KD: <@U0FN1B8KD> has joined the channel
* _2016-07-21 10:17:22_> @U07UEJC2H: <@U07UEJC2H> has joined the channel
* _2016-07-21 10:17:22_> @U0AAL4W13: <@U0AAL4W13> has joined the channel
* _2016-07-21 10:17:22_> @U0B47KC3S: <@U0B47KC3S> has joined the channel
* _2016-07-21 10:17:22_> @U0DRKLMS4: <@U0DRKLMS4> has joined the channel
* _2016-07-21 10:18:18_> @U04DFTZ7D: <@U1N5Q9334>: nous pouvons discuter de la documentation dans ce Channel dédié afin de pouvoir partager ensemble des avancées et les questions que cela pose. 
* _2016-07-21 11:50:39_> @U1N5Q9334: merci <@U04DFTZ7D>. Bonjour à tous! Pour l'instant je suis en train de travailler sur un guide qui détaille les différentes fonctions techniques à réaliser pour construire une sonde. Le premier jet (qui reprend des éléments trouvés sur le Drive et le wiki) est sur le Drive pour l'instant:  <https://docs.google.com/document/d/1JjaEAayUTHjAG_B0brFqLb6BwiHfy2bHRaP4YLBUkUU/edit#> Si vous vous avez un peu de temps pour y jeter un oeil et faire des modifications et des suggestions, n'hésitez surtout pas! Vous avez travaillé bien plus longtemps que moi sur le projet et vous pourrez corriger mes erreurs. J'ai fait les schémas sur google draw donc ils sont facilement modifiables :slightly_smiling_face:
* _2016-07-21 11:53:46_> @U1N5Q9334: La bibliographie n'est pas encore faite correctement, et il y a un problème de présentation au niveau du lien avec les solutions d'echopen. Pour régler le deuxième problème, il faudra penser à la mise en forme finale. Pour l'instant la forme choisie est un GitBook. C'est pour cela qu'en parallèle, nous travaillons sur la documentation des avancées d'echOpen sur Github, dans le dossier medicotechnical que <@U0GMX7QUB> a créé suite à une de vos précédentes discussions:  <https://github.com/echopen/medicotechnical/tree/master/>
* _2016-07-21 12:03:56_> @U1N5Q9334: par exemple, ce serait une bonne idée que chaque personne qui travaille sur un module technique mette le résumé de son carnet de labo sur github une fois qu'il a fini son module. Avec Benoit nous avons convenu de cette mise en forme, qui reprend celle suggérée sur le Drive:  <https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage_cockroft/readme.md>
* _2016-07-21 12:04:33_> @U04DFTZ7D: Merci <@U1N5Q9334> c'est parfait. Le format est donc un format markdown (Github markdown) et à restitution du guide devrait sans doute pouvoir de faire sur gitbook via fichier source su Github 
* _2016-07-21 12:07:59_> @U04DFTZ7D: Merci. On peut aussi penser à ajouter les liens des carnets de labo directement dans la fiche. Ensuite, que signifie Hand mande ? J'imagine que cela signifie "fait à la main" mais je ne vois pas bien l'idée de préciser cela ? A moins que quelque chose ne m'ai échappé ? 
* _2016-07-21 12:14:42_> @U1N5Q9334: <@U1N5Q9334> and commented: voilà un petit résumé des différents dossiers se trouvant dans medicotechnical  :wink:
* _2016-07-21 12:22:11_> @U1N5Q9334: "hand made" faisait opposition à "integrated circuit" qui sont aussi répertoriés dans "modules". Si j'ai bien compris Jérôme, l'idée de ce dossier est de regrouper toutes les tentatives qui ont été faites pour réaliser un module, fait-maison ou non, par exemple <https://github.com/Alienor134/medicotechnical/tree/master/modules/MDL-alimentation_high_voltage_recom> qui est en circuit intégré. La mise au propre se fait dans le dossier "doc", dans des readme.md générés automatiquement par des programmes python.  Ces programmes python se promèneront dans "modules", "fonctions", "interfaces", etc (d'où l'importance de la mise en forme des documents)
* _2016-07-21 12:22:39_> @U1N5Q9334: Merci pour l'idée des liens vers les carnets de bord!
* _2016-07-21 12:24:44_> @U1N5Q9334: j'ai une question parce que j'ai du mal à retrouver ces informations: est-ce que c'est important de mettre une date précise, et comment voyez-vous une bonne manière de nommer les versions?
* _2016-07-21 12:32:00_> @U04DFTZ7D: Bonne question.... Qu'en pensez-vous <@U0GMX7QUB> et <@U0AAL4W13> ? Je pense qu'une date serait bien, mais en effet, si script automatique, il faut définir un format. 
* _2016-07-21 17:56:52_> @U04DFTZ7D: <!channel>: Nous avions évoqué faire un petit workshop entre nous sur la documentation. Quand seriez-vous disponible pour ça ?  
* _2016-07-21 19:21:14_> @U0AAL4W13: Le format est plus ou moins établi i guess, mais il est vrai qu'il n'est pas strictement documenté. 
* _2016-07-21 19:22:58_> @U0AAL4W13: Après les vacances de Bivi i guess 
* _2016-07-21 19:23:36_> @U0AAL4W13: <@U1N5Q9334>: n'hésite pas non plus à voir comment le makedoc marche :)
* _2016-07-21 19:23:56_> @U0AAL4W13: (dans <http://github.com/kelu124/echomods>) 
* _2016-07-21 19:24:42_> @U0AAL4W13: Pour les versions,  tu n'as pas à te galerer, github te gère ça 
* _2016-07-21 20:17:29_> @U04DFTZ7D: <@U0AAL4W13>: oui, visiblement le format est plus ou moins établi. Mais l'idée est de de rédiger le guide ou les Process de documentation pour que nous puissions les diffuser aux contributeurs et surtout nous assurer que tous aient bien compris le fonctionnement pour pouvoir documenter progressivement. 
* _2016-07-21 20:19:07_> @U0AAL4W13: wep
* _2016-07-21 20:19:54_> @U0AAL4W13: je viens de faire un pull request pour les modules tobo (pulser) et goblin (TGC, enveloppe, ADC) sur medicotech
* _2016-07-21 20:20:38_> @U0AAL4W13: les deux readme et structures de fichier sont des references de structure
* _2016-07-21 20:20:53_> @U0AAL4W13: qui sont compatibles de base avec la structure des readme
* _2016-07-21 20:21:19_> @U0AAL4W13: le contenu de leur readme peut etre vidé pour en faire des templates :smiley:
* _2016-07-21 20:22:58_> @U04DFTZ7D: Ok, cool. Ensuite, il faudra que nous mettions en place les Process dont vous avez parlé de vérification et d'acceptation des merge 
* _2016-07-21 20:30:06_> @U0AAL4W13: c'est dans les issues du repo en effet
* _2016-07-21 20:31:42_> @U0AAL4W13: et ca devrait être une question dans l'ensemble des repos
* _2016-07-21 20:32:23_> @U0AAL4W13: :smiley:
* _2016-07-21 20:32:25_> @U04DFTZ7D: Oui, jusqu'à qu'on fixe une procédure 
* _2016-07-21 20:32:55_> @U04DFTZ7D: D'ailleurs, il faut aussi régler la question de la licence qui est absente du répo medicotech créée !!
* _2016-07-21 20:33:26_> @U0AAL4W13: en fait dans chaque module il y a une license deja (normalement), ca fait partie de la structure du readme
* _2016-07-21 20:33:45_> @U0AAL4W13: ensuite, a voir si une globale est pertinente puisque ca melange texte, hardware, software, ...
* _2016-07-21 20:33:58_> @U0AAL4W13: (sans compter les CR d'evenements etc)
* _2016-07-21 20:35:08_> @U04DFTZ7D: C'est dangereux d'avoir dès lice,ces différentes par module car on va perdre des contributeurs. Je suis un peu surpris puisque que nous avions fixé une licence tous ensemble il y a déjà pas mal de temps... 
* _2016-07-21 20:35:55_> @U0AAL4W13: pourquoi perdre des contributeurs?
* _2016-07-21 20:36:10_> @U0AAL4W13: La license qu'on a fixé est incomplète, on en avait également parlé par avant
* _2016-07-21 20:36:35_> @U04DFTZ7D: Le soft est plutôt sous licence open, le hard libre et les contenus sous CC BY SA
* _2016-07-21 20:36:37_> @U0AAL4W13: c'est pour ca que les licenses soft ne sont pas la license echopen
* _2016-07-21 20:36:46_> @U0AAL4W13: donc des licenses différentes
* _2016-07-21 20:37:02_> @U04DFTZ7D: En quoi elle est incomplète ?
* _2016-07-21 20:37:25_> @U0AAL4W13: "Finally, the open probe is complying to all european standards for medical devices. If you are strongly encouraged to check on your local standards to comply with it. "
* _2016-07-21 20:37:35_> @U0AAL4W13: "ANY CHANGE WITHIN THE DEFAULT SETTINGS MAY CAUSE HARM TO THE PATIENT ON WHICH THE PROBE IS USED ON. PLEASE CHECK WITH A SPECIALIST BEFORE ANY CHANGE. "
* _2016-07-21 20:37:36_> @U04DFTZ7D: Oui entre soft et hard ce&amp; a toujours été différent 
* _2016-07-21 20:38:11_> @U0AAL4W13: = non relevant pour la version non médicale
* _2016-07-21 20:38:28_> @U04DFTZ7D: Ok, à discuter lors de la prochaine réunion 
* _2016-07-21 20:39:25_> @U0AAL4W13: vu que les modules sont a la fois de la doc, du code, et des CR, on ne peut qu'avoir des licenses différentes
* _2016-07-21 20:39:28_> @U0AAL4W13: (anyhow)
* _2016-07-21 20:39:51_> @U0AAL4W13: d'autre part, je ne vois pas pourquoi un module sous license TAPR perdrait des contributeurs?
* _2016-07-21 20:48:20_> @U0AAL4W13: (du moment que la license est une license du libre)
* _2016-07-21 21:01:12_> @U0AAL4W13: anyhow
* _2016-07-21 21:01:29_> @U0AAL4W13: ce sera bien si le travail effectué peut s'aligner sur les standards déjà posés
* _2016-07-21 21:02:57_> @U0AAL4W13: <@U1N5Q9334>: pour le module recom, je vois que tu as utilisé globalement la meme structure, c'est top
* _2016-07-21 21:03:13_> @U0AAL4W13: ca permettrait de s'interfacer easily avec la production des graphes :smiley:
* _2016-07-21 23:47:38_> @U0FN1B8KD: <@U04DFTZ7D>: handmade ou homemade?
* _2016-07-21 23:50:30_> @U0FN1B8KD: pour la date on pourait mettre la date du release de la version correspondante? ou sinon juste mois/année.
* _2016-07-21 23:52:43_> @U04DFTZ7D: <@U0FN1B8KD>: sur la doc (accessible via le lien plus haut) il est écrit hand made d'où ma question. Mais visiblement la réponse d' <@U1N5Q9334> est que c'est fait à la main et non des circuits intégrés 
* _2016-07-21 23:55:41_> @U04DFTZ7D: <@U0AAL4W13>: il faut juste vérifier les compatibilités des licences hardware entre elles... Et la, seul un juriste pourrait nous répondre car de mon côté j'en sais rien. <@U0AAL4W13>, du coup je te laisse regarder ça ? Enfin je ne saisie pas le point sur les standards déjà posés ? De quels standards parles tu ?
* _2016-07-22 00:16:29_> @U0FN1B8KD: Justement il faut qu'on réfléchisse à un terme : je trouvai "made in echopen" ou homemade pas mal
* _2016-07-22 00:17:40_> @U0FN1B8KD: <@U1N5Q9334>: j'ai commenté et ajouté des modifications aux 12 premières pages j'espère que ça ira. En tout cas c'est vraiment génial ton travail ! :slightly_smiling_face:
* _2016-07-22 00:17:56_> @U0FN1B8KD: je continue plus tard :wink:
* _2016-07-22 08:19:38_> @U04DFTZ7D: Oui, je suis d'accord, "Echopen made" me plait bien
* _2016-07-22 09:41:51_> @U0GMX7QUB: <@U1N5Q9334>, <@U04DFTZ7D>, un petit retour d'expérience sur le nommage des versions. A ma connaissance il y a au moins 4 manières de nommer une version : - La classique *Vxx.yy.zz* : dans le principe c'est très bien, ça fournit des informations sur les évolutions, les corrections de bug, les compatibilités,... Dans les faits, il faut une gestion de projet super carré pour l'utiliser à bon escient et on finit souvent avec du 0.1, 0.2, 0.3 un peu au pif. Surtout avec une structure de développement décentralisée comme la notre. - Le n° de *build* : à chaque build, on  incrémente un n° et de tps en tps on sélectionne un build pour en faire une release. C'est automatique mais il y a des trous dans les n° et ils ne sont pas très porteurs de sens. - L'incrémentale simple *Vn*, *Vn+1* ... Ce n'est pas un hasard si Firefox, Chrome, ... l'on adopté, c'est bien adapté au cycles de dvp courts et ça fournit l'essentiel des infos nécessaires (sachant que le reste est fournit pas Git et la gestion de conf) : la place d'une release dans la liste chronologique de toutes les releases. L'équipe projet à quand même en charge la gestion centralisée de l'incrément de n° de version. - La date de release *Vaa.mm.jj*. C'est ce qu'utilise Ubuntu par exemple. C'est, à mes yeux, encore plus simple, consensuel, décentralisé (on vit tous dans le même espace temps) permet d'avoir naturellement une notion de fraicheur d'une release et aussi d'inscrire tous les projets/modules dans une même chronologie. Encore une fois, à condition que ce soit appuyé sur une solide gestion de conf (versionning, issues, dépendances, compatibilité). Sauf si on est contraints par des outils (gestionnaire de paquets pas ex) ou des méthodes adoptées, c'est ma solution préférée, simple et amplement suffisante la plupart du temps.
* _2016-07-22 09:50:11_> @U0AAL4W13: <@U04DFTZ7D>: standards: format utilisé so far dans la structure des dépôts + structure des readme 
* _2016-07-22 09:50:50_> @U0AAL4W13: <@U04DFTZ7D>: pour les licenses, jpense que tapr est un peu aligné avec la license echopen (elle s'en inspire un peu)
* _2016-07-22 09:51:30_> @U0AAL4W13: Avoir une license "classique" permet de gagner en simplicité pour les users, qui s'y reconnaîtront plus facilement qu'une license inconnue.
* _2016-07-22 09:51:49_> @U04DFTZ7D: Du coup, si je comprends bien tu dis qu'il faut utiliser les formats de doc établis ? Si c'est ça, on est complètement aligné. Ce sont les structures des informations permettant ensuite de faire la publication automatique ? 
* _2016-07-22 09:52:33_> @U0AAL4W13: Yup
* _2016-07-22 09:53:16_> @U0AAL4W13: Soumis à une incrementation si on a des besoins qui ne se transcrivent pas dans ce format 
* _2016-07-22 09:53:35_> @U0AAL4W13: Mais pas besoin de surcharger le Template si on veut du Kiss :)
* _2016-07-22 09:59:15_> @U0AAL4W13: <@U0FN1B8KD>: <@U1N5Q9334>: question bête..  Les modules ne sont pas tout circuit intégrés (ic) / composants discrets -- surtout que bitmaker vous confirmera que les ic peuvent être de base (off the shelf)
* _2016-07-22 09:59:27_> @U0AAL4W13: Un ao par exemple est un ic
* _2016-07-22 10:00:04_> @U0AAL4W13: Du coup, comment appeler homemade /made in /... Sur les circuits batards ?
* _2016-07-22 10:00:33_> @U0AAL4W13: Pour moi, tous les circuits sont réalisés par nous, donc homemade :)
* _2016-07-22 10:00:42_> @U04DFTZ7D: Pour les licences, nous avions acté tous ensemble l'utilisation de la licence rédigé pour Echopen, adapté au projet par un juriste. Sur le principe d'utiliser des licences existantes, je partage ce point de vue, mais il semble qu'aucune licence ne soit vraiment adapté au projet. Sauf qu'au dire d'un juriste vue avant hier, la GLP V3 pourrait maintenant convenir étant donné ses évolutions. Bref, la question qui se pose à nous est que toutes les contributions ont été faites sous licence Echopen pour le hardware (sauf Murgen) et que le mélange de plusieurs licences peut éventuellement créer des conflits entre deux modules hardware sous licence différentes. C'est précisément ce point qu'il faut lever, et ce de manière certaine. Ensuite, d'autres nous ont conseillé la licence CERN, là aussi avec ses avantages et ses inconvénients. Donc si nous voulons assurer la pérennité du projet, il me semble qu'une seule et unique licence hardware devrait être sélectionnée et que seules les contributions qui acceptent la licence choisie soient prises en compte.   D'où mon point de mettre cette question à ordre du jour d'une prochaine réunion. Nous pouvons encore changer la licence hardware, mais cela impliquera une acceptation de tous les contributeurs. Donc si nous devons faire cela, nous devons le faire rapidement. 
* _2016-07-22 10:01:55_> @U0AAL4W13:  Non, on a eu des retours de juristes comme quoi utiliser une license homemade était une faiblesse 
* _2016-07-22 10:02:38_> @U04DFTZ7D: Oui et d'autres qui ont dit le contraire. D'où l'idée d'en discuter pour trancher une bonne fois pour toute
* _2016-07-22 10:02:40_> @U0AAL4W13: Ensuite, la license echopen est, comme souligne avant, non adaptée à du matos non medicak
* _2016-07-22 10:02:56_> @U0AAL4W13: Faire un Capjuriste :)
* _2016-07-22 10:03:37_> @U0AAL4W13: Ça serait top
* _2016-07-22 10:03:43_> @U0AAL4W13: Et ça me rassurerait 
* _2016-07-22 10:03:46_> @U0AAL4W13: :)
* _2016-07-22 10:04:33_> @U04DFTZ7D: Ça n'est pas la question.... La question est de savoir si deux bouts de hardware sous licence différentes sont compatibles ou non =&gt; Là, comme déjà mentionné plus haut, je n'en sais rien, donc demander à quelqu'un qui pourrait avoir la réponse. Oui, on peut faire un workshop dédié, je te laisse l'organiser ? 
* _2016-07-22 10:05:49_> @U0AAL4W13: Si ça ne presse pas, pk pas 
* _2016-07-22 10:06:20_> @U0AAL4W13: Ma priorité est de sortir le kit maker avant la rentrée, mais pk pas après, quand j'aurai enfin du temps :)
* _2016-07-22 10:07:32_> @U0AAL4W13: Je veux bien que tu me passes les coordonnées des gens que tu connais sur la question :)
* _2016-07-22 10:08:00_> @U0FN1B8KD: Mehdi était chaud pour faire un capjuriste aussi, ya aussi la question du droit d'exploitation   En ce qui concerne le "Made in Echopen" c'est pour distinguer un circuit/composant acheté (ce qui était le cas de la plupart des composants de Emile ) par rapport à un composant fait "from scratch", à partir de briques très élémentaires par ex transducteur ENS/constant
* _2016-07-22 10:08:41_> @U04DFTZ7D: Du coup, ça presse un peu, car un kit Maker dont la question de la licence n'est pas claire risque de voir ce kit ne pas pouvoir se développer correctement... Pour le moment, ils sont en vacances !! 
* _2016-07-22 10:08:58_> @U04DFTZ7D: Mais avant de voir qui contacter, il faut rédiger un document de référence, un déroulé, etc. 
* _2016-07-22 10:09:17_> @U0FN1B8KD: Odj de la prochaine réu?
* _2016-07-22 10:09:22_> @U0AAL4W13: Yup
* _2016-07-22 10:09:32_> @U0AAL4W13: Serai pas là par contre :/
* _2016-07-22 10:10:28_> @U0AAL4W13:  Je ne vois pas en quoi mettre sous une license librexempêcherait des developpements futurs, puisque justement ce serait en libre :)
* _2016-07-22 10:10:41_> @U0AAL4W13: Mais à trancher avec des spécialistes oui
* _2016-07-22 10:18:28_> @U0AAL4W13: (pour rappel, les notes sur l'apero licenses libres sont sur <http://echopen.org/index.php/Ap%C3%A9ro_Licences_Ouvertes_avec_Benjamin_Jean>) 
* _2016-07-22 10:21:29_> @U0AAL4W13: Sans aller jusqu'à l'event complet, avoir qqun comme benjamin jean le lundi de la réunion pourrait être bien pour profiter de son avis
* _2016-07-22 14:43:04_> @U1N5Q9334: Merci beaucoup  <@U0FN1B8KD> pour la relecture! c'est tout pris en compte, surtout l'idée du glossaire
* _2016-07-22 14:45:28_> @U1N5Q9334: <@U0GMX7QUB>:  va pour la version V.aa.mm.jj alors :slightly_smiling_face: avec comme convention jj=00 si on ne connait pas la date exacte par exemple?
* _2016-07-22 14:48:19_> @U1N5Q9334: <@U0AAL4W13> si j'ai bien compris on cale tout sur ta mise en forme à présent? Pour le code je l'ai lu mais je ne suis pas sûre de pouvoir y toucher beaucoup avant mon départ mercredi...
* _2016-07-22 16:55:32_> @U0GMX7QUB: <@U1N5Q9334>: _jj=00_ : oui, pas mal. Pour la version, faut aussi voir si d'autres personnes n'ont pas un avis contraire. T'es sure que tu veux partir en vacances mercredi ? Ce serait plus simple si tu restais encore quelques mois :smiling_imp:.
* _2016-07-22 20:13:12_> @U0B47KC3S: grosse annonce de stackoverflow <!channel> (reactions: @U04DFTZ7D)
* _2016-07-22 20:13:22_> @U0B47KC3S: <https://stackoverflow.com/tour/documentation> <!channel>
* _2016-08-25 09:38:55_> @U0B47KC3S: <@U0AAL4W13> je suis en train de reprendre les challenges, les mettre au format markdown de gitbook, et de traduire ceux que j’ai postés. J’ai cleané le challenge data format. Il y a un morceau qui est en français /data format/challenge/Need to make it compatible with DICOM/Commentaires la trad. Qd tu as du temps tu peux faire un tour de trad ?
* _2016-08-25 09:39:04_> @U0B47KC3S: <https://echopen.gitbooks.io/android-app/content/data_format.html>
* _2016-08-25 22:16:41_> @U0B47KC3S: <@U0AAL4W13> je viens de voir ton post. par souci d’homogénéisation, tu peux porter le gitbook dans le compte echOpen ?
* _2016-08-26 13:13:14_> @U0AAL4W13: j'y reponds sous basecamp :smiley:
* _2016-10-10 09:18:41_> @U04DFTZ7D: <@U04DFTZ7D> has renamed the channel from "documentation" to "prj_commty_is"
* _2016-10-10 09:19:33_> @U04DFTZ7D: <@U04DFTZ7D> set the channel purpose: As the community is constantly documenting its work. A dedicated channel would be a great space to discuss documentation methods and processes. This is the Information System of echOpen.
* _2016-10-10 09:48:04_> @U2M9XDS5N: <@U2M9XDS5N> has joined the channel
* _2016-10-12 13:17:15_> @U2NAWHM9N: <@U2NAWHM9N> has joined the channel
* _2016-10-16 19:37:07_> @U2PTWF6SX: <@U2PTWF6SX> has joined the channel
* _2016-11-07 19:20:12_> @U0B47KC3S: <@U0B47KC3S> set the channel topic: dedicated to discuss documentation methods and processes. This is the Information System of echOpen.
* _2016-11-08 12:39:04_> @U04DFTZ7D: the gitbook starterkit is now in english !! it remains a few bugs, but we will correct it soon. Then, we will improve the content by adding some new info : <https://www.gitbook.com/book/echopen/starterkit/details>
* _2016-11-12 20:39:55_> @U32FZ0QLX: <@U32FZ0QLX> has joined the channel
* _2016-11-13 18:59:17_> @U31UCUFPW: <@U31UCUFPW> has joined the channel
* _2016-11-13 18:59:17_> @U3210MXC5: <@U3210MXC5> has joined the channel
* _2016-11-14 11:26:13_> @U0B47KC3S: <@U04DFTZ7D> do <@U0GMX7QUB> have an echOpen email ? if not how can we repair this affront;)
* _2016-11-14 11:27:04_> @U0B47KC3S: btw, <@U04DFTZ7D> does this channel adresses the question of valorization of contribution ?
* _2016-11-14 11:28:20_> @U04DFTZ7D: No, the channel to discuss about contributors is channel <#C2MBFSQ1L>
* _2016-11-15 02:06:29_> @U1NTT0ZPH: <@U1NTT0ZPH> has joined the channel
* _2016-11-15 02:06:29_> @U1NLWV4BZ: <@U1NLWV4BZ> has joined the channel
* _2016-11-15 02:06:29_> @U1NM17NHF: <@U1NM17NHF> has joined the channel
* _2016-11-16 09:38:23_> @U32AR6TED: <@U32AR6TED> has joined the channel
* _2016-11-16 15:55:09_> @U32UWGGN9: <@U32UWGGN9> has joined the channel
* _2016-11-16 16:11:44_> @U34231VFH: <@U34231VFH> has joined the channel
* _2016-11-18 22:22:32_> @U34N7NQNR: <@U34N7NQNR> has joined the channel
* _2016-11-19 09:36:52_> @U33817K25: <@U33817K25> has joined the channel
* _2016-11-23 17:50:03_> @U35LGETA4: <@U35LGETA4> has joined the channel
* _2016-11-24 21:45:02_> @U36QEPF51: <@U36QEPF51> has joined the channel
* _2016-11-25 11:17:43_> @U04DFTZ7D: <@U04DFTZ7D> has renamed the channel from "prj_commty_is" to "root_echopen"
* _2017-01-14 11:05:45_> @U3RKUJHHS: <@U3RKUJHHS> has joined the channel
