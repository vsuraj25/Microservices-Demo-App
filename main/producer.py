# amqps://lhaybuvf:eSQmWrod0QW4K41iMbjz4qwXmfHH557j@moose.rmq.cloudamqp.com/lhaybuvf
import pika, json

params = pika.URLParameters("amqps://lhaybuvf:eSQmWrod0QW4K41iMbjz4qwXmfHH557j@moose.rmq.cloudamqp.com/lhaybuvf")

conn = pika.BlockingConnection(params)

channel = conn.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)