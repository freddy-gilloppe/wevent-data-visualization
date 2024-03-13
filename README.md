# Wevent DataViz

Ce dépôt répertorie tous les fichiers nécessaires à l'élaboration d'un projet [Streamlit](https://streamlit.io/).  
Le but de ce projet est de centraliser la visualisation de données clées sur l'activité de Wevent.

## installation

### Virtual environment

L'environnement virtuel se trouve dans le dossier `venv/`.

Si le dossier n'existe pas, voici comment le créer :

```shell
$ python -m venv venv
```

Voici comment l'activer selon votre système d'exploitation :

```shell
# Windows
$ venv\Scripts\activate

# Linux / MacOS
$ source venv/bin/activate
```

Installer les dépendances via le fichier `requirements.txt` :

```shell
$ pip install -r requirements.txt
# pip doit être installé
```

En cas de mise à jour des dépendances, il est possible de mettre à jour le fichier `requirements.txt` via la commande suivante :

```shell
$ pip freeze > requirements.txt
# pip doit être installé
```

### Éxécution locale

Pour lancer le projet en local, il suffit d'éxécuter la commande suivante :

```shell
$ streamlit run Accueil.py --server.enableCORS false --server.enableXsrfProtection false
# ou, en cas de problème
$ streamlit run Accueil.py
# will run on http://localhost:8501
```
