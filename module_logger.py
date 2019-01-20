import logging


def create_module_logger(logger_name: str):
    """ Create logger object
    :param logger_name: module_name (Basically use __name__)
    :return: logger object
    """
    logger = logging.getLogger(logger_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
