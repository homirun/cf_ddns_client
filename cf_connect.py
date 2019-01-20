import requests
import json
import user_exception
import module_logger


class CFConnect:
    """CloudFlare API関連"""

    def __init__(self, domain_name, domain_record, email, ip, API_KEY, END_POINT_BASE_URL):
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
        self.ip = ip
        self.logger = module_logger.create_module_logger(__name__)

    def _get_zone_id(self):
        """Get zone_id
        :return zone_id: your domain's zone_id
        """
        url = self.END_POINT_BASE_URL + "zones?name=" + self.domain_name + "&status=active&page=1&per_page=20" \
                                                                           "&order=status&direction=desc&match=all"
        headers = {'X-Auth-Email': self.email, 'X-Auth-Key': self.API_KEY, 'Content-Type': "application/json"}
        res = requests.get(url, headers=headers)
        zone_id = json.loads(res.content)["result"][0]["id"]
        self.logger.info("zone id: " + zone_id)
        return zone_id

    def _get_record_id(self, zone_id):
        """Get record_id
        :return record_id: your domain's record_id
        """
        url = self.END_POINT_BASE_URL + "zones/" + zone_id + "/dns_records?name=" + self.domain_record
        headers = {'X-Auth-Email': self.email, 'X-Auth-Key': self.API_KEY, 'Content-Type': "application/json"}
        res = requests.get(url, headers=headers)
        record_id = json.loads(res.content)["result"][0]["id"]
        self.logger.info("record id: " + record_id)
        return record_id

    def update_dns_record(self):
        """ update dns record to CloudFlare
        :return: isSuccess
        """
        zone_id = self._get_zone_id()
        record_id = self._get_record_id(zone_id)
        self.logger.info("start update process")
        url = self.END_POINT_BASE_URL + "zones/" + zone_id + "/dns_records/" + record_id
        headers = {'X-Auth-Email': self.email, 'X-Auth-Key': self.API_KEY, 'Content-Type': 'application/json'}
        content = {'type': 'A', 'name': self.domain_name, 'content': self.ip}
        content = json.dumps(content)
        res = requests.put(url, content, headers=headers)
        if json.loads(res.content)["success"] is False:
            self.logger.exception("EXCEPTION DNSUpdateError")
            raise user_exception.DNSUpdateError

        self.logger.info("update process success")
        return True

