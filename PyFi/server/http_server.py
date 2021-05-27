"""
Basic Server
"""
import socketserver

from http.server import SimpleHTTPRequestHandler


__version__ = "0.6"

__all__ = [
    'run_server'
]


class MyHandler(SimpleHTTPRequestHandler):

    def log_message(self, formats: str, *args) -> None:
        pass


def run_server(port: int):
    """
    :param port:
    :return:
    """
    httpd = socketserver.TCPServer(("0.0.0.0", port), MyHandler)
    try:
        httpd.serve_forever()
    except OSError:
        httpd.server_close()
