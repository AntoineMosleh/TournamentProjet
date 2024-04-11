# TourNaMent

TourNaMent est une application web Django pour la création, la gestion et le suivi des tournois sportifs. Elle permet aux utilisateurs de créer des tournois, d'ajouter des équipes, de générer des matchs et de saisir les résultats.

## Fonctionnalités

- Création de tournois avec sélection du sport.
- Ajout d'équipes/participants aux tournois.
- Tirage au sort des matchs à jouer.
- Saisie des scores pour chaque match.
- Classement automatique des équipes basé sur les résultats des matchs.

## Prérequis

- Python 3.8+
- Django 3.2+

## Installation

1. Installez les dépendances :
pip install -r requirements.txt

2. Effectuez les migrations de la base de données :
python manage.py makemigrations
python manage.py migrate

3. Lancez le serveur de développement :
python manage.py runserver

## Utilisation

1. Accédez à l'application via votre navigateur à l'adresse `http://127.0.0.1:8000/`.
2. Suivez l'interface utilisateur pour créer des tournois et ajouter des participants.
