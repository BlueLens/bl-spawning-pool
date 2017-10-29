import json
import os
from pprint import pprint
import logging
import yaml
import subprocess

logging.basicConfig(filename='./log/podManager.log', level=logging.DEBUG)

TMP_CONFIG_FILE = "config.yaml"

class PodManager:
    def __init__(self):
        print('init PodManager')

    def spawnPod(self, podInfo):
        logging.debug('%s' % (podInfo))

        with open(TMP_CONFIG_FILE, 'w') as outfile:
            try:
                yaml.dump(podInfo, outfile, default_flow_style=False)
            finally:
                self.runInBash(TMP_CONFIG_FILE)


    def runInBash(self, fileName):

        cmd = 'kubectl --namespace=index create -f ' + fileName
        print(cmd)
        logging.debug('%s' % (cmd))

        output = subprocess.call(cmd, shell=True)
        # output.stdout.decode('utf-8')
        pprint(output)
        logging.debug('%s' % (output))
        # print('cat finished with return code %d' % output.returncode)


    def printPod(self):
        pprint(self.__podJson)