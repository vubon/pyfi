import psutil
import socket


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def test():
    for port in range(5000, 9001):
        if port not in [i.laddr.port for i in psutil.net_connections()]:
            return port


if __name__ == "__main__":
    print(test())
    print(get_ip_address())
