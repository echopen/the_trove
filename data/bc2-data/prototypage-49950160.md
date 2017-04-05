## V0 android-app commits



hello à tous,  
  
la V0 est sur la branche master.  
  
@loic : il y a à ce jour deux façons d'interagit avec la data  
  
\- scan conversion à partir de data sur port UDP. Hyacinthe a mis en ligne un
serveur qu'on peut déployer en local et émule la data de la redpitaya  
  
de mon côté, je la récupère et je la display  
  
la scan conversion initiale utilise des tableaux de char, ce qui n'est pas
très commode. Donc je scan-convert avec des tableaux d'int et je renvoie un
bitmap. Mais j'ai mis un Visitor qui permet de garder le traitement  par
`char`, notamment pour des data qu'on extrait d'un fichier csv. Btw, pour le
calcul des poids de la table, je le fais une seule fois via le Singleton qui
est la class Config, lequel est instancié dans le MainActivity. Je le mettrai
plus en amont asap  
  
A ce stade, il y a plusieurs bottleneck de perf : l'algo de scan conversion en
lui-m-même n'est pas très performant - la création d'u bitmap est coûteuse -
tout cela plaide pour à terme un traitement par GPU. Voici un peu de doc
spécifique android sur le sujet  
  
<http://arrayfire.com/getting-started-with-opencl-on-android/>  
<https://software.intel.com/sites/default/files/managed/d3/18/AndroidBasicOpenCL.pdf>  
  
\- dans /phantom une app plain java qui permet de tester l'algo en situation
basique aka non android  
  
voilà tout -



