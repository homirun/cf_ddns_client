from cf_connect import *

API_KEY = ""
END_POINT_BASE_URL = "https://api.cloudflare.com/client/v4/"


def main():
    """main method
    """

    domain_name = ""
    domain_record = ""
    email = ""

    # debug use only!
    def debug_init():
        """debug use only method
        デバッグ用のコンフィグを吸い出す
        """
        with open("./debug_config") as f:
            config = [s.strip() for s in f.readlines()]

            global API_KEY
            nonlocal domain_name, email, domain_record
            API_KEY = config[0]
            domain_name = config[1]
            domain_record = config[2]
            email = config[3]

    debug_init()

    ip = get_ip()
    connector = CFConnect(domain_name, domain_record, email, ip,API_KEY, END_POINT_BASE_URL)
    print(connector.update_dns_record())


def get_ip():
    """Get your global ip
    :return ip: your global ip
    """

    res = requests.get('http://api.ipify.org/')
    return res.content.decode('UTF-8')


if __name__ == '__main__':
    main()
