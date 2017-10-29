from multiprocessing import Process
import time
import redis
import os
import logging
import json
from util.PodManager import PodManager

REDIS_SERVER = os.environ['REDIS_SERVER']
SUBSCRIBE_TOPIC = os.environ['SUBSCRIBE_TOPIC']

logging.basicConfig(filename='./log/main.log', level=logging.DEBUG)

def sub(rconn, name):
    pubsub = rconn.pubsub()
    pubsub.subscribe([SUBSCRIBE_TOPIC])

    for item in pubsub.listen():
        logging.debug('%s' % (item['data']))
        print('%s' % (item['data']))

        try:
            if (isinstance( item['data'], int )):
                print('type is not json')
            else:
                work(item['data'])
        except ValueError:
            print("wait subscribe")

def work(data):
    pod = PodManager()
    pod.spawnPod(data)

def parse(text):
    try:
        return json.loads(text)
    except ValueError as e:
        print('invalid json: %s' % e)
        return None

if __name__ == '__main__':
    rconn = redis.StrictRedis(REDIS_SERVER, port=6379)
    Process(target=sub, args=(rconn, 'xxx')).start()
