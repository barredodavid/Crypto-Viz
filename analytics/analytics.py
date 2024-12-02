import pika
import json
import pandas as pd
from collections import defaultdict
import time

# Fonction pour tenter de se connecter à RabbitMQ
def connect_to_rabbitmq():
    while True:
        try:
            # Tentative de connexion à RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ n'est pas encore prêt. Nouvelle tentative dans 5 secondes...")
            time.sleep(5)

# Connexion à RabbitMQ
connection = connect_to_rabbitmq()
channel = connection.channel()

# Déclare la file d'attente pour consommer les messages
channel.queue_declare(queue='crypto_queue')

# Dictionnaire pour stocker les données collectées
data_store = defaultdict(list)

# Fonction pour traiter les données reçues
def process_data(ch, method, properties, body):
    data = json.loads(body)
    title = data['title']
    link = data['link']

    # Ajouter les données à la structure de données
    data_store['headlines'].append(title)
    data_store['links'].append(link)

    print(f"Processed data: {title}, {link}")

    # Analyser les données après chaque réception
    analyze_data()

# Fonction pour analyser les données collectées
def analyze_data():
    df = pd.DataFrame(data_store)  # Convertir les données en DataFrame
    print("Data summary:")
    print(df.head())  # Afficher un résumé des données

# Consommer les messages dans la queue RabbitMQ
channel.basic_consume(queue='crypto_queue', on_message_callback=process_data, auto_ack=True)

# Démarrer la consommation des messages
print("Starting analytics...")
channel.start_consuming()
