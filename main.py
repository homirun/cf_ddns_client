import requests
from cf_connect import *


def main():

    API_KEY = ""
    END_POINT_BASE_URL = "https://api.cloudflare.com/client/v4/"
    domain_name = ""
    domain_record = ""
    email = ""

    # debug use only!
    def debug_init():
        with open("./debug_config") as f:
            l = [s.strip() for s in f.readlines()]
            nonlocal API_KEY, domain_name, email, domain_record
            API_KEY = l[0]
            domain_name = l[1]
            domain_record = l[2]
            email = l[3]

    debug_init()

    ip = get_ip()
    connector = CFConnect(domain_name, domain_record, email, API_KEY, END_POINT_BASE_URL)
    connector.get_record_id()


def get_ip():
    res = requests.get('http://api.ipify.org/')
    return res


if __name__ == '__main__':
    main()
