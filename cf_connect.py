import requests
import json


class CFConnect:
    """CloudFlare API関連"""

    def __init__(self, domain_name, domain_record, email, API_KEY, END_POINT_BASE_URL):
        """
        :param domain_name: your domain name
        :param domain_record: your domein record
        :param email: E-mail address registered with CloudFlare
        :param API_KEY: your CloudFlare's apikey
        :param END_POINT_BASE_URL: CloudFlare's endpoint url
        """

        self.API_KEY = API_KEY
        self.END_POINT_BASE_URL = END_POINT_BASE_URL
        self.domain_name = domain_name
        self.domain_record = domain_record
        self.email = email

    def set_ip(self, ip):
        """ Set IP to CloudFlare
        :param ip: your global ip
        """
        pass

    def _get_zone_id(self):
        """Get zone_id
        :return zone_id: your domain's zone_id
        """

        url = self.END_POINT_BASE_URL + "zones?name=" + self.domain_name + "&status=active&page=1&per_page=20" \
                                                                           "&order=status&direction=desc&match=all"
        headers = {'X-Auth-Email': self.email, 'X-Auth-Key': self.API_KEY, 'Content-Type': "application/json"}
        res = requests.get(url, headers=headers)
        zone_id = json.loads(res.content)["result"][0]["id"]
        return zone_id

    def get_record_id(self):
        """Get record_id

        :return record_id: your domain's record_id
        """
        url = self.END_POINT_BASE_URL + "zones/" + self._get_zone_id() + "/dns_records?name=" + self.domain_record
        headers = {'X-Auth-Email': self.email, 'X-Auth-Key': self.API_KEY, 'Content-Type': "application/json"}
        res = requests.get(url, headers=headers)
        record_id = json.loads(res.content)["result"][0]["id"]
        return record_id
