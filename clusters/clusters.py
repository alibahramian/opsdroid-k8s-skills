from kubernetes import client, config

# function to config the client.configuration k8s
def gettoken(apiserver, token):
    TOKEN = token.read().strip()
    APISERVER = 'https://{}:6443'.format(apiserver)
    configuration = client.Configuration()
    configuration.host = APISERVER
    configuration.verify_ssl = False
    configuration.api_key = {"authorization": "Bearer " + TOKEN}
    client.Configuration.set_default(configuration)

# call the gettoken finction based on regions
def defineregion(region):
    if region == "REGIONNAME":
        apiserver = "APISERVER"
        token = open('PATH-TO-TOKE', 'r')
        gettoken(apiserver, token)
    if region == "REGIONNAME":
        apiserver = "APISERVER"
        token = open('PATH-TO-TOKE', 'r')
        gettoken(apiserver, token)
    else:
        print("Region not found")


