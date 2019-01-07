import requests
import json


class CFConnect:

    def __init__(self, domain_name, email, API_KEY, END_POINT_BASE_URL):
        self.API_KEY = API_KEY
        self.END_POINT_BASE_URL = END_POINT_BASE_URL
        self.domain_name = domain_name
        self.email = email

    def set_ip(self):
        res = requests.put()

    def _get_zone_id(self):
        url = self.END_POINT_BASE_URL + "zones?name=" + self.domain_name + "&status=active&page=1&per_page=20" \
                                                                           "&order=status&direction=desc&match=all"
        headers = {'X-Auth-Email': self.email, 'X-Auth-Key': self.API_KEY, 'Content-Type': "application/json"}
        res = requests.get(url, headers=headers)
        zone_id = json.loads(res.content)["result"][0]["id"]
        return zone_id

    def get_record_id(self):
        url = self.END_POINT_BASE_URL + "zones/" + self._get_zone_id() + ""
