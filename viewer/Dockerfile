# Utiliser l'image officielle Node.js
FROM node:16

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier package.json et package-lock.json pour installer les dépendances
COPY package.json package-lock.json /app/

# Installer les dépendances
RUN npm install

# Copier tout le reste du projet dans le conteneur
COPY . /app/

# Exposer le port 3000
EXPOSE 3000

# Démarrer l'application React
CMD ["npm", "start"]
