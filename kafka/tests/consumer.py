from kafka import KafkaClient, KafkaConsumer
import random

groupName='printTopicName'+str(random.randint(0,1))
print groupName

consumer = KafkaConsumer(
    'topicName'
    ,bootstrap_servers=['127.0.0.1:9092']
    ,group_id=groupName
    )

for msg in consumer:
    print msg

