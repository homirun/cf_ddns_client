import requests
from cf_connect import *


def main():
    # cloudflare's API KEY
    API_KEY = ""
    END_POINT_BASE_URL = "https://api.cloudflare.com/client/v4/"
    domain_name = ""
    email = ""
    ip = get_ip()
    connector = CFConnect(domain_name, email, API_KEY, END_POINT_BASE_URL)
    connector._get_zone_id()


def get_ip():
    res = requests.get('http://api.ipify.org/')
    return res


if __name__ == '__main__':
    main()
