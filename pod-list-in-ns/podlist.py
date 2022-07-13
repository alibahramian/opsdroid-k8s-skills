from kubernetes import client, config
from opsdroid.matchers import match_regex
from opsdroid.skill import Skill

class podlist(Skill):

    @match_regex('list pods in (?P<ns>\w+\S+)')
    async def podlist(self, message):
        ns: str = message.entities['ns']['value']

        config.load_incluster_config()
        v1 = client.CoreV1Api()

        pods = v1.list_namespaced_pod(ns).items

        pod_list = []

        for pod in pods:

            try:
                name = pod.metadata.name
                status = pod.status.phase
                pod_list.append({'name': name, 'status': status})

            except:
                pass
       
        await message.respond(str(json.dumps(pod_list, indent=2)))
