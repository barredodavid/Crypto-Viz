# Utiliser une image Python officielle
FROM python:3.8-slim

# Étape 1 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 2 : Copier le fichier requirements.txt
COPY requirements.txt /app/

# Étape 3 : Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 4 : Copier tous les fichiers du projet dans le conteneur
COPY . /app/

# Étape 5 : Exécuter le scraper
CMD ["python", "scraper/scraper.py"]
