from multiprocessing import Process
import time
import redis
import logging
import json
from util.PodManager import PodManager
import yaml

logging.basicConfig(filename='./log/main.log', level=logging.DEBUG)

def sub(r, name):
    pubsub = r.pubsub()
    pubsub.subscribe(['spawn/create'])

    podJson = {
        "projectName":"test",
        "namespace":"index",
        "envName":"test",
        "envValue":"123"}

    for item in pubsub.listen():
        logging.debug('%s : %s' % (name, item['data']))
        print('%s : %s' % (name, item['data']))

        try:
            if (isinstance( item['data'], int )):
                print('type is not json')
            else:
                # work(item['data'])
                # TODO: test code
                work(podJson)
        except ValueError:
            print("wait subscribe")

def work(data):
    # print(item['channel'], ":", item['data'])
    pod = PodManager()
    pod.spawnPod(data)

def parse(text):
    try:
        return json.loads(text)
    except ValueError as e:
        print('invalid json: %s' % e)
        return None

if __name__ == '__main__':
    r = redis.StrictRedis('bl-mem-store', port=6379)
    # r = redis.StrictRedis('35.187.244.252', port=6379)
    # Process(target=pub, args=(myredis,)).start()
    Process(target=sub, args=(r,'bl-mem-store')).start()
    # Process(target=Listener(r).sub, args=('bl-mem-store')).start()
