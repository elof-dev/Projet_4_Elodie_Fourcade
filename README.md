# Projet 4 - Application Chess

Ce projet est une application de gestion de tournois d'échecs développée en Python. Elle permet de créer des joueurs, organiser des tournois, gérer les rounds, et afficher les classements.

---

## **Pré-requis**

- **Python** : Version 3.13.1 ou ultérieure doit être installée sur votre machine.
- **Environnement virtuel** : Recommandé pour gérer les dépendances.

---

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

> **Note** : Des joueurs sont déjà présents dans le fichier `players.json` afin de pouvoir créer un tournoi rapidement.

Afin de générer un nouveau fichier flake8, il faut exécuter la commande suivante :
```bash
flake8 --format=html --htmldir=flake-report
```