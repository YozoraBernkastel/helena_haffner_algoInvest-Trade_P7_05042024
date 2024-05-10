# helena_haffner_books_online_P7_05042024

## Description du programme
Ce projet contient:
 - Un algorithme Bruteforce
 - Un algorithme Optimisé
 - Un csv listant 20 actions
 - Deux csv listant 1000 actions

Le but de chaque algorithme est de proposer une liste d'actions, dont le prix total ne dépasse pas 500€, dans lesquelles investir.

L'algorithme Bruteforce utilise le module itertools.combinations afin de trouver la meilleure combinaison possible. Toutefois, cette méthode consomme énormément de temps de calcul, temps augmentant de manière exponentielle en fonction du nombre d'éléments présent dans la liste d'actions.
L'algorithme optimisé ne permet pas d'assurer de trouver la meilleure combinaison mais son temps de calcul est très court et linéaire, de sorte qu'il peut être utilisé sur de très grandes listes d'actions sans que cela ne pose des problèmes de mémoire et de temps. Cet algorithme se fait en deux étapes.
Tout d'abord, il va privilégier les actions ayant le meilleur ratio prix/profit. Ensuite, dans un second temps, il fait un second calcul, privilgiant le profit brut de chaque action, afin de prévoir les cas où les actions ont des prix élevés et relativement proches de la somme maximale d'investissement.

L'environnement virtuel utilisé pour ce projet est Poetry.

Ce projet s'inscrit dans le cadre d'une formation Python et vise un site destiné à apprendre la récupération d'informations sur internet.

## Environnement Virtuel
Environnement Virtuel utilisé : Poetry

Installation:
```shell
curl -sSL https://install.python-poetry.org | python3 - 
```

Activer l'environnement virtuel : 
```shell
poetry shell
```
Installer les dépendances (les fichiers pyproject.toml ou poetry.lock doivent être présents dans le dossier et qui sont l'équivalent de requirements.txt): 
```shell
poetry install 
```
Sortir de l'environnement virtuel : 
```shell
exit
```

## Lancer le programme depuis l'environnement virtuel
Dans le terminal, à la racine du projet :
```shell
python3 main.py
```

## Lancer le programme sans l'environnement virtuel
Dans le terminal, à la racine du projet :
```shell
poetry run python3 main.py
```




