import socket
import string
import random
from subprocess import run, PIPE

import qrcode
import psutil

__all__ = [
    "qr_generator", "get_available_port", "get_ip_address", "command_processor"
]


def command_processor(command: str):
    """
    :param command:
    :return:
    """
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


def qr_generator(host: str, port: str, path: str):
    """
    :param host: Web server host
    :param port: Web port
    :param path: full path of the directory or single file
    :return:
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=2,
    )
    qr.add_data("http://" + host + ":" + port + path)
    qr.make()
    qr.print_ascii(tty=True)


def get_ip_address():
    """
    Get IP address
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_available_port():
    """
    Get available port
    :return:
    """
    for port in range(5000, 9001):
        if port not in [i.laddr.port for i in psutil.net_connections()]:
            return port


def short_code():
    """Short code"""
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return "".join(random.choices(letters, k=8))
