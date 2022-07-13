import os
from kubernetes import client, config

base_creds_path = 'PATH_TO_CREDS'
token = open(os.path.join(base_creds_path, 'TOKEN'))
service_host = "HOST"


def gettoken():
    Token = token.read()
    apiserver = 'https://{}:6443'.format(service_host)
    configuration = client.Configuration()
    configuration.host = apiserver
    configuration.verify_ssl = False
    configuration.api_key = {"authorization": "Bearer " + Token}
    client.Configuration.set_default(configuration)
    v1 = client.CoreV1Api()
    ns: str = "spark-operator"


    ret = v1.list_namespaced_pod(ns)
    for i in ret.items:
        print("%s\t%s\t%s" %
                (i.status.pod_ip, i.metadata.namespace, i.metadata.name)) 

gettoken()

