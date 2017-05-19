* _2016-04-03 10:35:23_> @U04DFTZ7D: <@U04DFTZ7D> has joined the channel
* _2016-04-03 10:35:23_> @U0AAL4W13: <@U0AAL4W13> has joined the channel
* _2016-04-03 10:35:23_> @U04DFTZ7D: <@U04DFTZ7D> set the channel purpose: Face aux multiples discussions au sein de la communauté et afin de les centraliser, je vous propose ce fil de chat pour échanger sur les questions de documentation. Il s’agit d’un enjeu majeur à la fois technique et communautaire.
* _2016-04-03 10:35:23_> @U0GMX7QUB: <@U0GMX7QUB> has joined the channel
* _2016-04-03 10:35:23_> @U0FN1B8KD: <@U0FN1B8KD> has joined the channel
* _2016-04-03 10:35:23_> @U0DRKLMS4: <@U0DRKLMS4> has joined the channel
* _2016-04-03 10:35:23_> @U0KPE2P16: <@U0KPE2P16> has joined the channel
* _2016-04-03 10:35:23_> @U0JFW4XTQ: <@U0JFW4XTQ> has joined the channel
* _2016-04-03 10:35:23_> @U0SHK0X1D: <@U0SHK0X1D> has joined the channel
* _2016-04-03 10:35:24_> @U0B47KC3S: <@U0B47KC3S> has joined the channel
* _2016-04-03 11:01:04_> @U04DFTZ7D: Le dossier du drive avec les documents de réflexion : <https://drive.google.com/folderview?id=0B-aFHCvM6eTeUno3LXBmemxKc0k&amp;usp=sharing>
* _2016-04-03 12:59:32_> @U0AAL4W13: Pour permettre de tester ce modèle sur une documentation complète, hésitez pas à commenter sur le github de Murgen - qu'est ce quimarche, qu'est ce qui ne marche pas.
* _2016-04-03 13:00:19_> @U0AAL4W13: :)
* _2016-04-03 13:00:37_> @U0FN1B8KD: et je remet le lien de luc ici : <http://semver.org/>
* _2016-04-03 13:00:58_> @U0AAL4W13: D'autre part (j'écrirai dans le doc aussi) - une doc n'est pas qu'une liste de composant. 
* _2016-04-03 13:01:37_> @U0AAL4W13: La doc commence au cahier des charges (qui détaillé ce qu'on veut faire) et qui donne du contexte 
* _2016-04-03 13:02:02_> @U0AAL4W13: Cf le doc d'amanda wozniak qui est excellent sur la doc.
* _2016-04-03 13:02:35_> @U0AAL4W13: (et qui m'a servi de référence pour documenter) 
* _2016-04-03 14:03:51_> @U04DFTZ7D: <@U0AAL4W13>, de quel modèle parles tu ?
* _2016-04-03 14:04:45_> @U04DFTZ7D: En effet, une doc n’est pas une liste de composants. Mais si j’ai bien compris la liste des composants reste indispensable car sans la BOM, je ne vois pas comment les contributeurs peuvent avancer ?
* _2016-04-03 14:05:13_> @U04DFTZ7D: <@U04DFTZ7D> et qui reste une bonne base de travail.
* _2016-04-03 14:08:16_> @U04DFTZ7D: Voilà la liste des éléments à inclure dans les fiches modules pour la partie elec &amp; such :   - GERBERS - NC Drill File - Assembly Drawing - Pick &amp; Place Coordinates - BOM - Part ID - Reference Designator(s) - Part Type - Package Footprint - Value/Description/Critical Spec  Manufacturer’s Part Number - Vendor’s Part Number
* _2016-04-03 15:14:50_> @U0AAL4W13: en fait justement le reste, tout à -fait le complémentaire de cette partie -&gt; plutôt ce qu'il y a avant
* _2016-04-03 15:15:34_> @U0AAL4W13: Mais au delà, le explique qu'il faut contextualiser le design, qu'il y a des séries de questions auxquelles répondre 
* _2016-04-03 15:15:45_> @U0AAL4W13: En gros résumer le cahier des charges en amont 
* _2016-04-03 15:16:18_> @U0AAL4W13: Car répondre à une question qui n'est pas posée n'apporte pas autant que de répondre à un cahier des charges explicité 
* _2016-04-03 15:16:57_> @U0AAL4W13: Et encore, cette liste y'a pas besoin de tout :) 
* _2016-04-03 15:20:23_> @U0AAL4W13: THIS ISTHESTORIED ENGINEERINGPROCESSLATHER. RINSE. REPEAT.T
* _2016-04-03 15:22:42_> @U0AAL4W13: La page 18 de la présentation est manquante dans cette méthodo de documentation
* _2016-04-03 15:24:21_> @U0AAL4W13: :stuck_out_tongue: 
* _2016-04-03 15:37:39_> @U0AAL4W13: Pour ta liste, <@U04DFTZ7D>, ces fichiers sont sensés être produits automatiquement à partir de la source des fichiers que bitmaker doit nous délivrer. 
* _2016-04-03 15:40:33_> @U0AAL4W13: C'est géré automatiquement dans un repo comme <https://github.com/kelu124/murgen-dev-kit/tree/master/Gerbers> ou tu as toute l'information, déjà standardisée. Par ex, tu envoies ces fichiers à un Fab et il te sort ton hardware. Pas besoin d'écrire ça dans un fichier à lire par un utilisateur lambda 
* _2016-04-03 15:42:10_> @U0AAL4W13: A fortiori, ça n'a pas de sens de mettre ces données sur une carte faite à la mano (pas de pick and place, pas de drill,...) 
* _2016-04-03 16:42:16_> @U04DFTZ7D: Ok, merci. Du coup, est-ce que tu peux ajouter ces éléments sur le Gdoc pour que nous puissions avoir une synthèse complète de ce qui est nécéssaire dans la documentation ? Notamment :   - Les éléments du cahier des charges explicité en amont dont tu parles  - La série de questions dont tu parles  - Les éléments inutiles de la liste que tu évoques   Enfin, je comprends que les fichiers sources réalisés (j’imagine dans un logiciel de DAO ou quelque chose comme ça) doivent générer automatiquement un certain nombre de trucs que nous n’avons pas besoin de documenter en plus. Je comprends alors que ça n’a pas de sens (je rappelle ici, que je n’y connais rien). Du coup, quelle serait la liste précise des éléments qu’il faut documenter ?
* _2016-04-14 09:27:21_> @U04DFTZ7D: <@U04DFTZ7D> has renamed the channel from "documentation" to "4_norm_regulation"
* _2016-06-07 15:01:22_> @U1EP1RDGE: <@U1EP1RDGE> has joined the channel
* _2016-06-07 15:49:02_> @U1EP1RDGE: Battery must be IEC 62133
* _2016-06-07 15:49:21_> @U04DFTZ7D: Thanks ;)
* _2016-10-10 11:22:20_> @U04DFTZ7D: <@U04DFTZ7D> has renamed the channel from "4_norm_regulation" to "prj_regul_norms"
* _2016-11-07 19:29:58_> @U0B47KC3S: <@U0B47KC3S> set the channel topic: dedicated to norms and certifications issues
* _2016-11-07 19:30:02_> @U0B47KC3S: <@U0B47KC3S> set the channel purpose: dedicated to norms and certifications issues
* _2016-11-15 02:08:21_> @U1NM17NHF: <@U1NM17NHF> has joined the channel
* _2016-11-15 02:08:21_> @U1NLWV4BZ: <@U1NLWV4BZ> has joined the channel
* _2016-11-15 02:08:21_> @U1NTT0ZPH: <@U1NTT0ZPH> has joined the channel
* _2016-11-30 09:53:41_> @U38JDLY2E: <@U38JDLY2E> has joined the channel
* _2016-12-08 22:03:08_> @U3CDR25JP: <@U3CDR25JP> has joined the channel
* _2016-12-21 15:09:51_> @U3HH0CEAW: <@U3HH0CEAW> has joined the channel
* _2017-01-05 15:56:26_> @U3ML4L01Z: <@U3ML4L01Z> has joined the channel
* _2017-01-05 23:07:56_> @U3N1SENJY: <@U3N1SENJY> has joined the channel
* _2017-01-09 11:53:12_> @U3NT8G2BC: <@U3NT8G2BC> has joined the channel
* _2017-01-16 19:56:48_> @U0AAL4W13: A wealth of info: FDA ... -- cf <https://www.accessdata.fda.gov/cdrh_docs/pdf14/K143493.pdf> : "Signostics   Ltd  believes  the  SignosRT Bladder  described  in  this  Submission   is   substantially  equivalent  to the predicate devices as follows:  a. Portascan Bladder  Scanner (K033906)  b. SignosRT  Ultrasound  System  (K130659)  etc..." (edit: going into english, sorry guys!)
* _2017-01-16 19:58:15_> @U0AAL4W13: other critical inputs such as .. "3MHz, 8Fps or 16Fps (Imaging only), 128 lines for 90º frame at 10cm, Materials: Sab ic Cy co lo y  HC1204HF,  Mits u i TPX-MED18, Sab ic Vers o llen  OMX1255NX-1, ..."
* _2017-01-16 19:59:07_> @U0AAL4W13: May be worth investigating and making a compilation of what's available :wink:
* _2017-01-16 20:20:09_> @U0AAL4W13: ping <@U38HVMZ6K>
* _2017-01-16 20:20:13_> @U38HVMZ6K: <@U38HVMZ6K> has joined the channel
* _2017-01-16 20:55:02_> @U0AAL4W13: Same for the Clarius probe : <http://www.accessdata.fda.gov/cdrh_docs/pdf16/K163138.pdf> (interesting remark -- The device is not intended for use in Emergency Medical Service, ambulance, or aircraft environments )
* _2017-01-16 20:57:19_> @U38HVMZ6K: Emergency services, ambulances and aircrafts are often special cases where you do not want to go if not forced to...
* _2017-01-16 20:57:53_> @U38HVMZ6K: The regulatory and certification burdens are higher.
* _2017-01-16 20:58:51_> @U38HVMZ6K: A common approach is to go without these, let the device in the field for some time and submit a second 510(k) with these additional environments.
* _2017-01-16 21:00:25_> @U38HVMZ6K: Thus you are more quickly on the market, have time to complete your documentation and finally release a "new" version of the product which is compatible with emergency setups :wink: 
* _2017-01-16 21:01:39_> @U38HVMZ6K: The same happen often with pediatric use of devices. Often release early without pediatric intended uses and covering these cases later.
* _2017-01-16 21:03:14_> @U0AAL4W13: :)
* _2017-01-16 21:50:20_> @U0AAL4W13: BTW, did a small exercice: mapping all the FDA requests that lead to the Clarius approval : <https://github.com/kelu124/echomods/tree/master/include/fda.gov>
* _2017-01-16 22:19:00_> @U38HVMZ6K: Nice! Small typo in the caption of the graphique 501(k) --&gt; 510(k)
* _2017-01-16 22:19:59_> @U0AAL4W13: thx
* _2017-01-16 22:22:38_> @U0AAL4W13: corrigé :smiley:
* _2017-01-17 15:45:11_> @U3T7KBEMV: <@U3T7KBEMV> has joined the channel
* _2017-01-17 20:34:46_> @U0AAL4W13: <@U38HVMZ6K> -- I updated the graph, added the name of the devices for a bit more readibility :smiley: (reactions: @U38HVMZ6K)
* _2017-01-19 20:17:51_> @U3TUWV3SQ: <@U3TUWV3SQ> has joined the channel
* _2017-01-21 19:48:37_> @U0FN1B8KD: 
* _2017-01-26 17:16:30_> @U3WRNP30B: <@U3WRNP30B> has joined the channel
* _2017-01-27 09:20:29_> @U38HVMZ6K: <@U38HVMZ6K> and commented: Very interesting white paper on regulatory and compliance for medical mobile apps.
* _2017-01-27 09:21:49_> @U38HVMZ6K: Came across this white paper and found it to be very useful for echOpen. Gives detailed insights, recommendations,... on regulatory, compliance and certification processes for medical mobile apps in US and EU.
* _2017-01-27 10:53:35_> @U0B47KC3S: over cool <@U38HVMZ6K> ping <@U352MKG4V> <@U32V2JWFJ>
* _2017-01-27 10:53:36_> @U0B47KC3S: cc <@U04DFTZ7D> <@U0JFW4XTQ> -&gt; we should make a point on that
* _2017-01-27 10:55:24_> @U38HVMZ6K: thanks <@U0B47KC3S> I am gladly "in" for any discussion related to regulatory, compliance, ... applied to software
* _2017-01-27 10:56:51_> @U38HVMZ6K: I have some experience from my job on FDA processes and we try to be IEC62304 compliant in our processes to let the door open for EU certification
* _2017-01-27 10:56:51_> @U0B47KC3S: yep !
* _2017-01-27 10:57:41_> @U38HVMZ6K: I'll try to establish a list of norms/guidances useful and/or mandatory for the mobile app
* _2017-01-27 10:58:28_> @U38HVMZ6K: everything is "easier" with US norms and guidances since they are all publicly available for free
* _2017-01-27 10:59:26_> @U38HVMZ6K: standards used in EU (IEC62304 among others) are only accessible with a fee :disappointed: (reactions: @U0B47KC3S)
* _2017-01-30 11:54:35_> @U3Y2FPGBV: <@U3Y2FPGBV> has joined the channel
* _2017-01-30 16:49:01_> @U3XHSAQHE: <@U3XHSAQHE> has joined the channel
* _2017-02-01 22:26:55_> @U0FN1B8KD: Hi the norms channel ! Will may be soon be conducting a clinical trial in Lao and Peru! When do you think we will be able to be certified ? "Primum non nocere"
* _2017-02-01 22:35:29_> @U38HVMZ6K: &gt; When do you think we will be certified? Ouch... Difficult question! There are many many questions and obstacles in the path!
* _2017-02-01 22:37:05_> @U38HVMZ6K: First we need a working prototype. We have a first starter-kit but still nothing similar to a real industrializable medical device.
* _2017-02-01 22:46:14_> @U38HVMZ6K: Then, the echOpen probe will not be certified in itself (as far as I understood) but the design will be taken over by an OEM/manufacturer which will have to create a complete set of documentation, test protocols, design documents,... This is a HUGE task! To get an idea about the kind and amount of documentation required for a medical device development and certification have a look at <http://blog.greenlight.guru/design-controls> which is a good reference with descriptions for both FDA in the US and CE in Europe.
* _2017-02-01 22:49:03_> @U38HVMZ6K: Rough personal estimation: happy path with sustained development effort, early involvement of a manufacturer bringing man power in the project/product: 2 years before certification
* _2017-02-01 22:49:35_> @U38HVMZ6K: Realistic estimation: 4-5 years (reactions: @U0AAL4W13)
* _2017-02-01 22:51:47_> @U38HVMZ6K: Other members may have different views but this is what I expect given my experience, current status of the project and my understanding of the work still to be done.
* _2017-02-01 23:02:10_> @U0FN1B8KD: wouaw... no certification=  no clinical trial?
* _2017-02-01 23:07:02_> @U38HVMZ6K: As an example, the now well-known Clarius portable ultrasound device (<http://www.clarius.me>) (reactions: @U0AAL4W13)
* _2017-02-01 23:08:58_> @U38HVMZ6K: No, to my knowledge, clinical trials are possible without certification but I don't know to which extent.
* _2017-02-01 23:10:37_> @U38HVMZ6K: Certification is the open-door to be able to *market* the device but AFAIK it is possible to perform clinical trials before.
* _2017-02-02 08:36:33_> @U0AAL4W13: <@U38HVMZ6K> I concur with the 4-5 years on a realistic scale, though with more resources, coordination, and a well defined (meaning with proper advisors) this could be lowered. 2 years all included seem really optimistic, but with a good support, indeed clarius showed it was feasible.
* _2017-02-02 08:37:50_> @U38HVMZ6K: yep sure... it was best and realistic paths. I don't speak about worst case...
* _2017-02-02 08:37:54_> @U0AAL4W13: but for these 2 year target, a strong full time team needs to be here, and I assume with the proper connections (we saw one of their engineers was far from being a noob and we'll connected)
* _2017-02-02 08:38:30_> @U0AAL4W13: plus, I do think that clarius already had something in their pockets before they even started as a company
* _2017-02-02 08:41:35_> @U38HVMZ6K: exactly... 2 years with a complete full-time team with experience in the medical device industry and ultrasound, 6.5M$ funding,...
* _2017-02-02 08:43:16_> @U0AAL4W13: there are two shortcuts I believe : the cheapest is working with shenzen, which will be moderately cheap, fast, but you won't get easy certification 
* _2017-02-02 08:43:42_> @U38HVMZ6K: &gt; we saw one of their engineers was far from being a noob "<https://www.clarius.me/brief-history-clarius/> &gt; I have spent my career in Ultrasound. 17 years ago I designed the first PC-based ultrasound research system and founded Ultrasonix. We became the leaders in ultrasound research interfaces, then expanded into point of care with programmable, software-based machines."
* _2017-02-02 08:44:59_> @U0AAL4W13: the second is hiring a company who designs probes for a living, pay them to deliver the design + proto
* _2017-02-02 08:44:59_> @U0AAL4W13: they will know the certification process, respect your terms of reference, will help the certification, will connect you with the right supplierz
* _2017-02-02 08:44:59_> @U0AAL4W13: but they will come at a cost
* _2017-02-04 13:50:39_> @U41049CQ2: <@U41049CQ2> has joined the channel
* _2017-02-07 15:53:42_> @U42P4AT7Z: <@U42P4AT7Z> has joined the channel
* _2017-03-03 00:59:54_> @U4CAG5ZFW: <@U4CAG5ZFW> has joined the channel
* _2017-03-03 00:59:54_> @U4DFR8RN3: <@U4DFR8RN3> has joined the channel
* _2017-04-10 13:29:48_> @U38HVMZ6K: European MDR and IVDR approved ! This will be a major change for EU medical device manufacturers <https://www.nicelabel.com/blog/2017-04-07/eu-mdr-ivdr-approved-whats-next/>
* _2017-04-10 13:30:34_> @U38HVMZ6K: "Controls will also be tightened on clinical trials" so even more difficult to do trials in EU !
* _2017-04-10 14:26:04_> @U0B47KC3S: <@U04DFTZ7D> it is 4 U :wink:
* _2017-04-10 14:37:42_> @U04DFTZ7D: Thanks ;) I know that. And it will be applied in 20 days  
* _2017-04-19 00:10:55_> @U0AAL4W13: An interesting read, somegood links too, at <https://www.quora.com/Would-it-be-possible-to-build-a-reasonably-cheap-ultrasound-machine-for-home-use>  .  Ping <@U38HVMZ6K> (reactions: @U38HVMZ6K)
* _2017-04-19 08:20:48_> @U38HVMZ6K: &gt; "But then I will have to mark it up by 20x to account for the 501k equivalence, testing, QA, QC and continued compliance and marketing/IP etc." This is where the whole problematic lies... Raw material costs are only the visible part of the iceberg in a medical device. You then have all the R&amp;D costs, lab testing and certification (EMC/ESD, FCC, UL, Bluetooth, ...) which are not specific to medical devices but mandtory as well and then the whole medical certification (510(k), MDR,...) with its huge amount of documentation, system tests, performance tests, substancial equivalence proof, ... which often represents a part bigger than the development itself.
* _2017-04-21 20:47:36_> @U38HVMZ6K: I'm currently working on cybersecurity issues and needs for our medical device and I came across following white paper on the topic applied especially to medical imaging. (reactions: @U0AAL4W13)
* _2017-04-21 20:48:04_> @U38HVMZ6K: <@U38HVMZ6K>
