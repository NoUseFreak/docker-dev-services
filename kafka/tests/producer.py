from kafka import KafkaClient, SimpleProducer, KafkaProducer
import random

producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:9092']
    )

print vars(producer.send('topicName', 'somemessage').get())
