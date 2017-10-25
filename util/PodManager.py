import json
import os
from pprint import pprint
import logging
import yaml
import subprocess

logging.basicConfig(filename='./log/podManager.log', level=logging.DEBUG)

class PodManager:
    def __init__(self):
        print('init PodManager')

    def spawnPod(self, podInfo):
        pprint('start pod' + podInfo['projectName'])
        logging.debug('%s' % (podInfo))

        if (podInfo['projectName'] is not None):
            projectName = podInfo['projectName']
        else :
            projectName = ""

        if (podInfo['namespace'] is not None):
            namespace = podInfo['namespace']
        else :
            namespace = ""

        if (podInfo['envName'] is not None):
            envName = podInfo['envName']
        else :
            envName = ""

        if (podInfo['envValue'] is not None):
            envValue = podInfo['envValue']
        else :
            envValue = ""

        podFormat = {'apiVersion': 'v1', 'kind': 'Pod',
                 'metadata': {'name': projectName, 'namespace': namespace, 'labels': {'name': projectName}}, 'spec': {
            'containers': [{'name': projectName, 'env': [{'value': envValue, 'name': envName}],
                            'image': 'gcr.io/bluelens-11b9b/'+projectName+':latest'}], 'restartPolicy': 'Never'}}

        podConfig = 'podConfig.yaml'

        with open(podConfig, 'w') as outfile:
            try:
                yaml.dump(podFormat, outfile, default_flow_style=False)
            finally:
                self.runInBash(podConfig)


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