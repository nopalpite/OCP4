# OCP2: Chess Tournament  

Ce script permet de gérer l'organisation de tournoi d'échecs d'un club en utilisant le système de classement suisse.

## Installation

Récupérez le dépot github :

```
git clone https://github.com/nopalpite/OCP4.git
```

Placez-vous dans le dossier OCP2 et créez un environnement virtuel:

```
python -m venv env
```
Activez l'environnement virtuel
Sur Windows :
```
env\Scripts\activate
```
Sur Linux:
```
source env/bin/activate
```
Installez les packages requis:
```
pip install -r requirements.txt
```
# Lancement de l'application

```
python main.py
```

# Fonctionnement

## Menu principal
```
###### MENU PRINCIPAL ######

[1] Créer un tournoi
[2] Ajouter des joueurs à la base de donnée
[3] Charger un tournoi
[4] Afficher un rapport
[5] Mettre à jour le classement elo d'un joueur

[q] Quitter
Entrez votre choix: 
```

Le menu principal vous permet d'accéder à toutes les fonctionnalités de l'application

## Menu des rapports

```
------menu des rapports------

[1] Liste des joueurs
[2] Liste des joueurs par tournoi
[3] Liste des tournois
[4] Liste des tours par tournoi
[5] Liste des matchs par tournoi

[r] Retour
Entrez votre choix: 
```
Le menu des rapports permet d'accéder à tous les rapports de la base de données des tournois

# Génération du rapport flake8

Pour vérifier la conformité du code lancer la commande suivante:

``flake8 --format=html --htmldir=flake-report``






