# Python-WorldHappy
Python Project on world happiness

## Sommaire
1. [Rapport d'analyse](#1-Rapport-d’analyse)
2. [User Guide](#2.-User-Guide)
3. [Developer Guide](#2.-Developer-Guide)
4. [Lien](#2.-Lien)


## 1. Rapport d’analyse

Notre projet porte sur la joie dans le monde de 2015 à 2020.

Les différents pays ont un score de joie, calculé à partir de plusieurs données comme expliqué: https://en.wikipedia.org/wiki/World_Happiness_Report . Ces différents facteurs sont aussi répertoriés dans nos différents csv. Nous pouvons donc observer l’influence de chaque facteur à travers les années par rapport au score total.

Nous pouvons donc voir qu’un pays riche n’est pas forcément heureux, mais aussi détecter des périodes de “creux” pour certains pays, notamment entre 2019 et 2020.

Passons aux graphiques:

Nous avons dans un premier temps un graphique en points montrant la relation entre le score de joie et une sélection d'autres variables, avec la taille des points représentants le GDP du pays (la population étant manquante de ce dataset). Nous pouvons donc remarquer facilement quelques exceptions comme la Syrie, ayant une espérance de vie élevée comparé à son score. Mais nous pouvons surtout remarquer que ces exceptions se situent dans la partie “basse du graphique”, là où le score est bas, ce qui signifie que les pays les plus joyeux ont tous des “caractéristiques” supérieures à la moyenne. Cela montre que pour avoir un score haut, il faut avoir tous les critères “bons” au minimum: un pays riche mais corrompu n’aura pas un bon score.

Pour l’histogramme, nous savons que le nombre de valeur n’est pas vraiment suffisant (avec seulement une valeur par pays) malheureusement regrouper toutes les années ne nous semblait pas une solutions viable car cela reviendrait à "multiplier" des valeurs à peu de chose près (sauf certaines exceptions) et cela ne nous semblait pas pertinent. D’autre part nous n’avons pas trouvé d’autres données pertinentes, en suffisamment grand nombre, et proche de notre projet pour faire un l’histogramme digne de ce nom, nous espérons que le petit nombre (dépendant des années) sera excusé. 

Malgré cela nous pouvons observer deux bosses distinctes, la première plutôt instable au travers des années (centre variant entre 3 et 4) et une seconde centrée autour de 6.

Nous pouvons aussi voir une récurrence au fil des années dans les zones géographiques, en effet les pays du sud de l’Afrique sont majoritairement dans la première bosse alors que l’Europe de l’Est et l’Amérique du Nord est plus présente dans la seconde bosse.


Cela est encore plus frappant sur la Bubble Map où nous pouvons constater que le score de joie est très souvent proportionnel à celle de ces voisins.


## 2. User Guide

Run pip install -r requirements.txt sous python pour installer les packages nécessaires

Run le fichier “WorldHapinessProject” puis ouvrir un navigateur à l’adresse suivante: http://127.0.0.1:8050/



Dans le cas où requirements est perdu voici le nom des packages nécessaires, à installer avec  “pip install (“name”==version)”

plotly-express==0.4.1
dash==2.0.0

## 3. Developer Guide

Nous avons séparé le code en plusieurs parties distinctes par l'utilisation de commentaires,  les variables globales sont gérées dès le début du code.

L’UI est géré dans l’ordre d’apparition sur la page WEB.


Les graphiques sont tous gérés dans deux fonctions, dépendant de la présence ou non de la zone géographique des pays.

Chaque graphique (hors map) est géré par la dataset nommé “data”, qui est changé selon les conditions.

## 3. Lien
https://www.kaggle.com/mathurinache/world-happiness-report
