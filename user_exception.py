class CFConnectError(Exception):
    pass


class DNSUpdateError(CFConnectError):
    pass


class ConfigCreateError(Exception):
    pass


class ConfigInsertBlankValueError(ConfigCreateError):
    pass
