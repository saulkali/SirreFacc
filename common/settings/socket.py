from helper import singleton

class Socket(object):
    is_master:bool = True
    is_ip_static:bool = False # DHCP or MANUAL
    ip_server:str = "8.8.8.8"
    hostname:str = "127.0.0.1"
    port:int = 8080
    client_listener:int = 10
    