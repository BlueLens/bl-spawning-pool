import json
import os
from bluelens_log import Logging
import subprocess
import yaml


TMP_CONFIG_FILE = "config.yaml"

REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
options = {
    'REDIS_SERVER': REDIS_SERVER,
    'REDIS_PASSWORD': REDIS_PASSWORD
}
log = Logging(options, tag='bl-spawning-pool')

class PodManager:
    def __init__(self):
        log.debug('init PodManager')

    def create(self, data):
        log.debug('%s' % (data))

        with open(TMP_CONFIG_FILE, 'w') as outfile:
            try:
              yaml.dump(data, outfile, default_flow_style=False)
            finally:
              cmd = 'cat config.yaml && kubectl --namespace=' + data['metadata']['namespace'] + ' create -f ' + TMP_CONFIG_FILE
              self.runInBash(cmd)

    def delete(self, data):
        log.debug(data)
        # cmd = 'kubectl delete pods --namespace=' + data['namespace'] + ' -l SPAWN_ID=' + data['id']
        cmd = 'kubectl delete pods --namespace=' + data['namespace'] + ' -l ' + data['key'] + '=' + data['value']
        log.debug(cmd)
        self.runInBash(cmd)

    def runInBash(self, cmd):
        log.debug(cmd)
        log.debug('%s' % (cmd))

        output = subprocess.call(cmd, shell=True)
        # output.stdout.decode('utf-8')
        log.debug(output)
        # log.debug('cat finished with return code %d' % output.returncode)


