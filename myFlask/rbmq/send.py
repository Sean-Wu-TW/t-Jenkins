#!/usr/bin/env python

# This file send messages to receive.py without exchange.

import pika, sys

def send(tosend):
    import pika, sys
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=tosend)
    print(" [x] Sent '{}'".format(tosend))

    connection.close()


if __name__ == '__main__':
    message = ' '.join(sys.argv[1:]) or "Hello World!"
    send(message)
