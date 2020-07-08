"""
Prototype: Bla bla bla

"""
import sys
import argparse

from PyFi.utils import *
from PyFi.server import run_server


class PySender:

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
    sender = PySender()
    sender.run("/" + args.file)
    # sender.run(path='/home/vubon/personal/PyFi/dist/dog.jpg')


if __name__ == "__main__":
    main()
