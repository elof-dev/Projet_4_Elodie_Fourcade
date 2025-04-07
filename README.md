# Projet 4 - Application Chess

Ce projet est une application de gestion de tournois d'échecs. Elle permet de créer des joueurs, et d'organiser des tournois.

## **Pré-requis**

- **Python** : Version 3.13.1 ou ultérieure.

## **Installation**

1. **Cloner le repository GitHub** :
    ```bash
    git clone https://github.com/elof-dev/Projet_4_Elodie_Fourcade.git
    ```

2. **Se positionner sur le dossier** :
    ```bash
    cd Projet_4_Elodie_Fourcade/application_chess
    ```

3. **Créer l'environnement virtuel** :
    ```bash
    py -m venv .venv
    ```

4. **Activer l'environnement virtuel** :
    - Sous Windows :
      ```bash
      .venv\Scripts\activate
      ```
    - Sous macOS/Linux :
      ```bash
      source .venv/bin/activate
      ```

5. **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

6. **Exécuter le script** :
    ```bash
    py main.py
    ```

## **Utilisation**

Lors du lancement du programme, vous arrivez sur le menu principal dont l'arborescence est la suivante :

```
Bienvenue dans le programme de gestion des échecs !

Menu principal :
1. Créer un joueur
2. Afficher les joueurs
3. Créer un tournoi
4. Reprendre un tournoi en cours
5. Voir les détails d'un tournoi
6. Quitter
Entrez votre choix :
```
> **Note** : L'application ne joue pas les matchs virtuellement. Les matchs sont joués dans la vie réelle, et les résultats sont ensuite saisis dans l'application.

## **Fonctionnement général**

1. **Création des joueurs** :
   - Les joueurs sont ajoutés dans l'application avec leurs informations personnelles (nom, prénom, date de naissance, et identifiant national d'échec).

2. **Création d'un tournoi** :
   - L'utilisateur peut créer un tournoi en lui donnant un nom, un lieu et une description (facultatif).
   - L'application génère automatiquement les matchs en fonction du nombre de joueurs présents. Les rounds sont prédéfinis à 4 par défaut comme demandé.
   - A chaque round créé, l'utilisateur saisit les résultats dans l'application.
   - Les scores sont enregistrés, et les prochains rounds sont générés en fonction des résultats précédents.
   - A la fin du tournoi, l'utilisateur peut mettre un commentaire s'il le souhaite.
   - Si les tournois se déroulent sur plusieurs jours par exemple, l'utilisateur peut reprendre la saisie de son tournoi lors de la réouverture de l'application. Tous les scores sont sauvegardés.

4. **Consultation des résultats** :
   - À la fin des tournois, l'utilisateur peut consulter les scores finaux et les classements des joueurs.

> **Note** : Des joueurs sont déjà présents dans le fichier `players.json` afin de pouvoir créer un tournoi rapidement.

---
Afin de générer un nouveau fichier flake8, il faut exécuter la commande suivante :
```bash
flake8 --format=html --htmldir=flake-report
```