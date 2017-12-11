import redis
import os
import json
from util.PodManager import PodManager

REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
SUBSCRIBE_TOPIC = os.environ['SUBSCRIBE_TOPIC']

rconn = redis.StrictRedis(REDIS_SERVER, port=6379, password=REDIS_PASSWORD)
spawn = PodManager()

def sub():
  pubsub = rconn.pubsub()
  pubsub.psubscribe([SUBSCRIBE_TOPIC])

  for item in pubsub.listen():
    try:
      if (isinstance(item['data'], int)):
        continue
    except ValueError:
      print("wait subscribe")

    if item['channel'] == b'spawn/create':
      data = json.loads(item['data'].decode('utf-8'))
      create(data)
    elif item['channel'] == b'spawn/delete':
      data = json.loads(item['data'].decode('utf-8'))
      delete(data)

def create(data):
  spawn.create(data)

def delete(data):
  spawn.delete(data)

def parse(text):
    try:
        return json.loads(text)
    except ValueError as e:
        print('invalid json: %s' % e)
        return None

if __name__ == '__main__':
  sub()
