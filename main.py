from cf_connect import *
import sys
import os
import json

END_POINT_BASE_URL = "https://api.cloudflare.com/client/v4/"


def main():
    """main method
    """
    logger = module_logger.create_module_logger(__name__)
    api_key, domain_name, domain_record, email = init(logger)
    ip = get_ip()
    logger.info("your IP: " + ip)
    connector = CFConnect(domain_name, domain_record, email, ip, api_key, END_POINT_BASE_URL)
    connector.update_dns_record()


# TODO: 配列にして複数ドメイン対応
# TODO: JSON形式の設定ファイル生成
def init(logger: module_logger):
    """initialize method
    :param logger: logging object
    :returns:
       - api_key: CloudFlare's API Key
       - domain_name: Your domain name
       - domain_record: domain_record registered in CloudFlare
       - email: Email address registered in CloudFlare
    """
    logger.info("start initialize process")
    api_key = ""
    domain_name = ""
    domain_record = ""
    email = ""

    def debug_init():
        """debug use only
        デバッグ用のコンフィグを吸い出す
        """
        logger.info("use debug mode")
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        with open("./debug_config") as f:
            config = [s.strip() for s in f.readlines()]
            nonlocal api_key, domain_name, email, domain_record
            api_key = config[0]
            domain_name = config[1]
            domain_record = config[2]
            email = config[3]

    # debug_init()

    api_key, domain_name, domain_record, email = _load_file(logger)
    logger.info("end initialize process")
    return api_key, domain_name, domain_record, email


def _load_file(logger: module_logger):
    """load config file
    :returns:
        api_key: CloudFlare's API Key
        domain_name: Your domain name
        domain_record: domain_record registered in CloudFlare
        email: Email address registered in CloudFlare
    """
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open("./cf_ddns.conf") as f:
        config = f.read()
        config = json.loads(config)
        api_key = config['api_key']
        domain_name = config['domain_name']
        domain_record = config['domain_record']
        email = config['email']
        return api_key, domain_name, domain_record, email


def get_ip() -> str:
    """Get your global ip
    :return ip: your global ip
    """
    res = requests.get('http://api.ipify.org/')
    return res.content.decode('UTF-8')


def create_config():
    config = {'api_key': '', 'domain_name': '',
              'domain_record': '', 'email': ''}
    try:
        while True:
            val = input('api key: ')
            if val == '':
                raise user_exception.ConfigInsertBlankValueError
            else:
                config['api_key'] = val

            val = input('domain name: ')
            if val == '':
                raise user_exception.ConfigInsertBlankValueError
            else:
                config['domain_name'] = val

            val = input('domain record: ')
            if val == '':
                raise user_exception.ConfigInsertBlankValueError
            else:
                config['domain_record'] = val

            val = input('email: ')
            if val == '':
                raise user_exception.ConfigInsertBlankValueError
            else:
                config['email'] = val

            json_config = json.dumps(config)
            print(json_config)

            with open('./cf_ddns.conf', 'w') as f:
                f.write(json_config)

            break

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    elif sys.argv[1] == "-c":
        create_config()
        main()
    elif sys.argv[1] == '-h':
        pass
    else:
        main()
