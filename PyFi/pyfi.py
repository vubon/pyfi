"""
Short Description: PyFi is a short form. Py means Python, Fi means File and Wifi.
PyFi is a file sharing project over WiFi network.

@Author: Vubon Roy
@since: Jun, 2020
"""
import sys
import argparse

from PyFi.utils import *
from PyFi.server import run_server


class PyFi:

    def __init__(self):
        self.__ip = get_ip_address()
        self.__port = get_available_port()

    def run(self, path: str):
        try:
            print("Send file or full directory over wifi................")
            print(f"Server is running on http://{self.__ip}:{self.__port}")
            qr_generator(host=self.__ip, port=str(self.__port), path=path)
            run_server(self.__port)
        except KeyboardInterrupt:
            sys.exit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File name or directory name with full path or run where is existing the file")
    args = parser.parse_args()
    sender = PyFi()
    sender.run("/" + args.file)


if __name__ == "__main__":
    main()
