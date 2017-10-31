import json
import os
from pprint import pprint
import logging
import subprocess
import yaml

logging.basicConfig(filename='./log/podManager.log', level=logging.DEBUG)

TMP_CONFIG_FILE = "config.yaml"

class PodManager:
    def __init__(self):
        print('init PodManager')

    def create(self, data):
        logging.debug('%s' % (data))

        with open(TMP_CONFIG_FILE, 'w') as outfile:
            try:
              yaml.dump(data, outfile, default_flow_style=False)
            finally:
              cmd = 'cat config.yaml && kubectl --namespace=index create -f ' + TMP_CONFIG_FILE
              self.runInBash(cmd)

    def delete(self, data):
        print(data)
        logging.debug(data)
        cmd = 'kubectl delete pods --namespace=' + data['namespace'] + ' -l SPAWN_ID=' + data['id']
        logging.debug(cmd)
        self.runInBash(cmd)

    def runInBash(self, cmd):
        print(cmd)
        logging.debug('%s' % (cmd))

        output = subprocess.call(cmd, shell=True)
        # output.stdout.decode('utf-8')
        pprint(output)
        logging.debug('%s' % (output))
        # print('cat finished with return code %d' % output.returncode)

