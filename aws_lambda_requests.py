__author__ = 'Zaheeb Shamsi'

import json
import requests


def load_json():
    with open('ec2.json') as env:
        return json.load(env)


class ScheduleEC2:
    @staticmethod
    def schedule_ec2(ec2json):
        """

        :param ec2json: The json from the user.
        :return: response from the aws server.
        """
        url = "https://4xmhdj3mgj.execute-api.us-east-2.amazonaws.com/live_ec2/start-stop"
        header = {
            "Content-Type": "application/json"
        }
        res = requests.post(url, data=json.dumps(ec2json, indent=4), headers=header)
        if res.status_code == 200:
            resp = res.content.decode('utf-8')
            return json.loads(resp)
        else:
            print("There was a problem in the API Response. ")
            resp = res.content.decode('utf-8')
            return json.loads(resp)


ec2_json = load_json()

obj = ScheduleEC2()
out = obj.schedule_ec2(ec2_json)
print(out)
