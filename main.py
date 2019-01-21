from cf_connect import *

API_KEY = ""
END_POINT_BASE_URL = "https://api.cloudflare.com/client/v4/"


def main():
    """main method
    """
    logger = module_logger.create_module_logger(__name__)
    logger.info("start initialize process")

    domain_name = ""
    domain_record = ""
    email = ""

    def debug_init():
        """debug use only method
        デバッグ用のコンフィグを吸い出す
        """
        logger.info("use debug mode")
        with open("./debug_config") as f:
            config = [s.strip() for s in f.readlines()]
            global API_KEY
            nonlocal domain_name, email, domain_record
            API_KEY = config[0]
            domain_name = config[1]
            domain_record = config[2]
            email = config[3]

    debug_init()
    logger.info("end initialize process")
    ip = get_ip()
    logger.info("your IP: " + ip)
    connector = CFConnect(domain_name, domain_record, email, ip, API_KEY, END_POINT_BASE_URL)
    connector.update_dns_record()


def get_ip() -> str:
    """Get your global ip
    :return ip: your global ip
    """
    res = requests.get('http://api.ipify.org/')
    return res.content.decode('UTF-8')


if __name__ == '__main__':
    main()
