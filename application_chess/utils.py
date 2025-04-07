import os
import json


def ensure_file_exists(file_path, default_content="[]"):
    """Crée un fichier avec un contenu par défaut s'il n'existe pas."""
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            file.write(default_content)


def load_json(file_path):
    """Charger le contenu d'un fichier JSON."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_json(file_path, data):
    """Sauvegarder des données dans un fichier JSON."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
