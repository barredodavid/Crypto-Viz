# Utiliser une image Python officielle
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt depuis la racine
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste des fichiers dans le conteneur
COPY . /app/

# Commande pour exécuter le scraper
CMD ["python", "scraper/scraper.py"]
