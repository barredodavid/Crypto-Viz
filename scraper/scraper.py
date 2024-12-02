import requests
from bs4 import BeautifulSoup
import pika
import json

# Setup RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='crypto_queue')

# Scrape the data (example from Crypto News API)
def scrape_data():
    url = 'https://www.cryptonews.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h3', {'class': 'crypto-news-title'})

    for headline in headlines:
        data = {
            'title': headline.text.strip(),
            'link': headline.find('a')['href']
        }
        send_to_queue(data)

def send_to_queue(data):
    channel.basic_publish(exchange='',
                          routing_key='crypto_queue',
                          body=json.dumps(data))

# Run the scraper
scrape_data()
connection.close()
